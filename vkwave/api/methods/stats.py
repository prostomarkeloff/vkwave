from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Stats(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        timestamp_from: typing.Optional[int] = None,
        timestamp_to: typing.Optional[int] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        stats_groups: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, StatsGetResponse]:
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
        self, owner_id: str, post_id: BaseBoolInt, return_raw_response: bool = False,
    ) -> typing.Union[dict, StatsGetPostReachResponse]:
        """
        :param owner_id: - post owner community id. Specify with "-" sign.
        :param post_id: - wall post id. Note that stats are available only for '300' last (newest) posts on a community wall.
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
        self, id: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("trackVisitor", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
