import typing
from abc import ABC, abstractmethod

from vkwave.bots.types.bot_type import BotType

if typing.TYPE_CHECKING:
    from ..dp.dp import Dispatcher


class BaseExtension(ABC):
    dp: "Dispatcher"

    @abstractmethod
    async def start(self):
        ...
