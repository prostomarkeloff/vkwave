from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Stats(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        group_id: Optional[int] = None,
        app_id: Optional[int] = None,
        timestamp_from: Optional[int] = None,
        timestamp_to: Optional[int] = None,
        interval: Optional[str] = None,
        intervals_count: Optional[int] = None,
        filters: Optional[List[str]] = None,
        stats_groups: Optional[List[str]] = None,
        extended: Optional[BaseBoolInt] = None,
    ) -> Union[dict, StatsGetResponse]:
        """
        :param group_id: - Community ID.
        :param app_id: - Application ID.
        :param timestamp_from:
        :param timestamp_to:
        :param interval:
        :param intervals_count:
        :param filters:
        :param stats_groups:
        :param extended:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = StatsGetResponse(**raw_result)
        return result

    async def get_post_reach(
        self,
        owner_id: str,
        post_ids: List[int],
        return_raw_response: bool = False,
    ) -> Union[dict, StatsGetPostReachResponse]:
        """
        :param owner_id: - post owner community id. Specify with "-" sign.
        :param post_ids: - wall posts id
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPostReach", params)
        if return_raw_response:
            return raw_result

        result = StatsGetPostReachResponse(**raw_result)
        return result

    async def track_visitor(
        self,
        id: str,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("trackVisitor", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
