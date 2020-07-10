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

Framework for building high-performance & easy to scale projects interacting with VK's API.

It's built over asyncio and Python's type hints. Minimal required version is `3.7`.

Our Telegram chat - [let's chat](https://t.me/vkwave)

Current maintainer of this project is [@kesha1225](https://github.com/kesha1225)

## Installation

Install tested and stable version from PyPi:

```
pip install vkwave
```

Or from GitHub but with the latest updates.
```
pip install https://github.com/fscdev/vkwave/archive/master.zip
```


## Performance

VKWave is not **the fastest**. It is because of our wish to make customizable and suitable for all kind of tasks library.

But we are always interested in improving performance, so feel free to make PRs and discuss performance problems.

## Community

VKWave is a young project.

### Chat

How been mentioned earlier we have [the chat in Telegram](https://t.me/vkwave).

There is no chat in VK but you always is able to create your own and ever get a mention here.

### Addons

If you want to create addon for VKWave (for example much easier way to write bots, like `vkwave.bots.addons.easy`) you should name your project like that: `vkwave-bots-really-easy`.

The general pattern for these things is `vkwave-<part-of-vkwave>-<name>`.

