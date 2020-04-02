import json
from typing import Optional

from vkwave.api.methods import APIOptionsRequestContext
from vkwave.bots.storage.base import NO_KEY, AbstractStorage, NoKeyOrValue
from vkwave.bots.storage.types import Dumper, Key, Loader, Value


class VKStorage(AbstractStorage):
    def __init__(
        self,
        api_context: APIOptionsRequestContext,
        # dumps object to str
        dumper: Dumper = json.dumps,
        # loads object from str
        loader: Loader = json.loads,
        user_id: Optional[int] = None,
    ):
        self._client: APIOptionsRequestContext = api_context
        self._loader = loader
        self._dumper = dumper
        self._user_id = user_id

    async def put(self, key: Key, value: Value) -> None:
        await self._put(key, value)

    async def get(self, key: Key, default: NoKeyOrValue = NO_KEY) -> Value:
        v = await self._get(key)
        if v:
            return self._loader(v)
        if default is NO_KEY:
            raise KeyError("There is no such key")

        return default

    async def delete(self, key: Key) -> None:
        await self._put(key)

    async def contains(self, key: Key) -> bool:
        return bool(self._get(key))

    async def _get(self, key: Key) -> Value:
        r = await self._client.storage.get(key=key, user_id=self._user_id)
        return r["response"].get("value")

    async def _put(self, key: Key, value: Optional[Value] = None):
        await self._client.storage.set(key=key, value=self._dumper(value), user_id=self._user_id)
