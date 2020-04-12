from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Likes(Category):
    async def add(
        self,
        type: str,
        item_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
    ) -> typing.Union[dict, LikesAddResponse]:
        """
        :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: - ID of the user or community that owns the object.
        :param item_id: - Object ID.
        :param access_key: - Access key required for an object owned by a private entity.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if return_raw_response:
            return raw_result

        result = LikesAddResponse(**raw_result)
        return result

    async def delete(
        self,
        type: str,
        item_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, LikesDeleteResponse]:
        """
        :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: - ID of the user or community that owns the object.
        :param item_id: - Object ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = LikesDeleteResponse(**raw_result)
        return result

    async def get_list(
        self,
        type: str,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        page_url: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        friends_only: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[BaseBoolInt] = None,
        skip_own: typing.Optional[bool] = None,
    ) -> typing.Union[dict, LikesGetListResponse, LikesGetListExtendedResponse]:
        """
        :param type: - , Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: - ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
        :param item_id: - Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
        :param page_url: - URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
        :param filter: - Filters to apply: 'likes' — returns information about all users who liked the object (default), 'copies' — returns information only about users who told their friends about the object
        :param friends_only: - Specifies which users are returned: '1' — to return only the current user's friends, '0' — to return all users (default)
        :param extended: - Specifies whether extended information will be returned. '1' — to return extended information about users and communities from the 'Likes' list, '0' — to return no additional information (default)
        :param offset: - Offset needed to select a specific subset of users.
        :param count: - Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
        :param skip_own:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getList", params)
        if return_raw_response:
            return raw_result

        result = (
            LikesGetListResponse(**raw_result)
            if not extended
            else LikesGetListExtendedResponse(**raw_result)
        )
        return result

    async def is_liked(
        self,
        type: str,
        item_id: int,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, LikesIsLikedResponse]:
        """
        :param user_id: - User ID.
        :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion
        :param owner_id: - ID of the user or community that owns the object.
        :param item_id: - Object ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("isLiked", params)
        if return_raw_response:
            return raw_result

        result = LikesIsLikedResponse(**raw_result)
        return result
