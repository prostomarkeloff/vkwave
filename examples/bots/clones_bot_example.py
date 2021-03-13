"""
create many bots with the same functionality
"""
import asyncio

from vkwave.bots import SimpleLongPollBot, TaskManager, ClonesBot


bot = SimpleLongPollBot(tokens=["Bot0TOKEN"], group_id=444,)


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleBotEvent):
    await event.answer("HELLO")


clones = ClonesBot(
    bot, SimpleLongPollBot("Bot1TOKEN", 192868628), SimpleLongPollBot("Bot2TOKEN", 172702125)
)


async def clone_request():
    # clones.clones - тупл с клонами (SimpleLongPollUserBot или SimpleLongPollBot)
    # Запрос с первого клона
    print(clones.clones[0].api_context.users.get())


asyncio.get_event_loop().run_until_complete(clone_request())

clones.run_all_bots()


# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
