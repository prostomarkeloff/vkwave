from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Utils(Category):
    async def check_link(
        self, url: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, UtilsCheckLinkResponse]:
        """
        :param url: - Link to check (e.g., 'http://google.com').
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("checkLink", params)
        if return_raw_response:
            return raw_result

        result = UtilsCheckLinkResponse(**raw_result)
        return result

    async def delete_from_last_shortened(
        self, key: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param key: - Link key (characters after vk.cc/).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteFromLastShortened", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get_last_shortened_links(
        self,
        return_raw_response: bool = False,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, UtilsGetLastShortenedLinksResponse]:
        """
        :param count: - Number of links to return.
        :param offset: - Offset needed to return a specific subset of links.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLastShortenedLinks", params)
        if return_raw_response:
            return raw_result

        result = UtilsGetLastShortenedLinksResponse(**raw_result)
        return result

    async def get_link_stats(
        self,
        key: str,
        return_raw_response: bool = False,
        source: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, UtilsGetLinkStatsResponse, UtilsGetLinkStatsExtendedResponse]:
        """
        :param key: - Link key (characters after vk.cc/).
        :param source: - Source of scope
        :param access_key: - Access key for private link stats.
        :param interval: - Interval.
        :param intervals_count: - Number of intervals to return.
        :param extended: - 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLinkStats", params)
        if return_raw_response:
            return raw_result

        result = (
            UtilsGetLinkStatsResponse(**raw_result)
            if not extended
            else UtilsGetLinkStatsExtendedResponse(**raw_result)
        )
        return result

    async def get_server_time(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, UtilsGetServerTimeResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getServerTime", params)
        if return_raw_response:
            return raw_result

        result = UtilsGetServerTimeResponse(**raw_result)
        return result

    async def get_short_link(
        self,
        url: str,
        return_raw_response: bool = False,
        private: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, UtilsGetShortLinkResponse]:
        """
        :param url: - URL to be shortened.
        :param private: - 1 — private stats, 0 — public stats.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getShortLink", params)
        if return_raw_response:
            return raw_result

        result = UtilsGetShortLinkResponse(**raw_result)
        return result

    async def resolve_screen_name(
        self, screen_name: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, UtilsResolveScreenNameResponse]:
        """
        :param screen_name: - Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("resolveScreenName", params)
        if return_raw_response:
            return raw_result

        result = UtilsResolveScreenNameResponse(**raw_result)
        return result
