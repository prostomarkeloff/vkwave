# Объединение фильтров

Вы можете указывать в качестве аргументов обработчиков несколько фильтров и по умолчанию они будут объединены логическим "И"

``` python hl_lines="3 4"
# Ловит все сообщения из приватных чатов, в которых есть hi
@bot.message_handler(
    filters.TextFilter("hi"),
    filters.MessageFromConversationTypeFilter("from_pm")
)
def only_hi_in_text_from_pm(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```


Дополнительно можно импортировать набор объединяющих классов: `#!python from vkwave.bots.core.dispatching.filters import base` и использовать отрицание, логическое "ИЛИ", логическое "И"

``` python hl_lines="3-6"
# Ловит все сообщения из приватных чатов или те в которых не встречается hi
@bot.message_handler(
    base.OrFilter(
        base.NotFilter(filters.TextFilter("hi")),
        filters.MessageFromConversationTypeFilter("from_pm")
    )
)
def not_hi_or_text_from_pm(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```
