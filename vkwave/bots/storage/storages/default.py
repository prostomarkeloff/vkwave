import typing

from vkwave.bots.storage.base import NO_KEY, AbstractStorage, NoKeyOrValue
from vkwave.bots.storage.types import Key, Value


class Storage(AbstractStorage):
    def __init__(self):
        self.data: typing.Dict[Key, Value] = {}

    async def get(
        self, key: Key, default: NoKeyOrValue = NO_KEY
    ) -> typing.Union[typing.NoReturn, Value]:
        if await self.contains(key):
            return self.data[key]
        if default is NO_KEY:
            raise KeyError("There is no such key")
        return default

    async def put(self, key: Key, value: Value) -> None:
        self.data[key] = value
        return None

    async def delete(self, key: Key) -> typing.Optional[typing.NoReturn]:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key.")
        del self.data[key]
        return None

    async def contains(self, key: Key) -> bool:
        return key in self.data
