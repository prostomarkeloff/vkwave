"""How to get token strategy."""

from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from vkwave_api.token.token import AnyABCToken

T = TypeVar("T")


class ABCGetTokenStrategy(ABC, Generic[T]):
    @abstractmethod
    async def get_token(self, id_to_check: T) -> AnyABCToken:
        ...


class NotImplementedGetTokenStrategy(ABCGetTokenStrategy[T]):
    async def get_token(self, id_to_check: T) -> AnyABCToken:
        raise NotImplementedError(
            "By default, events with unknown group (user) ID are ignored"
        )
