"""
@bot.message_handler(bot.text_filter("привет"))
class HelloHandler(BaseHandler):
    async def handle(self, event: BotEvent) -> str:
        return "Привет"

"""
from abc import ABC, abstractmethod, ABCMeta
from typing import Any, Optional
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.bots.core.dispatching.events.base import BaseEvent

class BaseHandler(ABC):
    @abstractmethod
    async def handle(self, event: BaseEvent) -> Any:
        ...

class ClassBasedHandlerCallback(BaseCallback):
    def __init__(self, handler: BaseHandler):
        self.handler = handler

    async def execute(self, event: BaseEvent) -> Any:
        return await self.handler.handle(event)


def class_based_handler_caster(x: BaseHandler) -> Optional[BaseCallback]:
    if not type(x) is ABCMeta:
        return False
    if issubclass(x, BaseHandler):
        return ClassBasedHandlerCallback(x())
    else:
        return None

def inject_to_caster():
    from vkwave.bots.core.dispatching.handler.cast import caster

    caster.add_caster(class_based_handler_caster)
