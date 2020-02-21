# vkwave-types

This part of vkwave contains pydantic types, based on official vk-schema.

## Installation

```bash
pip install vkwave-types
```

## Usage

You can use this vkwave module for standardization your vk data. For
example, you make request to vk api and want to get statically-typed object. Watch and learn!

```python3
import requests
from vkwave_types.responses import StatusGetResponse


def get_my_status(token: str) -> StatusGetResponse:
    resp = requests.get(
        "https://api.vk.com/method/status.get",
        params={"v": "5.103", "access_token": token},
    )
    return StatusGetResponse(**resp.json())


status: StatusGetResponse = get_my_status(token="123")
print(status.response.text)

```

Beautiful, isn't it? And more importantly, vkwave-types includes ALL of vk schema parts:
objects/responses/longpoll events.
