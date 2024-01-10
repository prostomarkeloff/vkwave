from asyncio import get_running_loop, sleep
from typing import TYPE_CHECKING
import warnings
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

    async def _start(self, ignore_errors: bool = True):
        options = ProcessEventOptions(do_not_handle=False)
        api_version = (
            await self.dp.api.get_context().groups.get_long_poll_settings(self.lp.data.group_id)
        ).response.api_version

        api_version_for_check = int(api_version.split(".")[-1])
        if api_version_for_check < 103:
            warnings.warn(
                f"LongPoll API versions less than 5.103 shall not work. \nYou are using {api_version}"
            )
        while True:
            if not ignore_errors:
                events = await self.lp.get_updates()
                for event in events:
                    get_running_loop().create_task(
                        self.dp.process_event(ExtensionEvent(BotType.BOT, event), options)
                    )
            else:
                try:
                    events = await self.lp.get_updates()
                    for event in events:
                        get_running_loop().create_task(
                            self.dp.process_event(ExtensionEvent(BotType.BOT, event), options)
                        )
                except Exception as e:
                    logger.error(f"Error in Longpoll ({e}): {traceback.format_exc()}")
                    await sleep(0.33)

    async def start(self, ignore_errors: bool = True):
        logger.info("Starting bot...")
        get_running_loop().create_task(self._start(ignore_errors))
