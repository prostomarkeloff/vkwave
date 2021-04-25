# Built-in filter

By default VkWave has several filters, which can be imported from `#!python from vkwave.bots.core.dispatching import filters`:

## EventTypeFilter

Filters by type of event (New message, user allowed to send messages, etc. Full list of events in [Vk's documentaton](https://vk.com/dev/groups_events))

``` python hl_lines="2"
# Handles all allows to send message...
@bot.handler(filters.EventTypeFilter("message_allow"))
def only_allows(event: SimpleBotEvent):
    event.ans("Hello!")  # ...and replies to them
```

## TextFilter

Filters by text of new message

``` python hl_lines="2"
# Catches all messages with hi
@bot.message_handler(filters.TextFilter("hi"))
def only_hi_in_text(event: SimpleBotEvent):
    event.ans("Привет!")  # ...and answers to them
```

You can pass a list of strings, then handler will work if any list's item is in message

``` python hl_lines="2"
# Catches all messages with hi or hello
@bot.message_handler(filters.TextFilter(["hi", "hello"))
def only_greetings_in_text(event: SimpleBotEvent):
    event.ans("Привет!")  # ...and answers to them
```

## PayloadFilter

Filters by payload of message [More about keyboards](https://vk.com/dev/bots_docs_3?f=4.%2B%D0%9A%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B%2B%D0%B4%D0%BB%D1%8F%2B%D0%B1%D0%BE%D1%82%D0%BE%D0%B2))

``` python hl_lines="2"
# Catches all messages which have payload {"button": "start"}
@bot.message_handler(filters.PayloadFilter({"button": "start"}))
def only_start_button_pressed(event: SimpleBotEvent):
    event.ans("Привет!")  # ...and answers to them
```


## ChatActionFilter

Filters by event in chat (i. e. new chat member. [Full of  action](https://vk.com/dev/objects/message))
``` python hl_lines="2"
# Catches all invites of new chat members
@bot.message_handler(filters.ChatActionFilter("chat_invite_user"))
def only_new_user_invited(event: SimpleBotEvent):
    event.ans("Welcome!")  # ...and answers to them
```

## CommandsFilter

Filters by command in messages' text. By default commands are the messages, starts with `!` or `/`, but you can configure it by passing an list or tuple to `prefixes` argument

``` python hl_lines="2"
# Catches all messages with `/hello` or `!hello`
@bot.message_handler(filters.CommandsFilter("hello"))
def only_new_user_invited(event: SimpleBotEvent):
    event.ans("Привет!")  # ...and answers to them
```

## RegexFilter

Filters by text message (with regex)
``` python hl_lines="2"
# Catches all messages with word starts with `h`, and last `o`
@bot.message_handler(filters.RegexFilter(r"^h\w*o$"))
def only_matched_by_regex(event: SimpleBotEvent):
    event.ans("Message matches regex!")  # ...and answers to them
```

## MessageFromConversationTypeFilter

Filters by type of chat

Available types of chats:

| Personal                            | Conversation         |
| ----------------------------------- | -------------------- |
| `from_pm`, `from_dm`, `from_direct` | `from_chat`, `chat`  |

``` python hl_lines="2"
# Catches all messages from personal dialogues
@bot.message_handler(filters.MessageFromConversationTypeFilter("from_pm"))
def only_private_messages(event: SimpleBotEvent):
    event.ans("New message from personal chat!")  # ...and answers to them
```

## FromMeFilter

Filters by sender of message (bot or his interlocutor). Works only for userbots.
``` python hl_lines="2"
# Catches all message from bot
@bot.message_handler(filters.FromMeFilter(True)
def only_by_me(event: SimpleBotEvent):
    event.ans("New message from me!")  # ...and answers to them
```

## MessageArgsFilter

Filters by amount of args in command

Have two parameters:

| Parameter        | Description                |
| ---------------- | -------------------------- |
| `args_count`     | Amount of arguments        |
| `command_length` | Amount of words in command |

``` python hl_lines="2"
# Catches all messages with two args in command (i. e., "/start arg1 arg2")
@bot.message_handler(filters.MessageArgsFilter(args_count=2))
def only_with_two_args(event: SimpleBotEvent):
    event.ans("The message has two args: {0}!".format(event['args']))  # ...and answers to them
```

## FwdMessagesFilter

Filters message by existing or amount of forwarded messages

If number didn't pass, reacts on any amount
``` python hl_lines="2"
# Cathces all messages which has forwarded messages
@bot.message_handler(filters.FwdMessagesFilter()
def with_forwarded_message(event: SimpleBotEvent):
    event.ans("Message was forwarded")  # ...and answers to them
```


## ReplyMessageFilter

Filters by having an reply to message

``` python hl_lines="2"
# Catches all messages with replied message
@bot.message_handler(filters.ReplyMessageFilter(True)
def with_replied_message(event: SimpleBotEvent):
    event.ans("Has replied message")  # ...and answers to them
```


## TextStartswithFilter

Filters by prefix of message
``` python hl_lines="2"
# Catches all messages started with "hell"
@bot.message_handler(filters.TextStartsWithFilter("hell")
def only_with_hell(event: SimpleBotEvent):
    event.ans("Hi!")  # ...and answers to them
```


## PayloadContainsFilter

Filters by having a key in payload (value not checked)

``` python hl_lines="2"
# Catches all messages with "button" key
@bot.message_handler(filters.PayloadContainsFilter("button")
def only_with_button_key(event: SimpleBotEvent):
    event.ans("Button with payload button was pressed!")  # ...and answers to them
```
