"""
@bot.message_handler(bot.text_filter("привет"))
class HelloHandler(BaseHandler):
    async def handle(self, event: BotEvent) -> str:
        return "Привет"

"""
from abc import ABC, abstractmethod, ABCMeta
from typing import Any, Optional, Union
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.bots.core.dispatching.handler.cast import caster


class BaseHandler(ABC):
    @abstractmethod
    async def handle(self, event: BaseEvent) -> Any:
        ...


class ClassBasedHandlerCallback(BaseCallback):
    def __init__(self, handler: BaseHandler):
        self.handler = handler

    async def execute(self, event: BaseEvent) -> Any:
        return await self.handler.handle(event)


def class_based_handler_caster(x: Union[BaseHandler, Any]) -> Optional[BaseCallback]:
    if not type(x) is ABCMeta or not issubclass(x, BaseHandler):
        return None
    return ClassBasedHandlerCallback(x())


caster.add_caster(class_based_handler_caster)
