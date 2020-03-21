from typing import Tuple, Union

from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots.types.bot_type import BotType

from .base import BaseFilter, FilterResult


class EventTypeFilter(BaseFilter):
    """
    Event type filter. It supports both user and bot events.
    
    >>> mn = EventTypeFilter("message_new") # bots' message_new event
    >>> @router.registrar.with_decorator(mn)

    >>> mn = EventTypeFilter(4) # users' message_new event (but we are a bit unsure about that)
    >>> @router.registrar.with_decorator(mn)
    """

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
        raise NotImplementedError("There is no implementation for this type of bot")

class TextFilter(BaseFilter):
    """Message text filter."""

    def __init__(self, text: str, ignore_case: bool = True):
        self.text = text
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        if not event.bot_type is BotType.BOT:
            raise NotImplementedError("It's not implemented for users' bots yet")

        text = event.object.object.message.text
        if self.ic:
            return FilterResult(text == self.text.lower())
        else:
            return FilterResult(text.lower() == self.text.lower())
