from vkwave_types.responses import *
from ._category import Category


class App(Category):
    async def widgets_update(
        self, code: str = None, type: str = None,
    ) -> BaseOkResponse:
        """
        :param code:
        :param type:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("update", params)
        result = BaseOkResponse(**raw_result)
        return result
