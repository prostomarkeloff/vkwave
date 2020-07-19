import inspect
import typing

from vkwave.bots import BotType, BaseEvent, UserEvent, BotEvent, EventTypeFilter
from vkwave.bots.core import BaseFilter
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import BaseBoolInt
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
        keyboard: typing.Optional[str] = None,
        attachment: typing.Optional[typing.List[str]] = None,
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
        attachment: typing.Optional[typing.Union[typing.List[str], str]] = None,
        payload: typing.Optional[str] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        sticker_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
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
            template=template,
        )

    async def callback_answer(self, event_data: typing.Dict[str, str]):
        await self.api_ctx.messages.send_message_event_answer(
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
