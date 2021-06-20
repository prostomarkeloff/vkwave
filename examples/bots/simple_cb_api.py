from vkwave.bots import SimpleCallbackBot


bot = SimpleCallbackBot(
    group_id=123456,
    host="127.0.0.1",
    path="/",
    port=80,
    tokens="Token",
    confirmation_key="CONFIRMATION_KEY",
    secret="SECRET_KEY",
)


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleBotEvent):
    await event.answer("HELLO")


bot.run_forever()
