from .base import BaseFilter
from .base import AsyncFuncFilter, SyncFuncFilter
from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Dict, Any, Type, cast as cast_t

POSSIBLE_CASTS: Dict[str, Type[BaseFilter]] = {"awaitable": AsyncFuncFilter, "sync": SyncFuncFilter}

def cast(to_cast: Any) -> BaseFilter:
    filter: Type[BaseFilter]
    if iscoroutinefunction(to_cast) or isawaitable(to_cast):
        filter = cast_t(Type[AsyncFuncFilter], POSSIBLE_CASTS["awaitable"])
        return filter(to_cast)

    elif isfunction(to_cast):
        filter = cast_t(Type[SyncFuncFilter], POSSIBLE_CASTS["sync"])
        return filter(to_cast)

    raise NotImplementedError

