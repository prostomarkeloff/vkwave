import typing
from io import BytesIO
from typing import BinaryIO, Generic, List, TypeVar

from vkwave.bots.utils.uploaders.uploader import BaseUploader
from vkwave.types.objects import PhotosPhoto


class PhotoUploader(BaseUploader[typing.List[PhotosPhoto]]):
    async def get_server(self, peer_id: int) -> str:
        server_data = await self.api_context.photos.get_messages_upload_server(peer_id=peer_id)
        return server_data.response.upload_url

    async def upload(
        self,
        upload_url: str,
        file_data: typing.BinaryIO,
        file_name: typing.Optional[str] = None,
        file_extension: typing.Optional[str] = None,
    ) -> typing.List[PhotosPhoto]:
        file_name = file_name or "Photo"
        file_extension = file_extension or "jpg"
        if not hasattr(file_data, "name"):
            setattr(file_data, "name", f"{file_name}.{file_extension}")

        upload_data = self.json_deserialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file1": file_data}
            )
        )

        self.handle_error(upload_data)

        photo_sizes = (
            await self.api_context.photos.save_messages_photo(
                photo=upload_data["photo"], server=upload_data["server"], hash=upload_data["hash"],
            )
        ).response
        return photo_sizes

    def attachment_name(self, photo: typing.List[PhotosPhoto]) -> str:
        p = photo[-1]
        return (
            f"photo{p.owner_id}_{p.id}"
            if not p.access_key
            else f"photo{p.owner_id}_{p.id}_{p.access_key}"
        )


class WallPhotoUploader(BaseUploader[typing.List[PhotosPhoto]]):
    # https://www.youtube.com/watch?v=W01B6CAGM5Q

    async def get_server(self, group_id: int) -> str:
        server_data = await self.api_context.photos.get_wall_upload_server(group_id=-group_id)
        return server_data.response.upload_url

    async def get_attachment_from_io(
        self,
        f: BinaryIO,
        group_id: typing.Optional[int] = None,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
    ) -> str:
        upload_url = await self.get_server(group_id)
        return self.attachment_name(await self.upload(upload_url, f, group_id=group_id))

    async def get_attachment_from_path(
        self,
        file_path: str,
        group_id: int,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
    ) -> str:
        with open(file_path, "rb") as file_data:
            return await self.get_attachment_from_io(f=file_data, group_id=group_id)

    async def get_attachments_from_paths(self, file_paths: List[str], group_id: int,) -> str:
        ready_attachments: List[str] = []
        for file in file_paths:
            ready_attachments.append(
                await self.get_attachment_from_path(group_id=group_id, file_path=file)
            )
        return ",".join(ready_attachments)

    async def get_attachment_from_link(
        self,
        link: str,
        group_id: int,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
    ) -> str:
        file_data = BytesIO(await self.client.request_data("GET", link))
        return await self.get_attachment_from_io(group_id=group_id, f=file_data)

    async def get_attachments_from_links(
        self,
        group_id: int,
        links: List[str],
        file_extensions: typing.Optional[str] = None,
        file_names: List[str] = None,
    ) -> str:
        # TODO: file_extension..., file_names
        ready_attachments: List[str] = []
        for link in links:
            ready_attachments.append(
                await self.get_attachment_from_link(group_id=group_id, link=link)
            )
        return ",".join(ready_attachments)

    async def upload(
        self,
        upload_url: str,
        file_data: typing.BinaryIO,
        group_id: typing.Optional[int] = None,
        file_extension: typing.Optional[str] = None,
        file_name: typing.Optional[str] = None,
    ) -> typing.List[PhotosPhoto]:
        file_name = file_name or "Photo"
        file_extension = file_extension or "jpg"
        if not hasattr(file_data, "name"):
            setattr(file_data, "name", f"{file_name}.{file_extension}")

        upload_data = self.json_deserialize(
            await self.client.request_text(
                method="POST", url=upload_url, data={"file1": file_data}
            )
        )

        self.handle_error(upload_data)

        photo_sizes = (
            await self.api_context.photos.save_wall_photo(
                photo=upload_data["photo"],
                server=upload_data["server"],
                hash=upload_data["hash"],
                group_id=abs(group_id),
            )
        ).response
        return photo_sizes

    def attachment_name(self, photo: typing.List[PhotosPhoto]) -> str:
        p = photo[-1]
        return (
            f"photo{p.owner_id}_{p.id}"
            if not p.access_key
            else f"photo{p.owner_id}_{p.id}_{p.access_key}"
        )
