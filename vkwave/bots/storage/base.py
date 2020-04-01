import typing
from abc import ABC, abstractmethod

from vkwave.bots.storage.types import TTL, Key, Value


class NOKEY:
    pass


NO_KEY = NOKEY()

NoKeyOrValue = typing.Union[NOKEY, Value]


class AbstractBaseStorage(ABC):
    @abstractmethod
    async def get(self, key: Key, default: NoKeyOrValue = NO_KEY) -> Value:
        ...

    @abstractmethod
    async def delete(self, key: Key) -> None:
        ...

    @abstractmethod
    async def contains(self, key: Key) -> bool:
        ...


class AbstractStorage(AbstractBaseStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value) -> None:
        ...


class AbstractExpiredStorage(AbstractBaseStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value, ttl: TTL) -> None:
        ...
