# Custom clients

Using of VKWave gives you good customization options. 


## What for?

When we creating application, we can get a lot of problems, like API limits, customers' requests and so on. 

Some of them you can solve by modifying *high-level* code. VKWave gives another way to do it - you can control *low-level* of your application and your code will remain *high-level*.

## Example

How to create custom client? It can be whatever you want, i. e. it can send requests to another server.


```python
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

Other parts of `vkwave core` will get http клиент as parameter.
