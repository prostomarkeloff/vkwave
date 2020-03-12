"""How to get token strategy."""

from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from .types import GroupId, UserId
from .types import UST, BST

T = TypeVar("T")
V = TypeVar("V")


class ABCGetTokenStrategy(ABC, Generic[T, V]):
    @abstractmethod
    async def get_token(self, id_to_check: T) -> V:
        ...


class NotImplementedGetTokenStrategy(ABCGetTokenStrategy[T, V]):
    async def get_token(self, group_id: T) -> V:
        raise NotImplementedError(
            "By default, events with unknown group (user) ID are ignored"
        )


NotImplementedGetTokenStrategyUserIdSync = NotImplementedGetTokenStrategy[UST, UserId]
NotImplementedGetTokenStrategyGroupIdSync = NotImplementedGetTokenStrategy[BST, GroupId]
