# Кастомные клиенты

Использование VKWave дает хорошие возможности для кастомизации. 

Конечно и другие библиотеки имеют похожие фишки, но VKWave дает больший простор для действий.

## Для чего?

Пока мы создаем приложение у нас возникают проблемы. Лимиты в API, пожелания заказчиков и подобные.

Некоторые из них вы можете решить, путем изменения `высокоуровневого` кода. VKWave представляет другой подход - вы можете контролировать `low-level` вашего приложения. И да, VKWave дает делать это простейшим путем, ваш код останется `high-level`.

## Пример

В этом примере я покажу вам как создать `поддельный` клиент. В реальность он может быть чем угодно, например, вы можете слать запросы в другой сервер.

**Note**: Тайп хинты будут опущены в данном примере.

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

Другие части `vkwave core` будут принимать http клиент как аргумент.
