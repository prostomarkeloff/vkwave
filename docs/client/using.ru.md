# Using

Эта часть библиотеки не должна быть использована напрямую, но чтение этого будет полезным если вы хотите создавать дополнения для VKWave.

## How to

Это просто.

```python
from vkwave.client.default import AIOHTTPClient
from vkwave.client.context import ResultState
import asyncio

async def main():
    base_params = {"access_token": "xxxxxx", "v": "5.103"}

    client = AIOHTTPClient()

    ctx = client.create_request("status.get", **base_params)
    await ctx.send_request()

    if ctx.result.state is ResultState.SUCCESS:
        print(ctx.result.data["response"]["text"])
    else:
        print(ctx.result.exception)
    await client.close()

asyncio.run(main())
```
