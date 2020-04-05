import typing
from abc import ABC, abstractmethod
from typing import Awaitable, Callable, NewType

from vkwave.bots.core.dispatching.events.base import BaseEvent

FilterResult = NewType("FilterResult", bool)


class BaseFilter(ABC):
    @abstractmethod
    async def check(self, event: BaseEvent) -> FilterResult:
        ...

    def __and__(self, other: "BaseFilter") -> "AndFilter":
        return AndFilter(self, other)

    def __not__(self) -> "NotFilter":
        return NotFilter(self)

    def __or__(self, other: "BaseFilter") -> "OrFilter":
        return OrFilter(self, other)


# sfilter: some filter


class NotFilter(BaseFilter):
    def __init__(self, sfilter: BaseFilter):
        self.func = sfilter

    async def check(self, event: BaseEvent) -> FilterResult:
        res = await self.func.check(event)
        return FilterResult(not res)


class AndFilter(BaseFilter):
    def __init__(self, *sfilters: BaseFilter):
        self.funcs = sfilters

    async def check(self, event: BaseEvent) -> FilterResult:
        for func in self.funcs:
            res = await func.check(event)
            if not res:
                return FilterResult(False)
        return FilterResult(True)


class OrFilter(BaseFilter):
    def __init__(self, *sfilters: BaseFilter):
        self.funcs = sfilters

    async def check(self, event: BaseEvent) -> FilterResult:
        res: typing.List[bool] = []
        for func in self.funcs:
            if await func.check(event):
                res.append(True)
                continue
            res.append(False)

        return FilterResult(any(res))


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
