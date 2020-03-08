from vkwave_types.responses import *
from ._category import Category


class Stats(Category):
    def get(
        self,
        group_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        timestamp_from: typing.Optional[int] = None,
        timestamp_to: typing.Optional[int] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        stats_groups: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
    ) -> StatsGetResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = StatsGetResponse(**raw_result)
        return result

    def get_post_reach(
        self,
        owner_id: typing.Optional[str] = None,
        post_id: typing.Optional[int] = None,
    ) -> StatsGetPostReachResponse:
        """
        :param owner_id: - post owner community id. Specify with "-" sign.
        :param post_id: - wall post id. Note that stats are available only for '300' last (newest) posts on a community wall.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getPostReach", params)
        result = StatsGetPostReachResponse(**raw_result)
        return result

    def track_visitor(self, id: typing.Optional[str] = None,) -> OkResponse:
        """
        :param id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("trackVisitor", params)
        result = OkResponse(**raw_result)
        return result
