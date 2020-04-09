"""
create many bots with the same functionality
"""

from vkwave.bots.easy import SimpleLongPollGroupBot, TaskManager, ClonesBot


bot = SimpleLongPollGroupBot(tokens=["Bot0TOKEN"], group_id=444, )


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleEvent):
    await event.answer("HELLO")


clones = ClonesBot(bot, SimpleLongPollGroupBot("Bot1TOKEN", 192868628), SimpleLongPollGroupBot("Bot2TOKEN", 172702125))

clones.run_all_bots()


# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
