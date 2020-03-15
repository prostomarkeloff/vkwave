from .base import BaseFilter
from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.types.bot_type import BotType
from .base import FilterResult
from typing import Union, Tuple

class EventTypeFilter(BaseFilter):
    def __init__(self, event_type: Union[str, Tuple[str, ...], Tuple[int, ...], int]):
        self.event_type = event_type

    async def check(self, event: BaseEvent) -> FilterResult:
        if event.bot_type is BotType.BOT:
            if isinstance(self.event_type, tuple):
                return FilterResult(event.object.type in self.event_type) 
            if isinstance(self.event_type, str):
                return FilterResult(event.object.type == self.event_type)
        else:
            if isinstance(self.event_type, tuple):
                return FilterResult(event.object.event_id in self.event_type) 
            if isinstance(self.event_type, int):
                return FilterResult(event.object.event_id == self.event_type)
        raise NotImplementedError
