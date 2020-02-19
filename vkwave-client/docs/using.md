# Using

This library shouldn't be used directly. 

But reading it may be useful for you if you want to create addons for vkwave.

## How to

It's easy.

```python
from vkwave_client.default import AIOHTTPClient
import asyncio

async def main():
    base_params = {"access_token": "xxxxxx", "v": "5.103"}

    client = AIOHTTPClient()

    status = await client.request("status.get", **base_params)

    print(status["response"]["text"])
    
    await client.close()

asyncio.run(main())
```
