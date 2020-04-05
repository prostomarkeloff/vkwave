import asyncio
import typing

from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.api.methods import API
from vkwave.client.default import AIOHTTPClient
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.bots.core.tokens.storage import TokenStorage
from vkwave.bots.core.dispatching.dp.dp import Dispatcher
from vkwave.bots.core.dispatching.extensions.longpoll_bot import BotLongpollExtension
from vkwave.bots.core.tokens.types import GroupId
from vkwave.bots.core.dispatching.router.router import DefaultRouter
from vkwave.longpoll.bot import BotLongpoll, BotLongpollData
from vkwave.bots.core.dispatching.filters.builtin import (
    EventTypeFilter,
    PayloadFilter,
    TextFilter,
    ChatActionFilter,
    CommandsFilter,
    RegexFilter,
)


class _APIContextManager:
    def __init__(self, tokens: typing.Union[str, typing.List[str]]):
        self.client = AIOHTTPClient()
        self.tokens = (
            BotSyncSingleToken(Token(tokens))
            if isinstance(tokens, str)
            else [BotSyncSingleToken(Token(token)) for token in tokens]
        )
        self.api = API(clients=self.client, tokens=self.tokens)

    async def __aenter__(self):
        return self.api.get_context()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.client.close()


def create_api_session_aiohttp(token: str) -> _APIContextManager:
    return _APIContextManager(token)


class SimpleLongPollBot:
    def __init__(self, tokens: typing.Union[str, typing.List[str]], group_id: int):
        self.BaseEvent = BaseEvent
        self.api_session = create_api_session_aiohttp(tokens)
        self.api_context = self.api_session.api.get_context()
        self._lp = BotLongpoll(self.api_context, BotLongpollData(group_id))
        self._token_storage = TokenStorage[GroupId]()
        self.dispatcher = Dispatcher(self.api_session.api, self._token_storage)
        self._lp = BotLongpollExtension(self.dispatcher, self._lp)
        self.router = DefaultRouter()
        self.message_handler = self.router.registrar.with_decorator
        self.dispatcher.add_router(self.router)

        self.text_filter = TextFilter
        self.event_type_filter = EventTypeFilter
        self.payload_filter = PayloadFilter
        self.chat_action_filter = ChatActionFilter
        self.command_filter = CommandsFilter
        self.regex_filter = RegexFilter

    async def _run(self):
        await self.dispatcher.cache_potential_tokens()
        await self._lp.start()

    def run(self, loop: asyncio.AbstractEventLoop = None):
        loop = loop or asyncio.get_event_loop()
        loop.create_task(self._run())
        loop.run_forever()
