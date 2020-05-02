import json
import re
import typing
from typing import Dict, Tuple, Union

from typing_extensions import Literal

from vkwave.bots.core.dispatching.events.base import BaseEvent, UserEvent
from vkwave.bots.core.types.bot_type import BotType
from vkwave.bots.core.types.json_types import JSONDecoder
from vkwave.types.objects import MessagesMessageActionStatus
from vkwave.types.user_events import EventId, MessageFlag

from .base import BaseFilter, FilterResult


MessageEventUser: Tuple[int] = EventId.MESSAGE_EVENT.value
MessageEventBot: str = "message_new"
InvalidEventError = ValueError(
    "Invalid event passed. Expected message event. You must add EventTypeFilter at first."
)


def is_from_me(event: UserEvent) -> bool:
    return bool(event.object.object.flags[-1] & MessageFlag.OUTBOX.value)


def is_message_event(event: BaseEvent):
    if event.bot_type is BotType.BOT:
        if event.object.type != MessageEventBot:
            raise InvalidEventError
    elif event.bot_type is BotType.USER:
        if event.object.object.event_id not in MessageEventUser:
            raise InvalidEventError


def get_text(event: BaseEvent) -> typing.Optional[str]:
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


AnyText = typing.Union[typing.Tuple[str, ...], typing.List[str], str]


class TextFilter(BaseFilter):
    """
    Message text filter.

    >>> text = TextFilter # alias
    >>> _ = text("hi")
    >>> _ = text(("hi",))
    >>> _ = text(["hi"])
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
            return FilterResult(False)

        if self.ic:
            text = text.lower()
        return FilterResult(text in self.text)


class PayloadFilter(BaseFilter):
    """Filter for message payload"""

    def __init__(self, payload: Dict[str, str], json_loader: JSONDecoder = json.loads):
        self.json_loader = json_loader
        self.payload = payload

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type is BotType.USER:
            current_payload = event.object.object.message_data.payload
        else:
            if event.object.object.dict().get("message") is None:
                return FilterResult(False)
            current_payload = event.object.object.message.payload
        if current_payload is None:
            return FilterResult(False)
        return FilterResult(self.json_loader(current_payload) == self.payload)


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
        prefixes: typing.Tuple[str, ...] = ("/", "!"),
        ignore_case: bool = True,
    ):
        self.commands = (commands,) if isinstance(commands, str) else commands
        self.prefixes = prefixes
        self.ic = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)

        if text is None:
            return FilterResult(False)

        if self.ic:
            text = text.lower()
        for command in self.commands:
            for prefix in self.prefixes:
                if text.startswith(f"{prefix}{command}"):
                    return FilterResult(True)
        return FilterResult(False)


class RegexFilter(BaseFilter):
    """
    Message text regex filter

    >>> regex = RegexFilter # alias
    >>> _ = regex(r".+")  # any string  (example match: "hello world!!!")
    >>> _ = regex(r"\d+")  # any integer number (example match: "254")  # noqa: W605
    >>> _ = regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")  # any email (example match: "email@example.com")  # noqa: W605
    >>> _ = regex(r"abc-\d\d", flags=re.IGNORECASE)  # example match: "Abc-54"  # noqa: W605

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
    
    >>> from_pm = conv_type("from_pm")
    >>> @router.registrar.with_decorator(from_pm)
    """

    def __init__(self, from_what: Literal["from_pm", "from_dm", "from_direct", "from_chat"]):
        # 0: pm; 1: chat
        self.from_what: Literal[0, 1] = 0 if from_what in (
            "from_pm",
            "from_dm",
            "from_direct",
        ) else 1

    async def check(self, event: BaseEvent) -> FilterResult:
        is_message_event(event)
        if event.bot_type is BotType.USER:
            raise NotImplementedError("Not implemented yet")
        else:
            peer_id: int
            from_id: int
            peer_id, from_id = (
                event.object.object.message.peer_id,
                event.object.object.message.from_id,
            )

            status: int

            if peer_id == from_id:
                status = 0
            else:
                status = 1

            return FilterResult(self.from_what == status)


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
            raise RuntimeError("Сannot be used in bot")
        event: UserEvent
        return FilterResult(self.from_me == is_from_me(event))


# TODO: MessageArgsFilter
