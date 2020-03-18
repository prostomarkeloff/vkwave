import time
import typing

from vkwave_bots_storage._types import TTL, Key, Value
from vkwave_bots_storage.base import AbstractExpiredStorage


class TTLStorage(AbstractExpiredStorage):
    def __init__(self, default_ttl: TTL = 10):
        self.data: typing.Dict[Key, typing.Tuple[Value, TTL]] = {}
        self.default_ttl = default_ttl

    async def put(self, key: Key, value: Value, ttl: typing.Optional[TTL] = None) -> None:
        if ttl is None:
            expire = TTL(time.time() + self.default_ttl)
        elif ttl == -1:
            expire = TTL(time.time() ** 2)
        else:
            expire = TTL(time.time() + ttl)
        self.data[key] = (value, expire)

    async def get(self, key: Key, default: typing.Optional[Value] = None) -> typing.Optional[Value]:
        if await self.contains(key):
            return self.data[key][0]
        return default

    async def delete(self, key: Key) -> None:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key.")
        del self.data[key]

    async def contains(self, key: Key) -> bool:
        if key not in self.data:
            return False
        _, expire = self.data[key]

        if expire < time.time():
            del self.data[key]
        return key in self.data
