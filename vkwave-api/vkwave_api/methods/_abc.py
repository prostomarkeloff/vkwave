from vkwave_client.abstract import AbstractAPIClient
from vkwave_client.types import MethodName
from vkwave_client.context import ResultState
from vkwave_api.token.token import ABCToken
from typing import Optional, cast

class TemporaryException(Exception):
    """It means nothing."""

class Category:
    def __init__(self, name: str):
        self.category_name = name
    
    def make_method_name(self, method_name: str) -> MethodName:
        return MethodName(f"{self.category_name}.{method_name}")

    async def api_request(self, client: AbstractAPIClient, method_name: str, params: dict) -> dict:
        method_name = self.make_method_name(method_name)
        ctx = client.create_request(method_name, params)
        await ctx.send_request()

        state = ctx.result.state

        if state is not ResultState.SUCCESS:
            raise TemporaryException()

        result = ctx.result.data
        result = cast(dict, result)
        return result

class RequestOptions:
    def __init__(self, client: AbstractAPIClient, token: ABCToken, api_version: str = "5.103"):
        self.client = client
        self.token = token
        self.v = api_version

class API:
    def __init__(self):
        self._curr_client: Optional[AbstractAPIClient] = None
        self._curr_token: Optional[ABCToken] = None
        self._curr_version: str = "5.103"

        self.messages = Category("messages")

    def with_options(self, options: RequestOptions) -> "API":
        self._curr_client = options.client
        self._curr_token = options.token
        self._curr_version = options.v
        return self
