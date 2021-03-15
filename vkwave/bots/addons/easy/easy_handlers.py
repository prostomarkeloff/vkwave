import inspect
import typing

from vkwave.bots import BotType, BaseEvent, UserEvent, BotEvent, EventTypeFilter
from vkwave.bots.core import BaseFilter
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.types.bot_events import BotEventType
from vkwave.types.responses import BaseOkResponse, MessagesSendResponse
from vkwave.types.user_events import EventId


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
        domain: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        reply_to: typing.Optional[int] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        forward: typing.Optional[str] = None,
        sticker_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        keyboard: typing.Optional[str] = None,
        template: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        content_source: typing.Optional[str] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        intent: typing.Optional[str] = None,
        subscribe_id: typing.Optional[int] = None,
    ) -> MessagesSendResponse:
        return await self.api_ctx.messages.send(
            message=message,
            forward=forward,
            template=template,
            content_source=content_source,
            intent=intent,
            subscribe_id=subscribe_id,
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
            random_id=0,
        )

    async def set_activity(
        self,
        type: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> MessagesSendResponse:
        """
        type:
            typing — пользователь начал набирать текст,
            audiomessage — пользователь записывает голосовое сообщение
        """
        return await self.api_ctx.messages.set_activity(
            user_id=user_id, type=type, peer_id=self.object.object.peer_id, group_id=group_id,
        )


def _check_event_type(event_type: str):
    if event_type not in (
        BotEventType.MESSAGE_NEW,
        BotEventType.MESSAGE_EDIT,
        BotEventType.MESSAGE_REPLY,
        BotEventType.MESSAGE_TYPING_STATE,
        BotEventType.MESSAGE_ALLOW,
    ):
        raise RuntimeError("You cant use event.answer() with this event")


class SimpleBotEvent(BotEvent):
    def __init__(self, event: BotEvent):
        super().__init__(event.object, event.api_ctx)
        self.user_data = event.user_data

    def __setitem__(self, key: typing.Any, item: typing.Any) -> None:
        self.user_data[key] = item

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self.user_data[key]

    @property
    def text(self) -> str:
        return self.object.object.text

    @property
    def peer_id(self) -> int:
        return self.object.object.peer_id

    @property
    def from_id(self) -> int:
        return self.object.object.from_id

    async def answer(
        self,
        message: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        reply_to: typing.Optional[int] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        forward: typing.Optional[str] = None,
        sticker_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        keyboard: typing.Optional[str] = None,
        template: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        content_source: typing.Optional[str] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        intent: typing.Optional[str] = None,
        subscribe_id: typing.Optional[int] = None,
    ) -> MessagesSendResponse:
        _check_event_type(self.object.type)
        return await self.api_ctx.messages.send(
            forward=forward,
            intent=intent,
            subscribe_id=subscribe_id,
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
            template=template,
            content_source=content_source,
        )

    async def set_activity(
        self,
        type: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> MessagesSendResponse:
        """
        type:
            typing — пользователь начал набирать текст,
            audiomessage — пользователь записывает голосовое сообщение
        """
        _check_event_type(self.object.type)
        return await self.api_ctx.messages.set_activity(
            user_id=user_id,
            type=type,
            peer_id=self.object.object.message.peer_id,
            group_id=group_id,
        )

    async def callback_answer(self, event_data: typing.Dict[str, str]) -> BaseOkResponse:
        if self.object.type != BotEventType.MESSAGE_EVENT:
            raise RuntimeError("You cant use event.callback_answer() with this event")
        return await self.api_ctx.messages.send_message_event_answer(
            user_id=self.object.object.user_id,
            peer_id=self.object.object.peer_id,
            event_id=self.object.object.event_id,
            event_data=event_data,
        )


class SimpleBotCallback(BaseCallback):
    def __init__(
        self, func: typing.Callable[[BaseEvent], typing.Awaitable[typing.Any]], bot_type: BotType,
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

    def __repr__(self):
        return f"<SimpleBotCallback {self.func.__name__} bot_type={self.bot_type}>"


def simple_bot_handler(router, *filters: BaseFilter):
    """
    Handler for all bot events
    """

    def decorator(func: typing.Callable[..., typing.Any]):
        record = router.registrar.new()
        record.with_filters(*filters)
        record.handle(SimpleBotCallback(func, BotType.BOT))
        router.registrar.register(record.ready())
        return func

    return decorator


def simple_user_handler(router, *filters: BaseFilter):
    """
    Handler for all user events
    """

    def decorator(func: typing.Callable[..., typing.Any]):
        record = router.registrar.new()
        record.with_filters(*filters)
        record.handle(SimpleBotCallback(func, BotType.USER))
        router.registrar.register(record.ready())
        return func

    return decorator


def simple_bot_message_handler(router, *filters: BaseFilter):
    """
    Handler only for message events
    """

    def decorator(func: typing.Callable[..., typing.Any]):
        record = router.registrar.new()
        record.with_filters(*filters)
        record.filters.append(EventTypeFilter(BotEventType.MESSAGE_NEW))
        record.handle(SimpleBotCallback(func, BotType.BOT))
        router.registrar.register(record.ready())
        return func

    return decorator


def simple_user_message_handler(router, *filters: BaseFilter):
    """
    Handler only for message events
    """

    def decorator(func: typing.Callable[..., typing.Any]):
        record = router.registrar.new()
        record.with_filters(*filters)
        record.filters.append(EventTypeFilter(EventId.MESSAGE_EVENT.value))
        record.handle(SimpleBotCallback(func, BotType.USER))
        router.registrar.register(record.ready())
        return func

    return decorator
