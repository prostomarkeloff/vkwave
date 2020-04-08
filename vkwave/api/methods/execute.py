from vkwave.types.responses import ExecuteResponse

from ._category import Category


class Execute(Category):
    async def __call__(self, code: str, return_raw_response: bool = False):

        raw_result = await self.api_request("", {"code": code})
        if return_raw_response:
            return raw_result

        result = ExecuteResponse(**raw_result)
        return result
