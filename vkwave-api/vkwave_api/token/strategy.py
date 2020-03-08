from typing import List, Union, Tuple, cast
from random import choice
from vkwave_api.token.token import (
    AnyABCToken,
    TokenType,
    GetTokenType,
    Token,
    ABCAsyncToken,
    ABCSyncToken,
)
from abc import ABC, abstractmethod


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
        if token.get_token_type is GetTokenType.ASYNC:
            token = cast(ABCAsyncToken, token)
            return await token.get_token()
        else:
            token = cast(ABCSyncToken, token)
            return token.get_token()
