import typing

from vkwave.bots.easy.base_easy_bot import BaseSimpleLongPollBot
from vkwave.bots.core.types.bot_type import BotType


class SimpleLongPollBot(BaseSimpleLongPollBot):
    def __init__(self, tokens: typing.Union[str, typing.List[str]], group_id: int):
        super().__init__(tokens, group_id=group_id, bot_type=BotType.BOT)
