import json
import random
import typing
import warnings
from typing import Any, Callable, Dict, List, Union

from pydantic import PrivateAttr

from vkwave.bots import BotEvent, BotType, EventTypeFilter, UserEvent
from vkwave.bots.core import BaseFilter
from vkwave.bots.core.dispatching.filters.builtin import get_payload, get_text
from vkwave.bots.core.dispatching.handler.callback import BaseCallback
from vkwave.bots.core.dispatching.handler.cast import caster as callback_caster
from vkwave.bots.core.types.json_types import JSONEncoder
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import (
    BaseBoolInt,
    MessagesMessageAttachment,
    MessagesMessageAttachmentType,
    UsersUser,
)
from vkwave.types.responses import BaseOkResponse, MessagesEditResponse, MessagesSendResponse
from vkwave.types.user_events import EventId

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

    @property
    def text(self) -> str:
        return get_text(self)

    @property
    def peer_id(self) -> int:
        return self.object.object.peer_id

    @property
    def from_id(self) -> int:
        return self.object.object.message_data.from_id

    @property
    def user_id(self) -> int:
        return self.from_id if self.peer_id > 2e9 else self.peer_id

    async def get_user(
        self, raw_mode: bool = False, **kwargs
    ) -> Union["UsersUser", dict]:  # getting information about the sender
        raw_user = (
            await self.api_ctx.api_request("users.get", {"user_ids": self.user_id, **kwargs})
        )["response"][0]
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
        expire_ttl: typing.Optional[int] = None,
        silent: typing.Optional[bool] = None,
    ) -> MessagesSendResponse:
        return await self.api_ctx.messages.send(
            message=message,
            forward=forward,
            template=template,
            content_source=content_source,
            intent=intent,
            subscribe_id=subscribe_id,
            expire_ttl=expire_ttl,
            silent=silent,
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
            random_id=random.randint(-2147483648, 2147483647),
        )

    async def reply(
        self,
        message: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
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
        expire_ttl: typing.Optional[int] = None,
        silent: typing.Optional[bool] = None,
    ) -> MessagesSendResponse:
        return await self.api_ctx.messages.send(
            message=message,
            forward=forward,
            template=template,
            content_source=content_source,
            intent=intent,
            subscribe_id=subscribe_id,
            expire_ttl=expire_ttl,
            silent=silent,
            domain=domain,
            lat=lat,
            long=long,
            attachment=attachment,
            reply_to=self.object.object.message_id,
            forward_messages=forward_messages,
            sticker_id=sticker_id,
            group_id=group_id,
            keyboard=keyboard,
            payload=payload,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            peer_id=self.object.object.peer_id,
            random_id=random.randint(-2147483648, 2147483647),
        )

    async def edit(
        self,
        message: typing.Optional[str] = None,
        return_raw_response: bool = False,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        keep_forward_messages: typing.Optional[BaseBoolInt] = None,
        keep_snippets: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
        dont_parse_links: typing.Optional[bool] = None,
        message_id: typing.Optional[int] = None,
        conversation_message_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
    ) -> MessagesEditResponse:
        return await self.api_ctx.messages.edit(
            message=message,
            peer_id=self.object.object.peer_id,
            return_raw_response=return_raw_response,
            lat=lat,
            long=long,
            attachment=attachment,
            keep_forward_messages=keep_forward_messages,
            keep_snippets=keep_snippets,
            group_id=group_id,
            dont_parse_links=dont_parse_links,
            message_id=message_id or self.object.object.message_id,
            conversation_message_id=conversation_message_id,
            template=template,
            keyboard=keyboard,
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
    """Базовый класс события."""

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
        """Получает текст сообщения

        Returns:
            str: Текст
        """
        return get_text(self)

    @property
    def peer_id(self) -> int:
        """Получает идентификатор чата

        Returns:
            int: идентификатор чата
        """
        if self.object.type == BotEventType.MESSAGE_EVENT.value:
            return self.object.object.peer_id
        return self.object.object.message.peer_id

    @property
    def from_id(self) -> int:
        """Получает идентификатор отправителя

        Returns:
            int: идентификатор отправителя
        """
        if self.object.type == BotEventType.MESSAGE_EVENT.value:
            return self.object.object.user_id
        return self.object.object.message.from_id

    @property
    def payload(self) -> typing.Optional[dict]:
        """Получает payload события

        Returns:
            int: payload события
        """
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
        """Получает список вложений

        Returns:
            typing.Optional[typing.List[SimpleAttachment]]: список вложений
        """
        if self.object.object.message.attachments is None:
            return None
        if self._attachments is None:
            self._attachments = Attachments(event=self)
        return self._attachments

    @property
    def user_id(self) -> int:
        """Шорткат для выбора from_id или peer_id

        Returns:
            int: идентификатор пользователя
        """
        return self.from_id if self.peer_id > 2e9 else self.peer_id

    async def get_user(self, raw_mode: bool = False, **kwargs) -> Union["UsersUser", dict]:
        """Получение объекта пользователя

        Returns:
            Union["UsersUser", dict]: Объект пользователя
        """
        raw_user = (
            await self.api_ctx.api_request("users.get", {"user_ids": self.user_id, **kwargs})
        )["response"][0]
        return raw_user if raw_mode else UsersUser(**raw_user)

    async def edit(
        self,
        message: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        keep_forward_messages: typing.Optional[BaseBoolInt] = None,
        keep_snippets: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        message_id: typing.Optional[int] = None,
        conversation_message_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
    ) -> MessagesEditResponse:
        """Шорткат для редактирования своего сообщения.

        Args:
            message (typing.Optional[str]): Текст.
            lat (typing.Optional[int]): Широта.
            long (typing.Optional[int]): Долгота.
            attachment (typing.Optional[str]): Вложения (строка с идентификаторами, разделёнными запятой).
            keep_forward_messages (typing.Optional[BaseBoolInt]): — сохранить прикрепленные пересланные сообщения.
            keep_snippets (typing.Optional[BaseBoolInt]): 1 — сохранить прикрепленные внешние ссылки (сниппеты).
            group_id (typing.Optional[int]): Идентификатор группы.
            dont_parse_links (typing.Optional[bool]): 1 — не создавать сниппет ссылки из сообщения.
            disable_mentions (typing.Optional[bool]): 1 — отключить уведомление об упоминании в сообщении.
            message_id (typing.Optional[int]): Идентификатор сообщения.
            conversation_message_id (typing.Optional[int]): Идентификатор сообщения в беседе.
            template (typing.Optional[str]): Шаблон.
            keyboard (typing.Optional[str]): Клавиатура.

        Returns:
            MessagesEditResponse: Ответ сервера
        """
        _check_event_type(self.object.type)
        return await self.api_ctx.messages.edit(
            peer_id=self.object.object.message.peer_id,
            message=message,
            lat=lat,
            long=long,
            attachment=attachment,
            keep_forward_messages=keep_forward_messages,
            keep_snippets=keep_snippets,
            group_id=group_id,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            message_id=message_id,
            conversation_message_id=conversation_message_id,
            template=template,
            keyboard=keyboard
        )

    async def reply(
        self,
        message: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
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
        expire_ttl: typing.Optional[int] = None,
        silent: typing.Optional[bool] = None,
        json_serialize: JSONEncoder = json.dumps,
    ) -> MessagesSendResponse:
        """Шорткат для отправки ответа на сообщение пользователю, от которого пришло событие

        Args:
            message (typing.Optional[str]): Текст.
            domain (typing.Optional[str]): Короткая ссылка пользователя.
            lat (typing.Optional[int]): Широта.
            long (typing.Optional[int]): Долгота.
            attachment (typing.Optional[str]): Вложения (строка с идентификаторами, разделёнными запятой).
            sticker_id (typing.Optional[int]): Идентификатор прикрепляемого стикера.
            group_id (typing.Optional[int]): Идентификатор группы.
            keyboard (typing.Optional[str]): Клавиатура.
            template (typing.Optional[str]): Шаблон (карусель, например).
            payload (typing.Optional[str]): Payload.
            content_source (typing.Optional[str]): Источник [пользовательского контента](https://vk.com/dev/bots_docs_2?f=3.3.+%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D1%81+%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%BC+%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82%D0%BE%D0%BC).
            dont_parse_links (typing.Optional[bool]): 1 &mdash; не создавать сниппет ссылки из сообщения.
            disable_mentions (typing.Optional[bool]): 1 &mdash; отключить создание упоминаний.
            intent (typing.Optional[str]): Строка, описывающая [интенты](https://vk.com/dev/bots_docs_4?f=7.+%D0%98%D0%BD%D1%82%D0%B5%D0%BD%D1%82%D1%8B).
            subscribe_id (typing.Optional[int]): число, которое в будущем будет предназначено для работы с интентами.
            expire_ttl (typing.Optional[int]): ???.
            silent (typing.Optional[bool]): ???.
            json_serialize (JSONEncoder): сериализация.

        Returns:
            MessagesSendResponse - Ответ сервера
        """
        _check_event_type(self.object.type)

        forward = {
            "is_reply": 1,
            "conversation_message_ids": self.object.object.message.conversation_message_id,
            "peer_id": self.object.object.message.peer_id,
        }
        return await self.api_ctx.messages.send(
            forward=json_serialize(forward),
            intent=intent,
            subscribe_id=subscribe_id,
            expire_ttl=expire_ttl,
            silent=silent,
            domain=domain,
            lat=lat,
            long=long,
            attachment=attachment,
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
        expire_ttl: typing.Optional[int] = None,
        silent: typing.Optional[bool] = None,
    ) -> MessagesSendResponse:
        """Шорткат для отправки сообщения пользователю, от которого пришло событие.

        Args:
            message (typing.Optional[str]): Текст.
            domain (typing.Optional[str]): Короткая ссылка пользователя.
            lat (typing.Optional[int]): Широта.
            long (typing.Optional[int]): Долгота.
            attachment (typing.Optional[str]): Вложения (строка с идентификаторами, разделёнными запятой).
            reply_to (typing.Optional[int]): Идентификатор сообщения, на которое нужно ответить.
            forward_messages (typing.Optional[typing.List[int]]): Идентификаторы пересылаемых сообщений.
            forward (typing.Optional[str]): JSON-объект (подробнее в [документации ВК](https://vk.com/dev/messages.send)).
            sticker_id (typing.Optional[int]): Идентификатор прикрепляемого стикера.
            group_id (typing.Optional[int]): Идентификатор группы.
            keyboard (typing.Optional[str]): Клавиатура.
            template (typing.Optional[str]): Шаблон (карусель, например).
            payload (typing.Optional[str]): Payload.
            content_source (typing.Optional[str]): Источник [пользовательского контента](https://vk.com/dev/bots_docs_2?f=3.3.+%D0%A1%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D1%81+%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%BC+%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82%D0%BE%D0%BC).
            dont_parse_links (typing.Optional[bool]): 1 &mdash; не создавать сниппет ссылки из сообщения.
            disable_mentions (typing.Optional[bool]): 1 &mdash; отключить создание упоминаний.
            intent (typing.Optional[str]): Строка, описывающая [интенты](https://vk.com/dev/bots_docs_4?f=7.+%D0%98%D0%BD%D1%82%D0%B5%D0%BD%D1%82%D1%8B).
            subscribe_id (typing.Optional[int]): число, которое в будущем будет предназначено для работы с интентами.
            expire_ttl (typing.Optional[int]): ???.
            silent (typing.Optional[bool]): ???.

        Returns:
            MessagesSendResponse: Ответ сервера
        """
        _check_event_type(self.object.type)
        return await self.api_ctx.messages.send(
            forward=forward,
            intent=intent,
            subscribe_id=subscribe_id,
            expire_ttl=expire_ttl,
            silent=silent,
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
        """Изменение статуса активности

        Args:
            type (typing.Optional[str], optional): Тип активности. (`typing` — пользователь начал набирать текст, `audiomessage` — пользователь записывает голосовое сообщение)
            user_id (typing.Optional[int], optional): Идентификатор пользователя-получателя.
            group_id (typing.Optional[int], optional): Идентификатор группы.

        Returns:
            MessagesSendResponse: Результат запроса.
        """
        _check_event_type(self.object.type)
        return await self.api_ctx.messages.set_activity(
            user_id=user_id,
            type=type,
            peer_id=self.object.object.message.peer_id,
            group_id=group_id,
        )

    async def callback_answer(self, event_data: typing.Dict[str, str]) -> BaseOkResponse:
        """Ответ на нажатие callback кнопки.

        Args:
            event_data (typing.Dict[str, str]): [описание данных](https://vk.com/dev/bots_docs_5?f=4.4.%2BCallback-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B8) для ответа на callback

        Raises:
            RuntimeError: Если вызван, когда событие не MessageEvent типа.

        Returns:
            BaseOkResponse: Результат запроса
        """
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
