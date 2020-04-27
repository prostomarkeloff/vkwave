from typing import Any, Callable, List, TypeVar

from vkwave.bots.core.dispatching.filters.base import AsyncFuncFilter, BaseFilter, SyncFuncFilter
from vkwave.bots.core.dispatching.filters.builtin import EventTypeFilter
from vkwave.bots.core.dispatching.handler.base import BaseHandler
from vkwave.bots.core.dispatching.handler.record import HandlerRecord

F = TypeVar("F", bound=Callable[..., Any])


class HandlerRegistrar:
    def __init__(self):
        self.default_filters: List[BaseFilter] = []
        self.handlers: List[BaseHandler] = []

    def add_default_filter(self, filter: BaseFilter):
        if isinstance(filter, (AsyncFuncFilter, SyncFuncFilter)):
            raise ValueError(
                "You should add custom filters derived from `BaseFilter` for using default as filter"
            )

        self.default_filters.append(filter)

    def with_decorator(self, *filters: BaseFilter):
        def decorator(func: Callable[..., Any]):
            record = self.new()
            record.with_filters(*filters)
            record.handle(func)
            handler = record.ready()
            self.register(handler)
            return func

        return decorator

    def new(self) -> HandlerRecord:
        record = HandlerRecord()
        return record

    def register(self, handler: BaseHandler):
        for filter in handler.filter_manager.filters.copy():
            if isinstance(filter, EventTypeFilter):
                handler.filter_manager.filters.insert(0, filter)
        for dfilter in self.default_filters:
            to_include: bool = True
            for afilter in handler.filter_manager.filters:
                if type(dfilter) is type(afilter):
                    to_include = False
                    break
            if to_include:
                handler.filter_manager.add_filter(dfilter)

        self.handlers.append(handler)
