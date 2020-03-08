from vkwave_types.responses import *
from ._category import Category


class Market(Category):
    def add(
        self,
        owner_id: typing.Optional[int],
        name: typing.Optional[str],
        description: typing.Optional[str],
        category_id: typing.Optional[int],
        price: typing.Optional[int],
        old_price: typing.Optional[int],
        deleted: typing.Optional[bool],
        main_photo_id: typing.Optional[int],
        photo_ids: typing.Optional[typing.List[int]],
        url: typing.Optional[str],
    ) -> MarketAddResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param name: - Item name.
        :param description: - Item description.
        :param category_id: - Item category ID.
        :param price: - Item price.
        :param old_price:
        :param deleted: - Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: - Cover photo ID.
        :param photo_ids: - IDs of additional photos.
        :param url: - Url for button in market item.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("add", params)
        result = MarketAddResponse(**raw_result)
        return result

    def add_album(
        self,
        owner_id: typing.Optional[int],
        title: typing.Optional[str],
        photo_id: typing.Optional[int],
        main_album: typing.Optional[bool],
    ) -> MarketAddAlbumResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param title: - Collection title.
        :param photo_id: - Cover photo ID.
        :param main_album: - Set as main ('1' – set, '0' – no).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addAlbum", params)
        result = MarketAddAlbumResponse(**raw_result)
        return result

    def add_to_album(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param album_ids: - Collections IDs to add item to.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addToAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def create_comment(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        message: typing.Optional[str],
        attachments: typing.Optional[typing.List[str]],
        from_group: typing.Optional[bool],
        reply_to_comment: typing.Optional[int],
        sticker_id: typing.Optional[int],
        guid: typing.Optional[str],
    ) -> MarketCreateCommentResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param message: - Comment text (required if 'attachments' parameter is not specified)
        :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: - '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: - ID of a comment to reply with current comment to.
        :param sticker_id: - Sticker ID.
        :param guid: - Random value to avoid resending one comment.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createComment", params)
        result = MarketCreateCommentResponse(**raw_result)
        return result

    def delete(
        self, owner_id: typing.Optional[int], item_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def delete_album(
        self, owner_id: typing.Optional[int], album_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an collection owner community.
        :param album_id: - Collection ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def delete_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> MarketDeleteCommentResponse:
        """
        :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: - comment id
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteComment", params)
        result = MarketDeleteCommentResponse(**raw_result)
        return result

    def edit(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        name: typing.Optional[str],
        description: typing.Optional[str],
        category_id: typing.Optional[int],
        price: typing.Optional[int],
        deleted: typing.Optional[bool],
        main_photo_id: typing.Optional[int],
        photo_ids: typing.Optional[typing.List[int]],
        url: typing.Optional[str],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param name: - Item name.
        :param description: - Item description.
        :param category_id: - Item category ID.
        :param price: - Item price.
        :param deleted: - Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: - Cover photo ID.
        :param photo_ids: - IDs of additional photos.
        :param url: - Url for button in market item.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_album(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        title: typing.Optional[str],
        photo_id: typing.Optional[int],
        main_album: typing.Optional[bool],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an collection owner community.
        :param album_id: - Collection ID.
        :param title: - Collection title.
        :param photo_id: - Cover photo id
        :param main_album: - Set as main ('1' – set, '0' – no).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def edit_comment(
        self,
        owner_id: typing.Optional[int],
        comment_id: typing.Optional[int],
        message: typing.Optional[str],
        attachments: typing.Optional[typing.List[str]],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param comment_id: - Comment ID.
        :param message: - New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        count: typing.Optional[int],
        offset: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> MarketGetResponse:
        """
        :param owner_id: - ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id:
        :param count: - Number of items to return.
        :param offset: - Offset needed to return a specific subset of results.
        :param extended: - '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = MarketGetResponse(**raw_result)
        return result

    def get_album_by_id(
        self,
        owner_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
    ) -> MarketGetAlbumByIdResponse:
        """
        :param owner_id: - identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: - collections identifiers to obtain data from
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbumById", params)
        result = MarketGetAlbumByIdResponse(**raw_result)
        return result

    def get_albums(
        self,
        owner_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> MarketGetAlbumsResponse:
        """
        :param owner_id: - ID of an items owner community.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of items to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbums", params)
        result = MarketGetAlbumsResponse(**raw_result)
        return result

    def get_by_id(
        self,
        item_ids: typing.Optional[typing.List[str]],
        extended: typing.Optional[bool],
    ) -> MarketGetByIdResponse:
        """
        :param item_ids: - Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: - '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = MarketGetByIdResponse(**raw_result)
        return result

    def get_categories(
        self, count: typing.Optional[int], offset: typing.Optional[int],
    ) -> MarketGetCategoriesResponse:
        """
        :param count: - Number of results to return.
        :param offset: - Offset needed to return a specific subset of results.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCategories", params)
        result = MarketGetCategoriesResponse(**raw_result)
        return result

    def get_comments(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        need_likes: typing.Optional[bool],
        start_comment_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        sort: typing.Optional[str],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
    ) -> MarketGetCommentsResponse:
        """
        :param owner_id: - ID of an item owner community
        :param item_id: - Item ID.
        :param need_likes: - '1' — to return likes info.
        :param start_comment_id: - ID of a comment to start a list from (details below).
        :param offset:
        :param count: - Number of results to return.
        :param sort: - Sort order ('asc' — from old to new, 'desc' — from new to old)
        :param extended: - '1' — comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: - List of additional profile fields to return. See the [vk.com/dev/fields|details]
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = MarketGetCommentsResponse(**raw_result)
        return result

    def remove_from_album(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param album_ids: - Collections IDs to remove item from.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeFromAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_albums(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        before: typing.Optional[int],
        after: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param album_id: - Collection ID.
        :param before: - ID of a collection to place current collection before it.
        :param after: - ID of a collection to place current collection after it.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderAlbums", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_items(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        item_id: typing.Optional[int],
        before: typing.Optional[int],
        after: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param album_id: - ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param item_id: - Item ID.
        :param before: - ID of an item to place current item before it.
        :param after: - ID of an item to place current item after it.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderItems", params)
        result = OkResponse(**raw_result)
        return result

    def report(
        self,
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
        reason: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("report", params)
        result = OkResponse(**raw_result)
        return result

    def report_comment(
        self,
        owner_id: typing.Optional[int],
        comment_id: typing.Optional[int],
        reason: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param comment_id: - Comment ID.
        :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reportComment", params)
        result = OkResponse(**raw_result)
        return result

    def restore(
        self, owner_id: typing.Optional[int], item_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Deleted item ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restore", params)
        result = OkResponse(**raw_result)
        return result

    def restore_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> MarketRestoreCommentResponse:
        """
        :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: - deleted comment id
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restoreComment", params)
        result = MarketRestoreCommentResponse(**raw_result)
        return result

    def search(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        q: typing.Optional[str],
        price_from: typing.Optional[int],
        price_to: typing.Optional[int],
        tags: typing.Optional[typing.List[int]],
        sort: typing.Optional[int],
        rev: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
        status: typing.Optional[int],
    ) -> MarketSearchResponse:
        """
        :param owner_id: - ID of an items owner community.
        :param album_id:
        :param q: - Search query, for example "pink slippers".
        :param price_from: - Minimum item price value.
        :param price_to: - Maximum item price value.
        :param tags: - Comma-separated tag IDs list.
        :param sort:
        :param rev: - '0' — do not use reverse order, '1' — use reverse order
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of items to return.
        :param extended: - '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = MarketSearchResponse(**raw_result)
        return result
