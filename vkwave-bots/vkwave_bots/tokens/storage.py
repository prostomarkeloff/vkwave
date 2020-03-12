from typing import Optional, Dict, Generic, TypeVar
from .types import GroupId, UserId
from .types import UST, UAT, BST, BAT
from .strategy import ABCGetTokenStrategy, NotImplementedGetTokenStrategy

T = TypeVar("T", GroupId, UserId)
V = TypeVar("V", UST, UAT, BST, BAT)

class TokenStorage(Generic[T, V]):
    def __init__(self, available: Optional[Dict[T, V]] = None, get_token_strategy: Optional[ABCGetTokenStrategy] = None):
        self.tokens: Dict[T, V] = available or Dict[T, V]()
        self.get_token_strategy: ABCGetTokenStrategy[T, V] = get_token_strategy or NotImplementedGetTokenStrategy[T, V]()

    def _get_cached(self, id_to_check: T) -> Optional[V]:
        return self.tokens.get(id_to_check)

    async def get_token(self, id_to_check: T) -> V:
        return self._get_cached(id_to_check) or (
            await self.get_token_strategy.get_token(id_to_check)
        )

