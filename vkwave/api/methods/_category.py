import typing

from vkwave.client.context import ResultState
from vkwave.client.types import MethodName

from ._error import Error, UnsuccessAPIRequestException

if typing.TYPE_CHECKING:
    from ._abc import APIOptionsRequestContext


class TemporaryException(Exception):
    """It means nothing."""


class Category:
    def __init__(self, name: str, api: "APIOptionsRequestContext"):
        self.category_name = name
        self.__api = api

    def make_method_name(self, method_name: str) -> MethodName:
        return MethodName(f"{self.category_name}.{method_name}")

    async def api_request(self, method_name: str, params: dict) -> dict:
        return await self.__api.api_request(self.make_method_name(method_name), params)
