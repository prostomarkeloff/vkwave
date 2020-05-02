from vkwave.bots import SimpleLongPollUserBot

bot = SimpleLongPollUserBot(tokens="UserToken")


# from_me_filter(False) -> message from other user
# from_me_filter(True) -> message from me
@bot.message_handler(bot.text_filter("hello"), bot.from_me_filter(False))
async def simple(event: bot.SimpleBotEvent):
    await event.answer("hello from vkwave!")


@bot.message_handler(bot.command_filter(commands=["start"]), bot.from_me_filter(False))
async def start(event: bot.SimpleBotEvent):
    user_data = (await bot.api_context.users.get(user_ids=event.object.object.peer_id)).response[0]
    user_name = user_data.first_name
    await event.answer(f"You just started, {user_name}")


bot.run_forever()

# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
