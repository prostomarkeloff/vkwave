import asyncio
import typing

from .easy_userbot import SimpleLongPollUserBot
from .easy_bot import SimpleLongPollBot
from ...core.dispatching.handler import DefaultHandler


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
        self.clones: typing.List[typing.Union[SimpleLongPollUserBot, SimpleLongPollBot]] = list(clones)

    def add_clone(self, clone: typing.Union[SimpleLongPollUserBot, SimpleLongPollBot]) -> None:
        self.clones.append(clone)

    def register_clones(self, last_handler: typing.Optional[typing.Callable]):
        if last_handler is None:
            for clone in self.clones:
                clone.router.registrar.handlers = self.router.registrar.handlers
            return

        for clone in self.clones:
            _last_handler = None
            for handler in self.router.registrar.handlers:
                if handler.callback.func.__name__ == last_handler.__name__:
                    _last_handler = handler
                    continue
                clone.router.registrar.handlers.append(handler)
            clone.router.registrar.handlers.append(_last_handler)

    def run_all_bots(
        self,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
        last_handler: typing.Optional[DefaultHandler] = None,
    ):
        self.register_clones(last_handler=last_handler)
        loop = loop or asyncio.get_event_loop()
        loop.create_task(self.base_bot.run())
        for clone in self.clones:
            loop.create_task(clone.run())
        loop.run_forever()
