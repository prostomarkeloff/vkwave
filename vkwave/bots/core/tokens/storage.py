from typing import Dict, Generic, Optional, TypeVar

from vkwave.api.token.token import AnyABCToken
from .strategy import ABCGetTokenStrategy, NotImplementedGetTokenStrategy
from .types import GroupId, UserId

T = TypeVar("T", GroupId, UserId)


class TokenStorage(Generic[T]):
    def __init__(
        self,
        available: Optional[Dict[T, AnyABCToken]] = None,
        get_token_strategy: Optional[ABCGetTokenStrategy] = None,
    ):
        self.tokens: Dict[T, AnyABCToken] = available or dict()
        self.get_token_strategy: ABCGetTokenStrategy[
            T
        ] = get_token_strategy or NotImplementedGetTokenStrategy[T]()

    def append(self, id_to_add: T, token: AnyABCToken):
        self.tokens[id_to_add] = token

    def _get_cached(self, id_to_check: T) -> Optional[AnyABCToken]:
        return self.tokens.get(id_to_check)

    async def get_token(self, id_to_check: T) -> AnyABCToken:
        return self._get_cached(id_to_check) or (
            await self.get_token_strategy.get_token(id_to_check)
        )
