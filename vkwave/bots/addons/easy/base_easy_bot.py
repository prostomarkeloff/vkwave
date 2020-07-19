import asyncio
import typing

from vkwave.api import API, APIOptionsRequestContext
from vkwave.api.token.token import (
    BotSyncPoolTokens,
    UserSyncSingleToken,
    Token,
    BotSyncSingleToken,
)
from vkwave.bots.addons.easy.easy_handlers import SimpleUserEvent, SimpleBotEvent, SimpleBotCallback
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
    FwdMessagesFilter,
    MessageArgsFilter,
    MessageFromConversationTypeFilter,
    TextContainsFilter,
    ReplyMessageFilter
)
from vkwave.bots.core.dispatching.dp.middleware.middleware import BaseMiddleware, MiddlewareResult
from vkwave.bots.core.dispatching.filters.extension_filters import VBMLFilter
from vkwave.bots.fsm.filters import StateFilter
from vkwave.bots.core.dispatching.router.router import BaseRouter
from vkwave.client import AIOHTTPClient
from vkwave.longpoll import BotLongpoll, BotLongpollData, UserLongpoll, UserLongpollData
from vkwave.types.bot_events import BotEventType
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


class BaseSimpleLongPollBot:
    def __init__(
        self,
        tokens: typing.Union[str, typing.List[str]],
        bot_type: BotType,
        router: typing.Optional[BaseRouter] = None,
        group_id: typing.Optional[int] = None,
        uvloop: bool = False,
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

        self.middleware_manager = self.dispatcher.middleware_manager  # auf

        self.router = router or DefaultRouter()
        self.dispatcher.add_router(self.router)

        self.text_filter = TextFilter
        self.event_type_filter = EventTypeFilter
        self.payload_filter = PayloadFilter
        self.chat_action_filter = ChatActionFilter
        self.command_filter = CommandsFilter
        self.regex_filter = RegexFilter
        self.state_filter = StateFilter
        self.vbml_filter = VBMLFilter
        self.reply_filter = ReplyMessageFilter
        self.args_filter = MessageArgsFilter
        self.fwd_filter = FwdMessagesFilter
        self.conversation_type_filter = MessageFromConversationTypeFilter
        self.text_contains_filter = TextContainsFilter
        if self.bot_type is BotType.USER:
            self.from_me_filter = FromMeFilter

    class SimpleBotMiddleware(BaseMiddleware):
        async def pre_process_event(self, event: BaseEvent) -> MiddlewareResult:
            pass

    def handler(self, *filters: BaseFilter):
        """
        Handler for all events
        """

        def decorator(func: typing.Callable[..., typing.Any]):
            record = self.router.registrar.new()
            record.with_filters(*filters)
            record.handle(SimpleBotCallback(func, self.bot_type))
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
            record.handle(SimpleBotCallback(func, self.bot_type))
            self.router.registrar.register(record.ready())
            return func

        return decorator

    def middleware(self):
        def decorator(
            func: typing.Callable[[typing.Union[UserEvent, BotEvent]], MiddlewareResult]
        ):
            middleware = self.SimpleBotMiddleware()
            middleware.pre_process_event = func
            self.middleware_manager.add_middleware(middleware)

            return func

        return decorator

    async def run(self, ignore_errors: bool = True):
        if self.bot_type is BotType.BOT:
            await self.dispatcher.cache_potential_tokens()
        await self._lp.start(ignore_errors)

    def run_forever(
        self, ignore_errors: bool = True, loop: typing.Optional[asyncio.AbstractEventLoop] = None
    ):
        loop = loop or asyncio.get_event_loop()
        loop.create_task(self.run(ignore_errors))
        loop.run_forever()
