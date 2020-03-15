from vkwave_bots.dispatching.filters.base import BaseFilter
from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.dispatching.handler.record import HandlerRecord
from vkwave_bots.dispatching.handler.base import BaseHandler
from typing import List

class HandlerRegistrar:
    def __init__(self):
        self.handlers: List[BaseHandler] = []

    def new(self) -> HandlerRecord:
        return HandlerRecord()

    def register(self, handler: BaseHandler):
        self.handlers.append(handler)

