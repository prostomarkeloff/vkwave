# Overview

VKWave API is very convinient part of the library.

It contains three parts:

* Working with tokens (Dynamic fetching tokens, multitokens.)
* Defining VK's API methods.
* Wrapper over methods and tokens.


## Working with tokens

Tokens in VKWave is regular Python classes with `get_token` method. It could be synchronous or asynchronous

```python
from vkwave.api.token.token import UserSyncSingleToken, BotSyncSingleToken, Token

# our tokens. we got them from VK
bot_plain_token = Token("...")
user_plain_token = Token("...")

# tokens that are ready for using.
bot_token = BotSyncSingleToken(bot_plain_token)
user_token = UserSyncSingleToken(user_plain_token)

bot_token.get_token()
# ...

user_token.get_token()
# ...

```

You can create your own class with your own logic. Let's create synchronous token.

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

Implement this, if you need a list of `UserSyncSingleToken` and you need make a request to API. 

By default VKWave uses `RandomGetTokenStrategy`, it's simply call `random.choice(tokens)`. In the example below we will implement our own strategy, to show that we can fetch tokens by network.

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

In this example we don't create new tokens, just fetching random and returns it.

## API


`API` is the core class. It contains all tokens and API's methods.

```python
from vkwave.api import API
from vkwave.client import AIOHTTPClient

api = API(tokens=my_token, clients=AIOHTTPClient())
```

In `APIOptions` we have `tokens`, `clients`, `strategy` and other stuff, you can get access to them `api.default_api_options`. I. e. you can add client, token or change strategy.

```python
api = API(...)

api.default_api_options.add_token(tokens=[...]) # or add only one token
```

But to make a request to API you must get a context.

```python
api_session = API(...)

api = api_session.get_context()
```


```python
result = await api.status.get()
print(result.response.text)
```

On each API's request context gets new token, according to strategy. It could be a problem in this case:

```python
friends = await api.friends.get()
result = await api.messages.send(...)
```

You fetching friend with one token, and sending messages with other. To avoid this you need to synchronize tokens.

```python
async with api.sync_token() as sapi:
    friends = await sapi.friends.get()
    ...
```
In the context manager will be used only one token.

To get context you can use `api_session.with_token` or `api_session.with_options`

```python
api = api_session.with_token(SomeToken(...))
api = api_session.with_options(APIOptions(...))
```
