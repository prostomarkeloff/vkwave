from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Pages(Category):
    async def clear_cache(
        self, url: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param url: - Address of the page where you need to refesh the cached version
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("clearCache", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        page_id: typing.Optional[int] = None,
        global_: typing.Optional[BaseBoolInt] = None,
        site_preview: typing.Optional[BaseBoolInt] = None,
        title: typing.Optional[str] = None,
        need_source: typing.Optional[bool] = None,
        need_html: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, PagesGetResponse]:
        """
        :param owner_id: - Page owner ID.
        :param page_id: - Wiki page ID.
        :param global_: - '1' — to return information about a global wiki page
        :param site_preview: - '1' — resulting wiki page is a preview for the attached link
        :param title: - Wiki page title.
        :param need_source:
        :param need_html: - '1' — to return the page as HTML,
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = PagesGetResponse(**raw_result)
        return result

    async def get_history(
        self,
        page_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, PagesGetHistoryResponse]:
        """
        :param page_id: - Wiki page ID.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getHistory", params)
        if return_raw_response:
            return raw_result

        result = PagesGetHistoryResponse(**raw_result)
        return result

    async def get_titles(
        self, return_raw_response: bool = False, group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, PagesGetTitlesResponse]:
        """
        :param group_id: - ID of the community that owns the wiki page.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTitles", params)
        if return_raw_response:
            return raw_result

        result = PagesGetTitlesResponse(**raw_result)
        return result

    async def get_version(
        self,
        version_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        need_html: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, PagesGetVersionResponse]:
        """
        :param version_id:
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :param need_html: - '1' — to return the page as HTML
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getVersion", params)
        if return_raw_response:
            return raw_result

        result = PagesGetVersionResponse(**raw_result)
        return result

    async def parse_wiki(
        self, text: str, return_raw_response: bool = False, group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, PagesParseWikiResponse]:
        """
        :param text: - Text of the wiki page.
        :param group_id: - ID of the group in the context of which this markup is interpreted.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("parseWiki", params)
        if return_raw_response:
            return raw_result

        result = PagesParseWikiResponse(**raw_result)
        return result

    async def save(
        self,
        return_raw_response: bool = False,
        text: typing.Optional[str] = None,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
    ) -> typing.Union[dict, PagesSaveResponse]:
        """
        :param text: - Text of the wiki page in wiki-format.
        :param page_id: - Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id: - User ID
        :param title: - Wiki page title.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("save", params)
        if return_raw_response:
            return raw_result

        result = PagesSaveResponse(**raw_result)
        return result

    async def save_access(
        self,
        page_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        view: typing.Optional[BaseBoolInt] = None,
        edit: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, PagesSaveAccessResponse]:
        """
        :param page_id: - Wiki page ID.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :param view: - Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: - Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("saveAccess", params)
        if return_raw_response:
            return raw_result

        result = PagesSaveAccessResponse(**raw_result)
        return result
