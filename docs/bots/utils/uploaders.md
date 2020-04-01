# Uploaders

It will help you with send attachments in messages.

Upload photo from file
```python
from vkwave.bots.utils.uploaders.photo_uploader import PhotoUploader

api = API(clients=client, tokens=token)
uploader = PhotoUploader(api.get_context())


async def main():
    big_attachment = await uploader.get_attachments_from_paths(
        peer_id=578716413,
        file_paths=["photo.jpg", "photo.jpg", "photo.jpg"],
    )
    await api.get_context().messages.send(
        user_id=578716413, attachment=big_attachment, random_id=0
    )
```


Upload photo by link
```python
big_attachment = await uploader.get_attachments_from_links(
    peer_id=578716413,
    links=[
        "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
        "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
        "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
    ],
)
```


Upload audio message

```python
from vkwave.bots.utils.uploaders.audio_uploader import VoiceUploader
uploader = VoiceUploader(api.get_context())


audio_message = await uploader.get_attachment_from_path(
    peer_id=578716413,
    file_path="audio.ogg",
)
await api.get_context().messages.send(
    user_id=578716413, attachment=audio_message, random_id=0
)
```