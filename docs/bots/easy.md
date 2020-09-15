# Easy bots

Обёртка над vkwave.bots для быстрого создания ботов.

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()
```

**vkwave.bots.easy** поддерживает:

- Простое создание сессий


```python
from vkwave.bots import create_api_session_aiohttp

api_session = create_api_session_aiohttp("TOKEN")

# api_session.api.get_context().users.get()
```


 - Пул токенов

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens=["MyToken1","MyToken2","MyToken3"], group_id=123456789)

# ...

bot.run_forever()
```

- ClonesBot (много ботов с одним роутером и одинаковыми хендлерами, боты-клоны)

```python
from vkwave.bots import SimpleLongPollBot, ClonesBot


bot = SimpleLongPollBot(tokens=["MyToken1","MyToken2","MyToken3"], group_id=123456789)

@bot.message_handler(bot.text_filter("hello"))
def handle(_) -> str:
    return "Hello world!"


clones = ClonesBot(
    bot,
    SimpleLongPollBot("Token1",11111111),
    SimpleLongPollBot("Token2",22222222),
)

clones.run_all_bots()

```

Все клоны ответят "Hello world!" на "hello".

Если вы не хотите использовать `SimpleLongPollBot`, но создание хендлеров хочется упростить - воспользуйтесь `easy_handlers`

```python3
from vkwave.bots import simple_bot_message_handler, SimpleBotEvent, DefaultRouter, TextFilter

router = DefaultRouter()


@simple_bot_message_handler(router, TextFilter("hello"))
async def easy(event: SimpleBotEvent):
    await event.answer("got hello")

```

`simple_bot_message_handler` нужен только для событий связанных с сообщениями, помимо него еще есть:
 simple_bot_handler (для всех событий), simple_user_handler (аналогично для юзерботов), simple_user_message_handler.
    
