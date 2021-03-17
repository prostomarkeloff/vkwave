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


Так же можно использовать символы `&`, `|` или `~` между фильтрами в хендлере для "И", "ИЛИ", "НЕ" соответственно:

``` python hl_lines="3-6"
# Ловит все сообщения из приватных чатов или те в которых не встречается hi
@bot.message_handler(
        ~filters.TextFilter("hi")
        | filters.MessageFromConversationTypeFilter("from_pm")
    )
)
def not_hi_or_text_from_pm(event: SimpleBotEvent):
    event.ans("Привет!")  # ...и отвечает на них
```
