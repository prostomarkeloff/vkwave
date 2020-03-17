from abc import ABC, abstractmethod
import typing
from .types import Key, Value


class AbstractStorage(ABC):
    @abstractmethod
    async def post(self, key: Key, value: Value) -> None:
        ...

    @abstractmethod
    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
        ...

    @abstractmethod
    async def put(self, key: Key, value: Value) -> None:
        ...

    @abstractmethod
    async def delete(self, key: Key) -> None:
        ...

    @abstractmethod
    async def contains(self, key: Key) -> bool:
        ...
