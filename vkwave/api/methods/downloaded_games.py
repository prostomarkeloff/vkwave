from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class DownloadedGames(Category):
    async def games_get_paid_status(
        self,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
    ) -> Union[dict, DownloadedGamesPaidStatusResponse]:
        """
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPaidStatus", params)
        if return_raw_response:
            return raw_result

        result = DownloadedGamesPaidStatusResponse(**raw_result)
        return result
