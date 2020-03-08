from vkwave_types.responses import *
from ._category import Category


class Fave(Category):
    def add_article(self, url: typing.Optional[str],) -> BaseBoolResponse:
        """
        :param url:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addArticle", params)
        result = BaseBoolResponse(**raw_result)
        return result

    def add_link(self, link: typing.Optional[str],) -> OkResponse:
        """
        :param link: - Link URL.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addLink", params)
        result = OkResponse(**raw_result)
        return result

    def add_page(
        self, user_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addPage", params)
        result = OkResponse(**raw_result)
        return result

    def add_post(
        self,
        owner_id: typing.Optional[int],
        id: typing.Optional[int],
        access_key: typing.Optional[str],
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addPost", params)
        result = OkResponse(**raw_result)
        return result

    def add_product(
        self,
        owner_id: typing.Optional[int],
        id: typing.Optional[int],
        access_key: typing.Optional[str],
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addProduct", params)
        result = OkResponse(**raw_result)
        return result

    def add_tag(self, name: typing.Optional[str],) -> FaveAddTagResponse:
        """
        :param name:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addTag", params)
        result = FaveAddTagResponse(**raw_result)
        return result

    def add_video(
        self,
        owner_id: typing.Optional[int],
        id: typing.Optional[int],
        access_key: typing.Optional[str],
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addVideo", params)
        result = OkResponse(**raw_result)
        return result

    def edit_tag(
        self, id: typing.Optional[int], name: typing.Optional[str],
    ) -> OkResponse:
        """
        :param id:
        :param name:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editTag", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        extended: typing.Optional[bool],
        item_type: typing.Optional[str],
        tag_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[str],
        is_from_snackbar: typing.Optional[bool],
    ) -> FaveGetResponse:
        """
        :param extended: - '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: - Tag ID.
        :param offset: - Offset needed to return a specific subset of users.
        :param count: - Number of users to return.
        :param fields:
        :param is_from_snackbar:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = FaveGetResponse(**raw_result)
        return result

    def get_pages(
        self,
        offset: typing.Optional[int],
        count: typing.Optional[int],
        type: typing.Optional[str],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
        tag_id: typing.Optional[int],
    ) -> FaveGetPagesResponse:
        """
        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getPages", params)
        result = FaveGetPagesResponse(**raw_result)
        return result

    def get_tags(self,) -> FaveGetTagsResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTags", params)
        result = FaveGetTagsResponse(**raw_result)
        return result

    def mark_seen(self,) -> BaseBoolResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markSeen", params)
        result = BaseBoolResponse(**raw_result)
        return result

    def remove_article(
        self, owner_id: typing.Optional[int], article_id: typing.Optional[int],
    ) -> BaseBoolResponse:
        """
        :param owner_id:
        :param article_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeArticle", params)
        result = BaseBoolResponse(**raw_result)
        return result

    def remove_link(
        self, link_id: typing.Optional[str], link: typing.Optional[str],
    ) -> OkResponse:
        """
        :param link_id: - Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: - Link URL
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeLink", params)
        result = OkResponse(**raw_result)
        return result

    def remove_page(
        self, user_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removePage", params)
        result = OkResponse(**raw_result)
        return result

    def remove_post(
        self, owner_id: typing.Optional[int], id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removePost", params)
        result = OkResponse(**raw_result)
        return result

    def remove_product(
        self, owner_id: typing.Optional[int], id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeProduct", params)
        result = OkResponse(**raw_result)
        return result

    def remove_tag(self, id: typing.Optional[int],) -> OkResponse:
        """
        :param id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeTag", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_tags(self, ids: typing.Optional[typing.List[int]],) -> OkResponse:
        """
        :param ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderTags", params)
        result = OkResponse(**raw_result)
        return result

    def set_page_tags(
        self,
        user_id: typing.Optional[int],
        group_id: typing.Optional[int],
        tag_ids: typing.Optional[typing.List[int]],
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :param tag_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setPageTags", params)
        result = OkResponse(**raw_result)
        return result

    def set_tags(
        self,
        item_type: typing.Optional[str],
        item_owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        tag_ids: typing.Optional[typing.List[int]],
        link_id: typing.Optional[str],
        link_url: typing.Optional[str],
    ) -> OkResponse:
        """
        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setTags", params)
        result = OkResponse(**raw_result)
        return result

    def track_page_interaction(
        self, user_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("trackPageInteraction", params)
        result = OkResponse(**raw_result)
        return result
