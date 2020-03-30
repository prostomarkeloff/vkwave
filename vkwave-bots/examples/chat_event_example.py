import logging
import asyncio

from vkwave_bots.dispatching.events.base import BotEvent
from vkwave_client.default import AIOHTTPClient
from vkwave_api.token.token import BotSyncSingleToken, Token
from vkwave_bots.tokens.storage import TokenStorage
from vkwave_bots.dispatching.dp.dp import Dispatcher
from vkwave_bots.dispatching.extensions.longpoll_bot import BotLongpollExtension
from vkwave_bots.dispatching.router.router import DefaultRouter
from vkwave_bots.tokens.types import GroupId
from vkwave_api.methods import API
from vkwave_bots.dispatching.filters.builtin import (
    ChatActionFilter,
)
from vkwave_longpoll.bot import BotLongpoll, BotLongpollData
from vkwave_types.objects import MessagesMessageActionStatus

logging.basicConfig(level=logging.DEBUG)
bot_token = Token(
    "123"
)
gid = 123
router = DefaultRouter()


@router.registrar.with_decorator(
    ChatActionFilter(MessagesMessageActionStatus.CHAT_INVITE_USER)
)
async def fdf(event: BotEvent):
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id,
        message=f"Wow, user with id {event.object.object.message.action.member_id} joined to chat!",
        random_id=0,
    )


async def main():
    client = AIOHTTPClient()
    token = BotSyncSingleToken(bot_token)
    api_session = API(token, client)
    api = api_session.get_context()
    lp_data = BotLongpollData(gid)
    longpoll = BotLongpoll(api, lp_data)
    token_storage = TokenStorage[GroupId]()
    dp = Dispatcher(api_session, token_storage)
    lp_extension = BotLongpollExtension(dp, longpoll)

    dp.add_router(router)
    await dp.cache_potential_tokens()
    await lp_extension.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
