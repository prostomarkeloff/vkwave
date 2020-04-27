import json
import typing
from abc import ABC, abstractmethod
from io import BytesIO
from typing import BinaryIO, Generic, List, TypeVar

from vkwave.api.methods import APIOptionsRequestContext
from vkwave.bots.core.types.json_types import JSONDecoder
from vkwave.http import AbstractHTTPClient

UploadResult = TypeVar("UploadResult")


class UploadException(Exception):
    pass


class BaseUploader(ABC, Generic[UploadResult]):
    def __init__(
        self,
        api_context: APIOptionsRequestContext,
        client: typing.Optional[AbstractHTTPClient] = None,
        json_deserialize: JSONDecoder = json.loads,
    ):
        self.api_context = api_context
        self.client: AbstractHTTPClient = client or api_context.api_options.get_client().http_client
        self.json_deserialize = json_deserialize

    @abstractmethod
    async def get_server(self, peer_id: int) -> str:
        pass

    @abstractmethod
    async def upload(self, server_url: str, file_data: BinaryIO) -> UploadResult:
        pass

    @abstractmethod
    def attachment_name(self, u: UploadResult) -> str:
        pass

    async def get_attachment_from_io(self, peer_id: int, f: BinaryIO) -> str:
        upload_url = await self.get_server(peer_id)
        return self.attachment_name(await self.upload(upload_url, f))

    async def get_attachment_from_path(self, peer_id: int, file_path: str) -> str:
        with open(file_path, "rb") as file_data:
            return await self.get_attachment_from_io(peer_id, file_data)

    async def get_attachments_from_paths(self, peer_id: int, file_paths: List[str]) -> str:
        ready_attachments: List[str] = []
        for file in file_paths:
            ready_attachments.append(await self.get_attachment_from_path(peer_id, file))
        return ",".join(ready_attachments)

    async def get_attachment_from_link(self, peer_id: int, link: str) -> str:
        file_data = BytesIO(await self.client.request_data("GET", link))
        return await self.get_attachment_from_io(peer_id, file_data)

    async def get_attachments_from_links(self, peer_id: int, links: List[str]) -> str:
        ready_attachments: List[str] = []
        for link in links:
            ready_attachments.append(await self.get_attachment_from_link(peer_id, link))
        return ",".join(ready_attachments)

    def handle_error(self, upload_data: dict):
        err = upload_data.get("error")
        if err:
            raise UploadException(err)
