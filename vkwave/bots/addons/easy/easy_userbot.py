import typing

from vkwave.bots.addons.easy.easy_handlers import SimpleUserEvent
from vkwave.bots.core.dispatching.router.router import BaseRouter
from vkwave.bots.addons.easy.base_easy_bot import BaseSimpleLongPollBot
from vkwave.bots.core.types.bot_type import BotType
from vkwave.client import AIOHTTPClient


class SimpleLongPollUserBot(BaseSimpleLongPollBot):
    def __init__(
        self,
        tokens: typing.Union[str, typing.List[str]],
        router: typing.Optional[BaseRouter] = None,
        uvloop: bool = False,
        client: typing.Optional[AIOHTTPClient] = None,
        event: typing.Optional[typing.Type[SimpleUserEvent]] = None
    ):
        super().__init__(
            tokens, group_id=None, bot_type=BotType.USER,
            router=router, uvloop=uvloop, client=client,
            event=event or SimpleUserEvent
        )
