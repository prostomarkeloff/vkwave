from vkwave_types.responses import *
from ._category import Category


class Photos(Category):
    async def confirm_tag(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param tag_id: - Tag ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("confirmTag", params)
        result = OkResponse(**raw_result)
        return result

    async def copy(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
    ) -> PhotosCopyResponse:
        """
        :param owner_id: - photo's owner ID
        :param photo_id: - photo ID
        :param access_key: - for private photos
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("copy", params)
        result = PhotosCopyResponse(**raw_result)
        return result

    async def create_album(
        self,
        title: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        description: typing.Optional[str] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        upload_by_admins_only: typing.Optional[bool] = None,
        comments_disabled: typing.Optional[bool] = None,
    ) -> PhotosCreateAlbumResponse:
        """
        :param title: - Album title.
        :param group_id: - ID of the community in which the album will be created.
        :param description: - Album description.
        :param privacy_view:
        :param privacy_comment:
        :param upload_by_admins_only:
        :param comments_disabled:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("createAlbum", params)
        result = PhotosCreateAlbumResponse(**raw_result)
        return result

    async def create_comment(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
        guid: typing.Optional[str] = None,
    ) -> PhotosCreateCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param message: - Comment text.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: - '1' — to post a comment from the community
        :param reply_to_comment:
        :param sticker_id:
        :param access_key:
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
        result = PhotosCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
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
        self,
        album_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param album_id: - Album ID.
        :param group_id: - ID of the community that owns the album.
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
        self,
        owner_id: typing.Optional[int] = None,
        comment_id: typing.Optional[int] = None,
    ) -> PhotosDeleteCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
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
        result = PhotosDeleteCommentResponse(**raw_result)
        return result

    async def edit(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        place_str: typing.Optional[str] = None,
        foursquare_id: typing.Optional[str] = None,
        delete_place: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param caption: - New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param latitude:
        :param longitude:
        :param place_str:
        :param foursquare_id:
        :param delete_place:
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
        album_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        upload_by_admins_only: typing.Optional[bool] = None,
        comments_disabled: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param album_id: - ID of the photo album to be edited.
        :param title: - New album title.
        :param description: - New album description.
        :param owner_id: - ID of the user or community that owns the album.
        :param privacy_view:
        :param privacy_comment:
        :param upload_by_admins_only:
        :param comments_disabled:
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
        comment_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - Comment ID.
        :param message: - New text of the comment.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
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
        album_id: typing.Optional[str] = None,
        photo_ids: typing.Optional[typing.List[str]] = None,
        rev: typing.Optional[bool] = None,
        extended: typing.Optional[bool] = None,
        feed_type: typing.Optional[str] = None,
        feed: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> PhotosGetResponse:
        """
        :param owner_id: - ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param album_id: - Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param photo_ids: - Photo IDs.
        :param rev: - Sort order: '1' — reverse chronological, '0' — chronological
        :param extended: - '1' — to return additional 'likes', 'comments', and 'tags' fields, '0' — (default)
        :param feed_type: - Type of feed obtained in 'feed' field of the method.
        :param feed: - unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param photo_sizes: - '1' — to return photo sizes in a [vk.com/dev/photo_sizes|special format]
        :param offset:
        :param count:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = PhotosGetResponse(**raw_result)
        return result

    async def get_albums(
        self,
        owner_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        need_system: typing.Optional[bool] = None,
        need_covers: typing.Optional[bool] = None,
        photo_sizes: typing.Optional[bool] = None,
    ) -> PhotosGetAlbumsResponse:
        """
        :param owner_id: - ID of the user or community that owns the albums.
        :param album_ids: - Album IDs.
        :param offset: - Offset needed to return a specific subset of albums.
        :param count: - Number of albums to return.
        :param need_system: - '1' — to return system albums with negative IDs
        :param need_covers: - '1' — to return an additional 'thumb_src' field, '0' — (default)
        :param photo_sizes: - '1' — to return photo sizes in a
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAlbums", params)
        result = PhotosGetAlbumsResponse(**raw_result)
        return result

    async def get_albums_count(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> PhotosGetAlbumsCountResponse:
        """
        :param user_id: - User ID.
        :param group_id: - Community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAlbumsCount", params)
        result = PhotosGetAlbumsCountResponse(**raw_result)
        return result

    async def get_all(
        self,
        owner_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        no_service_albums: typing.Optional[bool] = None,
        need_hidden: typing.Optional[bool] = None,
        skip_hidden: typing.Optional[bool] = None,
    ) -> PhotosGetAllResponse:
        """
        :param owner_id: - ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param extended: - '1' — to return detailed information about photos
        :param offset: - Offset needed to return a specific subset of photos. By default, '0'.
        :param count: - Number of photos to return.
        :param photo_sizes: - '1' – to return image sizes in [vk.com/dev/photo_sizes|special format].
        :param no_service_albums: - '1' – to return photos only from standard albums, '0' – to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param need_hidden: - '1' – to show information about photos being hidden from the block above the wall.
        :param skip_hidden: - '1' – not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAll", params)
        result = PhotosGetAllResponse(**raw_result)
        return result

    async def get_all_comments(
        self,
        owner_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> PhotosGetAllCommentsResponse:
        """
        :param owner_id: - ID of the user or community that owns the album(s).
        :param album_id: - Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param need_likes: - '1' — to return an additional 'likes' field, '0' — (default)
        :param offset: - Offset needed to return a specific subset of comments. By default, '0'.
        :param count: - Number of comments to return. By default, '20'. Maximum value, '100'.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAllComments", params)
        result = PhotosGetAllCommentsResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        photos: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        photo_sizes: typing.Optional[bool] = None,
    ) -> PhotosGetByIdResponse:
        """
        :param photos: - IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: - '1' — to return additional fields, '0' — (default)
        :param photo_sizes: - '1' — to return photo sizes in a
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getById", params)
        result = PhotosGetByIdResponse(**raw_result)
        return result

    async def get_chat_upload_server(
        self,
        chat_id: typing.Optional[int] = None,
        crop_x: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        crop_width: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param chat_id: - ID of the chat for which you want to upload a cover photo.
        :param crop_x:
        :param crop_y:
        :param crop_width: - Width (in pixels) of the photo after cropping.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getChatUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_comments(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> PhotosGetCommentsResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param need_likes: - '1' — to return an additional 'likes' field, '0' — (default)
        :param start_comment_id:
        :param offset: - Offset needed to return a specific subset of comments. By default, '0'.
        :param count: - Number of comments to return.
        :param sort: - Sort order: 'asc' — old first, 'desc' — new first
        :param access_key:
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
        result = PhotosGetCommentsResponse(**raw_result)
        return result

    async def get_market_album_upload_server(
        self, group_id: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param group_id: - Community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getMarketAlbumUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_market_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        main_photo: typing.Optional[bool] = None,
        crop_x: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        crop_width: typing.Optional[int] = None,
    ) -> PhotosGetMarketUploadServerResponse:
        """
        :param group_id: - Community ID.
        :param main_photo: - '1' if you want to upload the main item photo.
        :param crop_x: - X coordinate of the crop left upper corner.
        :param crop_y: - Y coordinate of the crop left upper corner.
        :param crop_width: - Width of the cropped photo in px.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getMarketUploadServer", params)
        result = PhotosGetMarketUploadServerResponse(**raw_result)
        return result

    async def get_messages_upload_server(
        self, peer_id: typing.Optional[int] = None,
    ) -> PhotosGetMessagesUploadServerResponse:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getMessagesUploadServer", params)
        result = PhotosGetMessagesUploadServerResponse(**raw_result)
        return result

    async def get_new_tags(
        self, offset: typing.Optional[int] = None, count: typing.Optional[int] = None,
    ) -> PhotosGetNewTagsResponse:
        """
        :param offset: - Offset needed to return a specific subset of photos.
        :param count: - Number of photos to return.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getNewTags", params)
        result = PhotosGetNewTagsResponse(**raw_result)
        return result

    async def get_owner_cover_photo_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        crop_x: typing.Optional[int] = None,
        crop_y: typing.Optional[int] = None,
        crop_x2: typing.Optional[int] = None,
        crop_y2: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: - X coordinate of the left-upper corner
        :param crop_y: - Y coordinate of the left-upper corner
        :param crop_x2: - X coordinate of the right-bottom corner
        :param crop_y2: - Y coordinate of the right-bottom corner
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getOwnerCoverPhotoUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_owner_photo_upload_server(
        self, owner_id: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param owner_id: - identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getOwnerPhotoUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_tags(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
    ) -> PhotosGetTagsResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param access_key:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getTags", params)
        result = PhotosGetTagsResponse(**raw_result)
        return result

    async def get_upload_server(
        self,
        group_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
    ) -> PhotosGetUploadServerResponse:
        """
        :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
        :param album_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getUploadServer", params)
        result = PhotosGetUploadServerResponse(**raw_result)
        return result

    async def get_user_photos(
        self,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
    ) -> PhotosGetUserPhotosResponse:
        """
        :param user_id: - User ID.
        :param offset: - Offset needed to return a specific subset of photos. By default, '0'.
        :param count: - Number of photos to return. Maximum value is 1000.
        :param extended: - '1' — to return an additional 'likes' field, '0' — (default)
        :param sort: - Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getUserPhotos", params)
        result = PhotosGetUserPhotosResponse(**raw_result)
        return result

    async def get_wall_upload_server(
        self, group_id: typing.Optional[int] = None,
    ) -> PhotosGetWallUploadServerResponse:
        """
        :param group_id: - ID of community to whose wall the photo will be uploaded.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getWallUploadServer", params)
        result = PhotosGetWallUploadServerResponse(**raw_result)
        return result

    async def make_cover(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param album_id: - Album ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("makeCover", params)
        result = OkResponse(**raw_result)
        return result

    async def move(
        self,
        owner_id: typing.Optional[int] = None,
        target_album_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param target_album_id: - ID of the album to which the photo will be moved.
        :param photo_id: - Photo ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("move", params)
        result = OkResponse(**raw_result)
        return result

    async def put_tag(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        x: typing.Optional[int] = None,
        y: typing.Optional[int] = None,
        x2: typing.Optional[int] = None,
        y2: typing.Optional[int] = None,
    ) -> PhotosPutTagResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param user_id: - ID of the user to be tagged.
        :param x: - Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: - Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param x2: - Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y2: - Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("putTag", params)
        result = PhotosPutTagResponse(**raw_result)
        return result

    async def remove_tag(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        tag_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param tag_id: - Tag ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeTag", params)
        result = OkResponse(**raw_result)
        return result

    async def reorder_albums(
        self,
        owner_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the album.
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

    async def reorder_photos(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param before: - ID of the photo before which the photo in question shall be placed.
        :param after: - ID of the photo after which the photo in question shall be placed.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reorderPhotos", params)
        result = OkResponse(**raw_result)
        return result

    async def report(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        reason: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
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
        owner_id: typing.Optional[int] = None,
        comment_id: typing.Optional[int] = None,
        reason: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - ID of the comment being reported.
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

    async def restore(
        self,
        owner_id: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
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
        self,
        owner_id: typing.Optional[int] = None,
        comment_id: typing.Optional[int] = None,
    ) -> PhotosRestoreCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
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
        result = PhotosRestoreCommentResponse(**raw_result)
        return result

    async def save(
        self,
        album_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        server: typing.Optional[int] = None,
        photos_list: typing.Optional[str] = None,
        hash: typing.Optional[str] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
    ) -> PhotosSaveResponse:
        """
        :param album_id: - ID of the album to save photos to.
        :param group_id: - ID of the community to save photos to.
        :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photos_list: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param latitude: - Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: - Geographical longitude, in degrees (from '-180' to '180').
        :param caption: - Text describing the photo. 2048 digits max.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("save", params)
        result = PhotosSaveResponse(**raw_result)
        return result

    async def save_market_album_photo(
        self,
        group_id: typing.Optional[int] = None,
        photo: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
    ) -> PhotosSaveMarketAlbumPhotoResponse:
        """
        :param group_id: - Community ID.
        :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveMarketAlbumPhoto", params)
        result = PhotosSaveMarketAlbumPhotoResponse(**raw_result)
        return result

    async def save_market_photo(
        self,
        group_id: typing.Optional[int] = None,
        photo: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
        crop_data: typing.Optional[str] = None,
        crop_hash: typing.Optional[str] = None,
    ) -> PhotosSaveMarketPhotoResponse:
        """
        :param group_id: - Community ID.
        :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_data: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveMarketPhoto", params)
        result = PhotosSaveMarketPhotoResponse(**raw_result)
        return result

    async def save_messages_photo(
        self,
        photo: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
    ) -> PhotosSaveMessagesPhotoResponse:
        """
        :param photo: - Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server:
        :param hash:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveMessagesPhoto", params)
        result = PhotosSaveMessagesPhotoResponse(**raw_result)
        return result

    async def save_owner_cover_photo(
        self, hash: typing.Optional[str] = None, photo: typing.Optional[str] = None,
    ) -> PhotosSaveOwnerCoverPhotoResponse:
        """
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveOwnerCoverPhoto", params)
        result = PhotosSaveOwnerCoverPhotoResponse(**raw_result)
        return result

    async def save_owner_photo(
        self,
        server: typing.Optional[str] = None,
        hash: typing.Optional[str] = None,
        photo: typing.Optional[str] = None,
    ) -> PhotosSaveOwnerPhotoResponse:
        """
        :param server: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :param hash: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveOwnerPhoto", params)
        result = PhotosSaveOwnerPhotoResponse(**raw_result)
        return result

    async def save_wall_photo(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        photo: typing.Optional[str] = None,
        server: typing.Optional[int] = None,
        hash: typing.Optional[str] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
    ) -> PhotosSaveWallPhotoResponse:
        """
        :param user_id: - ID of the user on whose wall the photo will be saved.
        :param group_id: - ID of community on whose wall the photo will be saved.
        :param photo: - Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server:
        :param hash:
        :param latitude: - Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: - Geographical longitude, in degrees (from '-180' to '180').
        :param caption: - Text describing the photo. 2048 digits max.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveWallPhoto", params)
        result = PhotosSaveWallPhotoResponse(**raw_result)
        return result

    async def search(
        self,
        q: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        radius: typing.Optional[int] = None,
    ) -> PhotosSearchResponse:
        """
        :param q: - Search query string.
        :param lat: - Geographical latitude, in degrees (from '-90' to '90').
        :param long: - Geographical longitude, in degrees (from '-180' to '180').
        :param start_time:
        :param end_time:
        :param sort: - Sort order:
        :param offset: - Offset needed to return a specific subset of photos.
        :param count: - Number of photos to return.
        :param radius: - Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("search", params)
        result = PhotosSearchResponse(**raw_result)
        return result
