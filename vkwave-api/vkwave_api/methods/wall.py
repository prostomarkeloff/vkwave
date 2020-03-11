from vkwave_types.responses import *
from ._category import Category


class Wall(Category):
    async def close_comments(
        self, owner_id: int = None, post_id: int = None,
    ) -> BaseBoolResponse:
        """
        :param owner_id:
        :param post_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("closeComments", params)
        result = BaseBoolResponse(**raw_result)
        return result

    async def create_comment(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: int = None,
        from_group: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        reply_to_comment: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> WallCreateCommentResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param from_group: - Group ID.
        :param message: - (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: - ID of comment to reply.
        :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: - Sticker ID.
        :param guid: - Unique identifier to avoid repeated comments.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("createComment", params)
        result = WallCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: - ID of the post to be deleted.
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

    async def delete_comment(
        self, owner_id: typing.Optional[int] = None, comment_id: int = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("deleteComment", params)
        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: int = None,
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
    ) -> WallEditResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("edit", params)
        result = WallEditResponse(**raw_result)
        return result

    async def edit_ads_stealth(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[bool] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
    ) -> OkResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("editAdsStealth", params)
        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        owner_id: typing.Optional[int] = None,
        comment_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> WallGetResponse:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param domain: - User or community short address.
        :param offset: - Offset needed to return a specific subset of posts.
        :param count: - Number of posts to return (maximum 100).
        :param filter: - Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall
        :param extended: - '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
        :param fields:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = WallGetResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        posts: typing.List[str] = None,
        extended: typing.Optional[bool] = None,
        copy_history_depth: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> WallGetByIdResponse:
        """
        :param posts: - User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: - '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
        :param copy_history_depth: - Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getById", params)
        result = WallGetByIdResponse(**raw_result)
        return result

    async def get_comments(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        preview_length: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        comment_id: typing.Optional[int] = None,
        thread_items_count: typing.Optional[int] = None,
    ) -> WallGetCommentsResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getComments", params)
        result = WallGetCommentsResponse(**raw_result)
        return result

    async def get_reposts(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> WallGetRepostsResponse:
        """
        :param owner_id: - User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :param offset: - Offset needed to return a specific subset of reposts.
        :param count: - Number of reposts to return.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getReposts", params)
        result = WallGetRepostsResponse(**raw_result)
        return result

    async def open_comments(
        self, owner_id: int = None, post_id: int = None,
    ) -> BaseBoolResponse:
        """
        :param owner_id:
        :param post_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("openComments", params)
        result = BaseBoolResponse(**raw_result)
        return result

    async def pin(
        self, owner_id: typing.Optional[int] = None, post_id: int = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("pin", params)
        result = OkResponse(**raw_result)
        return result

    async def post(
        self,
        owner_id: typing.Optional[int] = None,
        friends_only: typing.Optional[bool] = None,
        from_group: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        services: typing.Optional[str] = None,
        signed: typing.Optional[bool] = None,
        publish_date: typing.Optional[int] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        mark_as_ads: typing.Optional[bool] = None,
        close_comments: typing.Optional[bool] = None,
        mute_notifications: typing.Optional[bool] = None,
    ) -> WallPostResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("post", params)
        result = WallPostResponse(**raw_result)
        return result

    async def post_ads_stealth(
        self,
        owner_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        signed: typing.Optional[bool] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        link_button: typing.Optional[str] = None,
        link_title: typing.Optional[str] = None,
        link_image: typing.Optional[str] = None,
        link_video: typing.Optional[str] = None,
    ) -> WallPostAdsStealthResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("postAdsStealth", params)
        result = WallPostAdsStealthResponse(**raw_result)
        return result

    async def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the wall.
        :param comment_id: - Comment ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reportComment", params)
        result = OkResponse(**raw_result)
        return result

    async def report_post(
        self,
        owner_id: int = None,
        post_id: int = None,
        reason: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the wall.
        :param post_id: - Post ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reportPost", params)
        result = OkResponse(**raw_result)
        return result

    async def repost(
        self,
        object: str = None,
        message: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        mark_as_ads: typing.Optional[bool] = None,
        mute_notifications: typing.Optional[bool] = None,
    ) -> WallRepostResponse:
        """
        :param object: - ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param message: - Comment to be added along with the reposted object.
        :param group_id: - Target community ID when reposting to a community.
        :param mark_as_ads:
        :param mute_notifications:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("repost", params)
        result = WallRepostResponse(**raw_result)
        return result

    async def restore(
        self,
        owner_id: typing.Optional[int] = None,
        post_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: - ID of the post to be restored.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("restore", params)
        result = OkResponse(**raw_result)
        return result

    async def restore_comment(
        self, owner_id: typing.Optional[int] = None, comment_id: int = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: - Comment ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("restoreComment", params)
        result = OkResponse(**raw_result)
        return result

    async def search(
        self,
        owner_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        owners_only: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
    ) -> WallSearchResponse:
        """
        :param owner_id: - user or community id. "Remember that for a community 'owner_id' must be negative."
        :param domain: - user or community screen name.
        :param query: - search query string.
        :param owners_only: - '1' – returns only page owner's posts.
        :param count: - count of posts to return.
        :param offset: - Offset needed to return a specific subset of posts.
        :param extended: - show extended post info.
        :param fields:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("search", params)
        result = WallSearchResponse(**raw_result)
        return result

    async def unpin(
        self, owner_id: typing.Optional[int] = None, post_id: int = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: - Post ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unpin", params)
        result = OkResponse(**raw_result)
        return result
