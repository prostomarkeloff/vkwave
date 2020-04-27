import asyncio

from vkwave.streaming import StreamingClient
from vkwave.bots import create_api_session_aiohttp
from vkwave.http import AIOHTTPWSClient


async def main():
    api = create_api_session_aiohttp(token="SERVICE_TOKEN")
    client = StreamingClient(
        api.api.get_context(),
        api.api.default_api_options.get_client().http_client,
        AIOHTTPWSClient(),
    )

    await client.delete_all_rules()
    print(await client.get_rules())

    await client.add_rule(value="вконтакте", tag="cyrillic")
    await client.add_rule(value="vk", tag="latin")

    print(await client.get_rules())

    async for event in client.stream():
        print(event)


asyncio.get_event_loop().run_until_complete(main())
