import typing

from vkwave_bots_storage._types import Key, Value
from vkwave_bots_storage.base import AbstractStorage


class Storage(AbstractStorage):
    def __init__(self):
        self.data: typing.Dict[Key, Value] = {}

    async def get(self, key: Key, default: typing.Optional[Value] = None) -> typing.Optional[Value]:
        if await self.contains(key):
            return self.data[key]
        return default

    async def put(self, key: Key, value: Value) -> None:
        self.data[key] = value

    async def delete(self, key: Key) -> typing.Optional[typing.NoReturn]:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key.")
        del self.data[key]

    async def contains(self, key: Key) -> bool:
        return key in self.data
