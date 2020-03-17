from abc import ABC, abstractmethod
import typing
from vkwave_bots_storage._types import Key, Value, TTL


class AbstractBaseStorage(ABC):
    @abstractmethod
    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
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

    @abstractmethod
    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
        ...

    @abstractmethod
    async def delete(self, key: Key) -> None:
        ...

    @abstractmethod
    async def contains(self, key: Key) -> bool:
        ...


class AbstractExpiredStorage(AbstractBaseStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value, ttl: TTL) -> None:
        ...

    @abstractmethod
    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
        ...

    @abstractmethod
    async def delete(self, key: Key) -> None:
        ...

    @abstractmethod
    async def contains(self, key: Key) -> bool:
        ...
