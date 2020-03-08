from vkwave_types.responses import *
from ._category import Category


class App(Category):
    def widgets_update(
        self, code: typing.Optional[str] = None, type: typing.Optional[str] = None,
    ) -> BaseOkResponse:
        """
        :param code:
        :param type:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("update", params)
        result = BaseOkResponse(**raw_result)
        return result
