from vkwave.types.responses import *
from ._category import Category


class Gifts(Category):
    async def get(
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
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("get", params)
        result = GiftsGetResponse(**raw_result)
        return result
