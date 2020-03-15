from abc import ABC, abstractmethod
from vkwave_bots.types.bot_type import BotType
import typing

if typing.TYPE_CHECKING:
    from ..dp.dp import Dispatcher

class BaseExtension(ABC):
    dp: "Dispatcher"
    @abstractmethod
    async def start(self):
        ...

class ExtensionEvent:
    def __init__(self, bot_type: BotType, raw_event: dict):
        self.bot_type = bot_type
        self.raw_event = raw_event