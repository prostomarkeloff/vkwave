![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)

> Пришло время избавиться от vk_api и vkbottle. VKWave здесь.

[Почему VKWave?](./why_vkwave.md)

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()
```

<details>
  <summary>Максимум кастомизации</summary>

  ```python
import logging
import asyncio

from vkwave.bots import (
    BotEvent,
    TokenStorage,
    Dispatcher,
    DefaultRouter,
    GroupId,
    BotLongpollExtension,
    EventTypeFilter
)
from vkwave.client import AIOHTTPClient
from vkwave.api import API, BotSyncSingleToken, Token
from vkwave.longpoll import BotLongpoll, BotLongpollData

logging.basicConfig(level=logging.DEBUG)
bot_token = Token("123")
gid = 123
router = DefaultRouter()


@router.registrar.with_decorator(EventTypeFilter("message_new"))
async def handle(event: BotEvent):
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id,
        message=f"Hello world!",
        random_id=0,
    )


async def main():
    client = AIOHTTPClient()
    token = BotSyncSingleToken(bot_token)
    api_session = API(token, client)
    api = api_session.get_context()
    lp_data = BotLongpollData(gid)
    longpoll = BotLongpoll(api, lp_data)
    token_storage = TokenStorage[GroupId]()
    dp = Dispatcher(api_session, token_storage)
    lp_extension = BotLongpollExtension(dp, longpoll)

    dp.add_router(router)
    await dp.cache_potential_tokens()
    await lp_extension.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

  ```
</details>

[Простая библиотека для быстрого доступа к API](https://github.com/prostomarkeloff/vkwave-api)

# Что это?

VKWave - это фреймворк для создания производительных и лёгких в расширении проектов, взаимодействующих с API ВКонтакте.

Он создан с использованием asyncio и аннотаций типов Python. Минимальная требуемая версия - это `3.7`.

Наш телеграм чат - [давайте общаться!](https://t.me/vkwave)

Текущий мейнтейнер этого проекта [@kesha1225](https://github.com/kesha1225)

## Установка

Установить тестированную и стабильную версию с PyPi:

```
pip install vkwave
```

Или с GitHub, со всеми свежими обновлениями.
```
pip install https://github.com/fscdev/vkwave/archive/master.zip
```
[Учебники для лёгкого старта](https://github.com/VodoGamer/vkwave-textbooks/tree/master/textbooks)

[Документация](https://fscdev.github.io/vkwave/)

[Примеры использования](https://github.com/fscdev/vkwave/tree/master/examples)


## Производительность

VKWave - это не самая быстрая библиотека, из-за нашей уверенности в том, что лёгкая настройка под себя, а также удобность при использовании во всех задач являются более важными характеристиками библиотеки, чем скорость.

Но мы всегда заинтересованы в улучшении производительности, поэтому не стесняйтесь делать Pull Request-ы и обсуждать проблемы производительности.

## Сообщество

VKWave - это очень молодой проект.

Пример бота с вынесением логики можно посмотреть в [VkWaveBotExample](https://github.com/kesha1225/VkWaveBotExample)

### Чаты

Как упоминалось ранее, у нас есть [чат в Telegram](https://t.me/vkwave).

Во Вконтакте чата нет, но вы всегда можете создать свой собственный и получить его упоминание здесь.

### Дополнения

Если вы хотите создать дополнение для VKWave (например, более простой способ написания ботов, даже проще `vkwave.bots.addons.easy`), то вам следует назвать свой проект так: `vkwave-bots-really-easy`.

Общий паттерн для дополнений: `vkwave-<часть-vkwave>-<название-проекта>`.

