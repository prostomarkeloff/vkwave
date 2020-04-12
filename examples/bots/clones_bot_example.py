"""
create many bots with the same functionality
"""

from vkwave.bots.easy import SimpleLongPollBot, TaskManager, ClonesBot


bot = SimpleLongPollBot(tokens=["Bot0TOKEN"], group_id=444, )


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleBotEvent):
    await event.answer("HELLO")


clones = ClonesBot(bot, SimpleLongPollBot("Bot1TOKEN", 192868628), SimpleLongPollBot("Bot2TOKEN", 172702125))

clones.run_all_bots()


# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
