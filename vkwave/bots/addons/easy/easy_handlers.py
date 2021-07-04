import json
import warnings
import typing
from typing import Dict, List, Callable, Any, Union

from pydantic import PrivateAttr

from vkwave.bots import BotType, UserEvent, BotEvent, EventTypeFilter
from vkwave.bots.core import BaseFilter
from vkwave.bots.core.dispatching.filters.builtin import get_payload, get_text
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import (
    MessagesMessageAttachment,
    MessagesMessageAttachmentType,
    UsersUser,
)
from vkwave.types.responses import BaseOkResponse, MessagesSendResponse
from vkwave.types.user_events import EventId
from vkwave.bots.core.dispatching.handler.cast import caster as callback_caster

try:
    import aiofile
except ImportError:
    aiofile = None


class SimpleUserEvent(UserEvent):
    def __init__(self, event: UserEvent):
        super().__init__(event.object, event.api_ctx)
        self.user_data = event.user_data

    def __setitem__(self, key: typing.Any, item: typing.Any) -> None:
        self.user_data[key] = item

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self.user_data[key]

    async def get_user(self, raw_mode: bool = False, **kwargs) -> Union["UsersUser", dict]:
        raw_user = (await self.api_ctx.api_request("users.get", {"user_ids": self.object.object.message_data.from_id if self.object.object.peer_id > 2E9 else self.object.object.peer_id, **kwargs}))[
            "response"
        ][0]
        return raw_user if raw_mode else UsersUser(**raw_user)

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
            user_id=user_id,
            type=type,
            peer_id=self.object.object.peer_id,
            group_id=group_id,
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


class SimpleAttachment(MessagesMessageAttachment):
    _event: "SimpleBotEvent" = PrivateAttr()
    _data: typing.Optional[bytes] = PrivateAttr()
    _allowed_types: List[MessagesMessageAttachmentType] = PrivateAttr()
    _url_types: Dict[MessagesMessageAttachmentType, Callable] = PrivateAttr()

    def __init__(self, attachment: MessagesMessageAttachment, event: "SimpleBotEvent"):
        super().__init__(**attachment.dict())

        self._event = event
        self._data = None

        self._allowed_types = [
            MessagesMessageAttachmentType.AUDIO_MESSAGE,
            MessagesMessageAttachmentType.DOC,
            MessagesMessageAttachmentType.AUDIO,
            MessagesMessageAttachmentType.PHOTO,
            MessagesMessageAttachmentType.GRAFFITI,
        ]

        self._url_types = {
            MessagesMessageAttachmentType.PHOTO: lambda _attachment: _attachment.photo.sizes[
                -1
            ].url,
            MessagesMessageAttachmentType.AUDIO_MESSAGE: lambda _attachment: _attachment.audio_message.link_ogg,
            MessagesMessageAttachmentType.DOC: lambda _attachment: _attachment.doc.url,
            MessagesMessageAttachmentType.AUDIO: lambda _attachment: _attachment.audio.url,
            MessagesMessageAttachmentType.GRAFFITI: lambda _attachment: _attachment.graffiti.url,
        }

    @property
    def url(self) -> str:
        return self._url_types[self.type](self)

    async def download(self) -> typing.Union[typing.NoReturn, bytes]:
        if self._data is not None:
            return self._data
        if self.type not in self._allowed_types:
            raise RuntimeError("cannot download this attachment type")

        url = self.url
        client, token = await self._event.api_ctx.api_options.get_client_and_token()
        data = await client.http_client.request_data(method="GET", url=url)

        self._data = data
        return data

    async def save(self, path: str):
        attach_data = self._data
        if attach_data is None:
            attach_data = await self.download()
        if aiofile is None:
            warnings.warn("aiofile is not installed, saving synchronously")
            with open(path, "wb") as f:
                f.write(attach_data)
            return
        async with aiofile.async_open(path, "wb") as afp:
            await afp.write(attach_data)


class Attachments(list):
    def __init__(self, event: "SimpleBotEvent"):
        super().__init__(
            [
                SimpleAttachment(attachment, event=event)
                for attachment in event.object.object.message.attachments
            ]
        )


class SimpleBotEvent(BotEvent):
    def __init__(self, event: BotEvent):
        super().__init__(event.object, event.api_ctx)
        self.user_data = event.user_data
        self._attachments: typing.Optional[Attachments] = None
        self._payload: typing.Optional[dict] = None

    def __setitem__(self, key: typing.Any, item: typing.Any) -> None:
        self.user_data[key] = item

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self.user_data[key]

    @property
    def text(self) -> str:
        return get_text(self)

    @property
    def peer_id(self) -> int:
        if self.object.type == BotEventType.MESSAGE_EVENT.value:
            return self.object.object.peer_id
        return self.object.object.message.peer_id

    @property
    def from_id(self) -> int:
        if self.object.type == BotEventType.MESSAGE_EVENT.value:
            return self.object.object.user_id
        return self.object.object.message.from_id

    @property
    def payload(self) -> typing.Optional[dict]:
        current_payload = get_payload(self)
        if current_payload is None:
            return current_payload
        if self._payload is None:
            self._payload = (
                json.loads(current_payload)
                if not isinstance(current_payload, dict)
                else current_payload
            )
        return self._payload

    @property
    def attachments(self) -> typing.Optional[typing.List[SimpleAttachment]]:
        if self.object.object.message.attachments is None:
            return None
        if self._attachments is None:
            self._attachments = Attachments(event=self)
        return self._attachments

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
        self,
        func: Any,
        bot_type: BotType,
    ):
        self.bot_type = bot_type
        self.func = callback_caster.cast(func)

    async def execute(self, event: typing.Union[UserEvent, BotEvent]) -> typing.Any:
        if self.bot_type is BotType.BOT:
            new_event = SimpleBotEvent(event)
        else:
            new_event = SimpleUserEvent(event)
        return await self.func.execute(new_event)

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
