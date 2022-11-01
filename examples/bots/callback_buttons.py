from vkwave.bots import CallbackAnswer, Keyboard, PayloadFilter, SimpleLongPollBot
from vkwave.types.bot_events import BotEventType

bot = SimpleLongPollBot(tokens=["Token"], group_id=123)


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleBotEvent):
    kb = Keyboard()
    kb.add_callback_button(payload={"21321": "123"}, text="123")
    await event.answer("HELLO", keyboard=kb.get_keyboard())


@bot.handler(bot.event_type_filter(BotEventType.MESSAGE_EVENT), PayloadFilter({"21321": "123"}))
async def all(event: bot.SimpleBotEvent):
    await event.callback_answer(event_data=CallbackAnswer.open_link(link="https://google.com"))


bot.run_forever()
