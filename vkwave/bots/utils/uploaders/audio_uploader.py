import json

from vkwave.bots.core.types.json_types import JSONDecoder
from vkwave.http import AbstractHTTPClient
from vkwave.api.methods import APIOptionsRequestContext
from vkwave.types.responses import DocsSaveResponseModel


class VoiceUploader:
    def __init__(
            self,
            api_context: APIOptionsRequestContext,
            json_serialize: JSONDecoder = json.loads,
    ):
        self.api_context = api_context
        self.client: AbstractHTTPClient = api_context.api_options.get_client().http_client
        self.json_serialize = json_serialize

    async def get_server(self, peer_id: int) -> str:
        server_data = await self.api_context.docs.get_messages_upload_server(
            type="audio_message", peer_id=peer_id
        )
        return server_data.response.upload_url

    async def upload(self, upload_url: str, file_data) -> DocsSaveResponseModel:
        upload_data = self.json_serialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file": file_data}
            )
        )
        photo_sizes = (
            await self.api_context.docs.save(file=upload_data["file"])
        ).response
        return photo_sizes

    async def get_attachment_from_path(self, peer_id: int, file_path: str) -> str:
        upload_url = await self.get_server(peer_id)
        file_data = open(file_path, "rb")
        doc = await self.upload(upload_url, file_data)
        file_data.close()
        if doc.audio_message is None:
            raise TypeError("This is not a voice message")
        return f"doc{doc.audio_message.owner_id}_{doc.audio_message.id}"
