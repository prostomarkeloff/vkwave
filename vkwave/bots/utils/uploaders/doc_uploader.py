import typing
from abc import ABC
from typing import BinaryIO

from vkwave.bots.utils.uploaders.uploader import BaseUploader
from vkwave.types.responses import DocsDocAttachmentType, DocsSaveResponseModel


class DocUploaderMixin(BaseUploader[DocsSaveResponseModel], ABC):
    async def _get_server(self, peer_id: int, doc_type: DocsDocAttachmentType) -> str:
        server_data = await self.api_context.docs.get_messages_upload_server(
            type=doc_type.value, peer_id=peer_id
        )
        return server_data.response.upload_url

    async def upload(self, upload_url: str, file_data: BinaryIO) -> DocsSaveResponseModel:
        # really dirty hack
        # but it works
        if not hasattr(file_data, "name"):
            setattr(file_data, "name", "Document.jpg")

        upload_data = self.json_deserialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file": file_data}
            ),
        )

        # Check upload for errors
        self.handle_error(upload_data)

        doc_save = (await self.api_context.docs.save(file=upload_data["file"])).response
        return doc_save

    def attachment_name(self, doc: DocsSaveResponseModel) -> typing.Union[str, typing.NoReturn]:
        if not doc.type:
            raise TypeError("Invalid document type")

        if doc.type == DocsDocAttachmentType.AUDIO_MESSAGE:
            d = doc.audio_message
        elif doc.type == DocsDocAttachmentType.DOC:
            d = doc.doc
        elif doc.type == DocsDocAttachmentType.GRAFFITI:
            d = doc.graffiti
        else:
            raise TypeError("Unknown document type %s" % doc.type.value)

        return (
            f"doc{d.owner_id}_{d.id}"
            if not d.access_key
            else f"doc{d.owner_id}_{d.id}_{d.access_key}"
        )


class VoiceUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.AUDIO_MESSAGE)


class GraffitiUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.GRAFFITI)


class DocUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.DOC)
