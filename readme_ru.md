![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)

> Пришло время выбросить vk_api и vkbottle. VKWave здесь.

# Что это?

Библиотека для создания высокопроизводительных и легко масштабируемых проектов, взаимодействующих с API ВКонтакте.

Она построена на asyncio и тайп хинтах Python. Минимальная версия Python - `3.7`.

Наш Telegram чат - [присоединяйтесь](https://t.me/vkwave)

## Ядро VKWave

Этот репозиторий содержит только `ядро` VKWave. Это означает, что код в этом репозитории достаточно низкоуровневый.

## Производительность

VKWave - одна из самых быстрых Python библиотек для работы с API ВКонтакте.

## Core libs

VKWave client - [ядро](./vkwave-client)\
VKWave API - [используйте VK API самым причудливым способом](./vkwave-api)\
VKWave bots - [с легкостью создавайте великолепных ботов](./vkwave-bots)\
VKWave storage & VKWave FSM - [реализация FSM для VKWave](./vkwave-bots-fsm)\
VKWave bots utils - [клавиатуры, карусели, ...](./vkwave-bots-utils)\
VKWave longpoll - [доступ к VK longpoll  (пользователь/бот)](./vkwave-longpoll)

## Сообщество

VKWave - молодой проект.

Если вы хотите создать плагин или аддон для vkwave (как `fsm` для ботов или нечто подобное) вам следует назвать проект таким образом: `vkwave-bots-fsm`.
