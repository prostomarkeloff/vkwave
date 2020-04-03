from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class App(Category):
    async def widgets_update(
        self, code: str = None, type: str = None, raw: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param code:
        :param type:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("update", params)
        if raw:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
