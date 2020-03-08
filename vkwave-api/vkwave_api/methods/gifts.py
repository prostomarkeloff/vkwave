from vkwave_types.responses import *
from ._category import Category


class Gifts(Category):
    def get(
        self,
        user_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> GiftsGetResponse:
        """
        :param user_id: - User ID.
        :param count: - Number of gifts to return.
        :param offset: - Offset needed to return a specific subset of results.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = GiftsGetResponse(**raw_result)
        return result
