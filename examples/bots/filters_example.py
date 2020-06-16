from vkwave.bots import SimpleLongPollBot


bot = SimpleLongPollBot(tokens="1234", group_id=456)


@bot.message_handler(bot.conversation_type_filter(from_what="from_chat"))
async def handle(event: bot.SimpleBotEvent):
    await event.answer(f"hello to chat!")


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
