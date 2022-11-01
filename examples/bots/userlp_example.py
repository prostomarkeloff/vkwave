import asyncio
import logging

from vkwave.api import API, BotSyncSingleToken, Token
from vkwave.bots import (
    DefaultRouter,
    Dispatcher,
    EventTypeFilter,
    FromMeFilter,
    TextFilter,
    UserEvent,
    UserId,
    UserLongpollExtension,
    UserTokenStorage,
)
from vkwave.client import AIOHTTPClient
from vkwave.longpoll import UserLongpoll, UserLongpollData
from vkwave.types.user_events import EventId

logging.basicConfig(level=logging.DEBUG)


bot_token = Token("token")
router = DefaultRouter()


# EventTypeFilter((3, 4, 5, 18)) == EventTypeFilter(EventId.MESSAGE_EVENT.value)
@router.registrar.with_decorator(
    EventTypeFilter(EventId.MESSAGE_EVENT.value), FromMeFilter(from_me=True)
)
async def from_me(event: UserEvent):
    print("from me:", event.object.object.text)


# FromMeFilter(from_me=False) -> message from other user
# FromMeFilter(from_me=True) -> message from me
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
