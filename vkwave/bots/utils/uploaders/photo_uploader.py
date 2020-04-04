import typing

from vkwave.bots.utils.uploaders.uploader import BaseUploader
from vkwave.types.objects import PhotosPhoto


class PhotoUploader(BaseUploader[typing.List[PhotosPhoto]]):
    async def get_server(self, peer_id: int) -> str:
        server_data = await self.api_context.photos.get_messages_upload_server(peer_id=peer_id)
        return server_data.response.upload_url

    async def upload(
        self, upload_url: str, file_data: typing.BinaryIO
    ) -> typing.List[PhotosPhoto]:
        # really dirty hack
        # but it works
        if not hasattr(file_data, "name"):
            setattr(file_data, "name", "file.jpg")

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
