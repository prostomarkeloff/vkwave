from abc import ABC, abstractmethod
from typing import Awaitable, Callable, NewType

from vkwave_bots.dispatching.events.base import BaseEvent

FilterResult = NewType("FilterResult", bool)


class BaseFilter(ABC):
    @abstractmethod
    async def check(self, event: BaseEvent) -> FilterResult:
        ...


class SyncFuncFilter(BaseFilter):
    """It accepts lambda and sync functions."""

    def __init__(self, func: Callable[[BaseEvent], bool]):
        self.func = func

    async def check(self, event: BaseEvent) -> FilterResult:
        return FilterResult(self.func(event))


class AsyncFuncFilter(BaseFilter):
    """It accepts any callables that return awaitables."""

    def __init__(self, func: Callable[[BaseEvent], Awaitable[bool]]):
        self.func = func

    async def check(self, event: BaseEvent) -> FilterResult:
        return FilterResult(await self.func(event))
