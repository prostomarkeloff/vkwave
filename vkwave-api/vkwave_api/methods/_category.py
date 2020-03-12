from vkwave_client.types import MethodName
from vkwave_client.context import ResultState
from ._error import UnsuccessAPIRequestException
import typing

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
        client, token = await self.__api.api_options.get_client_and_token()
        method_name = self.make_method_name(method_name)

        params = self.__api.api_options.update_pre_request_params(params, token)
        ctx = client.create_request(method_name, params)
        await ctx.send_request()

        state = ctx.result.state
        
        exc_data = None
        data = None
        
        if state is ResultState.UNHANDLED_EXCEPTION:
            raise UnsuccessAPIRequestException()
        elif state is ResultState.HANDLED_EXCEPTION:
            exc_data = ctx.result.exception_data
            exc_data = typing.cast(dict, exc_data)
            if not ("error" in exc_data or "response" in exc_data):
                raise UnsuccessAPIRequestException()
        else:
            data = ctx.result.data
            data = typing.cast(dict, data)

        result = data or exc_data
        result = typing.cast(dict, result)

        if "error" in result:
            err_handler_result = await self.__api.handle_error(result)
            if err_handler_result:
                result = err_handler_result

        return result
