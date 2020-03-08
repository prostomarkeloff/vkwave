from vkwave_types.responses import *
from ._category import Category


class Stories(Category):
    def ban_owner(
        self, owners_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param owners_ids: - List of sources IDs
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("banOwner", params)
        result = OkResponse(**raw_result)
        return result

    def delete(
        self,
        owner_id: typing.Optional[int] = None,
        story_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - Story owner's ID. Current user id is used by default.
        :param story_id: - Story ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        owner_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
    ) -> StoriesGetResponse:
        """
        :param owner_id: - Owner ID.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = StoriesGetResponse(**raw_result)
        return result

    def get_banned(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> StoriesGetBannedResponse:
        """
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getBanned", params)
        result = StoriesGetBannedResponse(**raw_result)
        return result

    def get_by_id(
        self,
        stories: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> StoriesGetByIdResponse:
        """
        :param stories: - Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getById", params)
        result = StoriesGetByIdResponse(**raw_result)
        return result

    def get_photo_upload_server(
        self,
        add_to_news: typing.Optional[bool] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        reply_to_story: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> StoriesGetPhotoUploadServerResponse:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getPhotoUploadServer", params)
        result = StoriesGetPhotoUploadServerResponse(**raw_result)
        return result

    def get_replies(
        self,
        owner_id: typing.Optional[int] = None,
        story_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> StoriesGetRepliesResponse:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param access_key: - Access key for the private object.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getReplies", params)
        result = StoriesGetRepliesResponse(**raw_result)
        return result

    def get_stats(
        self,
        owner_id: typing.Optional[int] = None,
        story_id: typing.Optional[int] = None,
    ) -> StoriesGetStatsResponse:
        """
        :param owner_id: - Story owner ID. 
        :param story_id: - Story ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getStats", params)
        result = StoriesGetStatsResponse(**raw_result)
        return result

    def get_video_upload_server(
        self,
        add_to_news: typing.Optional[bool] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        reply_to_story: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> StoriesGetVideoUploadServerResponse:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getVideoUploadServer", params)
        result = StoriesGetVideoUploadServerResponse(**raw_result)
        return result

    def get_viewers(
        self,
        owner_id: typing.Optional[int] = None,
        story_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
    ) -> StoriesGetViewersResponse:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param count: - Maximum number of results.
        :param offset: - Offset needed to return a specific subset of results.
        :param extended: - '1' — to return detailed information about photos
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getViewers", params)
        result = StoriesGetViewersResponse(**raw_result)
        return result

    def hide_all_replies(
        self,
        owner_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param group_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("hideAllReplies", params)
        result = OkResponse(**raw_result)
        return result

    def hide_reply(
        self,
        owner_id: typing.Optional[int] = None,
        story_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param story_id: - Story ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("hideReply", params)
        result = OkResponse(**raw_result)
        return result

    def unban_owner(
        self, owners_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param owners_ids: - List of hidden sources to show stories from.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unbanOwner", params)
        result = OkResponse(**raw_result)
        return result
