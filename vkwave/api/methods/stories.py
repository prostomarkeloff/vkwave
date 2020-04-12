from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Stories(Category):
    async def ban_owner(
        self, owners_ids: typing.List[int], return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owners_ids: - List of sources IDs
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("banOwner", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete(
        self, owner_id: int, story_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - Story owner's ID. Current user id is used by default.
        :param story_id: - Story ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, StoriesGetResponse, StoriesGetExtendedResponse]:
        """
        :param owner_id: - Owner ID.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = (
            StoriesGetResponse(**raw_result)
            if not extended
            else StoriesGetExtendedResponse(**raw_result)
        )
        return result

    async def get_banned(
        self,
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, StoriesGetBannedResponse, StoriesGetBannedExtendedResponse]:
        """
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getBanned", params)
        if return_raw_response:
            return raw_result

        result = (
            StoriesGetBannedResponse(**raw_result)
            if not extended
            else StoriesGetBannedExtendedResponse(**raw_result)
        )
        return result

    async def get_by_id(
        self,
        stories: typing.List[str],
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, StoriesGetByIdResponse, StoriesGetByIdExtendedResponse]:
        """
        :param stories: - Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = (
            StoriesGetByIdResponse(**raw_result)
            if not extended
            else StoriesGetByIdExtendedResponse(**raw_result)
        )
        return result

    async def get_photo_upload_server(
        self,
        return_raw_response: bool = False,
        add_to_news: typing.Optional[BaseBoolInt] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        reply_to_story: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, StoriesGetPhotoUploadServerResponse]:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPhotoUploadServer", params)
        if return_raw_response:
            return raw_result

        result = StoriesGetPhotoUploadServerResponse(**raw_result)
        return result

    async def get_replies(
        self,
        owner_id: int,
        story_id: int,
        return_raw_response: bool = False,
        access_key: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, StoriesGetRepliesResponse, StoriesGetRepliesExtendedResponse]:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param access_key: - Access key for the private object.
        :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: - Additional fields to return
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getReplies", params)
        if return_raw_response:
            return raw_result

        result = (
            StoriesGetRepliesResponse(**raw_result)
            if not extended
            else StoriesGetRepliesExtendedResponse(**raw_result)
        )
        return result

    async def get_stats(
        self, owner_id: int, story_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, StoriesGetStatsResponse]:
        """
        :param owner_id: - Story owner ID. 
        :param story_id: - Story ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getStats", params)
        if return_raw_response:
            return raw_result

        result = StoriesGetStatsResponse(**raw_result)
        return result

    async def get_video_upload_server(
        self,
        return_raw_response: bool = False,
        add_to_news: typing.Optional[BaseBoolInt] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        reply_to_story: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, StoriesGetVideoUploadServerResponse]:
        """
        :param add_to_news: - 1 — to add the story to friend's feed.
        :param user_ids: - List of users IDs who can see the story.
        :param reply_to_story: - ID of the story to reply with the current.
        :param link_text: - Link text (for community's stories only).
        :param link_url: - Link URL. Internal links on https://vk.com only.
        :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getVideoUploadServer", params)
        if return_raw_response:
            return raw_result

        result = StoriesGetVideoUploadServerResponse(**raw_result)
        return result

    async def get_viewers(
        self,
        owner_id: int,
        story_id: int,
        return_raw_response: bool = False,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, StoriesGetViewersResponse, StoriesGetViewersExtendedResponse]:
        """
        :param owner_id: - Story owner ID.
        :param story_id: - Story ID.
        :param count: - Maximum number of results.
        :param offset: - Offset needed to return a specific subset of results.
        :param extended: - '1' — to return detailed information about photos
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getViewers", params)
        if return_raw_response:
            return raw_result

        result = (
            StoriesGetViewersResponse(**raw_result)
            if not extended
            else StoriesGetViewersExtendedResponse(**raw_result)
        )
        return result

    async def hide_all_replies(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("hideAllReplies", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def hide_reply(
        self, owner_id: int, story_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user whose replies should be hidden.
        :param story_id: - Story ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("hideReply", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def unban_owner(
        self, owners_ids: typing.List[int], return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owners_ids: - List of hidden sources to show stories from.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unbanOwner", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def search(
        self,
        q: str,
        place_id: typing.Optional[int] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        radius: typing.Optional[int] = None,
        mentioned_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, StoriesSearchResponseModel]:

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = StoriesSearchResponseModel(**raw_result)
        return result
