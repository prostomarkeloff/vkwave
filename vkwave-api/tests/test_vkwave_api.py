import asyncio
import os
import ssl

import pytest
from dotenv import load_dotenv

from vkwave_api import __version__
from vkwave_api.methods._abc import API
from vkwave_api.token.token import BotSyncSingleToken, Token
from vkwave_client.default import AIOHTTPClient
from vkwave_types.objects import BaseBoolInt

load_dotenv()
TOKEN = os.getenv("TOKEN")


async def get_api():
    client = AIOHTTPClient()
    token = Token(TOKEN)
    bot_token = BotSyncSingleToken(token)
    vk_session = API(clients=client, tokens=bot_token, )

    api = vk_session.get_context()
    return api


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
async def test_users_get():
    api = await get_api()
    request_data = await api.users.get(
        user_ids=[1, 2], fields=["photo_50", "city", "verified"]
    )
    assert request_data.response[0].first_name == "Павел"
    assert request_data.response[1].id == 2
    assert request_data.response[1].is_closed
    assert request_data.response[1].verified == BaseBoolInt.NO
