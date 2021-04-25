# Attachments' uploaders

## To message

### Images

```python
from vkwave.api import API
from vkwave.bots.utils.uploaders import PhotoUploader
from vkwave.client import AIOHTTPClient

api = API(clients=AIOHTTPClient(), tokens="token")
uploader = PhotoUploader(api.get_context())


async def main():
    big_attachment = await uploader.get_attachments_from_paths(
        peer_id=578716413,
        file_paths=["photo1.jpg", "photo2.jpg", "photo3.jpg"],
    )
    await api.get_context().messages.send(
        user_id=578716413, attachment=big_attachment, random_id=0
    )
```

### Voice message

```python
from vkwave.api import API
from vkwave.bots.utils.uploaders import VoiceUploader
from vkwave.client import AIOHTTPClient

api = API(clients=AIOHTTPClient(), tokens="token")
uploader = VoiceUploader(api.get_context())


audio_message = await uploader.get_attachment_from_path(
    peer_id=578716413,
    file_path="audio.ogg",
)
await api.get_context().messages.send(
    user_id=578716413, attachment=audio_message, random_id=0
)

```

### Documents
```python
from vkwave.api import API
from vkwave.bots.utils.uploaders import DocUploader
from vkwave.client import AIOHTTPClient

api = API(clients=AIOHTTPClient(), tokens="token")

doc = await DocUploader(api.get_context()).get_attachment_from_link(
        peer_id=123,
        link="https://user-images.githubusercontent.com/28061158/74590410-239e3300-501f-11ea-9774-27ee507a1e1e.jpg",
        title="my document title"
    )
await api.get_context().messages.send(user_id=1234, attachment=doc, random_id=0)
```


## To wall

**Works only with user's token**

### Images

```python
from vkwave.api import API
from vkwave.bots.utils.uploaders import WallPhotoUploader
from vkwave.client import AIOHTTPClient

api = API(clients=AIOHTTPClient(), tokens="token")

photo = await WallPhotoUploader(api.get_context()).get_attachment_from_link(
        group_id=-191949777,
        link="https://user-images.githubusercontent.com/28061158/74590410-239e3300-501f-11ea-9774-27ee507a1e1e.jpg",
    )
await api.get_context().wall.post(owner_id=-191949777, attachments=photo)
```
