# Обзор

VKWave API довольно удобная часть библиотеки. Скорее всего с процессе использования VKWave вы обязательно с ней столкнётесь

Она состоит из трёх частей:

* Работа с токенами (динамическое получение токенов, мультитокены, итд.)
* Определение всех VK's API методов.
* Обёртка над токенами и методами.


## Работа с токенами

Токены в VKWave представлены обычными Python классами с методом `get_token`. Он может бысть синхронным или асиннхронным

```python
from vkwave.api.token.token import UserSyncSingleToken, BotSyncSingleToken, Token

# Токен, который мы получаем от ВК 
bot_plain_token = Token("...")
user_plain_token = Token("...")

# Токен, который уже можно использовать
bot_token = BotSyncSingleToken(bot_plain_token)
user_token = UserSyncSingleToken(user_plain_token)

bot_token.get_token()
# ...

user_token.get_token()
# ...

```

Вы можете создать свой собственный класс токена с нужной логикой. Создадим синхронный токен для бота.

```python
import random

from typing import List
from vkwave.api.token.token import ABCBotSyncToken, Token

class BotSyncRandomToken(ABCBotSyncToken):
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def get_token(self, *args, **kwargs) -> Token:
        return random.choice(self.tokens)

```


### GetTokenStrategy

Реализуйте это, если вам нужен список `UserSyncSingleToken` и вам нужно доставать токен, чтобы сделать запрос в API. 

По умолчанию VKWave использует `RandomGetTokenStrategy`, она просто делает `random.choice(tokens)`. В примере ниже мы реализуем свою стратегию, чтобы показать, что токены можно получать и по сети.

```python
from vkwave.api.token.strategy import ABCGetTokenStrategy
from vkwave.api.token.token import Token, AnyABCToken, TokenType, GetTokenType

# AnyABCToken means really any token.

class ServerGetTokenStrategy(ABCGetTokenStrategy):
    token_type = (TokenType.BOT, TokenType.USER)
    get_token_type = (GetTokenType.SYNC, GetTokenType.ASYNC)

    # we will ignore tokens that VKWave gives us.
    async def get_token(self, _) -> Token:
        token = await self.some_fancy_api.get_random_token()
        return token
```

В этом примере не создаются токены, которые мы передаём в API обёртку. Он достаёт случайный и возвращает его.

## API

У нас есть 3 класса для работы с API: `API`, `APIOptions`, `APIOptionsRequestContext`.


API это ядро. Оно содержит все токены и клиенты.

```python
from vkwave.api import API
from vkwave.client import AIOHTTPClient

api = API(tokens=my_token, clients=AIOHTTPClient())
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

На каждый вызов API контекст получает токен, следуя стратегии. Это может быть проблемой с таким примером:
```python
friends = await api.friends.get()
result = await api.messages.send(...)
```

Потому что друзья получатся на один токен, а сообщения будут отправляться другим. Чтобы избежать этого нужно синхронизировать токены.

```python
async with api.sync_token() as sapi:
    friends = await sapi.friends.get()
    ...
```
Тут в пределах контекстного менеджера будет использоваться только один токен.

Написать `api_session.get_context()` не единственный способ получить контекст. Вы также можете использовать `api_session.with_token` или `api_session.with_options`

```python
api = api_session.with_token(SomeToken(...))
api = api_session.with_options(APIOptions(...))
```

