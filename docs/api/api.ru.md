# API

У нас есть 3 класса для работы с API: `API`, `APIOptions`, `APIOptionsRequestContext`.


API это ядро. Оно содержит все токены и клиенты.

```python
from vkwave.api import API, Token, UserSyncSingleToken

my_token = Token('token')
api = API(tokens=UserSyncSingleToken(my_token))
```

В `APIOptions` содержатся `tokens`, `clients`, `strategy` и другие вещи, вы можете получить к ним доступ через `api.default_api_options`. Например вы можете добавить клиент, токен или обновить стратегию

```python
api = API(...)

api.default_api_options.add_token(tokens=[...]) # или добавить только один токен
```

Но только с этим вы не можете сделать запрос в API.

Вам нужно получить контекст!

```python
api_session = API(...)

api = api_session.get_context()
```

Когда вы пишете это - вы получаете `APIOptionsRequestContext`. Он содержит все методы и собственный `APIOptions`.


```python
result = await api.status.get()
print(result.response.text)
```


## API Handler

У вас может возникнуть вопрос. Как получать контекст API, прямо из хендлера, неужели придется везде импортировать класс API? Но нет, получить контекст вы можете получить прямо из полученного вами события:
```python
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

bot = SimpleLongPollBot(tokens='mytoken', group_id=-1)

@bot.message_handler(bot.command_filter('getuser'))
async def get_user(event: SimpleBotEvent):
    api = event.api_ctx
    
    user_id = event.text.split()[1]
    user_info = (await api.users.get(user_ids=user_id)).response[0]
    
    return f'Информация о пользователе: {user_info}'

```

Через данный способ также можно получить доступ к опциям API через api.pi_options.
