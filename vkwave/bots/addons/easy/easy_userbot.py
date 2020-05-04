import typing

from vkwave.bots.core.dispatching.router.router import BaseRouter
from vkwave.bots.addons.easy.base_easy_bot import BaseSimpleLongPollBot
from vkwave.bots.core.types.bot_type import BotType


class SimpleLongPollUserBot(BaseSimpleLongPollBot):
    def __init__(
        self,
        tokens: typing.Union[str, typing.List[str]],
        router: typing.Optional[BaseRouter] = None,
        uvloop: bool = False
    ):
        super().__init__(tokens, group_id=None, bot_type=BotType.USER, router=router, uvloop=uvloop)
