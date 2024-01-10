from vkwave.bots import SimpleLongPollBot, SimpleBotEvent, simple_bot_message_handler


class MyEvent(SimpleBotEvent):
    def my_custom_method(self):
        return 'It\'s custom method!'


bot = SimpleLongPollBot(
    tokens="",
    group_id=123,
    event=MyEvent
)


@bot.message_handler(bot.text_filter('my_event'))
async def handler(event: MyEvent):
    return event.my_custom_method()


@simple_bot_message_handler(
    bot.router,
    bot.text_filter('my_event_router'),
    event=MyEvent
)
async def handler_from_router(event: MyEvent):
    return event.my_custom_method()


bot.run_forever()
