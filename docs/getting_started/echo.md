# Эхо-бот

Самый простой пример, для начала работы с фреймворком это бот, который в ответ на любое сообщение будет присылать его же.

``` python
# Импортируем необходимые классы
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

# Создаём объект бота
bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

# Региструем обработчик событий, который будет ловить все новые сообщения...
@bot.message_handler()
def handle(event: SimpleBotEvent) -> str:
    return event.object.object.message.text  # ...и отвечать на них текстом нового сообщения 

bot.run_forever()  # Запускаем бота
```