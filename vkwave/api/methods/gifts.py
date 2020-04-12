from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Gifts(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, GiftsGetResponse]:
        """
        :param user_id: - User ID.
        :param count: - Number of gifts to return.
        :param offset: - Offset needed to return a specific subset of results.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = GiftsGetResponse(**raw_result)
        return result
