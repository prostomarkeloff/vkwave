import typing
import json
import os

from vkwave.bots.types.json_types import JSONDecoder
from vkwave.http import AbstractHTTPClient
from vkwave.api.methods import APIOptionsRequestContext
from vkwave.types.objects import PhotosPhoto


class PhotoUploader:
    def __init__(
            self,
            api_context: APIOptionsRequestContext,
            json_serialize: JSONDecoder = json.loads,
    ):
        self.api_context = api_context
        self.client: AbstractHTTPClient = api_context.api_options.get_client().http_client
        self.json_serialize = json_serialize

    async def get_server(self, peer_id: int) -> str:
        server_data = await self.api_context.photos.get_messages_upload_server(
            peer_id=peer_id
        )
        return server_data.response.upload_url

    async def upload(self, upload_url: str, file_data) -> typing.List[PhotosPhoto]:
        upload_data = self.json_serialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"photo": file_data}
            )
        )
        photo_sizes = (
            await self.api_context.photos.save_messages_photo(
                photo=upload_data["photo"],
                server=upload_data["server"],
                hash=upload_data["hash"],
            )
        ).response
        return photo_sizes

    async def get_attachment_from_path(self, peer_id: int, file_path: str) -> str:
        upload_url = await self.get_server(peer_id)
        file_data = open(file_path, "rb")
        photo = await self.upload(upload_url, file_data)
        file_data.close()
        return f"photo{photo[-1].owner_id}_{photo[-1].id}"

    async def get_attachments_from_paths(
            self, peer_id: int, file_paths: typing.List[str]
    ) -> str:
        ready_attachments: typing.List[str] = []
        for file in file_paths:
            ready_attachments.append(await self.get_attachment_from_path(peer_id, file))
        return ",".join(ready_attachments)

    async def get_attachment_from_link(self, peer_id: int, link: str) -> str:
        filename = "__vkwave__temp__file__.jpg"
        photo_data = await self.client.request_data(method="GET", url=link)

        #  TODO: async saving
        with open(filename, "wb") as file:
            file.write(photo_data)
        attachment = await self.get_attachment_from_path(
            file_path=filename, peer_id=peer_id
        )
        os.remove(filename)
        return attachment

    async def get_attachments_from_links(
            self, peer_id: int, links: typing.List[str]
    ) -> str:
        ready_attachments: typing.List[str] = []
        for link in links:
            ready_attachments.append(await self.get_attachment_from_link(peer_id, link))
        return ",".join(ready_attachments)
