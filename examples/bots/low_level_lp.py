from vkwave.bots import LowLevelBot

bot = LowLevelBot("Token", 12345)  # Bot

#  bot = LowLevelBot("Token") # User


async def not_fast_mode():
    async for event in bot.listen():
        if event.object.message.text == "/start":
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event.object.message.peer_id,
                    message="i got start",
                    random_id=0,
                )
            )
        elif event.object.message.text == "/end":
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event.object.message.peer_id,
                    message="i got end",
                    random_id=0,
                )
            )
        else:
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event.object.message.peer_id,
                    message="don't understand",
                    random_id=0,
                )
            )


async def fast_mode():
    async for event in bot.listen(fast_mode=True):
        if event["object"]["message"]["text"] == "/start":
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event["object"]["message"]["peer_id"],
                    message="i got start",
                    random_id=0,
                )
            )
        elif event["object"]["message"]["text"] == "/end":
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event["object"]["message"]["peer_id"],
                    message="i got end",
                    random_id=0,
                )
            )
        else:
            bot.react(
                bot.api_context.messages.send(
                    peer_id=event["object"]["message"]["peer_id"],
                    message="don't understand",
                    random_id=0,
                )
            )


# bot.run(main_loop=fast_mode())
bot.run(main_loop=not_fast_mode())
