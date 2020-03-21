VKWave API is pretty easy to use library. You perhaps will use it always when touching vkwave.

It contains from 3 parts:

* Working with tokens (dynamically tokens getting, multitoken, etc.)
* Definitons of all VK's API methods.
* Wrapper around tokens and methods.

Will start from tokens.

## Working with tokens

Tokens are represented in VKWave as regular Python classes that just have method `get_token`. It can be synchronous and asynchronous. 

```python
from vkwave_api.token.token import UserSyncSingleToken, BotSyncSingleToken, Token

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

Also you can create own tokens with needed logic. We will create bot's synchronous token.

```python
import random

from typing import List
from vkwave_api.token.token import ABCBotSyncToken, Token

class BotSyncRandomToken(ABCBotSyncToken):
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def get_token(self, *args, **kwargs) -> Token:
        return random.choice(self.tokens)

```
It's very easy to understand and very clear.


### GetTokenStrategy

It's very interesting issue! Realize that you have a list of `UserSyncSingleToken` and you need to pick up something to make API request. Choose some of them it's pretty hard task.

By default VKWave uses `RandomGetTokenStrategy`, it just does `random.choice(tokens)`. We will implement own for showing that you even can get tokens from the net!

```python
from vkwave_api.token.strategy import ABCGetTokenStrategy
from vkwave_api.token.token import Token, AnyABCToken, TokenType, GetTokenType

# AnyABCToken means really any token.

class ServerGetTokenStrategy(ABCGetTokenStrategy):
    token_type = (TokenType.BOT, TokenType.USER)
    get_token_type = (GetTokenType.SYNC, GetTokenType.ASYNC)

    # we will ignore tokens that vkwave gives us.
    async def get_token(self, _) -> Token:
        token = await self.some_fancy_api.get_random_token()
        return token
```

This example doesn't use tokens that we will pass to API wrapper. It gets random and returns it.

## API

We have 3 classes for working with API: `API`, `APIOptions`, `APIOptionsRequestContext`.

I'll describe to you each of them.

API is core. It contains all tokens and clients. 

```python
from vkwave_api.methods import API

api = API(tokens=my_token, cliens=AIOHTTPClient())
```
Also I want to tell you that `tokens`, `clients`, `strategy` and other things are stored at `APIOptions` class. You can access them via `api.default_api_options`. For example you can add token or client, or update strategy, etc..

```python
api = API(...)

api.default_api_options.add_token(tokens=[...]) # or you can pass one token
```

But only with it you can't do API requests.

You should get context!

```python
api_session = API(...)

api = api_session.get_context()
```

When you write it you will get `APIOptionsRequestContext`. It contains all methods and own `APIOptions`.

```python
result = await api.status.get()
print(result.response.text)
```

On every API call context will pick token for it, via strategy. It can be problem if you write code such as:
```python
friends = await api.friends.get()
result = await api.messages.send(...)
```

Because you get friends of the one token, but send messages to these friends with the another token. We should sync token to avoid that.

```python
async with api.sync_token() as sapi:
    friends = await api.friends.get()
    ...
```
Here token is synced and used always.

Writing `api_session.get_context()` is not the one way to get context. You also can use either `api_session.with_token` or `api_session.with_options`

```python
api = api_session.with_token(SomeToken(...))
api = api_session.with_options(APIOptions(...))
```
