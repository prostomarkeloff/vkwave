from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Newsfeed(Category):
    async def add_ban(
        self,
        return_raw_response: bool = False,
        user_ids: Optional[List[int]] = None,
        group_ids: Optional[List[int]] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param user_ids:
        :param group_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addBan", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def delete_ban(
        self,
        return_raw_response: bool = False,
        user_ids: Optional[List[int]] = None,
        group_ids: Optional[List[int]] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param user_ids:
        :param group_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteBan", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def delete_list(
        self,
        list_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param list_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteList", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        filters: Optional[List[NewsfeedCommentsFilters]] = None,
        return_banned: Optional[BaseBoolInt] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        max_photos: Optional[int] = None,
        source_ids: Optional[str] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
        section: Optional[str] = None,
    ) -> Union[dict, NewsfeedGetResponse]:
        """
        :param filters: - Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends
        :param return_banned: - '1' — to return news items from banned sources
        :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: - Maximum number of photos to return. By default, '5'.
        :param source_ids: - Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
        :param start_from: - identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
        :param count: - Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param section:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedGetResponse(**raw_result)
        return result

    async def get_banned(
        self,
        return_raw_response: bool = False,
        extended: Optional[BaseBoolInt] = None,
        fields: Optional[List[UsersFields]] = None,
        name_case: Optional[str] = None,
    ) -> Union[dict, NewsfeedGetBannedResponse, NewsfeedGetBannedExtendedResponse]:
        """
        :param extended: - '1' — return extra information about users and communities
        :param fields: - Profile fields to return.
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getBanned", params)
        if return_raw_response:
            return raw_result

        result = (
            NewsfeedGetBannedResponse(**raw_result)
            if not extended
            else NewsfeedGetBannedExtendedResponse(**raw_result)
        )
        return result

    async def get_comments(
        self,
        return_raw_response: bool = False,
        count: Optional[int] = None,
        filters: Optional[List[NewsfeedCommentsFilters]] = None,
        reposts: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        last_comments_count: Optional[int] = None,
        start_from: Optional[str] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
    ) -> Union[dict, NewsfeedGetCommentsResponse]:
        """
        :param count: - Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param filters: - Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
        :param reposts: - Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
        :param start_time: - Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a comment to return. By default, the current time.
        :param last_comments_count:
        :param start_from: - Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedGetCommentsResponse(**raw_result)
        return result

    async def get_lists(
        self,
        return_raw_response: bool = False,
        list_ids: Optional[List[int]] = None,
        extended: Optional[BaseBoolInt] = None,
    ) -> Union[dict, NewsfeedGetListsResponse, NewsfeedGetListsExtendedResponse]:
        """
        :param list_ids: - numeric list identifiers.
        :param extended: - Return additional list info
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLists", params)
        if return_raw_response:
            return raw_result

        result = (
            NewsfeedGetListsResponse(**raw_result)
            if not extended
            else NewsfeedGetListsExtendedResponse(**raw_result)
        )
        return result

    async def get_mentions(
        self,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, NewsfeedGetMentionsResponse]:
        """
        :param owner_id: - Owner ID.
        :param start_time: - Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: - Offset needed to return a specific subset of posts.
        :param count: - Number of posts to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMentions", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedGetMentionsResponse(**raw_result)
        return result

    async def get_recommended(
        self,
        return_raw_response: bool = False,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        max_photos: Optional[int] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
    ) -> Union[dict, NewsfeedGetRecommendedResponse]:
        """
        :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: - Maximum number of photos to return. By default, '5'.
        :param start_from: - 'new_from' value obtained in previous call.
        :param count: - Number of news items to return.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRecommended", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedGetRecommendedResponse(**raw_result)
        return result

    async def get_suggested_sources(
        self,
        return_raw_response: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        shuffle: Optional[bool] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
    ) -> Union[dict, NewsfeedGetSuggestedSourcesResponse]:
        """
        :param offset: - offset required to choose a particular subset of communities or users.
        :param count: - amount of communities or users to return.
        :param shuffle: - shuffle the returned list or not.
        :param fields: - list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSuggestedSources", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedGetSuggestedSourcesResponse(**raw_result)
        return result

    async def ignore_item(
        self,
        type: str,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        item_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("ignoreItem", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def save_list(
        self,
        title: str,
        return_raw_response: bool = False,
        list_id: Optional[int] = None,
        source_ids: Optional[List[int]] = None,
        no_reposts: Optional[BaseBoolInt] = None,
    ) -> Union[dict, NewsfeedSaveListResponse]:
        """
        :param list_id: - numeric list identifier (if not sent, will be set automatically).
        :param title: - list name.
        :param source_ids: - users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param no_reposts: - reposts display on and off ('1' is for off).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("saveList", params)
        if return_raw_response:
            return raw_result

        result = NewsfeedSaveListResponse(**raw_result)
        return result

    async def search(
        self,
        return_raw_response: bool = False,
        q: Optional[str] = None,
        extended: Optional[BaseBoolInt] = None,
        count: Optional[int] = None,
        latitude: Optional[int] = None,
        longitude: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        start_from: Optional[str] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
    ) -> Union[dict, NewsfeedSearchResponse, NewsfeedSearchExtendedResponse]:
        """
        :param q: - Search query string (e.g., 'New Year').
        :param extended: - '1' — to return additional information about the user or community that placed the post.
        :param count: - Number of posts to return.
        :param latitude: - Geographical latitude point (in degrees, -90 to 90) within which to search.
        :param longitude: - Geographical longitude point (in degrees, -180 to 180) within which to search.
        :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param start_from:
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = (
            NewsfeedSearchResponse(**raw_result)
            if not extended
            else NewsfeedSearchExtendedResponse(**raw_result)
        )
        return result

    async def unignore_item(
        self,
        type: str,
        owner_id: int,
        item_id: int,
        return_raw_response: bool = False,
        track_code: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :param track_code: - Track code of unignored item
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unignoreItem", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def unsubscribe(
        self,
        type: str,
        item_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param type: - Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
        :param owner_id: - Object owner ID.
        :param item_id: - Object ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unsubscribe", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
