from vkwave.bots import SimpleLongPollBot
from vkwave.bots.addons.class_based_handlers import BaseHandler, inject_to_caster

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)
inject_to_caster() # возможность использовать ClassBasedHandlers

@bot.message_handler(bot.text_filter("привет"))
class HelloHandler(BaseHandler):
    async def handle(self, event: bot.SimpleBotEvent) -> str:
        return "Привет!!!"


bot.run_forever()
