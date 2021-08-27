# Роутеры

Роутеры - самая важная сущность любого бота в VkWave. В роутерах содержатся хендлеры, благодаря которым и осуществляется обработка событий.
## Создание

``` python
from vkwave.bots import DefaultRouter

router = DefaultRouter()
```

Роутеры могут принимать на вход [фильтры](filters/index.ru.md), благодаря которым события будут отсеиваться быстрее, не проходя сквозь все хендлеры

``` python
router = DefaultRouter(SomeFilter())

@bots.simple_bot_message_handler(
    router,
    <фильтры>
)
async def handler(ans: bots.SimpleBotEvent):
    await ans.answer(
        "Ответ",
    )
```

## Использование

```python

from module import router

bot = SimpleLongPollBot(tokens="Token", group_id=123)
bot.dispatcher.add_router(router)
```