import typing

from vkwave.bots.easy._base_easy_bot import BaseSimpleLongPollBot
from vkwave.bots.core.types.bot_type import BotType


class SimpleLongPollUserBot(BaseSimpleLongPollBot):
    def __init__(
        self, tokens: typing.Union[str, typing.List[str]],
    ):
        super().__init__(tokens, group_id=None, bot_type=BotType.USER)
