from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any, Optional

from vkwave.bots.core.dispatching.cast.default import DefaultCaster

from .base import AsyncFuncFilter, BaseFilter, SyncFuncFilter


class FilterCaster(DefaultCaster[BaseFilter]):
    def default(self, something: Any) -> Optional[BaseFilter]:
        filter: Optional[BaseFilter]
        if iscoroutinefunction(something) or isawaitable(something):
            filter = AsyncFuncFilter(something)
        elif isfunction(something):
            filter = SyncFuncFilter(something)
        else:
            filter = None

        return filter


caster = FilterCaster()
