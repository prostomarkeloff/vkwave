import logging
import asyncio

from vkwave.bots.core.dispatching.events.base import UserEvent
from vkwave.client.default import AIOHTTPClient
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.bots.core.tokens.storage import UserTokenStorage
from vkwave.bots.core.dispatching.dp.dp import Dispatcher
from vkwave.bots.core.dispatching.extensions.longpoll_user import UserLongpollExtension
from vkwave.bots.core.dispatching.router.router import DefaultRouter
from vkwave.bots.core.tokens.types import UserId
from vkwave.api.methods import API
from vkwave.bots.core.dispatching.filters.builtin import EventTypeFilter, FromMeFilter, TextFilter
from vkwave.longpoll.user import UserLongpollData, UserLongpoll

logging.basicConfig(level=logging.DEBUG)


bot_token = Token("token")
router = DefaultRouter()


@router.registrar.with_decorator(EventTypeFilter((3, 4, 5, 18)), FromMeFilter(from_me=True))
async def from_me(event: UserEvent):
    print("from me:", event.object.object.text)


@router.registrar.with_decorator(
    EventTypeFilter((3, 4, 5, 18)), FromMeFilter(from_me=False), TextFilter("hello")
)
async def answer_hello(event: UserEvent):
    await event.api_ctx.messages.send(
        user_id=event.object.object.peer_id, message="hello!", random_id=0
    )


async def main():
    client = AIOHTTPClient()
    token = BotSyncSingleToken(bot_token)
    api_session = API(token, client)
    api = api_session.get_context()
    longpoll = UserLongpoll(api, UserLongpollData())
    token_storage = UserTokenStorage[UserId](bot_token)
    dp = Dispatcher(api_session, token_storage)
    lp_extension = UserLongpollExtension(dp, longpoll)
    dp.add_router(router)
    await lp_extension.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
