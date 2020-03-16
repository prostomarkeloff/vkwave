from vkwave_bots.dispatching.filters.base import BaseFilter
from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.dispatching.handler.record import HandlerRecord
from vkwave_bots.dispatching.handler.base import BaseHandler
from typing import List, TypeVar, Callable, Any

F = TypeVar("F", bound=Callable[..., Any])


class HandlerRegistrar:
    def __init__(self):
        self.handlers: List[BaseHandler] = []

    def with_decorator(self, *filters: BaseFilter):
        def decorator(func: Callable[..., Any]):
            record = HandlerRecord()
            record.with_filters(*filters)
            record.handle(func)
            handler = record.ready()
            self.register(handler)
            return func

        return decorator

    def new(self) -> HandlerRecord:
        return HandlerRecord()

    def register(self, handler: BaseHandler):
        self.handlers.append(handler)
