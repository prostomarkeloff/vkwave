# Обзор

This part contains pydantic types, based on official vk-schema.

## Usage

You can use this module to normalize data got from VK and get static typed object.

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
