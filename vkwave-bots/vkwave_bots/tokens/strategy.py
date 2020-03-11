"""How to get token strategy."""

from abc import ABC, abstractmethod
from .types import GroupId
from vkwave_api.tokens.tokens import AnyABCToken


class ABCGetTokenStrategy(ABC):
    @abstractmethod
    async def get_token(self, group_id: GroupId) -> AnyABCToken:
        ...


class NotImplementedGetTokenStrategy(ABCGetTokenStrategy):
    async def get_token(self, group_id: GroupId) -> AnyABCToken:
        raise NotImplementedError(
            "By default, events with unknown group_id are ignored"
        )
