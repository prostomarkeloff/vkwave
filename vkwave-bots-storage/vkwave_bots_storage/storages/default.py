from vkwave_bots_storage.base import AbstractStorage
from vkwave_bots_storage._types import Key, Value
import typing


class Storage(AbstractStorage):
    def __init__(self):
        self.data: typing.Dict[Key, Value] = {}

    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
        if await self.contains(key):
            return self.data[key]
        return default

    async def put(self, key: Key, value: Value) -> typing.Optional[typing.NoReturn]:
        self.data[key] = value

    async def delete(self, key: Key) -> typing.Optional[typing.NoReturn]:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key.")
        del self.data[key]

    async def contains(self, key: Key) -> bool:
        return key in self.data
