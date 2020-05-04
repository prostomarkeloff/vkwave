import asyncio
import inspect
import typing

from vkwave.api import API, APIOptionsRequestContext
from vkwave.api.token.token import (
    BotSyncPoolTokens,
    UserSyncSingleToken,
    Token,
    BotSyncSingleToken,
)
from vkwave.bots.core import BaseFilter
from vkwave.bots import (
    Dispatcher,
    BaseEvent,
    UserEvent,
    BotEvent,
    BotLongpollExtension,
    UserLongpollExtension,
    ChatActionFilter,
    CommandsFilter,
    EventTypeFilter,
    PayloadFilter,
    RegexFilter,
    TextFilter,
    FromMeFilter,
    DefaultRouter,
    TokenStorage,
    UserTokenStorage,
    UserId,
    GroupId,
    BotType,
)
from vkwave.bots.core.dispatching.filters.extension_filters import VBMLFilter
from vkwave.bots.fsm.filters import StateFilter
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.bots.core.dispatching.router.router import BaseRouter
from vkwave.client import AIOHTTPClient
from vkwave.longpoll import BotLongpoll, BotLongpollData, UserLongpoll, UserLongpollData
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import BaseBoolInt
from vkwave.types.user_events import EventId


class _APIContextManager:
    def __init__(self, tokens: typing.Union[str, typing.List[str]], bot_type: BotType):
        self.client = AIOHTTPClient()
        if bot_type.USER:
            self.tokens = (
                UserSyncSingleToken(Token(tokens))
                if isinstance(tokens, str)
                else BotSyncPoolTokens([Token(token) for token in tokens])
            )
        else:
            self.tokens = (
                BotSyncSingleToken(Token(tokens))
                if isinstance(tokens, str)
                else BotSyncPoolTokens([Token(token) for token in tokens])
            )
        self.api = API(clients=self.client, tokens=self.tokens)

    async def __aenter__(self):
        return self.api.get_context()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.client.close()


def create_api_session_aiohttp(token: str, bot_type: BotType = BotType.BOT) -> _APIContextManager:
    return _APIContextManager(token, bot_type)


class SimpleUserEvent(UserEvent):
    def __init__(self, event: UserEvent):
        super().__init__(event.object, event.api_ctx)
        self.user_data = event.user_data

    def __setitem__(self, key: typing.Any, item: typing.Any) -> None:
        self.user_data[key] = item

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self.user_data[key]

    async def answer(
        self,
        message: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
        attachment: typing.Optional[BaseBoolInt] = None,
        payload: typing.Optional[str] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        sticker_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        reply_to: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ):
        await self.api_ctx.messages.send(
            domain=domain,
            lat=lat,
            long=long,
            attachment=attachment,
            reply_to=reply_to,
            forward_messages=forward_messages,
            sticker_id=sticker_id,
            group_id=group_id,
            keyboard=keyboard,
            payload=payload,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            peer_id=self.object.object.peer_id,
            message=message,
            random_id=0,
        )


class SimpleBotEvent(BotEvent):
    def __init__(self, event: BotEvent):
        super().__init__(event.object, event.api_ctx)
        self.user_data = event.user_data

    def __setitem__(self, key: typing.Any, item: typing.Any) -> None:
        self.user_data[key] = item

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self.user_data[key]

    async def answer(
        self,
        message: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
        attachment: typing.Optional[BaseBoolInt] = None,
        payload: typing.Optional[str] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        sticker_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        reply_to: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ):
        await self.api_ctx.messages.send(
            domain=domain,
            lat=lat,
            long=long,
            attachment=attachment,
            reply_to=reply_to,
            forward_messages=forward_messages,
            sticker_id=sticker_id,
            group_id=group_id,
            keyboard=keyboard,
            payload=payload,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            peer_id=self.object.object.message.peer_id,
            message=message,
            random_id=0,
        )


class BaseSimpleLongPollBot:
    def __init__(
        self,
        tokens: typing.Union[str, typing.List[str]],
        bot_type: BotType,
        router: typing.Optional[BaseRouter] = None,
        group_id: typing.Optional[int] = None,
        uvloop: bool = False
    ):
        if uvloop:
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.bot_type = bot_type
        self.api_session = create_api_session_aiohttp(tokens, bot_type)
        self.api_context: APIOptionsRequestContext = self.api_session.api.get_context()
        if self.bot_type is BotType.USER:
            if not isinstance(tokens, str):
                raise RuntimeError("Only one str token")

            self.SimpleBotEvent = SimpleUserEvent
            self._lp = UserLongpoll(self.api_context, UserLongpollData())
            self._token_storage = UserTokenStorage[UserId](tokens)
            self.dispatcher = Dispatcher(self.api_session.api, self._token_storage)
            self._lp = UserLongpollExtension(self.dispatcher, self._lp)
        else:
            self.SimpleBotEvent = SimpleBotEvent
            self._lp = BotLongpoll(self.api_context, BotLongpollData(group_id))
            self._token_storage = TokenStorage[GroupId]()
            self.dispatcher = Dispatcher(self.api_session.api, self._token_storage)
            self._lp = BotLongpollExtension(self.dispatcher, self._lp)
        self.router = router or DefaultRouter()
        self.handler = self.router.registrar.with_decorator
        self.dispatcher.add_router(self.router)

        self.text_filter = TextFilter
        self.event_type_filter = EventTypeFilter
        self.payload_filter = PayloadFilter
        self.chat_action_filter = ChatActionFilter
        self.command_filter = CommandsFilter
        self.regex_filter = RegexFilter
        self.state_filter = StateFilter
        self.vbml_filter = VBMLFilter
        if self.bot_type is BotType.USER:
            self.from_me_filter = FromMeFilter

    class SimpleBotCallback(BaseCallback):
        def __init__(
            self,
            func: typing.Callable[[BaseEvent], typing.Awaitable[typing.Any]],
            bot_type: BotType,
        ):
            self.bot_type = bot_type
            self.func = func

        async def execute(self, event: typing.Union[UserEvent, BotEvent]) -> typing.Any:
            if self.bot_type is BotType.BOT:
                new_event = SimpleBotEvent(event)
            else:
                new_event = SimpleUserEvent(event)
            if inspect.iscoroutinefunction(self.func):
                return await self.func(new_event)
            return self.func(new_event)

    def handler(self, *filters: BaseFilter):
        """
        Handler for all events
        """

        def decorator(func: typing.Callable[..., typing.Any]):
            record = self.router.registrar.new()
            record.with_filters(*filters)
            record.handle(self.SimpleBotCallback(func, self.bot_type))
            self.router.registrar.register(record.ready())
            return func

        return decorator

    def message_handler(self, *filters: BaseFilter):
        """
        Handler only for message events
        """

        def decorator(func: typing.Callable[..., typing.Any]):
            record = self.router.registrar.new()
            record.with_filters(*filters)
            if self.bot_type is BotType.BOT:
                record.filters.append(EventTypeFilter(BotEventType.MESSAGE_NEW))
            else:
                record.filters.append(EventTypeFilter(EventId.MESSAGE_EVENT.value))
            record.handle(self.SimpleBotCallback(func, self.bot_type))
            self.router.registrar.register(record.ready())
            return func

        return decorator

    async def run(self):
        if self.bot_type is BotType.BOT:
            await self.dispatcher.cache_potential_tokens()
        await self._lp.start()

    def run_forever(self, loop: typing.Optional[asyncio.AbstractEventLoop] = None):
        loop = loop or asyncio.get_event_loop()
        loop.create_task(self.run())
        loop.run_forever()
