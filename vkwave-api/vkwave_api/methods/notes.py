from vkwave_types.responses import *
from ._category import Category


class Notes(Category):
    def add(
        self,
        title: typing.Optional[str],
        text: typing.Optional[str],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
    ) -> NotesAddResponse:
        """
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("add", params)
        result = NotesAddResponse(**raw_result)
        return result

    def create_comment(
        self,
        note_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        reply_to: typing.Optional[int],
        message: typing.Optional[str],
        guid: typing.Optional[str],
    ) -> NotesCreateCommentResponse:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param reply_to: - ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param message: - Comment text.
        :param guid:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createComment", params)
        result = NotesCreateCommentResponse(**raw_result)
        return result

    def delete(self, note_id: typing.Optional[int],) -> OkResponse:
        """
        :param note_id: - Note ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    def delete_comment(
        self, comment_id: typing.Optional[int], owner_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteComment", params)
        result = OkResponse(**raw_result)
        return result

    def edit(
        self,
        note_id: typing.Optional[int],
        title: typing.Optional[str],
        text: typing.Optional[str],
        privacy_view: typing.Optional[typing.List[str]],
        privacy_comment: typing.Optional[typing.List[str]],
    ) -> OkResponse:
        """
        :param note_id: - Note ID.
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_comment(
        self,
        comment_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        message: typing.Optional[str],
    ) -> OkResponse:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param message: - New comment text.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editComment", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        note_ids: typing.Optional[typing.List[int]],
        user_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        sort: typing.Optional[int],
    ) -> NotesGetResponse:
        """
        :param note_ids: - Note IDs.
        :param user_id: - Note owner ID.
        :param offset:
        :param count: - Number of notes to return.
        :param sort:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = NotesGetResponse(**raw_result)
        return result

    def get_by_id(
        self,
        note_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        need_wiki: typing.Optional[bool],
    ) -> NotesGetByIdResponse:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param need_wiki:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = NotesGetByIdResponse(**raw_result)
        return result

    def get_comments(
        self,
        note_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        sort: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> NotesGetCommentsResponse:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param sort:
        :param offset:
        :param count: - Number of comments to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = NotesGetCommentsResponse(**raw_result)
        return result

    def restore_comment(
        self, comment_id: typing.Optional[int], owner_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restoreComment", params)
        result = OkResponse(**raw_result)
        return result
