from vkwave.bots.storage.storages.ttl import AbstractExpiredStorage, Key
from vkwave.bots.core.dispatching.filters.base import BaseFilter
from vkwave.bots.core.dispatching.filters.cast import caster
from vkwave.bots.core.dispatching.events.base import BaseEvent
import random
from typing import Any


def cached_filter(f: Any, st: AbstractExpiredStorage, ttl: int) -> BaseFilter:
    name = f"__filter{f.__class__.__name__}{random.randint(54, 100002210)}__"
    f = caster.cast(f)

    async def new_f(ev: BaseEvent):
        if await st.contains(Key(name)):
            r = await st.get(Key(name))
            return r
        else:
            r = await f.check(ev)
            await st.put(Key(name), r, ttl)
            return r

    return caster.cast(new_f)
