import json
import logging
import re
from typing import Dict, List, Optional, Tuple, Union

from typing_extensions import Literal

from vkwave.bots.core.dispatching.events.base import BaseEvent, UserEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.bots.core.types.json_types import JSONDecoder
from vkwave.types.bot_events import BotEventType
from vkwave.types.objects import MessagesMessageActionStatus
from vkwave.types.user_events import EventId, MessageFlag

from .base import BaseFilter, FilterResult

MessageEventUser: Tuple[int] = EventId.MESSAGE_EVENT.value
MessageEventBot: str = "message_new"
InvalidEventError = ValueError(
    "Invalid event passed. Expected message event. You must add EventTypeFilter at first."
)

logger = logging.getLogger(__name__)


def is_from_me(event: UserEvent) -> bool:
    return bool(event.object.object.flags[-1] & MessageFlag.OUTBOX.value)


def is_message_event(event: BaseEvent):
    if event.bot_type is BotType.BOT:
        if event.object.type != MessageEventBot:
            raise InvalidEventError
    elif event.bot_type is BotType.USER:
        if event.object.object.event_id not in MessageEventUser:
            raise InvalidEventError


def has_payload(event: BaseEvent):
    event_dict = event.object.object.dict()

    if event_dict.get("payload") is not None:
        logger.debug("has_payload is True")
        return True
    try:
        event_dict["message"]["payload"]
        logger.debug("has_payload is True")
        return True
    except (TypeError, KeyError):
        logger.debug("has_payload is False")
        return False


def get_text(event: BaseEvent) -> Optional[str]:
    is_message_event(event)
    event_obj = event.object.object
    if event.bot_type is BotType.USER:
        logger.debug("Bot type is User")
        if event_obj.dict().get("text") is None:
            logger.debug("Text is None")
            return None
        text = event_obj.text
    else:
        logger.debug("Bot type is Bot")
        if event_obj.dict().get("message") is None:
            logger.debug("Text is None")
            return None
        text = event_obj.message.text
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
        log_message = "event_type is {}"
        tup_message = log_message.format("tuple")

        if event.bot_type is BotType.BOT:
            logger.debug("Bot type is Bot")
            if isinstance(self.event_type, tuple):
                logger.debug(tup_message)
                return FilterResult(event.object.type in self.event_type)
            if isinstance(self.event_type, str):
                logger.debug(log_message.format("str"))
                return FilterResult(event.object.type == self.event_type)
        else:
            logger.debug("Bot type is User")
            if isinstance(self.event_type, tuple):
                logger.debug(tup_message)
                return FilterResult(event.object.object.event_id in self.event_type)
            if isinstance(self.event_type, int):
                logger.debug(log_message.format("int"))
                return FilterResult(event.object.object.event_id == self.event_type)
        logger.debug("raise NotImplementedError")
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
        self.text = (text,) if isinstance(text, str) else text
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)
        if text is None:
            logger.debug("text is None")
            return FilterResult(False)

        if self.ic:
            text = text.lower()
            self.text = self.text.lower()
            logger.debug("text ignore case added")

        return FilterResult(text in self.text)


class PayloadFilter(BaseFilter):
    """Filter for message payload"""

    def __init__(self, payload: Optional[Dict[str, str]], json_loader: JSONDecoder = json.loads):
        self.json_loader = json_loader
        self.payload = payload

    async def check(self, event: BaseEvent) -> FilterResult:
        if not has_payload(event):
            return FilterResult(False)
        if event.bot_type is BotType.USER:
            current_payload = self.json_loader(event.object.object.message_data.payload)
        else:
            if event.object.type == BotEventType.MESSAGE_EVENT.value:
                current_payload = event.object.object.payload
            else:
                current_payload = self.json_loader(event.object.object.message.payload)
        if current_payload is None:
            return FilterResult(False)
        if self.payload is None:
            return FilterResult(True)
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
        self, commands: AnyText, prefixes: Tuple[str, ...] = ("/", "!"), ignore_case: bool = True,
    ):
        self.commands = (commands,) if isinstance(commands, str) else commands
        self.prefixes = prefixes
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)

        if text is None:
            logger.debug("text is None: return False")
            return FilterResult(False)

        if self.ic:
            text = text.lower()
            logger.debug("text -> text.lower()")

        for command in self.commands:
            for prefix in self.prefixes:
                if text.startswith(f"{prefix}{command}"):
                    logger.debug("return True")
                    return FilterResult(True)
        logger.debug("return False")
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
            logger.debug("text is None: return False")
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
            logger.debug("raise ValueError: Unknown message type")
            raise ValueError(f"Unknown message type, got {from_what}")
        logger.debug(f"{self.from_what=}")

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        event_obj = event.object.object
        if event.bot_type is BotType.USER:
            peer_id = event_obj.peer_id
        else:
            peer_id = event_obj.message.peer_id
        logger.debug(f"{peer_id=}")

        status = (peer_id >= 2e9).real
        result = self.from_what == status

        logger.debug(f"return {result}")
        return FilterResult(result)


class FromMeFilter(BaseFilter):
    """
    Checking is message from me

    FromMeFilter(from_me=False) -> message from other user
    FromMeFilter(from_me=True) -> message from me
    """

    def __init__(self, from_me: bool):
        self.from_me = from_me

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type == BotType.BOT:
            logger.debug("raise RuntimeError: BotType is Bot")
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
        args = get_text(event).split()[self.command_length :]
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
        event_obj = event.object.object
        if event.bot_type == BotType.BOT:
            fwd_count = len(event_obj.message.fwd_messages or [])
        else:
            fwd_count = len(event_obj.message_data.fwd_count or [])

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
        self.text = (text,) if isinstance(text, str) else text
        self.ignore_case = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        message_text = get_text(event)
        if message_text is None:
            return FilterResult(False)

        if self.ignore_case:
            message_text = message_text.lower()

        for text in self.text:
            if self.ignore_case:
                text = text.lower()
            if text in message_text:
                return FilterResult(True)
        return FilterResult(False)
