from vkwave_types.responses import *
from ._category import Category


class Leads(Category):
    async def check_user(
        self,
        lead_id: typing.Optional[int] = None,
        test_result: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        auto_start: typing.Optional[bool] = None,
        age: typing.Optional[int] = None,
        country: typing.Optional[str] = None,
    ) -> LeadsCheckUserResponse:
        """
        :param lead_id: - Lead ID.
        :param test_result: - Value to be return in 'result' field when test mode is used.
        :param test_mode:
        :param auto_start:
        :param age: - User age.
        :param country: - User country code.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("checkUser", params)
        result = LeadsCheckUserResponse(**raw_result)
        return result

    async def complete(
        self,
        vk_sid: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
    ) -> LeadsCompleteResponse:
        """
        :param vk_sid: - Session obtained as GET parameter when session started.
        :param secret: - Secret key from the lead testing interface.
        :param comment: - Comment text.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("complete", params)
        result = LeadsCompleteResponse(**raw_result)
        return result

    async def get_stats(
        self,
        lead_id: typing.Optional[int] = None,
        secret: typing.Optional[str] = None,
        date_start: typing.Optional[str] = None,
        date_end: typing.Optional[str] = None,
    ) -> LeadsGetStatsResponse:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key obtained from the lead testing interface.
        :param date_start: - Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: - Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getStats", params)
        result = LeadsGetStatsResponse(**raw_result)
        return result

    async def get_users(
        self,
        offer_id: typing.Optional[int] = None,
        secret: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        reverse: typing.Optional[bool] = None,
    ) -> LeadsGetUsersResponse:
        """
        :param offer_id: - Offer ID.
        :param secret: - Secret key obtained in the lead testing interface.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param status: - Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: - Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getUsers", params)
        result = LeadsGetUsersResponse(**raw_result)
        return result

    async def metric_hit(
        self, data: typing.Optional[str] = None,
    ) -> LeadsMetricHitResponse:
        """
        :param data: - Metric data obtained in the lead interface.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("metricHit", params)
        result = LeadsMetricHitResponse(**raw_result)
        return result

    async def start(
        self,
        lead_id: typing.Optional[int] = None,
        secret: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
        aid: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        force: typing.Optional[bool] = None,
    ) -> LeadsStartResponse:
        """
        :param lead_id: - Lead ID.
        :param secret: - Secret key from the lead testing interface.
        :param uid:
        :param aid:
        :param test_mode:
        :param force:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("start", params)
        result = LeadsStartResponse(**raw_result)
        return result
