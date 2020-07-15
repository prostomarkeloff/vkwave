# Обзор

Эта часть содержит pydantic типы, основанные на официальной vk-schema.

## Usage

Вы можете использовать этот модуль для стандартизации ваших данных, полученных от Вконтакте. Для примера 
вы можете сделать запрос к vk api и получить статически типизированный объект.

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

Что важнее, `vkwave.types` содержит ВСЕ части vk-schema и постоянно обновляется.
