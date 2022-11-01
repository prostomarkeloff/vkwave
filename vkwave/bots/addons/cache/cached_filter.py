import random
from typing import Any

from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.bots.core.dispatching.filters.base import BaseFilter
from vkwave.bots.core.dispatching.filters.cast import caster
from vkwave.bots.storage.storages.ttl import AbstractExpiredStorage, Key


def cached_filter(filter_: Any, storage: AbstractExpiredStorage, ttl: int) -> BaseFilter:
    name = f"__filter{filter_.__class__.__name__}{random.randint(54, 100002210)}__"
    filter_ = caster.cast(filter_)

    async def new_filter(event: BaseEvent):
        if await storage.contains(Key(name)):
            return await storage.get(Key(name))
        else:
            result = await filter_.check(event)
            await storage.put(Key(name), result, ttl)
            return result

    return caster.cast(new_filter)
