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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = GiftsGetResponse(**raw_result)
        return result
