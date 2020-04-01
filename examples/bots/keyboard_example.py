import logging
import asyncio

from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.client.default import AIOHTTPClient
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.bots.core.tokens.storage import TokenStorage
from vkwave.bots.core.dispatching.dp.dp import Dispatcher
from vkwave.bots.core.dispatching.extensions.longpoll_bot import BotLongpollExtension
from vkwave.bots.core.dispatching.router.router import DefaultRouter
from vkwave.bots.core.tokens.types import GroupId
from vkwave.api.methods import API
from vkwave.bots.core.dispatching.filters.builtin import (
    EventTypeFilter,
    PayloadFilter,
    CommandsFilter,
)
from vkwave.longpoll.bot import BotLongpoll, BotLongpollData
from vkwave.types.bot_events import BotEventType
from vkwave.bots.utils.keyboards import Keyboard

logging.basicConfig(level=logging.DEBUG)
bot_token = Token("123")
gid = 123
router = DefaultRouter()


@router.registrar.with_decorator(
    CommandsFilter(["hello"]), EventTypeFilter(BotEventType.MESSAGE_NEW)
)
async def kb_handler(event: BaseEvent):
    kb = Keyboard(one_time=True)
    kb.add_text_button(text="123456", payload={"hello": "world"})
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id,
        message="123",
        keyboard=kb.get_keyboard(),
        random_id=0,
    )


@router.registrar.with_decorator(
    PayloadFilter({"hello": "world"}), EventTypeFilter(BotEventType.MESSAGE_NEW)
)
async def handler(event: BaseEvent):

    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id,
        message=f"Wow, you pressed the button! Your payload is {event.object.object.message.payload}",
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
