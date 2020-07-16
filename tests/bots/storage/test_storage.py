import os
import time
from typing import Union

import pytest

from vkwave.api.methods import API
from vkwave.api.token.token import BotSyncSingleToken
from vkwave.bots.storage.base import AbstractExpiredStorage, AbstractStorage
from vkwave.bots.storage.storages import RedisStorage, Storage, TTLStorage, VKStorage
from vkwave.bots.storage.types import TTL, Key
from vkwave.client.default import AIOHTTPClient
from vkwave.http import AIOHTTPClient


async def storage_interact_test(
    storage: Union[AbstractStorage, AbstractExpiredStorage],
    test_key=Key("test_key"),
    test_value="test_value",
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


@pytest.mark.asyncio
async def test_vk_storage():
    token = os.environ.get("VK_BOT_TOKEN")
    if not token:
        pytest.skip("unsupported configuration")

    client = AIOHTTPClient()
    token = BotSyncSingleToken(token)
    api_session = API(token, client)
    api = api_session.get_context()

    storage = VKStorage(api)
    await storage_interact_test(storage)
    await client.close()


async def ttl_test(storage: AbstractExpiredStorage):
    await storage.put(Key("my_key"), "my_value", TTL(1))  # one second ttl
    time.sleep(2)  # sleep two second

    flag = False
    try:
        await storage.get(Key("my_key"))  # key must not exist
    except KeyError:
        flag = True

    assert flag


@pytest.mark.asyncio
async def test_redis_storage():
    pytest.skip("not ready")

    storage = RedisStorage()
    await storage_interact_test(storage)
    await ttl_test(storage)
    await storage.close()


@pytest.mark.asyncio
async def test_ttl_storage():
    storage = TTLStorage()
    await storage_interact_test(storage)
    await ttl_test(storage)
