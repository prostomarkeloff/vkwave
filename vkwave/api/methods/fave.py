from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Fave(Category):
    async def add_article(
        self, url: str = None, raw: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param url:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addArticle", params)
        if raw:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def add_link(
        self, link: str = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param link: - Link URL.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addLink", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def add_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id:
        :param group_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addPage", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def add_post(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addPost", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def add_product(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addProduct", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def add_tag(
        self, name: typing.Optional[str] = None, raw: bool = False,
    ) -> typing.Union[dict, FaveAddTagResponse]:
        """
        :param name:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addTag", params)
        if raw:
            return raw_result

        result = FaveAddTagResponse(**raw_result)
        return result

    async def add_video(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addVideo", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_tag(
        self, id: int = None, name: str = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param id:
        :param name:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editTag", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        extended: typing.Optional[BaseBoolInt] = None,
        item_type: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        is_from_snackbar: typing.Optional[bool] = None,
        raw: bool = False,
    ) -> typing.Union[dict, FaveGetResponse, FaveGetExtendedResponse]:
        """
        :param extended: - '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: - Tag ID.
        :param offset: - Offset needed to return a specific subset of users.
        :param count: - Number of users to return.
        :param fields:
        :param is_from_snackbar:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = (
            FaveGetResponse(**raw_result)
            if not extended
            else FaveGetExtendedResponse(**raw_result)
        )
        return result

    async def get_pages(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        tag_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, FaveGetPagesResponse]:
        """
        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPages", params)
        if raw:
            return raw_result

        result = FaveGetPagesResponse(**raw_result)
        return result

    async def get_tags(
        self, raw: bool = False,
    ) -> typing.Union[dict, FaveGetTagsResponse]:
        """
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTags", params)
        if raw:
            return raw_result

        result = FaveGetTagsResponse(**raw_result)
        return result

    async def mark_seen(
        self, raw: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markSeen", params)
        if raw:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def remove_article(
        self, owner_id: int = None, article_id: int = None, raw: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param owner_id:
        :param article_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeArticle", params)
        if raw:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def remove_link(
        self,
        link_id: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param link_id: - Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: - Link URL
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeLink", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def remove_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id:
        :param group_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removePage", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def remove_post(
        self, owner_id: int = None, id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removePost", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def remove_product(
        self, owner_id: int = None, id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeProduct", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def remove_tag(
        self, id: int = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeTag", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def reorder_tags(
        self, ids: typing.List[int] = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param ids:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderTags", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_page_tags(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id:
        :param group_id:
        :param tag_ids:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setPageTags", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_tags(
        self,
        item_type: typing.Optional[str] = None,
        item_owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        link_id: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setTags", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def track_page_interaction(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id:
        :param group_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("trackPageInteraction", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result
