from vkwave_bots_storage.base import AbstractExpiredStorage
from vkwave_bots_storage._types import Key, Value, TTL
import typing
import time


class TTLStorage(AbstractExpiredStorage):
    def __init__(self, default_ttl: TTL = 10):
        self.data: typing.Dict[Key, typing.Tuple[Value, TTL]] = {}
        self.default_ttl = default_ttl

    async def put(self, key: Key, value: Value, ttl: TTL = None) -> None:
        if ttl is None:
            expire = TTL(time.time() + self.default_ttl)
        else:
            expire = TTL(time.time() + ttl)
        self.data[key] = (value, expire)

    async def get(self, key: Key, default: Value = None) -> typing.Optional[Value]:
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
        value, expire = self.data[key]

        if expire < time.time():
            del self.data[key]
        return key in self.data

