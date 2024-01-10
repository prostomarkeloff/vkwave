from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any, Optional, cast
from inspect import isclass

from vkwave.bots.core.dispatching.cast.default import DefaultCaster

from .base import AsyncFuncFilter, BaseFilter, SyncFuncFilter


class FilterCaster(DefaultCaster[BaseFilter]):
    def default(self, something: Any) -> Optional[BaseFilter]:
        filter: Optional[BaseFilter]

        if isclass(something) and issubclass(something.__class__, BaseFilter):
            return cast(BaseFilter, something)
        if iscoroutinefunction(something) or isawaitable(something):
            return AsyncFuncFilter(something)
        elif isfunction(something):
            return SyncFuncFilter(something)
        else:
            return None


caster = FilterCaster()
