from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any

from vkwave_bots.dispatching.cast.default import DefaultCaster

from .base import AsyncFuncFilter, BaseFilter, SyncFuncFilter


class FilterCaster(DefaultCaster[BaseFilter]):
    def cast(self, something: Any):
        filter: BaseFilter
        if iscoroutinefunction(something) or isawaitable(something):
            filter = AsyncFuncFilter(something)
            return filter

        elif isfunction(something):
            filter = SyncFuncFilter(something)
            return filter

        raise NotImplementedError("There is not caster for this type")


caster = FilterCaster()
