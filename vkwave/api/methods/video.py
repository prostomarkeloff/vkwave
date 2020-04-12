from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Video(Category):
    async def add(
        self,
        video_id: int,
        owner_id: int,
        return_raw_response: bool = False,
        target_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param target_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def add_album(
        self,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        privacy: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, VideoAddAlbumResponse]:
        """
        :param group_id: - Community ID (if the album will be created in a community).
        :param title: - Album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addAlbum", params)
        if return_raw_response:
            return raw_result

        result = VideoAddAlbumResponse(**raw_result)
        return result

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        return_raw_response: bool = False,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
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
        video_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> typing.Union[dict, VideoCreateCommentResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: - '1' — to post the comment from a community name (only if 'owner_id'<0)
        :param reply_to_comment:
        :param sticker_id:
        :param guid:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if return_raw_response:
            return raw_result

        result = VideoCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        video_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        target_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
        :param target_id:
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
        self,
        album_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID (if the album is owned by a community).
        :param album_id: - Album ID.
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
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment to be deleted.
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
        video_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        desc: typing.Optional[str] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param name: - New video title.
        :param desc: - New video description.
        :param privacy_view: - Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param privacy_comment: - Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param no_comments: - Disable comments for the group video.
        :param repeat: - '1' — to repeat the playback of the video, '0' — to play the video once,
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
        album_id: int,
        title: str,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        privacy: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID (if the album edited is owned by a community).
        :param album_id: - Album ID.
        :param title: - New album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
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
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - Comment ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
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
        videos: typing.Optional[typing.List[str]] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, VideoGetResponse, VideoGetExtendedResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video(s).
        :param videos: - Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        :param album_id: - ID of the album containing the video(s).
        :param count: - Number of videos to return.
        :param offset: - Offset needed to return a specific subset of videos.
        :param extended: - '1' — to return an extended response with additional fields
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = (
            VideoGetResponse(**raw_result)
            if not extended
            else VideoGetExtendedResponse(**raw_result)
        )
        return result

    async def get_album_by_id(
        self,
        album_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, VideoGetAlbumByIdResponse]:
        """
        :param owner_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param album_id: - Album ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAlbumById", params)
        if return_raw_response:
            return raw_result

        result = VideoGetAlbumByIdResponse(**raw_result)
        return result

    async def get_albums(
        self,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        need_system: typing.Optional[bool] = None,
    ) -> typing.Union[dict, VideoGetAlbumsResponse, VideoGetAlbumsExtendedResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video album(s).
        :param offset: - Offset needed to return a specific subset of video albums.
        :param count: - Number of video albums to return.
        :param extended: - '1' — to return additional information about album privacy settings for the current user
        :param need_system:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAlbums", params)
        if return_raw_response:
            return raw_result

        result = (
            VideoGetAlbumsResponse(**raw_result)
            if not extended
            else VideoGetAlbumsExtendedResponse(**raw_result)
        )
        return result

    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        return_raw_response: bool = False,
        target_id: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, VideoGetAlbumsByVideoResponse, VideoGetAlbumsByVideoExtendedResponse]:
        """
        :param target_id:
        :param owner_id:
        :param video_id:
        :param extended:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAlbumsByVideo", params)
        if return_raw_response:
            return raw_result

        result = (
            VideoGetAlbumsByVideoResponse(**raw_result)
            if not extended
            else VideoGetAlbumsByVideoExtendedResponse(**raw_result)
        )
        return result

    async def get_comments(
        self,
        video_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        need_likes: typing.Optional[BaseBoolInt] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, VideoGetCommentsResponse, VideoGetCommentsExtendedResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param need_likes: - '1' — to return an additional 'likes' field
        :param start_comment_id:
        :param offset: - Offset needed to return a specific subset of comments.
        :param count: - Number of comments to return.
        :param sort: - Sort order: 'asc' — oldest comment first, 'desc' — newest comment first
        :param extended:
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = (
            VideoGetCommentsResponse(**raw_result)
            if not extended
            else VideoGetCommentsExtendedResponse(**raw_result)
        )
        return result

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        return_raw_response: bool = False,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
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
        album_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the albums..
        :param album_id: - Album ID.
        :param before: - ID of the album before which the album in question shall be placed.
        :param after: - ID of the album after which the album in question shall be placed.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderAlbums", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def reorder_videos(
        self,
        owner_id: int,
        video_id: int,
        return_raw_response: bool = False,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        before_owner_id: typing.Optional[int] = None,
        before_video_id: typing.Optional[int] = None,
        after_owner_id: typing.Optional[int] = None,
        after_video_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param target_id: - ID of the user or community that owns the album with videos.
        :param album_id: - ID of the video album.
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - ID of the video.
        :param before_owner_id: - ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: - ID of the video before which the video in question shall be placed.
        :param after_owner_id: - ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: - ID of the video after which the photo in question shall be placed.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderVideos", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def report(
        self,
        owner_id: int,
        video_id: int,
        return_raw_response: bool = False,
        reason: typing.Optional[BaseBoolInt] = None,
        comment: typing.Optional[str] = None,
        search_query: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param comment: - Comment describing the complaint.
        :param search_query: - (If the video was found in search results.) Search query string.
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
        return_raw_response: bool = False,
        reason: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment being reported.
        :param reason: - Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
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
        self,
        video_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
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
    ) -> typing.Union[dict, VideoRestoreCommentResponse]:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the deleted comment.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        if return_raw_response:
            return raw_result

        result = VideoRestoreCommentResponse(**raw_result)
        return result

    async def save(
        self,
        return_raw_response: bool = False,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        is_private: typing.Optional[BaseBoolInt] = None,
        wallpost: typing.Optional[BaseBoolInt] = None,
        link: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[BaseBoolInt] = None,
        compression: typing.Optional[bool] = None,
    ) -> typing.Union[dict, VideoSaveResponse]:
        """
        :param name: - Name of the video.
        :param description: - Description of the video.
        :param is_private: - '1' — to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' — not to designate the video as private
        :param wallpost: - '1' — to post the saved video on a user's wall, '0' — not to post the saved video on a user's wall
        :param link: - URL for embedding the video from an external website.
        :param group_id: - ID of the community in which the video will be saved. By default, the current user's page.
        :param album_id: - ID of the album to which the saved video will be added.
        :param privacy_view:
        :param privacy_comment:
        :param no_comments:
        :param repeat: - '1' — to repeat the playback of the video, '0' — to play the video once,
        :param compression:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("save", params)
        if return_raw_response:
            return raw_result

        result = VideoSaveResponse(**raw_result)
        return result

    async def search(
        self,
        q: str,
        return_raw_response: bool = False,
        sort: typing.Optional[BaseBoolInt] = None,
        hd: typing.Optional[int] = None,
        adult: typing.Optional[BaseBoolInt] = None,
        filters: typing.Optional[typing.List[str]] = None,
        search_own: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        longer: typing.Optional[int] = None,
        shorter: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, VideoSearchResponse, VideoSearchExtendedResponse]:
        """
        :param q: - Search query string (e.g., 'The Beatles').
        :param sort: - Sort order: '1' — by duration, '2' — by relevance, '0' — by date added
        :param hd: - If not null, only searches for high-definition videos.
        :param adult: - '1' — to disable the Safe Search filter, '0' — to enable the Safe Search filter
        :param filters: - Filters to apply: 'youtube' — return YouTube videos only, 'vimeo' — return Vimeo videos only, 'short' — return short videos only, 'long' — return long videos only
        :param search_own:
        :param offset: - Offset needed to return a specific subset of videos.
        :param longer:
        :param shorter:
        :param count: - Number of videos to return.
        :param extended:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = (
            VideoSearchResponse(**raw_result)
            if not extended
            else VideoSearchExtendedResponse(**raw_result)
        )
        return result
