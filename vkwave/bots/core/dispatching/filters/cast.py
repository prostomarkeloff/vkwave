from asyncio import iscoroutinefunction
from inspect import isawaitable, isclass, isfunction
from typing import Any, Optional, cast

from vkwave.bots.core.dispatching.cast.default import DefaultCaster

from .base import AsyncFuncFilter, BaseFilter, SyncFuncFilter


class FilterCaster(DefaultCaster[BaseFilter]):
    def default(self, something: Any) -> Optional[BaseFilter]:
        filter: Optional[BaseFilter]

        if isclass(something):
            if issubclass(something.__class__, BaseFilter):
                return cast(BaseFilter, something)
        if iscoroutinefunction(something) or isawaitable(something):
            filter = AsyncFuncFilter(something)
        elif isfunction(something):
            filter = SyncFuncFilter(something)
        else:
            filter = None

        return filter


caster = FilterCaster()
