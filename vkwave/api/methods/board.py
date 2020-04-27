from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Board(Category):
    async def add_topic(
        self,
        group_id: int,
        title: str,
        return_raw_response: bool = False,
        text: typing.Optional[str] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, BoardAddTopicResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param title: - Topic title.
        :param text: - Text of the topic.
        :param from_group: - For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: - List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addTopic", params)
        if return_raw_response:
            return raw_result

        result = BoardAddTopicResponse(**raw_result)
        return result

    async def close_topic(
        self, group_id: int, topic_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("closeTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def create_comment(
        self,
        group_id: int,
        topic_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[BaseBoolInt] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> typing.Union[dict, BoardCreateCommentResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - ID of the topic to be commented on.
        :param message: - (Required if 'attachments' is not set.) Text of the comment.
        :param attachments: - (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
        :param from_group: - '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
        :param sticker_id: - Sticker ID.
        :param guid: - Unique identifier to avoid repeated comments.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if return_raw_response:
            return raw_result

        result = BoardCreateCommentResponse(**raw_result)
        return result

    async def delete_comment(
        self, group_id: int, topic_id: int, comment_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
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

    async def delete_topic(
        self, group_id: int, topic_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        group_id: int,
        topic_id: int,
        comment_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param comment_id: - ID of the comment on the topic.
        :param message: - (Required if 'attachments' is not set). New comment text.
        :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editComment", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_topic(
        self, group_id: int, topic_id: int, title: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param title: - New title of the topic.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def fix_topic(
        self, group_id: int, topic_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("fixTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        return_raw_response: bool = False,
        need_likes: typing.Optional[BaseBoolInt] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        sort: typing.Optional[str] = None,
    ) -> typing.Union[dict, BoardGetCommentsResponse, BoardGetCommentsExtendedResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param need_likes: - '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: - Offset needed to return a specific subset of comments.
        :param count: - Number of comments to return.
        :param extended: - '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
        :param sort: - Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = (
            BoardGetCommentsResponse(**raw_result)
            if not extended
            else BoardGetCommentsExtendedResponse(**raw_result)
        )
        return result

    async def get_topics(
        self,
        group_id: int,
        return_raw_response: bool = False,
        topic_ids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        preview: typing.Optional[BaseBoolInt] = None,
        preview_length: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, BoardGetTopicsResponse, BoardGetTopicsExtendedResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_ids: - IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        :param order: - Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param offset: - Offset needed to return a specific subset of topics.
        :param count: - Number of topics to return.
        :param extended: - '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
        :param preview: - '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
        :param preview_length: - Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTopics", params)
        if return_raw_response:
            return raw_result

        result = (
            BoardGetTopicsResponse(**raw_result)
            if not extended
            else BoardGetTopicsExtendedResponse(**raw_result)
        )
        return result

    async def open_topic(
        self, group_id: int, topic_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("openTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def restore_comment(
        self, group_id: int, topic_id: int, comment_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
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

    async def unfix_topic(
        self, group_id: int, topic_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID of the community that owns the discussion board.
        :param topic_id: - Topic ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unfixTopic", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
