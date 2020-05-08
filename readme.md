![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)

> It's time to carry out vk_api & vkbottle. VKWave is here.

[Русская версия](https://github.com/fscdev/vkwave/blob/master/readme_ru.md)

[Why VKWave?](./why_vkwave.md)

```python
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)

@bot.message_handler()
def handle(_) -> str:
    return "Hello world!"

bot.run_forever()

```

# What is it?

Framework for building high-performance & easy-to-scale projects to interact with VK's API.

It's built over asyncio and Python's type hints. Minimal version required is `3.7`.

Our Telegram chat - [let's chat](https://t.me/vkwave)

Current maintainer of this project is [@kesha1225](https://github.com/kesha1225)

## Installation

```
pip install vkwave
```

or with latest updates
```
pip install https://github.com/fscdev/vkwave/archive/master.zip
```

## VKWave core

This repostitory contains only `core` parts of VKWave. It means that code introduced in this repository is probably `low-level` and shouldn't be used directly unless otherwise specified.

## Performance

VKWave is the fastest library for Python for working with VK's API.

## Parts

- Client - [core part](./vkwave/client)
- API - [use VK's API in the most fancy way](./vkwave/api)
- Bots - [create awesome bots with ease](./vkwave/bots)
- FSM - [FSM implementation for VKWave](./vkwave/bots/fsm)
- Storage - [FSM Storage](./vkwave/bots/storage)
- Bots utils - [keyboards, carousels, ...](./vkwave/bots/utils)
- LongPoll - [acessing VK's longpoll (user/bot)](./vkwave/longpoll)

## Community

VKWave is young project.

If you want to create an addon for VKWave (like `fsm` for bots) you should name your project like that: `vkwave-bots-fsm`.
