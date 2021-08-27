# Using

This part of library shouldn't be used directly, but will be useful if you want to write VKWave's extensions.

## How to

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
