from vkwave_types.responses import *
from ._category import Category


class Video(Category):
    async def add(
        self,
        target_id: typing.Optional[int] = None,
        video_id: int = None,
        owner_id: int = None,
    ) -> OkResponse:
        """
        :param target_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("add", params)
        result = OkResponse(**raw_result)
        return result

    async def add_album(
        self,
        group_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        privacy: typing.Optional[typing.List[str]] = None,
    ) -> VideoAddAlbumResponse:
        """
        :param group_id: - Community ID (if the album will be created in a community).
        :param title: - Album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addAlbum", params)
        result = VideoAddAlbumResponse(**raw_result)
        return result

    async def add_to_album(
        self,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        owner_id: int = None,
        video_id: int = None,
    ) -> OkResponse:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addToAlbum", params)
        result = OkResponse(**raw_result)
        return result

    async def create_comment(
        self,
        owner_id: typing.Optional[int] = None,
        video_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> VideoCreateCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: - '1' — to post the comment from a community name (only if 'owner_id'<0)
        :param reply_to_comment:
        :param sticker_id:
        :param guid:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("createComment", params)
        result = VideoCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        video_id: int = None,
        owner_id: typing.Optional[int] = None,
        target_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
        :param target_id:
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

    async def delete_album(
        self, group_id: typing.Optional[int] = None, album_id: int = None,
    ) -> OkResponse:
        """
        :param group_id: - Community ID (if the album is owned by a community).
        :param album_id: - Album ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("deleteAlbum", params)
        result = OkResponse(**raw_result)
        return result

    async def delete_comment(
        self, owner_id: typing.Optional[int] = None, comment_id: int = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment to be deleted.
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
        video_id: int = None,
        name: typing.Optional[str] = None,
        desc: typing.Optional[str] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param name: - New video title.
        :param desc: - New video description.
        :param privacy_view: - Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param privacy_comment: - Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param no_comments: - Disable comments for the group video.
        :param repeat: - '1' — to repeat the playback of the video, '0' — to play the video once,
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    async def edit_album(
        self,
        group_id: typing.Optional[int] = None,
        album_id: int = None,
        title: str = None,
        privacy: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param group_id: - Community ID (if the album edited is owned by a community).
        :param album_id: - Album ID.
        :param title: - New album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("editAlbum", params)
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
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - Comment ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
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
        videos: typing.Optional[typing.List[str]] = None,
        album_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
    ) -> VideoGetResponse:
        """
        :param owner_id: - ID of the user or community that owns the video(s).
        :param videos: - Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        :param album_id: - ID of the album containing the video(s).
        :param count: - Number of videos to return.
        :param offset: - Offset needed to return a specific subset of videos.
        :param extended: - '1' — to return an extended response with additional fields
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = VideoGetResponse(**raw_result)
        return result

    async def get_album_by_id(
        self, owner_id: typing.Optional[int] = None, album_id: int = None,
    ) -> VideoGetAlbumByIdResponse:
        """
        :param owner_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param album_id: - Album ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAlbumById", params)
        result = VideoGetAlbumByIdResponse(**raw_result)
        return result

    async def get_albums(
        self,
        owner_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        need_system: typing.Optional[bool] = None,
    ) -> VideoGetAlbumsResponse:
        """
        :param owner_id: - ID of the user or community that owns the video album(s).
        :param offset: - Offset needed to return a specific subset of video albums.
        :param count: - Number of video albums to return.
        :param extended: - '1' — to return additional information about album privacy settings for the current user
        :param need_system:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAlbums", params)
        result = VideoGetAlbumsResponse(**raw_result)
        return result

    async def get_albums_by_video(
        self,
        target_id: typing.Optional[int] = None,
        owner_id: int = None,
        video_id: int = None,
        extended: typing.Optional[bool] = None,
    ) -> VideoGetAlbumsByVideoResponse:
        """
        :param target_id:
        :param owner_id:
        :param video_id:
        :param extended:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAlbumsByVideo", params)
        result = VideoGetAlbumsByVideoResponse(**raw_result)
        return result

    async def get_comments(
        self,
        owner_id: typing.Optional[int] = None,
        video_id: int = None,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> VideoGetCommentsResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getComments", params)
        result = VideoGetCommentsResponse(**raw_result)
        return result

    async def remove_from_album(
        self,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        owner_id: int = None,
        video_id: int = None,
    ) -> OkResponse:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeFromAlbum", params)
        result = OkResponse(**raw_result)
        return result

    async def reorder_albums(
        self,
        owner_id: typing.Optional[int] = None,
        album_id: int = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the albums..
        :param album_id: - Album ID.
        :param before: - ID of the album before which the album in question shall be placed.
        :param after: - ID of the album after which the album in question shall be placed.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reorderAlbums", params)
        result = OkResponse(**raw_result)
        return result

    async def reorder_videos(
        self,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        owner_id: int = None,
        video_id: int = None,
        before_owner_id: typing.Optional[int] = None,
        before_video_id: typing.Optional[int] = None,
        after_owner_id: typing.Optional[int] = None,
        after_video_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param target_id: - ID of the user or community that owns the album with videos.
        :param album_id: - ID of the video album.
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - ID of the video.
        :param before_owner_id: - ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: - ID of the video before which the video in question shall be placed.
        :param after_owner_id: - ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: - ID of the video after which the photo in question shall be placed.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reorderVideos", params)
        result = OkResponse(**raw_result)
        return result

    async def report(
        self,
        owner_id: int = None,
        video_id: int = None,
        reason: typing.Optional[int] = None,
        comment: typing.Optional[str] = None,
        search_query: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param comment: - Comment describing the complaint.
        :param search_query: - (If the video was found in search results.) Search query string.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("report", params)
        result = OkResponse(**raw_result)
        return result

    async def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment being reported.
        :param reason: - Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
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

    async def restore(
        self, video_id: int = None, owner_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
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
    ) -> VideoRestoreCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the deleted comment.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("restoreComment", params)
        result = VideoRestoreCommentResponse(**raw_result)
        return result

    async def save(
        self,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        is_private: typing.Optional[bool] = None,
        wallpost: typing.Optional[bool] = None,
        link: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        no_comments: typing.Optional[bool] = None,
        repeat: typing.Optional[bool] = None,
        compression: typing.Optional[bool] = None,
    ) -> VideoSaveResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("save", params)
        result = VideoSaveResponse(**raw_result)
        return result

    async def search(
        self,
        q: str = None,
        sort: typing.Optional[int] = None,
        hd: typing.Optional[int] = None,
        adult: typing.Optional[bool] = None,
        filters: typing.Optional[typing.List[str]] = None,
        search_own: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        longer: typing.Optional[int] = None,
        shorter: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
    ) -> VideoSearchResponse:
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
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("search", params)
        result = VideoSearchResponse(**raw_result)
        return result
