# Загрузчики вложений

Каждый загрузчик реализует интерфейс `BaseUploader`:

|          Метод             |                  Описание                  |
|----------------------------|--------------------------------------------|
|`get_attachment_from_io`    | Загружает вложение-последовательность байт |
|`get_attachment_from_path`  | Загружает вложение с диска                 |
|`get_attachments_from_paths`| Загружает несколько вложений с диска       |
|`get_attachment_from_link`  | Загружает вложение по ссылке               |
|`get_attachments_from_links`| Загружает несколько вложений по ссылкам    |


## В сообщение

### Изображения

```python
from vkwave.api import API
from vkwave.bots.utils.uploaders import PhotoUploader
from vkwave.client import AIOHTTPClient

api = API(clients=AIOHTTPClient(), tokens="token")
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

### Голосовые сообщения

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

### Документы
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

!!! note
    На данный момент загрузка документов не работает ([#112](https://github.com/fscdev/vkwave/issues/112))

## На стену

**Работает только с токеном пользователя**

### Изображения

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
