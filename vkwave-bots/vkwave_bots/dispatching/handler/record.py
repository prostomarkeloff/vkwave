from .cast import caster as callback_caster
from vkwave_bots.dispatching.handler.callback import BaseCallback
from typing import cast, Union, Type, List, Optional, Any
from vkwave_bots.dispatching.filters.base import BaseFilter
from vkwave_bots.dispatching.filters import EventTypeFilter, filter_caster
from vkwave_bots.dispatching.handler import DefaultHandler
from vkwave_bots.dispatching.handler import BaseHandler


class HandlerRecord:
    def __init__(self):
        self.filters: List[BaseFilter] = []
        self.callback: Optional[BaseCallback] = None
        self.handler_type: Type[BaseHandler] = DefaultHandler

    def with_handler_type(self, handler_type: Type[BaseHandler]) -> "HandlerRecord":
        self.handler_type = handler_type
        return self

    def with_filters(self, *filters: Union[BaseFilter, Any]) -> "HandlerRecord":
        for filter in filters:
            if isinstance(filter, BaseFilter):
                self.filters.append(filter)
            else:
                self.filters.append(filter_caster.cast(filter))
        return self

    def handle(self, callback: Union[BaseCallback, Any]) -> "HandlerRecord":
        if isinstance(callback, BaseCallback):
            self.callback = callback
        else:
            self.callback = callback_caster.cast(callback)
        return self

    def ready(self) -> BaseHandler:
        return self.handler_type(
            cast(BaseCallback, self.callback), filters=self.filters
        )
