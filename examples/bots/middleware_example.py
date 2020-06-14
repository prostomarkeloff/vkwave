"""
Answer on all messages besides "dog"
"""


from vkwave.bots import SimpleLongPollBot, BotEvent, BaseMiddleware, MiddlewareResult

bot = SimpleLongPollBot(tokens="123", group_id=456,)

# raw middleware
# class Middleware(BaseMiddleware):
#     async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
#         if event.object.object.message.text == "dog":
#             return MiddlewareResult(False)
#         return MiddlewareResult(True)
# bot.middleware_manager.add_middleware(Middleware())


@bot.middleware()
async def check(event: BotEvent) -> MiddlewareResult:
    if event.object.object.message.text == "dog":
        print(f"{event.object.object.message.from_id} loves dogs")
        return MiddlewareResult(False)
    return MiddlewareResult(True)


@bot.message_handler()
async def handle(event: bot.SimpleBotEvent):
    await event.answer(f"i love cats")


bot.run_forever()
