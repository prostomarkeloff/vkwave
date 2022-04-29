# Работа с токенами

Токены в VKWave представлены обычными Python классами с методом `get_token`. Он может быть синхронным или асинхронным

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
from vkwave.api.token.token import Token, TokenType, GetTokenType

# AnyABCToken means really any token.

class ServerGetTokenStrategy(ABCGetTokenStrategy):
    token_type = (TokenType.BOT, TokenType.USER)
    get_token_type = (GetTokenType.SYNC, GetTokenType.ASYNC)
    
    # we will ignore tokens that VKWave gives us.
    async def get_token(self, _) -> Token:
        token = await self.some_fancy_api.get_random_token()
        return token
```

В этом примере не создаются токены, которые мы передаём в API обёртку. Он получает случайный токен из стороннего API и возвращает его.

