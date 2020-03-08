from vkwave_types.responses import *
from ._category import Category


class Newsfeed(Category):
    def add_ban(
        self,
        user_ids: typing.Optional[typing.List[int]],
        group_ids: typing.Optional[typing.List[int]],
    ) -> OkResponse:
        """
        :param user_ids:
        :param group_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addBan", params)
        result = OkResponse(**raw_result)
        return result

    def delete_ban(
        self,
        user_ids: typing.Optional[typing.List[int]],
        group_ids: typing.Optional[typing.List[int]],
    ) -> OkResponse:
        """
        :param user_ids:
        :param group_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteBan", params)
        result = OkResponse(**raw_result)
        return result

    def delete_list(self, list_id: typing.Optional[int],) -> OkResponse:
        """
        :param list_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteList", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        filters: typing.Optional[typing.List[NewsfeedFilters]],
        return_banned: typing.Optional[bool],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        max_photos: typing.Optional[int],
        source_ids: typing.Optional[str],
        start_from: typing.Optional[str],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
        section: typing.Optional[str],
    ) -> NewsfeedGetResponse:
        """
        :param filters: - Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends, 'note' — new notes
        :param return_banned: - '1' — to return news items from banned sources
        :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: - Maximum number of photos to return. By default, '5'.
        :param source_ids: - Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
        :param start_from: - identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
        :param count: - Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param section:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = NewsfeedGetResponse(**raw_result)
        return result

    def get_banned(
        self,
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
        name_case: typing.Optional[str],
    ) -> NewsfeedGetBannedResponse:
        """
        :param extended: - '1' — return extra information about users and communities
        :param fields: - Profile fields to return.
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getBanned", params)
        result = NewsfeedGetBannedResponse(**raw_result)
        return result

    def get_comments(
        self,
        count: typing.Optional[int],
        filters: typing.Optional[typing.List[NewsfeedCommentsFilters]],
        reposts: typing.Optional[str],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        last_comments_count: typing.Optional[int],
        start_from: typing.Optional[str],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> NewsfeedGetCommentsResponse:
        """
        :param count: - Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param filters: - Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
        :param reposts: - Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
        :param start_time: - Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a comment to return. By default, the current time.
        :param last_comments_count:
        :param start_from: - Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = NewsfeedGetCommentsResponse(**raw_result)
        return result

    def get_lists(
        self,
        list_ids: typing.Optional[typing.List[int]],
        extended: typing.Optional[bool],
    ) -> NewsfeedGetListsResponse:
        """
        :param list_ids: - numeric list identifiers.
        :param extended: - Return additional list info
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLists", params)
        result = NewsfeedGetListsResponse(**raw_result)
        return result

    def get_mentions(
        self,
        owner_id: typing.Optional[int],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> NewsfeedGetMentionsResponse:
        """
        :param owner_id: - Owner ID.
        :param start_time: - Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: - Offset needed to return a specific subset of posts.
        :param count: - Number of posts to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMentions", params)
        result = NewsfeedGetMentionsResponse(**raw_result)
        return result

    def get_recommended(
        self,
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        max_photos: typing.Optional[int],
        start_from: typing.Optional[str],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> NewsfeedGetRecommendedResponse:
        """
        :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: - Maximum number of photos to return. By default, '5'.
        :param start_from: - 'new_from' value obtained in previous call.
        :param count: - Number of news items to return.
        :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRecommended", params)
        result = NewsfeedGetRecommendedResponse(**raw_result)
        return result

    def get_suggested_sources(
        self,
        offset: typing.Optional[int],
        count: typing.Optional[int],
        shuffle: typing.Optional[bool],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> NewsfeedGetSuggestedSourcesResponse:
        """
        :param offset: - offset required to choose a particular subset of communities or users.
        :param count: - amount of communities or users to return.
        :param shuffle: - shuffle the returned list or not.
        :param fields: - list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSuggestedSources", params)
        result = NewsfeedGetSuggestedSourcesResponse(**raw_result)
        return result

    def ignore_item(
        self,
        type: typing.Optional[str],
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("ignoreItem", params)
        result = OkResponse(**raw_result)
        return result

    def save_list(
        self,
        list_id: typing.Optional[int],
        title: typing.Optional[str],
        source_ids: typing.Optional[typing.List[int]],
        no_reposts: typing.Optional[bool],
    ) -> NewsfeedSaveListResponse:
        """
        :param list_id: - numeric list identifier (if not sent, will be set automatically).
        :param title: - list name.
        :param source_ids: - users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param no_reposts: - reposts display on and off ('1' is for off).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveList", params)
        result = NewsfeedSaveListResponse(**raw_result)
        return result

    def search(
        self,
        q: typing.Optional[str],
        extended: typing.Optional[bool],
        count: typing.Optional[int],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        start_from: typing.Optional[str],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
    ) -> NewsfeedSearchResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = NewsfeedSearchResponse(**raw_result)
        return result

    def unignore_item(
        self,
        type: typing.Optional[str],
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("unignoreItem", params)
        result = OkResponse(**raw_result)
        return result

    def unsubscribe(
        self,
        type: typing.Optional[str],
        owner_id: typing.Optional[int],
        item_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param type: - Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
        :param owner_id: - Object owner ID.
        :param item_id: - Object ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("unsubscribe", params)
        result = OkResponse(**raw_result)
        return result
