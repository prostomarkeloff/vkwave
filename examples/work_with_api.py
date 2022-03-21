import asyncio

from vkwave.api import API, BotSyncSingleToken, Token


async def main():
    token = BotSyncSingleToken(Token("token"))
    async with API(tokens=token) as api:
        api_ctx = api.get_context()
        get_user = (await api_ctx.users.get(user_ids=1)).response[0].first_name
        await api_ctx.api_options.clients[0].close()
        print(get_user)


asyncio.get_event_loop().run_until_complete(main())
