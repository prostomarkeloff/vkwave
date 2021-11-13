from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Notes(Category):
    async def add(
        self,
        title: str,
        text: str,
        return_raw_response: bool = False,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
    ) -> Union[dict, NotesAddResponse]:
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
        if return_raw_response:
            return raw_result

        result = NotesAddResponse(**raw_result)
        return result

    async def create_comment(
        self,
        note_id: int,
        message: str,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        reply_to: Optional[int] = None,
        guid: Optional[str] = None,
    ) -> Union[dict, NotesCreateCommentResponse]:
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

        result = NotesCreateCommentResponse(**raw_result)
        return result

    async def delete(
        self,
        note_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param note_id: - Note ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def delete_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteComment", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def edit(
        self,
        note_id: int,
        title: str,
        text: str,
        return_raw_response: bool = False,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
    ) -> Union[dict, BaseOkResponse]:
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
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param message: - New comment text.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editComment", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        note_ids: Optional[List[int]] = None,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[int] = None,
    ) -> Union[dict, NotesGetResponse]:
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
        if return_raw_response:
            return raw_result

        result = NotesGetResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        note_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        need_wiki: Optional[bool] = None,
    ) -> Union[dict, NotesGetByIdResponse]:
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

        result = NotesGetByIdResponse(**raw_result)
        return result

    async def get_comments(
        self,
        note_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, NotesGetCommentsResponse]:
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

        result = NotesGetCommentsResponse(**raw_result)
        return result

    async def restore_comment(
        self,
        comment_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param comment_id: - Comment ID.
        :param owner_id: - Note owner ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restoreComment", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
