from asyncio import get_running_loop
from typing import TYPE_CHECKING

from vkwave.bots.core.dispatching.dp.processing_options import ProcessEventOptions
from vkwave.bots.core.dispatching.events.raw import ExtensionEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.longpoll.user import UserLongpoll

from .base import BaseExtension

if TYPE_CHECKING:
    from ..dp.dp import Dispatcher


class UserLongpollExtension(BaseExtension):
    def __init__(self, dp: "Dispatcher", lp: UserLongpoll):
        self.dp = dp
        self.lp = lp

    async def _start(self):
        options = ProcessEventOptions(do_not_handle=False)
        while True:
            events = await self.lp.get_updates()
            for event in events:
                get_running_loop().create_task(
                    self.dp.process_event(ExtensionEvent(BotType.USER, event), options)
                )

    async def start(self):
        get_running_loop().create_task(self._start())
