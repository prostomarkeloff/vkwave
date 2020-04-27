import time
import typing

from vkwave.bots.storage.base import NO_KEY, AbstractExpiredStorage, NoKeyOrValue
from vkwave.bots.storage.types import TTL, Key, Value

INF = float("inf")


class TTLStorage(AbstractExpiredStorage):
    def __init__(self, default_ttl: TTL = TTL(10)):
        self.data: typing.Dict[Key, typing.Tuple[Value, TTL]] = {}
        self.default_ttl = default_ttl

    async def put(self, key: Key, value: Value, ttl: typing.Optional[TTL] = None) -> None:
        if ttl is None:
            expire = TTL(time.time() + self.default_ttl)
        elif ttl == -1:
            expire = TTL(INF)
        else:
            expire = TTL(time.time() + ttl)
        self.data[key] = (value, expire)

    async def get(self, key: Key, default: NoKeyOrValue = NO_KEY) -> Value:
        if await self.contains(key):
            return self.data[key][0]
        if default is NO_KEY:
            raise KeyError("There is no such key")
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
