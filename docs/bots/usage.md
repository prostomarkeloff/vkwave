# Usage

With this module you can create group/user bots easily. For 
setting up a simple handler you'll need  less than six lines od code

In this example you can see a group bot with filter on ```message_new```
event, on text ```hello``` and with handler, which cast your string for 
answer to user to normal response.
```python
import logging
import asyncio

from vkwave.client import AIOHTTPClient
from vkwave.api import BotSyncSingleToken, Token, API
from vkwave.bots import (
    TokenStorage,
    Dispatcher,
    BotLongpollExtension,
    DefaultRouter,
    GroupId,
    EventTypeFilter,
)
from vkwave.types.bot_events import BotEventType
from vkwave.longpoll import BotLongpollData, BotLongpoll


logging.basicConfig(level=logging.DEBUG)
bot_token = Token("123")
gid = 456


async def main():
    client = AIOHTTPClient()
    token = BotSyncSingleToken(bot_token)
    api_session = API(token, client)
    api = api_session.get_context()
    lp_data = BotLongpollData(gid)
    longpoll = BotLongpoll(api, lp_data)
    token_storage = TokenStorage[GroupId]()
    dp = Dispatcher(api_session, token_storage)
    lp_extension = BotLongpollExtension(dp, longpoll)
    router = DefaultRouter()

    simple_handler = (
        router.registrar.new()
        .with_filters(
            lambda event: event.object.object.message.text == "hello",
            EventTypeFilter(BotEventType.MESSAGE_NEW),
        )
        .handle(lambda event: f"hello, {event.object.object.message.from_id}")
        .ready()
    )
    #  >> hello
    #  >> hello, 578716413

    router.registrar.register(simple_handler)

    dp.add_router(router)
    await dp.cache_potential_tokens()
    await lp_extension.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

```

Also if you want to create it with another way.

```python
...

class TextFilter(BaseFilter):
    async def check(self, event: BotEvent) -> FilterResult:
        return FilterResult(event.object.object.message.text == "hello")


class MyCallback(BaseCallback):
    def __init__(self, func: Callable[[BaseEvent], Awaitable[Any]]):
        self.func = func

    async def execute(self, event: BaseEvent) -> Any:
        # do smth
        await asyncio.sleep(5)
        return await self.func(event)


async def answer(event: BotEvent):
    event: BotEvent
    return f"hello, {event.object.object.message.from_id}"


def get_handler(router):
    event_type_filter = EventTypeFilter(BotEventType.MESSAGE_NEW)
    text_filter = TextFilter()
    result_callback = MyCallback(answer)

    simple_handler = router.registrar.new()
    simple_handler.filters = [event_type_filter, text_filter]
    simple_handler.callback = result_callback
    return simple_handler


async def main():
    ...

    simple_handler = get_handler(router)
    router.registrar.register(simple_handler.ready())

    dp.add_router(router)
    await dp.cache_potential_tokens()
    await lp_extension.start()

```

And another one:


```python
router = DefaultRouter()


@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "hello",
    EventTypeFilter(BotEventType.MESSAGE_NEW),
)
def simple_handler(event: BotEvent):
    return f"hello, {event.object.object.message.from_id}"


@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "bye",
    EventTypeFilter(BotEventType.MESSAGE_NEW),
)
async def another_simple_handler(event: BotEvent):
    return await event.api_ctx.messages.send(
        message=f"bye, {event.object.object.message.from_id}",
        random_id=0,
        user_id=event.object.object.message.from_id,
    )

```