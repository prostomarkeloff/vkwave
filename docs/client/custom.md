# Custom clients

Using VKWave you get good chance to customize your workflow. 

However, other libraries for VK-API support this feature, but VKWave allows you more.

## For what?

While creating applications we get __the__ problems. It can be - limits of APIs, wishes of customers, so on.

Some of those you might solve by changing your `high-level` code. VKWave introduces another way - you should control `low-level` part of code. And yes, VKWave lets you to do it by the easiest way, your code is still staying `high-level`.

## Example

In this 'article' I'll show you how to create a `fake` client. In reality it can be anything, you could send requests to another server, for example.

**Note**: I omitted type hints in this example.

```python
from vkwave.client.abstract import AbstractAPIClient
from vkwave.client.context import RequestContext

async def callback(method_name, **kwargs):
    return {"response": {"text": "it's fake!"}}

class FakeClient(AbstractHTTPClient):
    async def request(self, method_name, **kwargs):
        return RequestContext(exceptions={}, method_name=method_name, request_callback=callback, request_params=kwargs)

    async def close(self):
        print("closing nothing...")

```

Other parts of `vkwave core` will accept http client as argument.
