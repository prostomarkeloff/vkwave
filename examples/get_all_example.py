import asyncio

from vkwave.api import Fetcher
from vkwave.bots import create_api_session_aiohttp

api = create_api_session_aiohttp(token="TOKEN").api


async def main():
    async for post_list in Fetcher.get_all_wall_posts_iter(api=api.get_context(), wall_owner_id=-172598718):
        print(post_list[0]["id"])


asyncio.get_event_loop().run_until_complete(main())
