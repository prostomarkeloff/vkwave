from vkwave.bots import SimpleLongPollBot, TTLStorage
from vkwave.bots.storage.types import Key


bot = SimpleLongPollBot(tokens="MyToken", group_id=1)
ttl = TTLStorage(default_ttl=360)


@bot.message_handler(
    bot.text_filter('удалить')
)
async def delete_data(event: bot.SimpleBotEvent):
    from_id = event.object.object.from_id
    await ttl.delete(Key(from_id))
    await event.answer('Вы успешно удалены из хранилища бота.')


@bot.message_handler()
async def get_data(event: bot.SimpleBotEvent):
    from_id = event.object.object.from_id
    user_data = await ttl.get(Key(from_id), default=None)
    if not user_data:
        await event.answer('Вы не найдены в хранилище бота. Записываю вас...')
        user_name = (await event.api_ctx.users.get(user_ids=from_id)).response[0].first_name
        await ttl.put(Key(from_id), user_name)
        await event.answer('Вы успешно записаны в хранилище бота. Ваши данные будут храниться 5 минут.')

    else:
        await event.answer('Отлично! Ваши данные есть в хранилище бота.')


bot.run_forever()
