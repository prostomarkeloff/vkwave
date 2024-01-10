from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Podcasts(Category):
    async def clear_recent_searches(
        self,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("clearRecentSearches", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)

    async def get_popular(
        self,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, PodcastsGetPopularResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPopular", params)
        if return_raw_response:
            return raw_result

        return PodcastsGetPopularResponse(**raw_result)

    async def get_recent_search_requests(
        self,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, PodcastsGetRecentSearchRequestsResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRecentSearchRequests", params)
        if return_raw_response:
            return raw_result

        return PodcastsGetRecentSearchRequestsResponse(**raw_result)

    async def search(
        self,
        search_string: str,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, PodcastsSearchResponse]:
        """
        :param search_string:
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        return PodcastsSearchResponse(**raw_result)
