from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Market(Category):
    async def add(
        self,
        owner_id: int,
        name: str,
        description: str,
        category_id: int,
        main_photo_id: int,
        return_raw_response: bool = False,
        price: typing.Optional[int] = None,
        old_price: typing.Optional[int] = None,
        deleted: typing.Optional[BaseBoolInt] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        url: typing.Optional[str] = None,
    ) -> typing.Union[dict, MarketAddResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if return_raw_response:
            return raw_result

        result = MarketAddResponse(**raw_result)
        return result

    async def add_album(
        self,
        owner_id: int,
        title: str,
        return_raw_response: bool = False,
        photo_id: typing.Optional[int] = None,
        main_album: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, MarketAddAlbumResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param title: - Collection title.
        :param photo_id: - Cover photo ID.
        :param main_album: - Set as main ('1' – set, '0' – no).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addAlbum", params)
        if return_raw_response:
            return raw_result

        result = MarketAddAlbumResponse(**raw_result)
        return result

    async def add_to_album(
        self,
        owner_id: int,
        item_id: int,
        album_ids: typing.List[int],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param album_ids: - Collections IDs to add item to.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addToAlbum", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def create_comment(
        self,
        owner_id: int,
        item_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> typing.Union[dict, MarketCreateCommentResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param message: - Comment text (required if 'attachments' parameter is not specified)
        :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: - '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: - ID of a comment to reply with current comment to.
        :param sticker_id: - Sticker ID.
        :param guid: - Random value to avoid resending one comment.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if return_raw_response:
            return raw_result

        result = MarketCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self, owner_id: int, item_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_album(
        self, owner_id: int, album_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an collection owner community.
        :param album_id: - Collection ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteAlbum", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_comment(
        self, owner_id: int, comment_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, MarketDeleteCommentResponse]:
        """
        :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: - comment id
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteComment", params)
        if return_raw_response:
            return raw_result

        result = MarketDeleteCommentResponse(**raw_result)
        return result

    async def edit(
        self,
        owner_id: int,
        item_id: int,
        name: str,
        description: str,
        category_id: int,
        price: int,
        main_photo_id: int,
        return_raw_response: bool = False,
        deleted: typing.Optional[BaseBoolInt] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        url: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_album(
        self,
        owner_id: int,
        album_id: int,
        title: str,
        return_raw_response: bool = False,
        photo_id: typing.Optional[int] = None,
        main_album: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an collection owner community.
        :param album_id: - Collection ID.
        :param title: - Collection title.
        :param photo_id: - Cover photo id
        :param main_album: - Set as main ('1' – set, '0' – no).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editAlbum", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        owner_id: int,
        comment_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[BaseBoolInt] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param comment_id: - Comment ID.
        :param message: - New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, MarketGetResponse, MarketGetExtendedResponse]:
        """
        :param owner_id: - ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id:
        :param count: - Number of items to return.
        :param offset: - Offset needed to return a specific subset of results.
        :param extended: - '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = (
            MarketGetResponse(**raw_result)
            if not extended
            else MarketGetExtendedResponse(**raw_result)
        )
        return result

    async def get_album_by_id(
        self, owner_id: int, album_ids: typing.List[int], return_raw_response: bool = False,
    ) -> typing.Union[dict, MarketGetAlbumByIdResponse]:
        """
        :param owner_id: - identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: - collections identifiers to obtain data from
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAlbumById", params)
        if return_raw_response:
            return raw_result

        result = MarketGetAlbumByIdResponse(**raw_result)
        return result

    async def get_albums(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, MarketGetAlbumsResponse]:
        """
        :param owner_id: - ID of an items owner community.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of items to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAlbums", params)
        if return_raw_response:
            return raw_result

        result = MarketGetAlbumsResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        item_ids: typing.List[str],
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, MarketGetByIdResponse, MarketGetByIdExtendedResponse]:
        """
        :param item_ids: - Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: - '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = (
            MarketGetByIdResponse(**raw_result)
            if not extended
            else MarketGetByIdExtendedResponse(**raw_result)
        )
        return result

    async def get_categories(
        self,
        return_raw_response: bool = False,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, MarketGetCategoriesResponse]:
        """
        :param count: - Number of results to return.
        :param offset: - Offset needed to return a specific subset of results.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCategories", params)
        if return_raw_response:
            return raw_result

        result = MarketGetCategoriesResponse(**raw_result)
        return result

    async def get_comments(
        self,
        owner_id: int,
        item_id: int,
        return_raw_response: bool = False,
        need_likes: typing.Optional[BaseBoolInt] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, MarketGetCommentsResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = MarketGetCommentsResponse(**raw_result)
        return result

    async def remove_from_album(
        self,
        owner_id: int,
        item_id: int,
        album_ids: typing.List[int],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param album_ids: - Collections IDs to remove item from.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeFromAlbum", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def reorder_albums(
        self,
        owner_id: int,
        album_id: int,
        return_raw_response: bool = False,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param album_id: - Collection ID.
        :param before: - ID of a collection to place current collection before it.
        :param after: - ID of a collection to place current collection after it.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderAlbums", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def reorder_items(
        self,
        owner_id: int,
        item_id: int,
        return_raw_response: bool = False,
        album_id: typing.Optional[BaseBoolInt] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param album_id: - ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param item_id: - Item ID.
        :param before: - ID of an item to place current item before it.
        :param after: - ID of an item to place current item after it.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderItems", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def report(
        self,
        owner_id: int,
        item_id: int,
        return_raw_response: bool = False,
        reason: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Item ID.
        :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("report", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def report_comment(
        self,
        owner_id: int,
        comment_id: int,
        reason: BaseBoolInt,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param comment_id: - Comment ID.
        :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reportComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def restore(
        self, owner_id: int, item_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of an item owner community.
        :param item_id: - Deleted item ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restore", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def restore_comment(
        self, owner_id: int, comment_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, MarketRestoreCommentResponse]:
        """
        :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: - deleted comment id
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        if return_raw_response:
            return raw_result

        result = MarketRestoreCommentResponse(**raw_result)
        return result

    async def search(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        album_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        tags: typing.Optional[typing.List[int]] = None,
        sort: typing.Optional[int] = None,
        rev: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        status: typing.Optional[int] = None,
    ) -> typing.Union[dict, MarketSearchResponse, MarketSearchExtendedResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = (
            MarketSearchResponse(**raw_result)
            if not extended
            else MarketSearchExtendedResponse(**raw_result)
        )
        return result
