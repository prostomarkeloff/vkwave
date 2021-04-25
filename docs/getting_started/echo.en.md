# Echo-bot

Simpliest example to start working with VKWave is bot, which to any message answers the same message.

``` python
# Needed imports
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

# Creating instance of the bot
bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

# Registering handler, which will catch all incoming messages...
@bot.message_handler()
def echo(event: SimpleBotEvent) -> str:
    return event.object.object.message.text  # ...and answering to it with text of new message 

bot.run_forever()  # Run the bot
```