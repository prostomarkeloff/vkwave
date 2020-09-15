from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)


@bot.message_handler()
def handle(_) -> str:
    """ 
    Функция может быть как синхронной, так и асинхронной
    """
    return "Hello world!"


bot.run_forever()
