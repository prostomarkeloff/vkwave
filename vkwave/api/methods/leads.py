from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Leads(Category):
    async def check_user(
        self,
        lead_id: int,
        return_raw_response: bool = False,
        test_result: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        auto_start: typing.Optional[bool] = None,
        age: typing.Optional[int] = None,
        country: typing.Optional[str] = None,
    ) -> typing.Union[dict, LeadsCheckUserResponse]:
        """
        :param lead_id: - Lead ID.
        :param test_result: - Value to be return in 'result' field when test mode is used.
        :param test_mode:
        :param auto_start:
        :param age: - User age.
        :param country: - User country code.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("checkUser", params)
        if return_raw_response:
            return raw_result

        result = LeadsCheckUserResponse(**raw_result)
        return result

    async def complete(
        self,
        vk_sid: str,
        secret: str,
        return_raw_response: bool = False,
        comment: typing.Optional[str] = None,
    ) -> typing.Union[dict, LeadsCompleteResponse]:
        """
        :param vk_sid: - Session obtained as GET parameter when session started.
        :param secret: - Secret key from the lead testing interface.
        :param comment: - Comment text.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("complete", params)
        if return_raw_response:
            return raw_result

        result = LeadsCompleteResponse(**raw_result)
        return result

    async def get_stats(
        self,
        lead_id: int,
        return_raw_response: bool = False,
        secret: typing.Optional[str] = None,
        date_start: typing.Optional[BaseBoolInt] = None,
        date_end: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, LeadsGetStatsResponse]:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key obtained from the lead testing interface.
        :param date_start: - Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: - Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getStats", params)
        if return_raw_response:
            return raw_result

        result = LeadsGetStatsResponse(**raw_result)
        return result

    async def get_users(
        self,
        offer_id: int,
        secret: str,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        status: typing.Optional[BaseBoolInt] = None,
        reverse: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, LeadsGetUsersResponse]:
        """
        :param offer_id: - Offer ID.
        :param secret: - Secret key obtained in the lead testing interface.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param status: - Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: - Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUsers", params)
        if return_raw_response:
            return raw_result

        result = LeadsGetUsersResponse(**raw_result)
        return result

    async def metric_hit(
        self, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, LeadsMetricHitResponse]:
        """
        :param data: - Metric data obtained in the lead interface.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("metricHit", params)
        if return_raw_response:
            return raw_result

        result = LeadsMetricHitResponse(**raw_result)
        return result

    async def start(
        self,
        lead_id: int,
        secret: str,
        return_raw_response: bool = False,
        uid: typing.Optional[int] = None,
        aid: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        force: typing.Optional[bool] = None,
    ) -> typing.Union[dict, LeadsStartResponse]:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key from the lead testing interface.
        :param uid:
        :param aid:
        :param test_mode:
        :param force:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("start", params)
        if return_raw_response:
            return raw_result

        result = LeadsStartResponse(**raw_result)
        return result
