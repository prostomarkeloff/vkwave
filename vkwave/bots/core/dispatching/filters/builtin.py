import json
import logging
import re
import typing
from typing import Dict, List, Optional, Tuple, Union

from typing_extensions import Literal

from vkwave.bots.core.dispatching.events.base import BaseEvent, UserEvent, BotEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.bots.core.types.json_types import JSONDecoder
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import MessagesMessageActionStatus, MessagesMessageAttachmentType
from vkwave.types.user_events import EventId, MessageFlag
from .base import BaseFilter, FilterResult

logger = logging.getLogger(__name__)

try:
    from .builtin_cyth import text_filter_cyth
except ImportError:
    text_filter_cyth = None

MessageEventUser: Tuple[int] = EventId.MESSAGE_EVENT.value
AdvancedMessageEventUser: Tuple[int] = (
    MessageEventUser + EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE.value
)
MessageEventBot: str = "message_new"
CallbackMessageEventBot: str = "message_event"
InvalidEventError = ValueError(
    "Invalid event passed. Expected message event. You must add EventTypeFilter at first."
    " Also maybe filter in need of flags, but event doesn't have it"
)


def any_text_to_list_or_tuple(t: "AnyText") -> Union[Tuple[str, ...], List[str]]:
    return (t,) if isinstance(t, str) else t


def is_from_me(event: UserEvent) -> bool:
    return bool(event.object.object.flags[-1] & MessageFlag.OUTBOX.value)


def is_message_event(event: BaseEvent, flags_needed: bool = False):
    if event.bot_type is BotType.BOT:
        if event.object.type not in [MessageEventBot, CallbackMessageEventBot]:
            raise InvalidEventError
    elif event.bot_type is BotType.USER:
        event_for_check = AdvancedMessageEventUser if not flags_needed else MessageEventUser
        if event.object.object.event_id not in event_for_check:
            raise InvalidEventError


def get_payload(event: BaseEvent) -> Optional[str]:
    is_message_event(event)
    if event.bot_type is BotType.USER:
        if (
            event.object.object.get("message_data") is not None
            and event.object.object.message_data.payload is not None
        ):
            return event.object.object.message_data.payload

    if event.object.type == BotEventType.MESSAGE_EVENT.value:
        return event.object.object.payload

    if event.object.object.dict()["message"].get("payload") is not None:
        return event.object.object.message.payload
    return None


def get_text(event: BaseEvent) -> Optional[str]:
    is_message_event(event)
    if event.bot_type is BotType.USER:
        if event.object.object.dict().get("text") is None:
            return None
        text = event.object.object.text
    else:
        if event.object.object.dict().get("message") is None:
            return None
        text = event.object.object.message.text
    return text


class EventTypeFilter(BaseFilter):
    """
    Event type filter. It supports both user and bot events.

    >>> mn = EventTypeFilter("message_new") # bots' message_new event
    >>> @router.registrar.with_decorator(mn)

    >>> mn = EventTypeFilter(4) # users' message_new event (but we are a bit unsure about that)
    >>> @router.registrar.with_decorator(mn)
    """

    def __init__(self, event_type: Union[str, Tuple[str, ...], Tuple[int, ...], int]):
        self.event_type = event_type

    async def check(self, event: BaseEvent) -> FilterResult:
        if event.bot_type is BotType.BOT:
            if isinstance(self.event_type, tuple):
                return FilterResult(event.object.type in self.event_type)
            if isinstance(self.event_type, str):
                return FilterResult(event.object.type == self.event_type)
        else:
            if isinstance(self.event_type, tuple):
                return FilterResult(event.object.object.event_id in self.event_type)
            if isinstance(self.event_type, int):
                return FilterResult(event.object.object.event_id == self.event_type)
        raise NotImplementedError("There is no implementation for this type of bot")


AnyText = Union[Tuple[str, ...], List[str], str]


class TextFilter(BaseFilter):
    """
    Message text filter.

    >>> text = TextFilter # alias
    >>> _ = text("hi")
    >>> _ = text(("hi", "hello"))
    >>> _ = text(["hi", "hello"])
    >>> _ = text("hI", ignore_case=False)

    >>> text_filter = text("hi")
    >>> @router.registrar.with_decorator(text_filter)
    """

    def __init__(self, text: AnyText, ignore_case: bool = True):
        self.text = any_text_to_list_or_tuple(text)
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)
        if text is None:
            return FilterResult(False)

        if self.ic:
            text = text.lower()
        if text_filter_cyth:
            logger.debug("using Cythonized text filter")
            return FilterResult(text_filter_cyth(self.text, text))
        return FilterResult(text in self.text)


class PayloadFilter(BaseFilter):
    """Filter for message payload"""

    def __init__(
        self, payload: Optional[Dict[str, str]] = None, json_loader: JSONDecoder = json.loads
    ):
        self.json_loader = json_loader
        self.payload = payload

    async def check(self, event: BaseEvent) -> FilterResult:
        current_payload = get_payload(event)
        if current_payload is None:
            return FilterResult(False)
        if self.payload is None:
            return FilterResult(True)

        if not isinstance(current_payload, dict):
            current_payload = self.json_loader(current_payload)
        return FilterResult(current_payload == self.payload)


class ChatActionFilter(BaseFilter):
    """Filter for actions in chat"""

    def __init__(self, action: MessagesMessageActionStatus):
        self.action = action

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type is BotType.USER:
            current_action = event.object.object.message_data.source_act
        else:
            if event.object.object.dict().get("message") is None:
                return FilterResult(False)
            if event.object.object.message.action is None:
                return FilterResult(False)
            current_action = event.object.object.message.action.type
        return FilterResult(current_action == self.action)


class CommandsFilter(BaseFilter):
    """
    Filter for commands in message.

    >>> cm = CommandsFilter # alias
    >>> _ = cm("start")
    >>> _ = cm(("start",))
    >>> _ = cm(("start", "notstart"))
    >>> _ = cm(["start"])
    >>> _ = cm("start", prefixes=("/",))

    >>> command_filter = cm("start", prefixes=("/",))
    >>> @router.registrar.with_decorator(command_filter)
    """

    def __init__(
        self,
        commands: AnyText,
        prefixes: Tuple[str, ...] = ("/", "!"),
        ignore_case: bool = True,
    ):
        self.commands = any_text_to_list_or_tuple(commands)
        self.prefixes = prefixes
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)

        if text is None:
            return FilterResult(False)

        if self.ic:
            text = text.lower()

        for prefix in self.prefixes:
            if not text.startswith(prefix):
                continue
            for command in self.commands:
                pfcmd = f"{prefix}{command}"
                cmd = text.split(" ")[0]
                if cmd == pfcmd:
                    return FilterResult(True)
        return FilterResult(False)


class RegexFilter(BaseFilter):
    """
    Message text regex filter

    >>> regex = RegexFilter # alias
    >>> _ = regex(r".+")  # any string  (example match: "hello world!!!")
    >>> _ = regex(r"\d+")  # any integer number (example match: "254") # noqa: W605
    >>> _ = regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    # any email (example match: "email@example.com")  # noqa: W605
    >>> _ = regex(r"abc-\d\d", flags=re.IGNORECASE)  # example match: "Abc-54" # noqa: W605

    >>> regex_filter = regex(r"user#\d{1,4}")  # example match: "user#723"  # noqa: W605
    >>> @router.registrar.with_decorator(regex_filter)
    """

    def __init__(self, regex: str, flags: int = 0):
        self.pattern = re.compile(regex, flags)

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)
        if text is None:
            return FilterResult(False)
        return FilterResult(self.pattern.match(text) is not None)


class MessageFromConversationTypeFilter(BaseFilter):
    """
    Filtering events by their conversation's type.

    >>> conv_type = MessageFromConversationTypeFilter # alias
    >>> _ = conv_type("from_pm")
    >>> _ = conv_type("from_direct")
    >>> _ = conv_type("from_dm")
    >>> _ = conv_type("from_chat")
    >>> _ = conv_type("chat")

    >>> from_pm = conv_type("from_pm")
    >>> @router.registrar.with_decorator(from_pm)
    """

    PERSONAL_MESSAGE_TYPES = ("from_pm", "from_dm", "from_direct")
    CHAT_MESSAGE_TYPES = ("from_chat", "chat")

    def __init__(
        self, from_what: Literal["from_pm", "from_dm", "from_direct", "from_chat", "chat"]
    ):
        # 0: personal message; 1: chat message
        self.from_what: Literal[0, 1]
        if from_what in self.PERSONAL_MESSAGE_TYPES:
            self.from_what = 0
        elif from_what in self.CHAT_MESSAGE_TYPES:
            self.from_what = 1
        else:
            raise ValueError(f"Unknown message type, got {from_what}")

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type is BotType.USER:
            peer_id = event.object.object.peer_id
        else:
            peer_id = event.object.object.message.peer_id
        status = (peer_id >= 2e9).real

        return FilterResult(self.from_what == status)


class FromMeFilter(BaseFilter):
    """
    Checking is message from me

    FromMeFilter(from_me=False) -> message from other user
    FromMeFilter(from_me=True) -> message from me
    """

    def __init__(self, from_me: bool):
        self.from_me = from_me

    async def check(self, event: UserEvent) -> FilterResult:
        is_message_event(event, flags_needed=True)
        if event.bot_type == BotType.BOT:
            raise RuntimeError("Сannot be used in bot")
        return FilterResult(self.from_me == is_from_me(event))


class MessageArgsFilter(BaseFilter):
    """
    Checking is message has args

    MessageArgsFilter(args_count=2, command_length=1) -> "/start arg1 arg2"
    MessageArgsFilter(args_count=1, command_length=2) -> "/long command arg1"
    """

    def __init__(self, args_count: int, command_length: int = 1):
        self.args_count = args_count
        self.command_length = command_length

    async def check(self, event: BaseEvent) -> FilterResult:
        args = get_text(event).split()[self.command_length:]
        event["args"] = args
        return FilterResult(len(args) == self.args_count)


class FwdMessagesFilter(BaseFilter):
    """
    Checking is message has forward messages

    FwdMessagesFilter() -> any count of fwd
    FwdMessagesFilter(fwd_count=2) -> 2 fwd messages
    """

    def __init__(self, fwd_count: int = -1):
        self.fwd_count = fwd_count

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type == BotType.BOT:
            fwd_count = len(event.object.object.message.fwd_messages or [])
        else:
            if self.fwd_count not in (0, -1):
                raise RuntimeError("In the case of user bots we don't know how many forwards there are, so you have "
                                   "only one option: check if there are forwards or there aren't any")
            fwd_count = event.object.object.extra_message_data.get("fwd")
            print("fwd_count before: ", fwd_count)
            if fwd_count:
                fwd_count = 1
            else:
                fwd_count = 0
            print("fwd_count after: ", fwd_count)

        if self.fwd_count == -1 and fwd_count:
            return FilterResult(True)
        return FilterResult(fwd_count == self.fwd_count)


class ReplyMessageFilter(BaseFilter):
    """
    Checking is message has reply messages
    """

    def __init__(self, with_reply: bool = True):
        self.with_reply = with_reply

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type == BotType.BOT:
            has_reply = event.object.object.message.reply_message is not None
        else:
            event: UserEvent
            extra_message_data = event.object.object.extra_message_data
            has_reply = extra_message_data is not None and "reply" in extra_message_data

        return FilterResult(has_reply == self.with_reply)


class TextContainsFilter(BaseFilter):
    """
    Checking text contains
    """

    def __init__(self, text: AnyText, ignore_case: bool = True):
        self.text = any_text_to_list_or_tuple(text)
        self.ignore_case = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        message_text = get_text(event)

        for text in self.text:
            r = (
                text in message_text
                if not self.ignore_case
                else text.lower() in message_text.lower()
            )
            if r:
                return FilterResult(True)
        return FilterResult(False)


class TextStartswithFilter(BaseFilter):
    def __init__(self, text: AnyText, ignore_case: bool = True):
        self.text = any_text_to_list_or_tuple(text)
        self.ignore_case = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        text = get_text(event)
        if self.ignore_case:
            text = text.lower()
        for t in self.text:
            if text.startswith(t):
                return FilterResult(True)
        return FilterResult(False)


class PayloadContainsFilter(BaseFilter):
    """
    Checking payload dict contains some key
    """

    def __init__(self, key: str, json_loader: JSONDecoder = json.loads):
        self.key = key
        self.json_loader = json_loader

    async def check(
        self,
        event: BaseEvent,
    ) -> FilterResult:
        current_payload = get_payload(event)
        if current_payload is None:
            return FilterResult(False)
        if not isinstance(current_payload, dict):
            current_payload = self.json_loader(current_payload)
        return FilterResult(self.key in current_payload)


class AttachmentTypeFilter(BaseFilter):
    """
    Checking attachments consist of chosen type

    >>> _ = AttachmentTypeFilter(attachment_type="audio")
    >>> _ = AttachmentTypeFilter(attachment_type=MessagesMessageAttachmentType.PHOTO)
    >>> _ = AttachmentTypeFilter(attachment_type=MessagesMessageAttachmentType.PHOTO, _any=True)
            if one of attachments should be photo
    """

    def __init__(
        self, attachment_type: Union[MessagesMessageAttachmentType, str], _any: bool = False
    ):
        self.attachment_type = (
            attachment_type if isinstance(attachment_type, str) else attachment_type.value
        )
        self._any = _any

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if not event.object.object.message.attachments:
            return FilterResult(False)

        attachments_map = map(
            lambda attachment: attachment.type.value is self.attachment_type,
            event.object.object.message.attachments,
        )

        if self._any:
            return FilterResult(any(attachments_map))

        return FilterResult(all(attachments_map))


class IsAdminFilter(BaseFilter):
    def __init__(self, is_admin: bool = True):
        self.is_admin = is_admin

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type is BotType.BOT:
            peer_id = event.object.object.message.peer_id
        else:
            raise NotImplementedError("Currently only for bots not users")

        if peer_id < 2e9:
            raise RuntimeError("Cannot be used not in chats")

        event = typing.cast(BotEvent, event)
        res = await event.api_ctx.messages.get_conversation_members(peer_id)
        users = res.response.items
        for user in users:
            if user.member_id == event.object.object.message.from_id:
                return FilterResult(self.is_admin == user.is_admin)
        return FilterResult(False)
