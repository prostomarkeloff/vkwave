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
from vkwave.client.factory import DefaultFactory, AbstractFactory

async def callback(method_name, params: dict):
    return {"response": {"text": "it's fake!"}}

class FakeClient(AbstractHTTPClient):
    def __init__(self):
        self._factory = DefaultFactory()

    @property
    def context_factory(self) -> AbstractFactory:
        return self._factory

    def set_context_factory(self, factory: AbstractFactory):
        self._factory = factory

    async def request(self, method_name, params: dict):
        ctx = self.context_factory.create_context(
            request_callback=callback,
            method_name=method_name,
            request_params=params,
            exceptions={},
        )
        return ctx

    async def close(self):
        print("closing nothing...")

```

Other parts of `vkwave core` will accept http client as argument.
