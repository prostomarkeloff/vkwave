from .base import BaseFilter
from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.types.bot_type import BotType
from .base import FilterResult

class EventTypeFilter(BaseFilter):
    def __init__(self, event_type: str):
        self.event_type = event_type

    async def check(self, event: BaseEvent) -> FilterResult:
        if event.bot_type is BotType.BOT:
            return FilterResult(event.object.type == self.event_type)
        else:
            raise NotImplementedError("Now it's not implemented")
