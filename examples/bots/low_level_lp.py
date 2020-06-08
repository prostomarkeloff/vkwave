from vkwave.bots import LowLevelBot
from vkwave.types.bot_events import BotEventType


bot = LowLevelBot("Token", 12345)  # Bot

#  bot = LowLevelBot("Token") # User (not recommended, because events will come in strange lists)


async def not_fast_mode():
    # You can ignore all lp errors
    async for event in bot.listen(ignore_errors=True):

        # for User:
        # from vkwave.types.user_events import EventId
        # event[0] == EventId.MESSAGE_EVENT

        if event.type == BotEventType.MESSAGE_NEW:
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
        if event["type"] == BotEventType.MESSAGE_NEW:
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
