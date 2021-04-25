# Storage

Этот модуль поможет вам хранить данные внутри бота.

У вас есть выбор из трёх стандартных хранилищ:
 - dict-like хранилище
 - ttl хранилище
 - redis хранилище
 

```python
import asyncio

from vkwave.bots.storage.storages import Storage
from vkwave.bots.storage.types import Key


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

Если вам нужны time-to-life ключи:

```python
from vkwave.bots.storage.storages import TTLStorage
from vkwave.bots.storage.types import Key

storage = TTLStorage(default_ttl=10)


async def main():
    my_key = Key("123")

    await storage.put(my_key, 456, ttl=2)

    print(await storage.contains(my_key))  # True
    await asyncio.sleep(2)
    print(await storage.contains(my_key))  # False
```

Если вы используете Redis:

```python
from vkwave.bots.storage.storages import RedisStorage

storage = RedisStorage(default_ttl=10)  # you can also specify the host, port, db and password


async def main():
    my_key = Key("123")

    await storage.put(my_key, 456, ttl=2)

    print(await storage.contains(my_key))  # True
    await asyncio.sleep(2)
    print(await storage.contains(my_key))  # False
    
    await storage.close()
    await storage.wait_closed()
```
