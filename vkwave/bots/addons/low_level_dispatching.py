import asyncio
import typing
import logging

from vkwave.bots.addons.easy import create_api_session_aiohttp
from vkwave.longpoll import BotLongpoll, BotLongpollData, UserLongpollData, UserLongpoll
from vkwave.longpoll.bot import Update
from vkwave.types.user_events import get_event_object as user_get_event_object, BaseUserEvent
from vkwave.types.bot_events import get_event_object as bot_get_event_object, BaseBotEvent


logger = logging.getLogger(__name__)


class LowLevelBot:
    """
    Bot with raw longpoll for more performance
    """

    def __init__(
        self,
        token: str,
        group_id: typing.Optional[int] = None,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
        uvloop: bool = False
    ):
        """
        exist group_id - bot_type == BOT
        group_id is none - bot_type == USER
        """
        if uvloop:
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.token = token
        self.group_id = group_id
        self._api_session = create_api_session_aiohttp(token)
        self.api = self._api_session.api
        self.api_context = self.api.get_context()
        self.loop = loop or asyncio.get_event_loop()

        if self.group_id is not None:
            self.longpoll = BotLongpoll(self.api_context, BotLongpollData(self.group_id))
            self.get_event_object = bot_get_event_object
        else:
            self.longpoll = UserLongpoll(self.api_context, UserLongpollData())
            self.get_event_object = user_get_event_object

    async def _listen(self, ignore_errors: bool):
        if ignore_errors:
            while True:
                try:
                    async for event in self.longpoll.event_by_event():
                        yield event
                except Exception as e:
                    logger.error(e)
                    await asyncio.sleep(0.1)
                    continue
        else:
            async for event in self.longpoll.event_by_event():
                yield event

    async def listen(
        self, fast_mode: bool = False, ignore_errors: bool = False
    ) -> typing.AsyncGenerator[typing.Union[BaseBotEvent, BaseUserEvent, Update], None]:
        """
        Listening for events

        :param fast_mode: - return raw events
        :param ignore_errors: - ignore all lp errors, (internet connection or vk internal server errors)
        """
        if fast_mode:
            return_event = lambda _event: _event
        else:
            return_event = lambda _event: self.get_event_object(_event)

        async for event in self._listen(ignore_errors=ignore_errors):
            yield return_event(event)

    def react(self, reaction: typing.Union[typing.Awaitable]):
        self.loop.create_task(reaction)

    def run(self, main_loop: typing.Awaitable):
        self.loop.create_task(main_loop)
        self.loop.run_forever()
