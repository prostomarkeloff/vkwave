# Using

This library shouldn't be used directly. 

But reading it may be useful for you if you want to create addons for vkwave.

## How to

It's easy.

```python
from vkwave_client.default import AIOHTTPClient
from vkwave_client.context import ResultState
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
