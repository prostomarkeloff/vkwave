from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any, Optional

from vkwave.bots.core.dispatching.cast.default import DefaultCaster

from .callback import AsyncFuncCallback, BaseCallback, SyncFuncCallback


class CallbackCaster(DefaultCaster[BaseCallback]):
    def default(self, something: Any) -> Optional[BaseCallback]:
        cb: Optional[BaseCallback]
        if iscoroutinefunction(something) or isawaitable(something):
            cb = AsyncFuncCallback(something)
        elif isfunction(something):
            cb = SyncFuncCallback(something)
        elif isinstance(something, str):
            cb = SyncFuncCallback(lambda event: something)
        else:
            cb = None

        return cb


caster = CallbackCaster()
