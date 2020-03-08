from vkwave_client.abstract import AbstractAPIClient
from vkwave_client.types import MethodName
from vkwave_client.context import ResultState
from vkwave_api.token.token import AnyABCToken, Token
from vkwave_api.token.strategy import ABCGetTokenStrategy, RandomGetTokenStrategy
from vkwave_api.methods._error import ErrorDispatcher, Error
from typing import Optional, cast, Tuple, List, Union

import copy
import random


class TemporaryException(Exception):
    """It means nothing."""


class Category:
    def __init__(self, name: str, api: "APIOptionsRequestContext"):
        self.category_name = name
        self.__api = api

    def make_method_name(self, method_name: str) -> MethodName:
        return MethodName(f"{self.category_name}.{method_name}")

    async def api_request(self, method_name: str, params: dict) -> dict:
        client, token = await self.__api.get_client_and_token()
        method_name = self.make_method_name(method_name)

        params = self.__api.update_pre_request_params(params, token)
        ctx = client.create_request(method_name, params)
        await ctx.send_request()

        state = ctx.result.state

        if state is not ResultState.SUCCESS:
            raise TemporaryException()

        result = ctx.result.data
        result = cast(dict, result)
        
        if "error" in result:
            err_handler_result = await self.__api.handle_error(result["error"])
            if err_handler_result:
                result = err_handler_result

        return result


TokensInput = Union[List[AnyABCToken], AnyABCToken]
ClientsInput = Union[List[AbstractAPIClient], AbstractAPIClient]


class APIOptions:
    def __init__(
        self,
        tokens: TokensInput,
        clients: ClientsInput,
        get_token_strategy: ABCGetTokenStrategy,
        api_version: str,
        error_dispatcher: ErrorDispatcher,
    ):
        self.tokens = tokens if isinstance(tokens, list) else [tokens]
        self.clients = clients if isinstance(clients, list) else [clients]
        self.get_token_strategy = get_token_strategy
        self.api_version: str = api_version
        self.error_dispatcher = error_dispatcher


class APIOptionsRequestContext:
    def __init__(self, api_options: APIOptions):
        self.api_options = api_options

        self.messages = Category("messages", self)

    async def handle_error(self, error: Error) -> Optional[dict]:
        dispatcher = self.api_options.error_dispatcher
        result = await dispatcher.process_error(error, self)
        return result

    async def _get_token(self) -> Token:
        return await self.api_options.get_token_strategy.get_token(
            self.api_options.tokens
        )

    async def _get_client(self) -> AbstractAPIClient:
        # TODO: maybe get_client_strategy
        return random.choice(self.api_options.clients)

    async def get_client_and_token(self) -> Tuple[AbstractAPIClient, Token]:
        return (await self._get_client(), await self._get_token())

    def update_pre_request_params(self, params: dict, token: Token) -> dict:
        params.update(v=self.api_options.api_version, access_token=token)
        return params


class API:
    def __init__(
        self,
        tokens: TokensInput,
        clients: ClientsInput,
        get_token_strategy: Optional[ABCGetTokenStrategy] = None,
        api_version: Optional[str] = None,
        error_dispatcher: Optional[ErrorDispatcher] = None,
    ):
        self.default_api_options = APIOptions(
            tokens,
            clients,
            get_token_strategy or RandomGetTokenStrategy(),
            api_version or "5.103",
            error_dispatcher or ErrorDispatcher()
        )

    def get_context(self) -> APIOptionsRequestContext:
        return APIOptionsRequestContext(self.default_api_options)
