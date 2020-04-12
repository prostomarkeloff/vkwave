from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Docs(Category):
    async def add(
        self,
        owner_id: int,
        doc_id: int,
        return_raw_response: bool = False,
        access_key: typing.Optional[str] = None,
    ) -> typing.Union[dict, DocsAddResponse]:
        """
        :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :param access_key: - Access key. This parameter is required if 'access_key' was returned with the document's data.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if return_raw_response:
            return raw_result

        result = DocsAddResponse(**raw_result)
        return result

    async def delete(
        self, owner_id: int, doc_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        owner_id: int,
        doc_id: int,
        return_raw_response: bool = False,
        title: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :param title: - Document title.
        :param tags: - Document tags.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, DocsGetResponse]:
        """
        :param count: - Number of documents to return. By default, all documents.
        :param offset: - Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = DocsGetResponse(**raw_result)
        return result

    async def get_by_id(
        self, docs: typing.List[str], return_raw_response: bool = False,
    ) -> typing.Union[dict, DocsGetByIdResponse]:
        """
        :param docs: - Document IDs. Example: , "66748_91488,66748_91455",
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = DocsGetByIdResponse(**raw_result)
        return result

    async def get_messages_upload_server(
        self,
        return_raw_response: bool = False,
        type: typing.Optional[str] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, BaseGetUploadServerResponse]:
        """
        :param type: - Document type.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMessagesUploadServer", params)
        if return_raw_response:
            return raw_result

        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_types(
        self, owner_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, DocsGetTypesResponse]:
        """
        :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTypes", params)
        if return_raw_response:
            return raw_result

        result = DocsGetTypesResponse(**raw_result)
        return result

    async def get_upload_server(
        self, return_raw_response: bool = False, group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, DocsGetUploadServer]:
        """
        :param group_id: - Community ID (if the document will be uploaded to the community).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUploadServer", params)
        if return_raw_response:
            return raw_result

        result = DocsGetUploadServer(**raw_result)
        return result

    async def get_wall_upload_server(
        self, return_raw_response: bool = False, group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, BaseGetUploadServerResponse]:
        """
        :param group_id: - Community ID (if the document will be uploaded to the community).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getWallUploadServer", params)
        if return_raw_response:
            return raw_result

        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def save(
        self,
        file: str,
        return_raw_response: bool = False,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> typing.Union[dict, DocsSaveResponse]:
        """
        :param file: - This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: - Document title.
        :param tags: - Document tags.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("save", params)
        if return_raw_response:
            return raw_result

        result = DocsSaveResponse(**raw_result)
        return result

    async def search(
        self,
        q: str,
        return_raw_response: bool = False,
        search_own: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, DocsSearchResponse]:
        """
        :param q: - Search query string.
        :param search_own:
        :param count: - Number of results to return.
        :param offset: - Offset needed to return a specific subset of results.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = DocsSearchResponse(**raw_result)
        return result
