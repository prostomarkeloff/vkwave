from vkwave_client.types import MethodName
from vkwave_client.context import ResultState
import typing

if typing.TYPE_CHECKING:
	from vkwave_api.methods._abc import APIOptionsRequestContext

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
        result = typing.cast(dict, result)

        if "error" in result:
            err_handler_result = await self.__api.handle_error(result["error"])
            if err_handler_result:
                result = err_handler_result

        return result
