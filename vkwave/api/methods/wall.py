from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Wall(Category):
    async def close_comments(
        self, owner_id: int, post_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param owner_id:
        :param post_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("closeComments", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def create_comment(
        self,
        post_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        from_group: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        reply_to_comment: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> typing.Union[dict, WallCreateCommentResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param from_group: - Group ID.
        :param message: - (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: - ID of comment to reply.
        :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: - Sticker ID.
        :param guid: - Unique identifier to avoid repeated comments.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if return_raw_response:
            return raw_result

        result = WallCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - ID of the post to be deleted.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        post_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        publish_date: typing.Optional[int] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        close_comments: typing.Optional[bool] = None,
        poster_bkg_id: typing.Optional[int] = None,
        poster_bkg_owner_id: typing.Optional[int] = None,
        poster_bkg_access_hash: typing.Optional[str] = None,
    ) -> typing.Union[dict, WallEditResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id:
        :param friends_only:
        :param message: - (Required if 'attachments' is not set.) Text of the post.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
        :param services:
        :param signed:
        :param publish_date:
        :param lat:
        :param long:
        :param place_id:
        :param mark_as_ads:
        :param close_comments:
        :param poster_bkg_id:
        :param poster_bkg_owner_id:
        :param poster_bkg_access_hash:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = WallEditResponse(**raw_result)
        return result

    async def edit_ads_stealth(
        self,
        post_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[BaseBoolInt] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        place_id: typing.Optional[int] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID. Used for publishing of scheduled and suggested posts.
        :param message: - (Required if 'attachments' is not set.) Text of the post.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: - ID of the location where the user was tagged.
        :param link_button: - Link button ID
        :param link_title: - Link title
        :param link_image: - Link image url
        :param link_video: - Link video ID in format "<owner_id>_<media_id>"
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editAdsStealth", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
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
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[BaseBoolInt] = None,
        filter: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, WallGetResponse, WallGetExtendedResponse]:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param domain: - User or community short address.
        :param offset: - Offset needed to return a specific subset of posts.
        :param count: - Number of posts to return (maximum 100).
        :param filter: - Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall
        :param extended: - '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = (
            WallGetResponse(**raw_result)
            if not extended
            else WallGetExtendedResponse(**raw_result)
        )
        return result

    async def get_by_id(
        self,
        posts: typing.List[str],
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, WallGetByIdResponse, WallGetByIdExtendedResponse]:
        """
        :param posts: - User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: - '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
        :param copy_history_depth: - Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = (
            WallGetByIdResponse(**raw_result)
            if not extended
            else WallGetByIdExtendedResponse(**raw_result)
        )
        return result

    async def get_comments(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        need_likes: typing.Optional[BaseBoolInt] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[BaseBoolInt] = None,
        sort: typing.Optional[str] = None,
        preview_length: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
    ) -> typing.Union[dict, WallGetCommentsResponse, WallGetCommentsExtendedResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param need_likes: - '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: - Offset needed to return a specific subset of comments.
        :param count: - Number of comments to return (maximum 100).
        :param sort: - Sort order: 'asc' — chronological, 'desc' — reverse chronological
        :param preview_length: - Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
        :param extended:
        :param fields:
        :param comment_id: - Comment ID.
        :param thread_items_count: - Count items in threads.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = (
            WallGetCommentsResponse(**raw_result)
            if not extended
            else WallGetCommentsExtendedResponse(**raw_result)
        )
        return result

    async def get_reposts(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, WallGetRepostsResponse]:
        """
        :param owner_id: - User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param offset: - Offset needed to return a specific subset of reposts.
        :param count: - Number of reposts to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getReposts", params)
        if return_raw_response:
            return raw_result

        result = WallGetRepostsResponse(**raw_result)
        return result

    async def open_comments(
        self, owner_id: int, post_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param owner_id:
        :param post_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("openComments", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def pin(
        self,
        post_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("pin", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def post(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        friends_only: typing.Optional[BaseBoolInt] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[BaseBoolInt] = None,
        publish_date: typing.Optional[int] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        place_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        mark_as_ads: typing.Optional[bool] = None,
        close_comments: typing.Optional[bool] = None,
        mute_notifications: typing.Optional[bool] = None,
    ) -> typing.Union[dict, WallPostResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only: - '1' — post will be available to friends only, '0' — post will be available to all users (default)
        :param from_group: - For a community: '1' — post will be published by the community, '0' — post will be published by the user (default)
        :param message: - (Required if 'attachments' is not set.) Text of the post.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param services: - List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
        :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param publish_date: - Publication date (in Unix time). If used, posting will be delayed until the set time.
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: - ID of the location where the user was tagged.
        :param post_id: - Post ID. Used for publishing of scheduled and suggested posts.
        :param guid:
        :param mark_as_ads:
        :param close_comments:
        :param mute_notifications:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("post", params)
        if return_raw_response:
            return raw_result

        result = WallPostResponse(**raw_result)
        return result

    async def post_ads_stealth(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[BaseBoolInt] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        place_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
    ) -> typing.Union[dict, WallPostAdsStealthResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param message: - (Required if 'attachments' is not set.) Text of the post.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: - ID of the location where the user was tagged.
        :param guid: - Unique identifier to avoid duplication the same post.
        :param link_button: - Link button ID
        :param link_title: - Link title
        :param link_image: - Link image url
        :param link_video: - Link video ID in format "<owner_id>_<media_id>"
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("postAdsStealth", params)
        if return_raw_response:
            return raw_result

        result = WallPostAdsStealthResponse(**raw_result)
        return result

    async def report_comment(
        self,
        owner_id: int,
        comment_id: int,
        return_raw_response: bool = False,
        reason: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the wall.
        :param comment_id: - Comment ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reportComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def report_post(
        self,
        owner_id: int,
        post_id: int,
        return_raw_response: bool = False,
        reason: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the wall.
        :param post_id: - Post ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reportPost", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def repost(
        self,
        object: str,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        mute_notifications: typing.Optional[bool] = None,
    ) -> typing.Union[dict, WallRepostResponse]:
        """
        :param object: - ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param message: - Comment to be added along with the reposted object.
        :param group_id: - Target community ID when reposting to a community.
        :param mark_as_ads:
        :param mute_notifications:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("repost", params)
        if return_raw_response:
            return raw_result

        result = WallRepostResponse(**raw_result)
        return result

    async def restore(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: - ID of the post to be restored.
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
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def search(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        owners_only: typing.Optional[BaseBoolInt] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> typing.Union[dict, WallSearchResponse, WallSearchExtendedResponse]:
        """
        :param owner_id: - user or community id. "Remember that for a community 'owner_id' must be negative."
        :param domain: - user or community screen name.
        :param query: - search query string.
        :param owners_only: - '1' – returns only page owner's posts.
        :param count: - count of posts to return.
        :param offset: - Offset needed to return a specific subset of posts.
        :param extended: - show extended post info.
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = (
            WallSearchResponse(**raw_result)
            if not extended
            else WallSearchExtendedResponse(**raw_result)
        )
        return result

    async def unpin(
        self,
        post_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unpin", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
