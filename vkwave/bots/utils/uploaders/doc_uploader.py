import typing
import itertools
from abc import ABC
from io import BytesIO
from typing import BinaryIO

from vkwave.bots.utils.uploaders.uploader import BaseUploader, UploadException
from vkwave.types.responses import DocsDocAttachmentType, DocsSaveResponseModel


class DocUploaderMixin(BaseUploader[DocsSaveResponseModel], ABC):
    async def _get_server(self, peer_id: int, doc_type: DocsDocAttachmentType) -> str:
        server_data = await self.api_context.docs.get_messages_upload_server(
            type=doc_type.value, peer_id=peer_id
        )
        return server_data.response.upload_url

    async def upload(
        self,
        upload_url: str,
        file_data: BinaryIO,
        file_extension: str,
        file_name: str,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> DocsSaveResponseModel:
        file_name = file_name or "Document"
        file_extension = file_extension or "jpg"
        if not hasattr(file_data, "name"):
            try:
                setattr(file_data, "name", f"{file_name}.{file_extension}")
            except AttributeError:
                raise RuntimeError(
                    "'bytes' object has no attribute 'name', put your bytes in BytesIO"
                )

        upload_data = self.json_deserialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file": file_data}
            ),
        )

        # Check upload for errors
        self.handle_error(upload_data)

        doc_save = (
            await self.api_context.docs.save(file=upload_data["file"], title=title, tags=tags)
        ).response
        return doc_save

    async def get_attachment_from_io(
        self,
        peer_id: int,
        f: BinaryIO,
        file_name: typing.Optional[str] = None,
        file_extension: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> str:
        upload_url = await self.get_server(peer_id)
        return self.attachment_name(
            await self.upload(
                upload_url,
                f,
                title=title,
                tags=tags,
                file_extension=file_extension,
                file_name=file_name,
            )
        )

    async def get_attachment_from_path(
        self,
        peer_id: int,
        file_path: str,
        file_name: typing.Optional[str] = None,
        file_extension: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> str:
        with open(file_path, "rb") as file_data:
            return await self.get_attachment_from_io(
                peer_id,
                file_data,
                title=title,
                tags=tags,
                file_extension=file_extension,
                file_name=file_name,
            )

    async def get_attachments_from_paths(
        self,
        peer_id: int,
        file_paths: typing.List[str],
        file_names: typing.Sequence[str] = (),
        file_extensions: typing.Sequence[str] = (),
        titles: typing.Sequence[str] = (),
        tags_list: typing.Sequence[str] = (),
    ) -> str:
        ready_attachments: typing.List[str] = []
        for file, title, tags, file_extension, file_name in itertools.zip_longest(
            file_paths, titles, tags_list, file_extensions, file_names, fillvalue="Document"
        ):
            ready_attachments.append(
                await self.get_attachment_from_path(
                    peer_id,
                    file,
                    title=title,
                    tags=tags,
                    file_extension=file_extension,
                    file_name=file_name,
                )
            )
        return ",".join(ready_attachments)

    async def get_attachment_from_link(
        self,
        peer_id: int,
        link: str,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> str:
        file_data = BytesIO(await self.client.request_data("GET", link))
        return await self.get_attachment_from_io(
            peer_id,
            file_data,
            title=title,
            tags=tags,
            file_extension=file_extension,
            file_name=file_name,
        )

    async def get_attachments_from_links(
        self,
        peer_id: int,
        links: typing.List[str],
        file_extensions: typing.Sequence[str] = (),
        file_names: typing.Sequence[str] = (),
        titles: typing.Sequence[str] = (),
        tags_list: typing.Sequence[str] = (),
    ) -> str:
        ready_attachments: typing.List[str] = []
        for link, title, tags, file_extension, file_name in itertools.zip_longest(
            links, titles, tags_list, file_extensions, file_names, fillvalue="Document"
        ):
            ready_attachments.append(
                await self.get_attachment_from_link(
                    peer_id,
                    link,
                    title=title,
                    tags=tags,
                    file_extension=file_extension,
                    file_name=file_name,
                )
            )
        return ",".join(ready_attachments)

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

    @staticmethod
    def handle_error(upload_data: dict):
        err = upload_data.get("error")
        if err == "bad_image":
            err = (
                "bad_image. You chose bad file extension or mismatch it."
                " Add extension parameter - file_extension='your_file_extension'"
            )
        if err:
            raise UploadException(err)


class VoiceUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.AUDIO_MESSAGE)

    async def upload(
        self,
        upload_url: str,
        file_data: BinaryIO,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
    ) -> DocsSaveResponseModel:
        if not hasattr(file_data, "name"):
            setattr(file_data, "name", "Document.ogg")

        upload_data = self.json_deserialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file": file_data}
            ),
        )

        self.handle_error(upload_data)
        doc_save = (
            await self.api_context.docs.save(file=upload_data["file"], title=title, tags=tags)
        ).response
        return doc_save


class GraffitiUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.GRAFFITI)


class DocUploader(DocUploaderMixin):
    async def get_server(self, peer_id: int) -> str:
        return await self._get_server(peer_id, DocsDocAttachmentType.DOC)
