import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from ..dp.dp import Dispatcher


class BaseExtension(ABC):
    dp: "Dispatcher"

    @abstractmethod
    async def start(self):
        ...
