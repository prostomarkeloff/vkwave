from typing import Any, Awaitable, Callable, Dict, Optional, Type

from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.bots.core.types.bot_type import BotType


class ResultCaster:
    def __init__(self):
        self.available: Dict[Type[Any], Callable[[Any, BaseEvent], Awaitable[None]]] = {}

        self.add_caster(str, _default_str_handler)
        self.add_caster(type(None), _default_none_handler)

    def add_caster(self, typeof: Type[Any], handler: Callable[[Any, BaseEvent], Awaitable[None]]):
        self.available[typeof] = handler

    async def cast(self, result: Any, event: BaseEvent):
        typeof = type(result)
        handler: Optional[Callable[[Any, BaseEvent], Awaitable[None]]] = self.available.get(typeof)
        if not handler:
            raise NotImplementedError("implementation for this type doesn't exist")
        await handler(result, event)


async def _default_none_handler(some, event: BaseEvent):
    pass


async def _default_str_handler(some: str, event: BaseEvent):
    if event.bot_type is BotType.USER:
        raise NotImplementedError("Default 'str' handler is not implemented yet")

    await event.api_ctx.messages.send(
        random_id=0, peer_id=event.object.object.message.peer_id, message=some
    )
