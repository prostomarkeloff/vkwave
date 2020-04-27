from abc import ABC, abstractmethod
from random import choice
from typing import List, Tuple, Union, cast

from vkwave.api.token.token import (
    ABCAsyncToken,
    ABCSyncToken,
    AnyABCToken,
    GetTokenType,
    Token,
    TokenType,
    BotSyncSingleToken)


class ABCGetTokenStrategy(ABC):
    token_type: Union[TokenType, Tuple[TokenType, ...]]
    get_token_type: Union[GetTokenType, Tuple[GetTokenType, ...]]

    @abstractmethod
    async def get_token(self, tokens: List[AnyABCToken]) -> Token:
        ...


class RandomGetTokenStrategy(ABCGetTokenStrategy):
    token_type = (TokenType.BOT, TokenType.USER)
    get_token_type = (GetTokenType.SYNC, GetTokenType.ASYNC)

    async def get_token(self, tokens: List[AnyABCToken]) -> Token:
        token = choice(tokens)
        if isinstance(token, str):
            return cast(Token, token)

        if token.get_token_type is GetTokenType.ASYNC:
            token = cast(ABCAsyncToken, token)
            return await token.get_token()
        token = cast(ABCSyncToken, token)
        return token.get_token()
