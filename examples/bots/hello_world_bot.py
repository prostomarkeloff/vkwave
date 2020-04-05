from vkwave.bots.easy import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)


@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"


bot.run_forever()
