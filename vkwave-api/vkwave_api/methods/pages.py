from vkwave_types.responses import *
from ._category import Category


class Pages(Category):
    def clear_cache(self, url: typing.Optional[str] = None,) -> OkResponse:
        """
        :param url: - Address of the page where you need to refesh the cached version
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("clearCache", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        owner_id: typing.Optional[int] = None,
        page_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        site_preview: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        need_source: typing.Optional[bool] = None,
        need_html: typing.Optional[bool] = None,
    ) -> PagesGetResponse:
        """
        :param owner_id: - Page owner ID.
        :param page_id: - Wiki page ID.
        :param global_: - '1' — to return information about a global wiki page
        :param site_preview: - '1' — resulting wiki page is a preview for the attached link
        :param title: - Wiki page title.
        :param need_source:
        :param need_html: - '1' — to return the page as HTML,
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = PagesGetResponse(**raw_result)
        return result

    def get_history(
        self,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
    ) -> PagesGetHistoryResponse:
        """
        :param page_id: - Wiki page ID.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getHistory", params)
        result = PagesGetHistoryResponse(**raw_result)
        return result

    def get_titles(
        self, group_id: typing.Optional[int] = None,
    ) -> PagesGetTitlesResponse:
        """
        :param group_id: - ID of the community that owns the wiki page.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getTitles", params)
        result = PagesGetTitlesResponse(**raw_result)
        return result

    def get_version(
        self,
        version_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        need_html: typing.Optional[bool] = None,
    ) -> PagesGetVersionResponse:
        """
        :param version_id:
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :param need_html: - '1' — to return the page as HTML
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getVersion", params)
        result = PagesGetVersionResponse(**raw_result)
        return result

    def parse_wiki(
        self, text: typing.Optional[str] = None, group_id: typing.Optional[int] = None,
    ) -> PagesParseWikiResponse:
        """
        :param text: - Text of the wiki page.
        :param group_id: - ID of the group in the context of which this markup is interpreted.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("parseWiki", params)
        result = PagesParseWikiResponse(**raw_result)
        return result

    def save(
        self,
        text: typing.Optional[str] = None,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
    ) -> PagesSaveResponse:
        """
        :param text: - Text of the wiki page in wiki-format.
        :param page_id: - Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id: - User ID
        :param title: - Wiki page title.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("save", params)
        result = PagesSaveResponse(**raw_result)
        return result

    def save_access(
        self,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
        edit: typing.Optional[int] = None,
    ) -> PagesSaveAccessResponse:
        """
        :param page_id: - Wiki page ID.
        :param group_id: - ID of the community that owns the wiki page.
        :param user_id:
        :param view: - Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: - Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveAccess", params)
        result = PagesSaveAccessResponse(**raw_result)
        return result
