from vkwave.bots.easy import SimpleLongPollGroupBot, TaskManager


bot = SimpleLongPollGroupBot(tokens="MyToken", group_id=123456789)

# or if you want do a lot of requests without 'to many requests' errors
# bot = SimpleLongPollBot(tokens=["MyToken1", "MyToken2", "MyToken3"], group_id=123456789)


@bot.message_handler(bot.text_filter("hello"))
async def simple(event: bot.SimpleEvent):
    await event.answer("hello from vkwave!")


@bot.message_handler(bot.command_filter(commands=["start"]))
async def start(event: bot.SimpleEvent):
    user_data = (
        await bot.api_context.users.get(user_ids=event.object.object.message.peer_id)
    ).response[0]
    user_name = user_data.first_name
    await event.answer(f"You just started, {user_name}")


bot.run_forever()

# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
