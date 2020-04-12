from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class App(Category):
    async def widgets_update(
        self, code: str, type: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param code:
        :param type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("update", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
