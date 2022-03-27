"""
create many bots with the same functionality
"""
import asyncio

from vkwave.bots import SimpleLongPollBot, TaskManager, ClonesBot


bot = SimpleLongPollBot(tokens=["Bot0TOKEN"], group_id=444,)


@bot.message_handler(bot.text_filter("123"))
async def simple(event: bot.SimpleBotEvent):
    await event.answer("HELLO")


@bot.message_handler()
async def any_(event: bot.SimpleBotEvent):
    await event.answer("any")


clones = ClonesBot(
    bot, SimpleLongPollBot("Bot1TOKEN", 192868628), SimpleLongPollBot("Bot2TOKEN", 172702125)
)


async def clone_request():
    # clones.clones - тупл с клонами (SimpleLongPollUserBot или SimpleLongPollBot)
    # Запрос с первого клона
    print(await clones.clones[0].api_context.users.get())


def add_clone(clone):
    # Добавляет клона в общий список
    clones.add_clone(SimpleLongPollBot("Bot3Token", 122134648))


asyncio.get_event_loop().run_until_complete(clone_request())

clones.run_all_bots(last_handler=any_)
# В клонах хендлеры могут перемешаться, так что ставим хендлер который реагирует
# на все подряд последним


# or
# task_manager = TaskManager()
# task_manager.add_task(bot.run)
# task_manager.run()
© 2022 GitHub, Inc.
Terms
Privacy