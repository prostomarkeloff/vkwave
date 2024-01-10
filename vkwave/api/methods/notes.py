from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Notes(Category):
    async def add(
        self,
        title: str,
        text: str,
        return_raw_response: bool = False,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, NotesAddResponse]:
        """
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        return raw_result if return_raw_response else NotesAddResponse(**raw_result)

    async def create_comment(
        self,
        note_id: int,
        message: str,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
    ) -> typing.Union[dict, NotesCreateCommentResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param reply_to: - ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param message: - Comment text.
        :param guid:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createComment", params)
        if return_raw_response:
            return raw_result

        return NotesCreateCommentResponse(**raw_result)

    async def delete(
        self,
        note_id: int,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param note_id: - Note ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)

    async def delete_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteComment", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)

    async def edit(
        self,
        note_id: int,
        title: str,
        text: str,
        return_raw_response: bool = False,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param note_id: - Note ID.
        :param title: - Note title.
        :param text: - Note text.
        :param privacy_view:
        :param privacy_comment:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param message: - New comment text.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editComment", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)

    async def get(
        self,
        return_raw_response: bool = False,
        note_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
    ) -> typing.Union[dict, NotesGetResponse]:
        """
        :param note_ids: - Note IDs.
        :param user_id: - Note owner ID.
        :param offset:
        :param count: - Number of notes to return.
        :param sort:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        return raw_result if return_raw_response else NotesGetResponse(**raw_result)

    async def get_by_id(
        self,
        note_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        need_wiki: typing.Optional[bool] = None,
    ) -> typing.Union[dict, NotesGetByIdResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param need_wiki:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        return NotesGetByIdResponse(**raw_result)

    async def get_comments(
        self,
        note_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, NotesGetCommentsResponse]:
        """
        :param note_id: - Note ID.
        :param owner_id: - Note owner ID.
        :param sort:
        :param offset:
        :param count: - Number of comments to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        return NotesGetCommentsResponse(**raw_result)

    async def restore_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)
