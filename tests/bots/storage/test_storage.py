import pytest

from vkwave.bots.storage.base import AbstractStorage, AbstractExpiredStorage
from vkwave.bots.storage.storages.redis import RedisStorage
from vkwave.bots.storage.storages import TTLStorage, Storage

import time


async def storage_interact_test(
    storage: AbstractStorage, test_key="test_key", test_value="test_value"
):
    await storage.put(test_key, test_value)  # add key
    r = await storage.get(test_key)
    assert r == test_value

    await storage.delete(test_key)
    assert not await storage.contains(test_key)
    flag = False
    try:
        await storage.get(test_key)  # key must not exist
    except KeyError:
        flag = True

    assert flag


@pytest.mark.asyncio
async def test_storage():
    storage = Storage()
    await storage_interact_test(storage)


async def ttl_test(storage: AbstractExpiredStorage):
    await storage.put("my_key", "my_value", 1)  # one second ttl
    time.sleep(2)  # sleep two second

    flag = False
    try:
        await storage.get("my_key")  # key must not exist
    except KeyError:
        flag = True

    assert flag


@pytest.mark.asyncio
async def test_redis_storage():
    storage = RedisStorage()
    await storage_interact_test(storage)
    await ttl_test(storage)
    await storage.close()


@pytest.mark.asyncio
async def test_ttl_storage():
    storage = TTLStorage()
    await storage_interact_test(storage)
    await ttl_test(storage)
