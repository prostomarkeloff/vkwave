![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)

> It's time to carry out vk_api & vkbottle. VKWave is here.

# What is it?

VKWave - is a set of tools for applications that interact with VK's API.

It's built over asyncio and Python's type hints. Minimal required version is `3.7`.

## VKWave core

This repostitory contains only `core` parts of VKWave. It means that code introduced in this repository is probably `low-level` and shouldn't be used directly unless otherwise specified.

## Performance

VKWave is a most fast library for Python for working with VK's API.

## Core libs

VKWave client - [core library](./vkwave-client)
VKWave API - [use VK's API in most fancy way](./vkwave-api)
VKWave bots - [create awesome bots with ease](./vkwave-bots)
VKWave storage & VKWave FSM - [FSM implementation for VKWave](./vkwave-bots-fsm)
VKWave bots utils - [keyboards, carousels, ...](./vkwave-bots-utils)
VKWave longpoll - [acessing VK's longpoll (user/bot)](./vkwave-longpoll)

## Community

VKWave is a young project.

If you want to create addon for vkwave (like `fsm` for bots or something like that) you should name your project like that: `vkwave-bots-fsm`.
