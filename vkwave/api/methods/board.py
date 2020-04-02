from vkwave.types.responses import *

from ._category import Category


class Board(Category):
    async def add_topic(
        self,
        group_id: int = None,
        title: str = None,
        text: typing.Optional[str] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> BoardAddTopicResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param title: - Topic title.
        :param text: - Text of the topic.
        :param from_group: - For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: - List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("addTopic", params)
        result = BoardAddTopicResponse(**raw_result)
        return result

    async def close_topic(self, group_id: int = None, topic_id: int = None,) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("closeTopic", params)
        result = OkResponse(**raw_result)
        return result

    async def create_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> BoardCreateCommentResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - ID of the topic to be commented on.
        :param message: - (Required if 'attachments' is not set.) Text of the comment.
        :param attachments: - (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
        :param from_group: - '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
        :param sticker_id: - Sticker ID.
        :param guid: - Unique identifier to avoid repeated comments.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("createComment", params)
        result = BoardCreateCommentResponse(**raw_result)
        return result

    async def delete_comment(
        self, group_id: int = None, topic_id: int = None, comment_id: int = None,
    ) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param comment_id: - Comment ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("deleteComment", params)
        result = OkResponse(**raw_result)
        return result

    async def delete_topic(self, group_id: int = None, topic_id: int = None,) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("deleteTopic", params)
        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param comment_id: - ID of the comment on the topic.
        :param message: - (Required if 'attachments' is not set). New comment text.
        :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    async def edit_topic(
        self, group_id: int = None, topic_id: int = None, title: str = None,
    ) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param title: - New title of the topic.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("editTopic", params)
        result = OkResponse(**raw_result)
        return result

    async def fix_topic(self, group_id: int = None, topic_id: int = None,) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("fixTopic", params)
        result = OkResponse(**raw_result)
        return result

    async def get_comments(
        self,
        group_id: int = None,
        topic_id: int = None,
        need_likes: typing.Optional[BaseBoolInt] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[BoardGetCommentsResponse, BoardGetCommentsExtendedResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param need_likes: - '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: - Offset needed to return a specific subset of comments.
        :param count: - Number of comments to return.
        :param extended: - '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
        :param sort: - Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getComments", params)

        result = (
            BoardGetCommentsResponse(**raw_result)
            if not extended
            else BoardGetCommentsExtendedResponse(**raw_result)
        )
        return result

    async def get_topics(
        self,
        group_id: int = None,
        topic_ids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        preview: typing.Optional[BaseBoolInt] = None,
        preview_length: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[BoardGetTopicsResponse, BoardGetTopicsExtendedResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_ids: - IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        :param order: - Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param offset: - Offset needed to return a specific subset of topics.
        :param count: - Number of topics to return.
        :param extended: - '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
        :param preview: - '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
        :param preview_length: - Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getTopics", params)

        result = (
            BoardGetTopicsResponse(**raw_result)
            if not extended
            else BoardGetTopicsExtendedResponse(**raw_result)
        )
        return result

    async def open_topic(self, group_id: int = None, topic_id: int = None,) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("openTopic", params)
        result = OkResponse(**raw_result)
        return result

    async def restore_comment(
        self, group_id: int = None, topic_id: int = None, comment_id: int = None,
    ) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param comment_id: - Comment ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("restoreComment", params)
        result = OkResponse(**raw_result)
        return result

    async def unfix_topic(self, group_id: int = None, topic_id: int = None,) -> OkResponse:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("unfixTopic", params)
        result = OkResponse(**raw_result)
        return result
