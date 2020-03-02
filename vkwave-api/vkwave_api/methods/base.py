from vkwave_client.abstract import AbstractAPIClient
from vkwave_client.types import MethodName

class MethodsCategory:
    def __init__(self, name: str):
        self.category_name = name

    async def api_request(self, client: AbstractAPIClient, method_name: str, params: dict) -> dict:
        method_name = self.prepare_method_name(method_name)
        ctx = client.create_request(method_name, params)
        await ctx.send_request()

        # TODO: error handling. i hate it...
        return ctx

    def prepare_method_name(self, method_name_second_part: str) -> MethodName:
        return MethodName(f"{self.category_name}.{method_name_second_part}")

class MethodsWrapper:
    def __init__(self):
        # TODO: all categories

