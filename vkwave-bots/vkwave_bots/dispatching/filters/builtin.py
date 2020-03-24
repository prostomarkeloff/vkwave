from typing import Tuple, Union, Dict
import json

from vkwave_bots.dispatching.events.base import BaseEvent, UserEvent
from vkwave_bots.types.bot_type import BotType
from vkwave_bots.types.json_types import JSONDecoder
from vkwave_types.objects import MessagesMessageActionStatus

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
        if event.bot_type is BotType.USER:
            text = event.object.object.text
        else:
            text = event.object.object.message.text
        if self.ic:
            return FilterResult(text == self.text.lower())
        return FilterResult(text.lower() == self.text.lower())


class PayloadFilter(BaseFilter):
    """Filter for message payload"""

    def __init__(self, payload: Dict[str, str], json_loader: JSONDecoder = json.loads):
        self.json_loader = json_loader
        self.payload = payload

    async def check(self, event: BaseEvent) -> FilterResult:
        if event.bot_type is BotType.USER:
            current_payload = event.object.object.message_data.payload
        else:
            current_payload = event.object.object.message.payload
        if current_payload is None:
            return FilterResult(False)
        return FilterResult(self.json_loader(current_payload) == self.payload)


class ChatActionFilter(BaseFilter):
    """Filter for actions in chat"""

    def __init__(self, action: MessagesMessageActionStatus):
        self.action = action

    async def check(self, event: BaseEvent) -> FilterResult:
        if event.bot_type is BotType.USER:
            current_action = event.object.object.message_data.source_act
        else:
            current_action = event.object.object.message.action.type
        return FilterResult(current_action == self.action)
