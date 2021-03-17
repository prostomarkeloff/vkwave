# Боты-клоны

Если возникает необходимость иметь несколько копий одного и того же бота в разных сообществах, можно использовать `ClonesBot`

``` python
from vkwave.bots import SimpleLongPollBot, ClonesBot


bot = SimpleLongPollBot("Token1", 123456789)

@bot.message_handler(bot.text_filter("hello"))
def handle(_) -> str:
    return "Hello world!"


clones = ClonesBot(
    bot,
    SimpleLongPollBot("Token2",11111111),
    SimpleLongPollBot("Token3",22222222),
)

clones.run_all_bots()
```