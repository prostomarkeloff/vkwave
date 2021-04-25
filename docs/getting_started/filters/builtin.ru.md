# Встроенные фильтры

По умолчанию в VkWave есть несколько фильтров, которые импортируются как `#!python from vkwave.bots.core.dispatching import filters`:

## EventTypeFilter

Отсеивает по типу события (новое сообщение, пользователь разрешил писать ему от имени бота и пр. Полный список событий в [документации ВК](https://vk.com/dev/groups_events))

``` python hl_lines="2"
# Ловит все разрешения на отправку сообщений...
@bot.handler(filters.EventTypeFilter("message_allow"))
def only_allows(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```

## TextFilter

Отсеивает по тексту пришедшего сообщения

``` python hl_lines="2"
# Ловит все сообщения, в которых есть hi
@bot.message_handler(filters.TextFilter("hi"))
def only_hi_in_text(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```

Можно передать список из нескольких строк, тогда обработчик сработает, когда хотя бы строка из списка встретилась в сообщении

``` python hl_lines="2"
# Ловит все сообщения, в которых есть hi или hello или привет или ку
@bot.message_handler(filters.TextFilter(["hi", "hello", "привет", "ку"]))
def only_greetings_in_text(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```

## PayloadFilter

Отсеивает по payload`у (полезная нагрузка) пришедшего сообщения
(Скрытая строка, которая приходит, когда пользователь нажимает на кнопку встроенной клавиатуры. [Подробнее о клавиатурах](https://vk.com/dev/bots_docs_3?f=4.%2B%D0%9A%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B%2B%D0%B4%D0%BB%D1%8F%2B%D0%B1%D0%BE%D1%82%D0%BE%D0%B2))

``` python hl_lines="2"
# Ловит все сообщения, пейлоад которых равен {"button": "start"}
@bot.message_handler(filters.PayloadFilter({"button": "start"}))
def only_start_button_pressed(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```


## ChatActionFilter

Отсеивает по событию в беседе (например, новый участник беседы. [Полный список событий беседы в описании поля action](https://vk.com/dev/objects/message))
``` python hl_lines="2"
# Ловит все приглашения новых участников беседы
@bot.message_handler(filters.ChatActionFilter("chat_invite_user"))
def only_new_user_invited(event: SimpleBotEvent):
    event.ans("Добро пожаловать!")  # ...и отвечает на них
```

## CommandsFilter

Отсеивает по наличию команд в тексте сообщения. По умолчанию командой считаются сообщения, начинающиеся с `!` или `/`, но это можно настроить, передав фильтру аргумент `prefixes` со списком или кортежем
``` python hl_lines="2"
# Ловит все сообщения с командой `/hello` или `!hello`
@bot.message_handler(filters.CommandsFilter("hello"))
def only_new_user_invited(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```

## RegexFilter

Отсеивает по тексту сообщения (с использованием регулярных выражений)
``` python hl_lines="2"
# Ловит все сообщения со словом, первая буква которого `п`, последняя `т`
@bot.message_handler(filters.RegexFilter(r"^п\w*т$"))
def only_matched_by_regex(event: SimpleBotEvent):
    event.ans("Сообщение соответствует регулярке!")  # ...и отвечает на них
```

## MessageFromConversationTypeFilter

Отсеивает по типу диалога, откуда пришло сообщение

Доступные типы диалогов:

| Личные                              | Беседы               |
| ----------------------------------- | -------------------- |
| `from_pm`, `from_dm`, `from_direct` | `from_chat`, `chat`  |

``` python hl_lines="2"
# Ловит все сообщения из личных переписок бота
@bot.message_handler(filters.MessageFromConversationTypeFilter("from_pm"))
def only_private_messages(event: SimpleBotEvent):
    event.ans("Новое сообщение из личного чата!")  # ...и отвечает на них
```

## FromMeFilter

Отсеивает по отправителю сообщения (бот или его собеседник). Работает только для юзерботов.
``` python hl_lines="2"
# Ловит все сообщения от бота
@bot.message_handler(filters.FromMeFilter(True)
def only_by_me(event: SimpleBotEvent):
    event.ans("Новое сообщение от меня")  # ...и отвечает на них
```

## MessageArgsFilter

Отсеивает по количеству аргументов в команде

Имеет два параметра:

| Параметр         | Описание                  |
| ---------------- | ------------------------- |
| `args_count`     | Количество аргументов     |
| `command_length` | Количество слов в команде |

``` python hl_lines="2"
# Ловит все сообщения в которых есть два аргумента (например, "/start arg1 arg2")
@bot.message_handler(filters.MessageArgsFilter(args_count=2))
def only_with_two_args(event: SimpleBotEvent):
    event.ans("В сообщении два аргумента: {0}!".format(event['args']))  # ...и отвечает на них
```

## FwdMessagesFilter

Отсеивает по количеству пересланных сообщений

Если число не указано, реагирует на любое количество
``` python hl_lines="2"
# Ловит все сообщения от бота, в которых есть пересылаемые сообщения
@bot.message_handler(filters.FwdMessagesFilter()
def only_by_me(event: SimpleBotEvent):
    event.ans("Переслали сообщение")  # ...и отвечает на них
```


## ReplyMessageFilter

Отсеивает по наличию ответа на сообщение

``` python hl_lines="2"
# Ловит все сообщения от бота, которые отвечают на сообщение
@bot.message_handler(filters.ReplyMessageFilter(True)
def only_by_me(event: SimpleBotEvent):
    event.ans("Есть ответ на сообщение")  # ...и отвечает на них
```


## TextStartswithFilter

Отсеивает по тому, начинается ли текст сообщения с указанной строки (может принимать список, тогда фильтр сработает, если хотя бы одна проверка сработала)

``` python hl_lines="2"
# Ловит все сообщения, начинающиеся на "приве"
@bot.message_handler(filters.TextStartsWithFilter("приве")
def only_by_me(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```


## PayloadContainsFilter

Отсеивает по наличию ключа в пейлоаде (значение при этом не проверяется)

``` python hl_lines="2"
# Ловит все сообщения, в пейлоаде которых есть ключ button
@bot.message_handler(filters.PayloadContainsFilter("button")
def only_by_me(event: SimpleBotEvent):
    event.ans("Нажата кнопка с пейлоадом button!")  # ...и отвечает на них
```
