# Overview

Документация для VKWave [WIP] [^1]

# Что это?

Фреймворк для создания высокопроизводительных и легких для расширения проектов, взаимодействующих с VK API.

Он построен на asyncio и тайп хинтах. Минимальная поддерживаемая версия python - `3.7`.


Наш телеграм чат - [let's chat](https://t.me/vkwave)

## Производительность

VKWave - это не самая быстрая библиотека, из-за нашей уверенности в том, что лёгкая настройка под себя, а также удобность при использовании во всех задач явлюятся более важными характеристиками библиотеки, чем скорость.

Но мы всегда заинтересованы в улучшении производительности, поэтому не стесняйтесь делать Pull Request-ы и обсуждать проблемы производительности.

## Части

- Client - [core part](./client)
- API - [use VK's API in the most fancy way](./api)
- Bots - [create awesome bots with ease](./bots)
- FSM - [FSM implementation for VKWave](./bots/fsm)
- Storage - [FSM Storage](./bots/storage)
- Bots utils - [keyboards, carousels, ...](./bots/utils)
- LongPoll - [acessing VK's longpoll (user/bot)](./longpoll)


## Дополнения

Если вы хотите создать дополнение для VKWave (например, более простой способ написания ботов, даже проще `vkwave.bots.addons.easy`), то вам следует назвать свой проект так: `vkwave-bots-really-easy`.

Общий паттерн для дополнений: `vkwave-<часть-vkwave>-<название-проекта>`.
