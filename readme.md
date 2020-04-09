![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)

> It's time to carry out vk_api & vkbottle. VKWave is here.


```python
from vkwave.bots.easy.easy_bot import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()

```

[Русская версия](https://github.com/fscdev/vkwave/blob/master/readme_ru.md)
# What is it?

Framework for building high-performance & easy to scale projects interacting with VK's API.

It's built over asyncio and Python's type hints. Minimal required version is `3.7`.

Our Telegram chat - [let's chat](https://t.me/vkwave)

## VKWave core

This repostitory contains only `core` parts of VKWave. It means that code introduced in this repository is probably `low-level` and shouldn't be used directly unless otherwise specified.

## Performance

VKWave is a most fast library for Python for working with VK's API.

## Parts

- Client - [core part](./vkwave/client)
- API - [use VK's API in the most fancy way](./vkwave/api)
- Bots - [create awesome bots with ease](./vkwave/bots)
- FSM - [FSM implementation for VKWave](./vkwave/bots/fsm)
- Storage - [FSM Storage](./vkwave/bots/storage)
- Bots utils - [keyboards, carousels, ...](./vkwave/bots/utils)
- LongPoll - [acessing VK's longpoll (user/bot)](./vkwave/longpoll)

## Community

VKWave is a young project.

If you want to create addon for VKWave (like `fsm` for bots or something like that) you should name your project like that: `vkwave-bots-fsm`.
