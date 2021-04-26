# Easy bots

Wrapper over `vkwave.bots` to fast bots creating.

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()
```

**vkwave.bots.easy** supports:

- Simple sessions creating


```python
from vkwave.bots import create_api_session_aiohttp

api_session = create_api_session_aiohttp("TOKEN")

# api_session.api.get_context().users.get()
```


 - Multiple tokens

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens=["MyToken1","MyToken2","MyToken3"], group_id=123456789)

@bot.message_handler(bot.text_filter("bye"))
def handle(_) -> str:
    return "bye world"

@bot.message_handler(bot.text_filter("hello"))
async def handle(event: bot.SimpleBotEvent):
    await event.answer("hello world!")

bot.run_forever()
```

- Bots-clones (many bots with common handlers)

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

If don't wanna use `SimpleLongPollBot`, but wanna simplify creating handlers - use `easy_handlers`

```python
from vkwave.bots import simple_bot_message_handler, SimpleBotEvent, DefaultRouter, TextFilter

router = DefaultRouter()


@simple_bot_message_handler(router, TextFilter("hello"))
async def easy(event: SimpleBotEvent):
    await event.answer("got hello")

```

It have several handlers:
    - `simple_bot_message_handler` - Catches new messages in group's bot
    - `simple_bot_handler` - Catches all events in group's bot
    - `simple_user_message_handler` - Catches new messages in user's bot
    - `simple_user_handler` - Catches all events in group's bot
