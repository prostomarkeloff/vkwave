# Overview

Documentation for VKWave [WIP] [^1]

# What is it?

Framework for building high-performance & easy to scale projects interacting with VK's API.

It's built over asyncio and Python's type hints. Minimal required version is `3.7`.

Our Telegram chat - [let's chat](https://t.me/vkwave)

## VKWave core

This repostitory contains only `core` parts of VKWave. It means that code introduced in this repository is probably `low-level` and shouldn't be used directly unless otherwise specified.

## Performance

VKWave is a most fast library for Python for working with VK's API.

## Parts

- Client - [core part](./client)
- API - [use VK's API in the most fancy way](./api)
- Bots - [create awesome bots with ease](./bots)
- FSM - [FSM implementation for VKWave](./bots/fsm)
- Storage - [FSM Storage](./bots/storage)
- Bots utils - [keyboards, carousels, ...](./bots/utils)
- LongPoll - [acessing VK's longpoll (user/bot)](./longpoll)

## Community

VKWave is a young project.

If you want to create addon for VKWave (like `fsm` for bots or something like that) you should name your project like that: `vkwave-bots-fsm`.

[^1]: work in progress
