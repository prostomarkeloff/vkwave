from vkwave.bots import Keyboard, SimpleLongPollBot
from vkwave.types.bot_events import BotEventType

bot = SimpleLongPollBot(
    tokens=["123"],
    group_id=123,
)

last_pages = {}
test_lst = list(range(20))


def get_kb(event):
    kb = Keyboard(inline=True)
    last_page = last_pages.get(event.from_id)
    if last_page is None:
        last_pages[event.from_id] = last_page = 0

    kb.add_text_button(
        text=f"текст со страницы {last_page}", payload={"button": f"button1_{last_page}"}
    )
    kb.add_row()
    kb.add_text_button(
        text=f"текст со страницы {last_page}", payload={"button": f"button1_{last_page}"}
    )
    kb.add_row()
    kb.add_text_button(
        text=f"текст со страницы {last_page}", payload={"button": f"button1_{last_page}"}
    )
    kb.add_row()
    if last_page > 0:
        kb.add_callback_button(text=f"<< {last_page - 1}", payload={"cmd": f"prev_{last_page}"})
    kb.add_callback_button(text=f"{last_page + 1} >>", payload={"cmd": f"next_{last_page}"})
    return kb


@bot.message_handler(bot.conversation_type_filter("from_pm"), ~bot.payload_filter())
async def simple(event: bot.SimpleBotEvent):
    kb = get_kb(event)
    return await event.answer(message="privet", keyboard=kb.get_keyboard())


@bot.handler(bot.event_type_filter(BotEventType.MESSAGE_EVENT))
async def pld(event: bot.SimpleBotEvent):
    cmd, number = event.payload["cmd"].split("_")
    if cmd == "next":
        last_pages[event.from_id] += 1
        kb = get_kb(event)
    elif cmd == "prev":
        last_pages[event.from_id] -= 1
        kb = get_kb(event)

    await event.api_ctx.messages.edit(
        peer_id=event.peer_id,
        message="privet",
        conversation_message_id=event.object.object.conversation_message_id,
        keyboard=kb.get_keyboard(),
        group_id=bot.group_id,
    )
    return


bot.run_forever()
