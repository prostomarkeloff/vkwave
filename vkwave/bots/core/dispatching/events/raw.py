import typing

from vkwave.bots.core.types.bot_type import BotType


class ExtensionEvent:
    def __init__(self, bot_type: BotType, raw_event: typing.Union[list, dict]):
        self.bot_type = bot_type
        self.raw_event = raw_event

    def __repr__(self) -> str:
        return f"ExtensionEvent(bot_type={self.bot_type}, raw_event={self.raw_event})"
