# vkwave-bots-storage

This module will help you with storing your bot data.
You have choice of two default storage:
 - simple dict-like storage
 - ttl storage
 

```python3
from vkwave_bots_storage.storages import Storage
from vkwave_bots_storage.types import Key
import asyncio


storage = Storage()


async def main():
    my_key = Key("123")

    await storage.put(my_key, 456)

    print(await storage.contains(my_key))  # True
    await storage.delete(my_key)
    print(await storage.contains(my_key))  # False
    print(await storage.get(my_key, default=789))  # 789


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

```

If you require in time-to-life keys:

```python3
storage = TTLStorage(default_ttl=10)


async def main():
    my_key = Key("123")

    await storage.put(my_key, 456, ttl=2)

    print(await storage.contains(my_key))  # True
    await asyncio.sleep(2)
    print(await storage.contains(my_key))  # False
```