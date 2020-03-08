from vkwave_types.responses import *
from ._category import Category


class Photos(Category):
    def confirm_tag(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[str],
        tag_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param tag_id: - Tag ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("confirmTag", params)
        result = OkResponse(**raw_result)
        return result

    def copy(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        access_key: typing.Optional[str],
    ) -> PhotosCopyResponse:
        """
        :param owner_id: - photo's owner ID
        :param photo_id: - photo ID
        :param access_key: - for private photos
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("copy", params)
        result = PhotosCopyResponse(**raw_result)
        return result

    def create_album(
        self,
        title: typing.Optional[str],
        group_id: typing.Optional[int],
        description: typing.Optional[str],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
        upload_by_admins_only: typing.Optional[bool],
        comments_disabled: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createAlbum", params)
        result = PhotosCreateAlbumResponse(**raw_result)
        return result

    def create_comment(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        message: typing.Optional[str],
        attachments: typing.Optional[typing.List[str]],
        from_group: typing.Optional[bool],
        reply_to_comment: typing.Optional[int],
        sticker_id: typing.Optional[int],
        access_key: typing.Optional[str],
        guid: typing.Optional[str],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createComment", params)
        result = PhotosCreateCommentResponse(**raw_result)
        return result

    def delete(
        self, owner_id: typing.Optional[int], photo_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def delete_album(
        self, album_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param album_id: - Album ID.
        :param group_id: - ID of the community that owns the album.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteAlbum", params)
        result = OkResponse(**raw_result)
        return result

    def delete_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> PhotosDeleteCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - Comment ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteComment", params)
        result = PhotosDeleteCommentResponse(**raw_result)
        return result

    def edit(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        caption: typing.Optional[str],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        place_str: typing.Optional[str],
        foursquare_id: typing.Optional[str],
        delete_place: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_album(
        self,
        album_id: typing.Optional[int],
        title: typing.Optional[str],
        description: typing.Optional[str],
        owner_id: typing.Optional[int],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
        upload_by_admins_only: typing.Optional[bool],
        comments_disabled: typing.Optional[bool],
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
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - Comment ID.
        :param message: - New text of the comment.
        :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[str],
        photo_ids: typing.Optional[typing.List[str]],
        rev: typing.Optional[bool],
        extended: typing.Optional[bool],
        feed_type: typing.Optional[str],
        feed: typing.Optional[int],
        photo_sizes: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = PhotosGetResponse(**raw_result)
        return result

    def get_albums(
        self,
        owner_id: typing.Optional[int],
        album_ids: typing.Optional[typing.List[int]],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        need_system: typing.Optional[bool],
        need_covers: typing.Optional[bool],
        photo_sizes: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbums", params)
        result = PhotosGetAlbumsResponse(**raw_result)
        return result

    def get_albums_count(
        self, user_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> PhotosGetAlbumsCountResponse:
        """
        :param user_id: - User ID.
        :param group_id: - Community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAlbumsCount", params)
        result = PhotosGetAlbumsCountResponse(**raw_result)
        return result

    def get_all(
        self,
        owner_id: typing.Optional[int],
        extended: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        photo_sizes: typing.Optional[bool],
        no_service_albums: typing.Optional[bool],
        need_hidden: typing.Optional[bool],
        skip_hidden: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAll", params)
        result = PhotosGetAllResponse(**raw_result)
        return result

    def get_all_comments(
        self,
        owner_id: typing.Optional[int],
        album_id: typing.Optional[int],
        need_likes: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> PhotosGetAllCommentsResponse:
        """
        :param owner_id: - ID of the user or community that owns the album(s).
        :param album_id: - Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param need_likes: - '1' — to return an additional 'likes' field, '0' — (default)
        :param offset: - Offset needed to return a specific subset of comments. By default, '0'.
        :param count: - Number of comments to return. By default, '20'. Maximum value, '100'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAllComments", params)
        result = PhotosGetAllCommentsResponse(**raw_result)
        return result

    def get_by_id(
        self,
        photos: typing.Optional[typing.List[str]],
        extended: typing.Optional[bool],
        photo_sizes: typing.Optional[bool],
    ) -> PhotosGetByIdResponse:
        """
        :param photos: - IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: - '1' — to return additional fields, '0' — (default)
        :param photo_sizes: - '1' — to return photo sizes in a
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = PhotosGetByIdResponse(**raw_result)
        return result

    def get_chat_upload_server(
        self,
        chat_id: typing.Optional[int],
        crop_x: typing.Optional[int],
        crop_y: typing.Optional[int],
        crop_width: typing.Optional[int],
    ) -> BaseGetUploadServerResponse:
        """
        :param chat_id: - ID of the chat for which you want to upload a cover photo.
        :param crop_x:
        :param crop_y:
        :param crop_width: - Width (in pixels) of the photo after cropping.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getChatUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    def get_comments(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        need_likes: typing.Optional[bool],
        start_comment_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        sort: typing.Optional[str],
        access_key: typing.Optional[str],
        extended: typing.Optional[bool],
        fields: typing.Optional[typing.List[UsersFields]],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = PhotosGetCommentsResponse(**raw_result)
        return result

    def get_market_album_upload_server(
        self, group_id: typing.Optional[int],
    ) -> BaseGetUploadServerResponse:
        """
        :param group_id: - Community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMarketAlbumUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    def get_market_upload_server(
        self,
        group_id: typing.Optional[int],
        main_photo: typing.Optional[bool],
        crop_x: typing.Optional[int],
        crop_y: typing.Optional[int],
        crop_width: typing.Optional[int],
    ) -> PhotosGetMarketUploadServerResponse:
        """
        :param group_id: - Community ID.
        :param main_photo: - '1' if you want to upload the main item photo.
        :param crop_x: - X coordinate of the crop left upper corner.
        :param crop_y: - Y coordinate of the crop left upper corner.
        :param crop_width: - Width of the cropped photo in px.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMarketUploadServer", params)
        result = PhotosGetMarketUploadServerResponse(**raw_result)
        return result

    def get_messages_upload_server(
        self, peer_id: typing.Optional[int],
    ) -> PhotosGetMessagesUploadServerResponse:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMessagesUploadServer", params)
        result = PhotosGetMessagesUploadServerResponse(**raw_result)
        return result

    def get_new_tags(
        self, offset: typing.Optional[int], count: typing.Optional[int],
    ) -> PhotosGetNewTagsResponse:
        """
        :param offset: - Offset needed to return a specific subset of photos.
        :param count: - Number of photos to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getNewTags", params)
        result = PhotosGetNewTagsResponse(**raw_result)
        return result

    def get_owner_cover_photo_upload_server(
        self,
        group_id: typing.Optional[int],
        crop_x: typing.Optional[int],
        crop_y: typing.Optional[int],
        crop_x2: typing.Optional[int],
        crop_y2: typing.Optional[int],
    ) -> BaseGetUploadServerResponse:
        """
        :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: - X coordinate of the left-upper corner
        :param crop_y: - Y coordinate of the left-upper corner
        :param crop_x2: - X coordinate of the right-bottom corner
        :param crop_y2: - Y coordinate of the right-bottom corner
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getOwnerCoverPhotoUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    def get_owner_photo_upload_server(
        self, owner_id: typing.Optional[int],
    ) -> BaseGetUploadServerResponse:
        """
        :param owner_id: - identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getOwnerPhotoUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    def get_tags(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        access_key: typing.Optional[str],
    ) -> PhotosGetTagsResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param access_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTags", params)
        result = PhotosGetTagsResponse(**raw_result)
        return result

    def get_upload_server(
        self, group_id: typing.Optional[int], album_id: typing.Optional[int],
    ) -> PhotosGetUploadServerResponse:
        """
        :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
        :param album_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUploadServer", params)
        result = PhotosGetUploadServerResponse(**raw_result)
        return result

    def get_user_photos(
        self,
        user_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
        sort: typing.Optional[str],
    ) -> PhotosGetUserPhotosResponse:
        """
        :param user_id: - User ID.
        :param offset: - Offset needed to return a specific subset of photos. By default, '0'.
        :param count: - Number of photos to return. Maximum value is 1000.
        :param extended: - '1' — to return an additional 'likes' field, '0' — (default)
        :param sort: - Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUserPhotos", params)
        result = PhotosGetUserPhotosResponse(**raw_result)
        return result

    def get_wall_upload_server(
        self, group_id: typing.Optional[int],
    ) -> PhotosGetWallUploadServerResponse:
        """
        :param group_id: - ID of community to whose wall the photo will be uploaded.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getWallUploadServer", params)
        result = PhotosGetWallUploadServerResponse(**raw_result)
        return result

    def make_cover(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        album_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param album_id: - Album ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("makeCover", params)
        result = OkResponse(**raw_result)
        return result

    def move(
        self,
        owner_id: typing.Optional[int],
        target_album_id: typing.Optional[int],
        photo_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param target_album_id: - ID of the album to which the photo will be moved.
        :param photo_id: - Photo ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("move", params)
        result = OkResponse(**raw_result)
        return result

    def put_tag(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        user_id: typing.Optional[int],
        x: typing.Optional[int],
        y: typing.Optional[int],
        x2: typing.Optional[int],
        y2: typing.Optional[int],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("putTag", params)
        result = PhotosPutTagResponse(**raw_result)
        return result

    def remove_tag(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        tag_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param tag_id: - Tag ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeTag", params)
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
        :param owner_id: - ID of the user or community that owns the album.
        :param album_id: - Album ID.
        :param before: - ID of the album before which the album in question shall be placed.
        :param after: - ID of the album after which the album in question shall be placed.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderAlbums", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_photos(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        before: typing.Optional[int],
        after: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param before: - ID of the photo before which the photo in question shall be placed.
        :param after: - ID of the photo after which the photo in question shall be placed.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderPhotos", params)
        result = OkResponse(**raw_result)
        return result

    def report(
        self,
        owner_id: typing.Optional[int],
        photo_id: typing.Optional[int],
        reason: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
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
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - ID of the comment being reported.
        :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reportComment", params)
        result = OkResponse(**raw_result)
        return result

    def restore(
        self, owner_id: typing.Optional[int], photo_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param photo_id: - Photo ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restore", params)
        result = OkResponse(**raw_result)
        return result

    def restore_comment(
        self, owner_id: typing.Optional[int], comment_id: typing.Optional[int],
    ) -> PhotosRestoreCommentResponse:
        """
        :param owner_id: - ID of the user or community that owns the photo.
        :param comment_id: - ID of the deleted comment.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restoreComment", params)
        result = PhotosRestoreCommentResponse(**raw_result)
        return result

    def save(
        self,
        album_id: typing.Optional[int],
        group_id: typing.Optional[int],
        server: typing.Optional[int],
        photos_list: typing.Optional[str],
        hash: typing.Optional[str],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        caption: typing.Optional[str],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("save", params)
        result = PhotosSaveResponse(**raw_result)
        return result

    def save_market_album_photo(
        self,
        group_id: typing.Optional[int],
        photo: typing.Optional[str],
        server: typing.Optional[int],
        hash: typing.Optional[str],
    ) -> PhotosSaveMarketAlbumPhotoResponse:
        """
        :param group_id: - Community ID.
        :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveMarketAlbumPhoto", params)
        result = PhotosSaveMarketAlbumPhotoResponse(**raw_result)
        return result

    def save_market_photo(
        self,
        group_id: typing.Optional[int],
        photo: typing.Optional[str],
        server: typing.Optional[int],
        hash: typing.Optional[str],
        crop_data: typing.Optional[str],
        crop_hash: typing.Optional[str],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveMarketPhoto", params)
        result = PhotosSaveMarketPhotoResponse(**raw_result)
        return result

    def save_messages_photo(
        self,
        photo: typing.Optional[str],
        server: typing.Optional[int],
        hash: typing.Optional[str],
    ) -> PhotosSaveMessagesPhotoResponse:
        """
        :param photo: - Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server:
        :param hash:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveMessagesPhoto", params)
        result = PhotosSaveMessagesPhotoResponse(**raw_result)
        return result

    def save_owner_cover_photo(
        self, hash: typing.Optional[str], photo: typing.Optional[str],
    ) -> PhotosSaveOwnerCoverPhotoResponse:
        """
        :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveOwnerCoverPhoto", params)
        result = PhotosSaveOwnerCoverPhotoResponse(**raw_result)
        return result

    def save_owner_photo(
        self,
        server: typing.Optional[str],
        hash: typing.Optional[str],
        photo: typing.Optional[str],
    ) -> PhotosSaveOwnerPhotoResponse:
        """
        :param server: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :param hash: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: - parameter returned after [vk.com/dev/upload_files|photo upload].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveOwnerPhoto", params)
        result = PhotosSaveOwnerPhotoResponse(**raw_result)
        return result

    def save_wall_photo(
        self,
        user_id: typing.Optional[int],
        group_id: typing.Optional[int],
        photo: typing.Optional[str],
        server: typing.Optional[int],
        hash: typing.Optional[str],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        caption: typing.Optional[str],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("saveWallPhoto", params)
        result = PhotosSaveWallPhotoResponse(**raw_result)
        return result

    def search(
        self,
        q: typing.Optional[str],
        lat: typing.Optional[int],
        long: typing.Optional[int],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
        sort: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        radius: typing.Optional[int],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = PhotosSearchResponse(**raw_result)
        return result
