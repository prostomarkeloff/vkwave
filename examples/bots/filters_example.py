from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="1234", group_id=456)

# from vkwave.bots.core.dispatching.filters.base import BaseEvent, BaseFilter, FilterResult

# class BotFilter(BaseFilter):
#     async def check(self, event: BaseEvent) -> FilterResult:

#         text: str = event.object.object.message.text

#         if "я бот" in text:
#             return FilterResult(True)
#         return FilterResult(False)

# @bot.message_handler(BotFilter())
# async def handle(event: bot.SimpleBotEvent):
#     await event.answer("Бот Детектед")

# Мы переопределили метод check в классе-фильтре. Он у фильтра главный.


# На самом деле bot.command_filter, bot.args_filter и тд. - ссылки на классы-фильтры(наследуемые от BaseFilter).

# из исходников :

# class CommandsFilter(BaseFilter):
#     ...

# class BaseSimpleLongPollBot:
#     def __init__(self, ...):
#     ...
#     self.command_filter = CommandsFilter
#     ...

# Я, конечно же, сократил код, но суть вы поняли.


@bot.message_handler(
    bot.conversation_type_filter(from_what="from_chat")
)  # В хэндлер, к слову, вы можете запихать сколько душе угодно фильтров(там *args стоит).
async def handle(event: bot.SimpleBotEvent):
    await event.answer("hello to chat!")


@bot.message_handler(bot.fwd_filter(fwd_count=3))  # bot.fwd_filter() for any count
async def handle(event: bot.SimpleBotEvent):
    await event.answer("3 fwd...")


@bot.message_handler(bot.args_filter(args_count=2))
async def handle(event: bot.SimpleBotEvent):
    args = event["args"]
    await event.answer(f"Your args - {args}")


@bot.message_handler(bot.text_contains_filter("wow"))
async def handle(event: bot.SimpleBotEvent):
    await event.answer(f"Your text contains 'wow', wow!")


bot.run_forever()

# P.S.

# @bot.message_handler()
# async def handle(event: BotEvent):
#     await event.answer("Hello World!")
# и

# @bot.message_handler()
# async def handle(event: BotEvent):
#     return "Hello World!"

# одно и тоже(есть свои нюансы, но вцелом это так)
