from typing import Optional, Dict, Generic, TypeVar
from .types import GroupId, UserId
from .types import UST, UAT, BST, BAT
from .strategy import ABCGetTokenStrategy, NotImplementedGetTokenStrategy

from vkwave_api.token.token import AnyABCToken

T = TypeVar("T", GroupId, UserId)


class TokenStorage(Generic[T]):
    def __init__(
        self,
        available: Optional[Dict[T, AnyABCToken]] = None,
        get_token_strategy: Optional[ABCGetTokenStrategy] = None,
    ):
        self.tokens: Dict[T, AnyABCToken] = available or Dict[T, AnyABCToken]()
        self.get_token_strategy: ABCGetTokenStrategy[
            T
        ] = get_token_strategy or NotImplementedGetTokenStrategy[T]()

    def _get_cached(self, id_to_check: T) -> Optional[AnyABCToken]:
        return self.tokens.get(id_to_check)

    async def get_token(self, id_to_check: T) -> AnyABCToken:
        return self._get_cached(id_to_check) or (
            await self.get_token_strategy.get_token(id_to_check)
        )
