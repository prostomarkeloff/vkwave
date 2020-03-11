from typing import Optional, Dict
from .types import GroupId
from .strategy import ABCGetTokenStrategy, NotImplementedGetTokenStrategy
from vkwave_api.tokens.tokens import AnyABCToken


class TokenStorage:
    def __init__(
        self,
        available: Optional[Dict[GroupId, AnyABCToken]] = None,
        get_token_strategy: Optional[ABCGetTokenStrategy] = None,
    ):
        self.tokens: Dict[GroupId, AnyABCToken] = available or {}
        self.get_token_strategy: ABCGetTokenStrategy = get_token_strategy or NotImplementedGetTokenStrategy()

    def _get_cached(self, group_id: GroupId) -> Optional[AnyABCToken]:
        return self.tokens.get(group_id)

    async def get_token(self, group_id: GroupId) -> AnyABCToken:
        return self._get_cached(group_id) or (await self.get_token_strategy.get_token(group_id))
