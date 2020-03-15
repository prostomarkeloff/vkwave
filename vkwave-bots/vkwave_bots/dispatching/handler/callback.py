from abc import ABC, abstractmethod
from vkwave_bots.dispatching.events.base import BaseEvent
from typing import Any, Callable, Awaitable


class BaseCallback(ABC):
    @abstractmethod
    async def execute(self, event: BaseEvent) -> Any:
        ...


class AsyncFuncCallback(BaseCallback):
    def __init__(self, func: Callable[[BaseEvent], Awaitable[Any]]):
        self.func = func

    async def execute(self, event: BaseEvent) -> Any:
        return await self.func(event)


class SyncFuncCallback(BaseCallback):
    def __init__(self, func: Callable[[BaseEvent], Any]):
        self.func = func

    async def execute(self, event: BaseEvent) -> Any:
        return self.func(event)
