import asyncio
import json
import ssl
import typing

try:
    import aioredis
except ImportError:
    aioredis = None

from vkwave.bots.storage.base import NO_KEY, AbstractExpiredStorage, NoKeyOrValue
from vkwave.bots.storage.types import TTL, Dumper, Key, Loader, Value


class RedisStorage(AbstractExpiredStorage):
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        ssl_context: typing.Optional[ssl.SSLContext] = None,
        pool_size: int = 10,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
        # dumps object to str
        dumper: Dumper = json.dumps,
        # loads object from str
        loader: Loader = json.loads,
        default_ttl: TTL = TTL(10),
        **kwargs,
    ):
        if aioredis is None:
            raise RuntimeError("You have to install aioredis - pip install aioredis")

        self._kwargs = kwargs

        self._host = host
        self._port = port
        self._db = db
        self._password = password
        self._ssl = ssl_context
        self._pool_size = pool_size
        self._loop = loop or asyncio.get_event_loop()

        self._dumper = dumper
        self._loader = loader
        self._default_ttl = default_ttl

        self._redis: typing.Optional["aioredis.Redis"] = None
        self._connection_lock = asyncio.Lock(loop=self._loop)

    async def get(
        self, key: Key, default: NoKeyOrValue = NO_KEY
    ) -> typing.Union[typing.NoReturn, Value]:
        redis = await self.redis()

        v = await redis.get(key)
        if v:
            return self._loader(v)
        if default is NO_KEY:
            raise KeyError("There is no such key")

        return default

    async def put(self, key: Key, value: Value, ttl: typing.Optional[TTL] = None) -> None:
        redis = await self.redis()

        if ttl is None:
            pexpire = int(self._default_ttl * 1000)
        elif ttl == -1:
            pexpire = None
        else:
            pexpire = int(ttl * 1000)

        await redis.set(key, self._dumper(value), pexpire=pexpire)
        return None

    async def delete(self, key: Key) -> typing.Optional[typing.NoReturn]:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key.")

        redis = await self.redis()

        await redis.delete(key)
        return None

    async def contains(self, key: Key) -> bool:
        redis = await self.redis()

        return await redis.exists(key)

    async def redis(self) -> "aioredis.Redis":
        async with self._connection_lock:
            if self._redis is None or self._redis.closed:
                self._redis = await aioredis.create_redis_pool(
                    (self._host, self._port),
                    db=self._db,
                    password=self._password,
                    ssl=self._ssl,
                    loop=self._loop,
                    maxsize=self._pool_size,
                    **self._kwargs,
                )

        return self._redis

    async def close(self):
        async with self._connection_lock:
            if self._redis and not self._redis.closed:
                self._redis.close()

    async def wait_closed(self) -> bool:
        async with self._connection_lock:
            if self._redis:
                return await self._redis.wait_closed()
            return True
