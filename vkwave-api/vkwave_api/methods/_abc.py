from vkwave_client.abstract import AbstractAPIClient
from vkwave_client.types import MethodName
from vkwave_client.context import ResultState
from vkwave_api.token.token import AnyABCToken, Token
from vkwave_api.token.strategy import ABCGetTokenStrategy, RandomGetTokenStrategy
from vkwave_api.methods._error import ErrorDispatcher, Error
from typing import Optional, cast, Tuple, List, Union, AsyncGenerator
from contextlib import asynccontextmanager
from .status import Status

import copy
import random


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

        self.status = Status("status", self)

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
            error_dispatcher or ErrorDispatcher(),
        )

    def get_context(self) -> APIOptionsRequestContext:
        return APIOptionsRequestContext(self.default_api_options)

    def with_token(self, token: AnyABCToken) -> APIOptionsRequestContext:
        copied = copy.copy(self.default_api_options)
        copied.tokens = [token]
        new = APIOptionsRequestContext(copied)
        return new

    @asynccontextmanager
    async def sync_token(self) -> AsyncGenerator[APIOptionsRequestContext, None]:
        """Grab random token and work only with it"""
        copied = copy.copy(self.default_api_options)
        copied.tokens = [random.choice(copied.tokens)]
        new = APIOptionsRequestContext(copied)
        yield new
        del copied
        del new
