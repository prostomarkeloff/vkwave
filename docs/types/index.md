# Oveview

This part of VKWave contains pydantic types, based on official vk-schema.

## Usage

You can use this VKWave module for standardization your vk data. For
example, you make request to vk api and want to get statically-typed object. Watch and learn!

```python
import requests
from vkwave.types.responses import StatusGetResponse


def get_my_status(token: str) -> StatusGetResponse:
    resp = requests.get(
        "https://api.vk.com/method/status.get",
        params={"v": "5.103", "access_token": token},
    )
    return StatusGetResponse(**resp.json())


status: StatusGetResponse = get_my_status(token="123")
print(status.response.text)

```

Beautiful, isn't it? And more importantly, vkwave.types includes ALL of vk schema parts:
objects/responses/longpoll events.
