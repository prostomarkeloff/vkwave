from inspect import isfunction, isawaitable
from asyncio import iscoroutinefunction
from typing import Any, Dict, Type, cast as cast_t
from .callback import SyncFuncCallback, AsyncFuncCallback
from .callback import BaseCallback

POSSIBLE_CASTS: Dict[str, Type[BaseCallback]] = {
    "awaitable": AsyncFuncCallback,
    "sync": SyncFuncCallback,
}


def cast(to_cast: Any) -> BaseCallback:
    cb: BaseCallback
    if iscoroutinefunction(to_cast) or isawaitable(to_cast):
        cb = cast_t(Type[AsyncFuncCallback], POSSIBLE_CASTS["awaitable"])(to_cast)
        return cb
    if isfunction(to_cast):
        cb = cast_t(Type[SyncFuncCallback], POSSIBLE_CASTS["sync"])(to_cast)
        return cb
    if isinstance(to_cast, str):
        return SyncFuncCallback(lambda event: to_cast)
    raise NotImplementedError
