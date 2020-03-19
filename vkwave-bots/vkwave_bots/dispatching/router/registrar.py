from typing import Any, Callable, List, TypeVar

from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.dispatching.filters.base import BaseFilter
from vkwave_bots.dispatching.handler.base import BaseHandler
from vkwave_bots.dispatching.handler.record import HandlerRecord

F = TypeVar("F", bound=Callable[..., Any])


class HandlerRegistrar:
    def __init__(self):
        self.default_filters: List[BaseFilter] = []
        self.handlers: List[BaseHandler] = []

    def add_default_filter(self, filter: BaseFilter):
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
        record.with_filters(*self.default_filters)
        return record

    def register(self, handler: BaseHandler):
        self.handlers.append(handler)
