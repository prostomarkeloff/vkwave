import asyncio
import logging

from vkwave.api import API, BotSyncSingleToken, Token
from vkwave.bots import (
    BaseEvent,
    CommandsFilter,
    DefaultRouter,
    Dispatcher,
    EventTypeFilter,
    GroupId,
    TokenStorage,
)
from vkwave.bots.core.dispatching.extensions.callback import AIOHTTPCallbackExtension
from vkwave.bots.core.dispatching.extensions.callback.conf import ConfirmationStorage
from vkwave.client import AIOHTTPClient
from vkwave.types.bot_events import BotEventType

logging.basicConfig(level=logging.DEBUG)
bot_token = Token("Token")
gid = 123456
router = DefaultRouter()


@router.registrar.with_decorator(
    CommandsFilter(["hello"]), EventTypeFilter(BotEventType.MESSAGE_NEW)
)
async def hello_handler(event: BaseEvent):
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id, message="hellooooooooooooo!", random_id=0,
    )


async def main():
    client = AIOHTTPClient()
    token = BotSyncSingleToken(bot_token)
    api_session = API(token, client)
    token_storage = TokenStorage[GroupId]()
    dp = Dispatcher(api_session, token_storage)

    storage = ConfirmationStorage()
    storage.add_confirmation(GroupId(gid), "CONFIRMATION_KEY")

    cb_extension = AIOHTTPCallbackExtension(
        dp, path="/", host="127.0.0.1", port=80, secret="SECRET_KEY", confirmation_storage=storage
    )

    dp.add_router(router)
    await dp.cache_potential_tokens()
    await cb_extension.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
