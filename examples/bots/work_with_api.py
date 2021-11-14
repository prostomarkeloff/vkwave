import asyncio

from vkwave.api import API, BotSyncSingleToken, Token
from vkwave.client import AIOHTTPClient

client = AIOHTTPClient()
api = API(tokens=BotSyncSingleToken(Token("token")), clients=client)
api_ctx = api.get_context()


async def main():
    get_user = (await api_ctx.users.get(user_ids = 1)).response[0].first_name
    await api_ctx.api_options.clients[0].close()
    return get_user


asyncio.get_event_loop().run_until_complete(main())
