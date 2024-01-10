import logging
import traceback
from asyncio import get_running_loop
from typing import TYPE_CHECKING

from vkwave.bots.core.dispatching.dp.processing_options import ProcessEventOptions
from vkwave.bots.core.dispatching.events.raw import ExtensionEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.longpoll.user import UserLongpoll

from .base import BaseExtension

if TYPE_CHECKING:
    from ..dp.dp import Dispatcher


logger = logging.getLogger(__name__)


class UserLongpollExtension(BaseExtension):
    def __init__(self, dp: "Dispatcher", lp: UserLongpoll):
        self.dp = dp
        self.lp = lp

    async def _start(self, ignore_errors: bool = True):
        options = ProcessEventOptions(do_not_handle=False)
        while True:
            if not ignore_errors:
                events = await self.lp.get_updates()
                for event in events:
                    get_running_loop().create_task(
                        self.dp.process_event(ExtensionEvent(BotType.USER, event), options)
                    )
            else:
                try:
                    events = await self.lp.get_updates()
                    for event in events:
                        get_running_loop().create_task(
                            self.dp.process_event(ExtensionEvent(BotType.USER, event), options)
                        )
                except Exception as e:
                    logger.error(f"Error in Longpoll ({e}): {traceback.format_exc()}")

    async def start(self, ignore_errors: bool = True):
        get_running_loop().create_task(self._start(ignore_errors))
