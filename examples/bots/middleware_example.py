"""
Answer on all messages besides "dog"
"""


from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult, SimpleLongPollBot

bot = SimpleLongPollBot(tokens="123", group_id=456,)

# raw middleware:
# class Middleware(BaseMiddleware):
#     async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
#         if event.object.object.message.text == "dog":
#             return MiddlewareResult(False)
#         return MiddlewareResult(True)

# bot.middleware_manager.add_middleware(Middleware())
# или
# bot.add_middleware(Middleware())


"""
Мидлварь имеет два основных асинхронных(!) метода:
1)  pre_process_event(event: BaseEvent) -> MiddlewareResult
обязательный, исполняется перед роутингом;


2)  post_process_event(event: BaseEvent):
необязательный, выполняется после роутинга
(и после обработки хендлером, если таковой имеется).

"""


@bot.middleware()
async def check(event: BotEvent) -> MiddlewareResult:
    """
    Этот вариант хуже по нескольким показателям:
    - не может передавать аргументы в мидлварь
    - не имеет доступа к методу post_process_event
    
    Используйте если вам не нужно вышеперечисленное или для сокращения кода.
    """
    if event.object.object.message.text == "dog":
        print(f"{event.object.object.message.from_id} loves dogs")
        return MiddlewareResult(False)
    return MiddlewareResult(True)


@bot.message_handler()
async def handle(event: bot.SimpleBotEvent):
    await event.answer("i love cats")


bot.run_forever()

"""
Вы можете создать свой мидлварь, сделать pull request,
поместив мидлварь в vkwave.bots.core.dispatching.dp.middleware.extension_middlewares,
если считаете его полезным и хотите видеть его в vkwave из коробки.
"""
