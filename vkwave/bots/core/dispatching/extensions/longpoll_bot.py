from asyncio import get_running_loop
from typing import TYPE_CHECKING
import logging
import traceback

from vkwave.bots.core.dispatching.dp.processing_options import ProcessEventOptions
from vkwave.bots.core.dispatching.events.raw import ExtensionEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.longpoll.bot import BotLongpoll

from .base import BaseExtension

if TYPE_CHECKING:
    from ..dp.dp import Dispatcher

logger = logging.getLogger(__name__)


class BotLongpollExtension(BaseExtension):
    def __init__(self, dp: "Dispatcher", lp: BotLongpoll):
        self.dp = dp
        self.lp = lp

    async def _start(self, ignore_errors: bool):
        options = ProcessEventOptions(do_not_handle=False)
        if not ignore_errors:
            while True:
                events = await self.lp.get_updates()
                for event in events:
                    get_running_loop().create_task(
                        self.dp.process_event(ExtensionEvent(BotType.BOT, event), options)
                    )
        else:
            while True:
                try:
                    events = await self.lp.get_updates()
                    for event in events:
                        get_running_loop().create_task(
                            self.dp.process_event(ExtensionEvent(BotType.BOT, event), options)
                        )
                except Exception as e:
                    logger.error(f"Error in Longpoll ({e}): {traceback.format_exc()}")
                    continue

    async def start(self, ignore_errors: bool = False):
        logger.info("Starting bot...")
        get_running_loop().create_task(self._start(ignore_errors))
