"""
Working with API tokens.
"""
from enum import Enum, auto
from typing import NewType, Union, ClassVar
from typing_extensions import Protocol

Token = NewType("Token", str)


class TokenType(Enum):
    USER = auto()
    BOT = auto()


class GetTokenType(Enum):
    SYNC = auto()
    ASYNC = auto()


AnyABCToken = Union["ABCSyncToken", "ABCAsyncToken"]


class ABCSyncToken(Protocol):
    get_token_type: ClassVar[GetTokenType] = GetTokenType.SYNC
    typeof: ClassVar[TokenType]

    def get_token(self, *args, **kwargs) -> Token:
        ...


class ABCAsyncToken(Protocol):
    get_token_type: ClassVar[GetTokenType] = GetTokenType.ASYNC
    token_type: ClassVar[TokenType]

    async def get_token(self, *args, **kwargs) -> Token:
        ...


class ABCUserSyncToken(ABCSyncToken):
    typeof: ClassVar[TokenType] = TokenType.USER


class ABCUserAsyncToken(ABCAsyncToken):
    typeof: ClassVar[TokenType] = TokenType.USER


class ABCBotSyncToken(ABCSyncToken):
    typeof: ClassVar[TokenType] = TokenType.BOT


class ABCBotAsyncToken(ABCAsyncToken):
    typeof: ClassVar[TokenType] = TokenType.BOT


class UserSyncSingleToken(ABCUserSyncToken):
    def __init__(self, token: Token):
        self._token: Token = token

    def get_token(self, *args, **kwargs) -> Token:
        return self._token


class BotSyncSingleToken(ABCBotSyncToken):
    def __init__(self, token: Token):
        self._token: Token = token

    def get_token(self, *args, **kwargs) -> Token:
        return self._token
