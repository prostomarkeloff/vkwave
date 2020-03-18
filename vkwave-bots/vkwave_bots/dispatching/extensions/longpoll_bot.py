from asyncio import get_running_loop
from typing import TYPE_CHECKING

from vkwave_bots.types.bot_type import BotType
from vkwave_longpoll.bot import BotLongpoll

from .base import BaseExtension, ExtensionEvent

if TYPE_CHECKING:
    from ..dp.dp import Dispatcher


class BotLongpollExtension(BaseExtension):
    def __init__(self, dp: "Dispatcher", lp: BotLongpoll):
        self.dp = dp
        self.lp = lp

    async def _start(self):
        while True:
            events = await self.lp.get_updates()
            for event in events:
                get_running_loop().create_task(
                    self.dp.process_event(ExtensionEvent(BotType.BOT, event))
                )

    async def start(self):
        get_running_loop().create_task(self._start())
