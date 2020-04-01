from vkwave.types.responses import *

from ._category import Category


class Utils(Category):
    async def check_link(self, url: str = None, ) -> UtilsCheckLinkResponse:
        """
        :param url: - Link to check (e.g., 'http://google.com').
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("checkLink", params)
        result = UtilsCheckLinkResponse(**raw_result)
        return result

    async def delete_from_last_shortened(self, key: str = None, ) -> OkResponse:
        """
        :param key: - Link key (characters after vk.cc/).
        :return:
        """

        params = {}
        for key_, value in locals().items():
            if key_ not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key_] = value

        raw_result = await self.api_request("deleteFromLastShortened", params)
        result = OkResponse(**raw_result)
        return result

    async def get_last_shortened_links(
            self, count: typing.Optional[int] = None, offset: typing.Optional[int] = None,
    ) -> UtilsGetLastShortenedLinksResponse:
        """
        :param count: - Number of links to return.
        :param offset: - Offset needed to return a specific subset of links.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getLastShortenedLinks", params)
        result = UtilsGetLastShortenedLinksResponse(**raw_result)
        return result

    async def get_link_stats(
            self,
            key: str = None,
            source: typing.Optional[str] = None,
            access_key: typing.Optional[str] = None,
            interval: typing.Optional[str] = None,
            intervals_count: typing.Optional[int] = None,
            extended: typing.Optional[bool] = None,
    ) -> UtilsGetLinkStatsResponse:
        """
        :param key: - Link key (characters after vk.cc/).
        :param source: - Source of scope
        :param access_key: - Access key for private link stats.
        :param interval: - Interval.
        :param intervals_count: - Number of intervals to return.
        :param extended: - 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        :return:
        """

        params = {}
        for key_, value in locals().items():
            if key_ not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key_] = value

        raw_result = await self.api_request("getLinkStats", params)
        result = UtilsGetLinkStatsResponse(**raw_result)
        return result

    async def get_server_time(self, ) -> UtilsGetServerTimeResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getServerTime", params)
        result = UtilsGetServerTimeResponse(**raw_result)
        return result

    async def get_short_link(
            self, url: str = None, private: typing.Optional[bool] = None,
    ) -> UtilsGetShortLinkResponse:
        """
        :param url: - URL to be shortened.
        :param private: - 1 — private stats, 0 — public stats.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getShortLink", params)
        result = UtilsGetShortLinkResponse(**raw_result)
        return result

    async def resolve_screen_name(
            self, screen_name: str = None,
    ) -> UtilsResolveScreenNameResponse:
        """
        :param screen_name: - Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("resolveScreenName", params)
        result = UtilsResolveScreenNameResponse(**raw_result)
        return result
