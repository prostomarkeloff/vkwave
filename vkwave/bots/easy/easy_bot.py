import typing

from vkwave.bots import GroupId
from vkwave.bots.core.dispatching.extensions.callback import AIOHTTPCallbackExtension
from vkwave.bots.core.dispatching.extensions.callback.conf import ConfirmationStorage
from vkwave.bots.easy.base_easy_bot import BaseSimpleLongPollBot
from vkwave.bots.core.types.bot_type import BotType


class SimpleLongPollBot(BaseSimpleLongPollBot):
    def __init__(self, tokens: typing.Union[str, typing.List[str]], group_id: int):
        super().__init__(tokens, group_id=group_id, bot_type=BotType.BOT)


class SimpleCallbackBot(BaseSimpleLongPollBot):
    def __init__(
            self,
            tokens: typing.Union[str, typing.List[str]],
            group_id: int,
            path: str,
            host: str,
            port: int,
            confirmation_key: typing.Optional[str] = None,
            secret: typing.Optional[str] = None,
    ):
        super().__init__(tokens, bot_type=BotType.BOT, group_id=group_id)
        storage = ConfirmationStorage()
        storage.add_confirmation(GroupId(group_id), confirmation_key)

        self.cb_extension = AIOHTTPCallbackExtension(
            self.dispatcher,
            path=path,
            host=host,
            port=port,
            secret=secret,
            confirmation_storage=storage,
        )

    async def run(self):
        await self.dispatcher.cache_potential_tokens()
        await self.cb_extension.start()
