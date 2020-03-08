from vkwave_types.responses import *
from ._category import Category


class Video(Category):
    def add(
        self,
        target_id: typing.Optional[int],
        video_id: typing.Optional[int],
        owner_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param target_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("add", params)
        result = OkResponse(**raw_result)
        return result

    def add_album(
        self,
        group_id: typing.Optional[int],
        title: typing.Optional[str],
        privacy: typing.Optional[typing.List[str]],
    ) -> VideoAddAlbumResponse:
        """
        :param group_id: - Community ID (if the album will be created in a community).
        :param title: - Album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addAlbum", params)
        result = VideoAddAlbumResponse(**raw_result)
        return result

    def add_to_album(
        self,
        target_id: typing.Optional[int],
        album_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addToAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def create_comment(
        self,
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        message: typing.Optional[str],
        attachments: typing.Optional[typing.List[str]],
        from_group: typing.Optional[bool],
        reply_to_comment: typing.Optional[int],
        sticker_id: typing.Optional[int],
        guid: typing.Optional[str],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createComment", params)
        result = VideoCreateCommentResponse(**raw_result)
        return result

    def delete(
        self,
        video_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        target_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
        :param target_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def delete_album(
        self, group_id: typing.Optional[int], album_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID (if the album is owned by a community).
        :param album_id: - Album ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def delete_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment to be deleted.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteComment", params)
        result = OkResponse(**raw_result)
        return result

    def edit(
        self,
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        name: typing.Optional[str],
        desc: typing.Optional[str],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
        no_comments: typing.Optional[bool],
        repeat: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_album(
        self,
        group_id: typing.Optional[int],
        album_id: typing.Optional[int],
        title: typing.Optional[str],
        privacy: typing.Optional[typing.List[str]],
    ) -> OkResponse:
        """
        :param group_id: - Community ID (if the album edited is owned by a community).
        :param album_id: - Album ID.
        :param title: - New album title.
        :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def edit_comment(
        self,
        owner_id: typing.Optional[int],
        comment_id: typing.Optional[int],
        message: typing.Optional[str],
        attachments: typing.Optional[typing.List[str]],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - Comment ID.
        :param message: - New comment text.
        :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        owner_id: typing.Optional[int],
        videos: typing.Optional[typing.List[str]],
        album_id: typing.Optional[int],
        count: typing.Optional[int],
        offset: typing.Optional[int],
        extended: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = VideoGetResponse(**raw_result)
        return result

    def get_album_by_id(
        self, owner_id: typing.Optional[int], album_id: typing.Optional[int],
    ) -> VideoGetAlbumByIdResponse:
        """
        :param owner_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param album_id: - Album ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbumById", params)
        result = VideoGetAlbumByIdResponse(**raw_result)
        return result

    def get_albums(
        self,
        owner_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
        need_system: typing.Optional[bool],
    ) -> VideoGetAlbumsResponse:
        """
        :param owner_id: - ID of the user or community that owns the video album(s).
        :param offset: - Offset needed to return a specific subset of video albums.
        :param count: - Number of video albums to return.
        :param extended: - '1' — to return additional information about album privacy settings for the current user
        :param need_system:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbums", params)
        result = VideoGetAlbumsResponse(**raw_result)
        return result

    def get_albums_by_video(
        self,
        target_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> VideoGetAlbumsByVideoResponse:
        """
        :param target_id:
        :param owner_id:
        :param video_id:
        :param extended:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbumsByVideo", params)
        result = VideoGetAlbumsByVideoResponse(**raw_result)
        return result

    def get_comments(
        self,
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        need_likes: typing.Optional[bool],
        start_comment_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        sort: typing.Optional[str],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[str]],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = VideoGetCommentsResponse(**raw_result)
        return result

    def remove_from_album(
        self,
        target_id: typing.Optional[int],
        album_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param target_id:
        :param album_id:
        :param album_ids:
        :param owner_id:
        :param video_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeFromAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_albums(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        before: typing.Optional[int],
        after: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the albums..
        :param album_id: - Album ID.
        :param before: - ID of the album before which the album in question shall be placed.
        :param after: - ID of the album after which the album in question shall be placed.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderAlbums", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_videos(
        self,
        target_id: typing.Optional[int],
        album_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        before_owner_id: typing.Optional[int],
        before_video_id: typing.Optional[int],
        after_owner_id: typing.Optional[int],
        after_video_id: typing.Optional[int],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderVideos", params)
        result = OkResponse(**raw_result)
        return result

    def report(
        self,
        owner_id: typing.Optional[int],
        video_id: typing.Optional[int],
        reason: typing.Optional[int],
        comment: typing.Optional[str],
        search_query: typing.Optional[str],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param video_id: - Video ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param comment: - Comment describing the complaint.
        :param search_query: - (If the video was found in search results.) Search query string.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("report", params)
        result = OkResponse(**raw_result)
        return result

    def report_comment(
        self,
        owner_id: typing.Optional[int],
        comment_id: typing.Optional[int],
        reason: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the comment being reported.
        :param reason: - Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reportComment", params)
        result = OkResponse(**raw_result)
        return result

    def restore(
        self, video_id: typing.Optional[int], owner_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param video_id: - Video ID.
        :param owner_id: - ID of the user or community that owns the video.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restore", params)
        result = OkResponse(**raw_result)
        return result

    def restore_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> VideoRestoreCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the video.
        :param comment_id: - ID of the deleted comment.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restoreComment", params)
        result = VideoRestoreCommentResponse(**raw_result)
        return result

    def save(
        self,
        name: typing.Optional[str],
        description: typing.Optional[str],
        is_private: typing.Optional[bool],
        wallpost: typing.Optional[bool],
        link: typing.Optional[str],
        group_id: typing.Optional[int],
        album_id: typing.Optional[int],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
        no_comments: typing.Optional[bool],
        repeat: typing.Optional[bool],
        compression: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("save", params)
        result = VideoSaveResponse(**raw_result)
        return result

    def search(
        self,
        q: typing.Optional[str],
        sort: typing.Optional[int],
        hd: typing.Optional[int],
        adult: typing.Optional[bool],
        filters: typing.Optional[typing.List[str]],
        search_own: typing.Optional[bool],
        offset: typing.Optional[int],
        longer: typing.Optional[int],
        shorter: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = VideoSearchResponse(**raw_result)
        return result
