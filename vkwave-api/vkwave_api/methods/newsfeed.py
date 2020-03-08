from vkwave_types.responses import *
from ._category import Category


class Newsfeed(Category):
    async def add_ban(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        group_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param user_ids:
        :param group_ids:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addBan", params)
        result = OkResponse(**raw_result)
        return result

    async def delete_ban(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        group_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param user_ids:
        :param group_ids:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("deleteBan", params)
        result = OkResponse(**raw_result)
        return result

    async def delete_list(self, list_id: typing.Optional[int] = None,) -> OkResponse:
        """
        :param list_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("deleteList", params)
        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        filters: typing.Optional[typing.List[NewsfeedFilters]] = None,
        return_banned: typing.Optional[bool] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        max_photos: typing.Optional[int] = None,
        source_ids: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        section: typing.Optional[str] = None,
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = NewsfeedGetResponse(**raw_result)
        return result

    async def get_banned(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> NewsfeedGetBannedResponse:
        """
        :param extended: - '1' — return extra information about users and communities
        :param fields: - Profile fields to return.
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getBanned", params)
        result = NewsfeedGetBannedResponse(**raw_result)
        return result

    async def get_comments(
        self,
        count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[NewsfeedCommentsFilters]] = None,
        reposts: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        last_comments_count: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getComments", params)
        result = NewsfeedGetCommentsResponse(**raw_result)
        return result

    async def get_lists(
        self,
        list_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[bool] = None,
    ) -> NewsfeedGetListsResponse:
        """
        :param list_ids: - numeric list identifiers.
        :param extended: - Return additional list info
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getLists", params)
        result = NewsfeedGetListsResponse(**raw_result)
        return result

    async def get_mentions(
        self,
        owner_id: typing.Optional[int] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> NewsfeedGetMentionsResponse:
        """
        :param owner_id: - Owner ID.
        :param start_time: - Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: - Offset needed to return a specific subset of posts.
        :param count: - Number of posts to return.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getMentions", params)
        result = NewsfeedGetMentionsResponse(**raw_result)
        return result

    async def get_recommended(
        self,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        max_photos: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getRecommended", params)
        result = NewsfeedGetRecommendedResponse(**raw_result)
        return result

    async def get_suggested_sources(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        shuffle: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> NewsfeedGetSuggestedSourcesResponse:
        """
        :param offset: - offset required to choose a particular subset of communities or users.
        :param count: - amount of communities or users to return.
        :param shuffle: - shuffle the returned list or not.
        :param fields: - list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getSuggestedSources", params)
        result = NewsfeedGetSuggestedSourcesResponse(**raw_result)
        return result

    async def ignore_item(
        self,
        type: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("ignoreItem", params)
        result = OkResponse(**raw_result)
        return result

    async def save_list(
        self,
        list_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        source_ids: typing.Optional[typing.List[int]] = None,
        no_reposts: typing.Optional[bool] = None,
    ) -> NewsfeedSaveListResponse:
        """
        :param list_id: - numeric list identifier (if not sent, will be set automatically).
        :param title: - list name.
        :param source_ids: - users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param no_reposts: - reposts display on and off ('1' is for off).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveList", params)
        result = NewsfeedSaveListResponse(**raw_result)
        return result

    async def search(
        self,
        q: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("search", params)
        result = NewsfeedSearchResponse(**raw_result)
        return result

    async def unignore_item(
        self,
        type: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: - Item identifier
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unignoreItem", params)
        result = OkResponse(**raw_result)
        return result

    async def unsubscribe(
        self,
        type: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param type: - Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
        :param owner_id: - Object owner ID.
        :param item_id: - Object ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unsubscribe", params)
        result = OkResponse(**raw_result)
        return result
