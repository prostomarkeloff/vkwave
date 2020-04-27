import asyncio
import typing

from .easy_userbot import SimpleLongPollUserBot
from .easy_bot import SimpleLongPollBot


class ClonesBot:
    """
    Create many bots with the same functionality
    """

    def __init__(
        self,
        base_bot: typing.Union[SimpleLongPollUserBot, SimpleLongPollBot],
        *clones: typing.Union[SimpleLongPollUserBot, SimpleLongPollBot],
    ):
        self.base_bot = base_bot
        self.router = self.base_bot.router
        self.clones: typing.Tuple[typing.Union[SimpleLongPollUserBot, SimpleLongPollBot]] = clones

    def run_all_bots(self, loop: typing.Optional[asyncio.AbstractEventLoop] = None):
        loop = loop or asyncio.get_event_loop()
        loop.create_task(self.base_bot.run())
        for clone in self.clones:
            clone.router.registrar.handlers.extend(self.router.registrar.handlers)
            clone.router.registrar.handlers = list(set(clone.router.registrar.handlers))
            loop.create_task(clone.run())
        loop.run_forever()
