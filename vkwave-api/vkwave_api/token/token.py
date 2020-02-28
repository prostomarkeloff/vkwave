"""
Working with API tokens.
"""
from enum import Enum, auto
from typing import NewType, Callable, Awaitable, Union, ClassVar

Token = NewType("Token", str)
GetTokenSync = Callable[..., Token]
GetTokenAsync = Callable[..., Awaitable[Token]]

class TokenType(Enum):
    USER = auto()
    BOT = auto()

class GetTokenType(Enum):
    SYNC = auto()
    ASYNC = auto()


class ABCToken:
    """
    This class represents abstract token subject.
    You should inherit from it if you want to create own abstraction over token.
    """

    typeof: ClassVar[TokenType]
    get_token_type: ClassVar[GetTokenType]
    get_token: Union[GetTokenSync, GetTokenAsync]

class ABCSyncToken(ABCToken):
    get_token_type = GetTokenType.SYNC

class ABCAsyncToken(ABCToken):
    get_token_type = GetTokenType.ASYNC

class ABCUserToken(ABCToken):
    typeof = TokenType.USER
    
class ABCUserSyncToken(ABCUserToken, ABCSyncToken):
    pass

class ABCUserAsyncToken(ABCUserToken, ABCAsyncToken):
    pass

class ABCBotToken(ABCToken):
    typeof = TokenType.BOT

class ABCBotSyncToken(ABCBotToken, ABCSyncToken):
    pass

class ABCBotAsyncToken(ABCBotToken, ABCAsyncToken):
    pass

class UserSyncSingleToken(ABCUserSyncToken):
    def __init__(self, token: Token):
        self._token: Token = token
        self.get_token = self._get_token

    def _get_token(self, *args, **kwargs) -> Token:
        return self._token

class BotSyncSingleToken(ABCBotSyncToken):
    def __init__(self, token: Token):
        self._token: Token = token
        self.get_token = self._get_token

    def _get_token(self, *args, **kwargs) -> Token:
        return self._token
