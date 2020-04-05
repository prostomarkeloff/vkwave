from vkwave.api.methods import API
from vkwave.client.default import AIOHTTPClient
import asyncio

async def main():

    async def error_handler(error: dict, api_ctx):
        print(error)
        # some crazy stuff

    # on some code errors you can re-do request and return result of response
    # they are: 1, 6, 14

    async def error_handler_another(error: dict, api_ctx) -> dict:
        # doing request
        result = ...
        return result


    api = API(tokens="...", clients=AIOHTTPClient())
    api.default_api_options.error_dispatcher.add_handler(3, error_handler)  # unknown method passed
    api.default_api_options.error_dispatcher.add_handler(6, error_handler_another)  # too many requests

    ctx = api.get_context()

    await ctx.status.get()

asyncio.run(main())

