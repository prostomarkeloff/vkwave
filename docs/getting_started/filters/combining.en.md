# Filters combining

You can combine multiple filters in handlers, they will be combined by logical "AND"

``` python hl_lines="3 4"
# Catches all messages from private chats with hi in text
@bot.message_handler(
    filters.TextFilter("hi"),
    filters.MessageFromConversationTypeFilter("from_pm")
)
def only_hi_in_text_from_pm(event: SimpleBotEvent):
    event.ans("Привет!")  # ...and answers to it
```


Also you can use `&`, `|` or `~` between filters as "AND", "OR", "NOT":

``` python hl_lines="3-4"
# Catches all messages without hi in text or from private chats
@bot.message_handler(
        ~filters.TextFilter("hi")
        | filters.MessageFromConversationTypeFilter("from_pm")
    )
)
def not_hi_or_text_from_pm(event: SimpleBotEvent):
    event.ans("Hello!")  # ...and answers to it
```
