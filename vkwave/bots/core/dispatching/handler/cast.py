from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any, Optional

from vkwave.bots.core.dispatching.cast.default import DefaultCaster

from .callback import AsyncFuncCallback, BaseCallback, SyncFuncCallback


class CallbackCaster(DefaultCaster[BaseCallback]):
    def default(self, something: Any) -> Optional[BaseCallback]:
        cb: Optional[BaseCallback]
        if iscoroutinefunction(something) or isawaitable(something):
            return AsyncFuncCallback(something)
        elif isfunction(something):
            return SyncFuncCallback(something)
        elif isinstance(something, str):
            return SyncFuncCallback(lambda event: something)
        else:
            return None



caster = CallbackCaster()
