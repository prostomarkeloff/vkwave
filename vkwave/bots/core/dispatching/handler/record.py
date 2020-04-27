from typing import Any, List, Optional, Type, Union, cast

from vkwave.bots.core.dispatching.filters import filter_caster
from vkwave.bots.core.dispatching.filters.base import BaseFilter
from vkwave.bots.core.dispatching.handler import BaseHandler, DefaultHandler
from vkwave.bots.core.dispatching.handler.callback import BaseCallback

from .cast import caster as callback_caster


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
        return self.handler_type(cast(BaseCallback, self.callback), filters=self.filters)
