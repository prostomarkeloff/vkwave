# Easy bots

Wrapper over vkwave.bots for faster bot creating.

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()
```

**vkwave.bots.easy** supports:

- Simple session


```python
from vkwave.bots.easy import create_api_session_aiohttp

api_session = create_api_session_aiohttp("TOKEN")

# api_session.api.get_context().users.get()
```


 - Tokens pool

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens=["MyToken1","MyToken2","MyToken3"], group_id=123456789)

@bot.message_handler(bot.text_filter("bye"))
def handle(_) -> str:
    return "bye world"

@bot.message_handler(bot.text_filter("hello"))
def handle(event: bot.SimpleBotEvent):
    await event.answer("hello world!")

bot.run_forever()
```

- ClonesBot (a lot of bots with same router)

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

All clones will answer "Hello world!" on "hello".