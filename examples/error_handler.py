from vkwave.api import API
from vkwave.client import AIOHTTPClient
from vkwave.api.methods import RETURN_RESULT_ERRORS  # errors when you can return result from handler
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

    # also you can set default error handler if handler for this code is not found.
    # code 4 -> finding handler -> ...
    # found -> run that handler
    # not found -> run this handler

    # if default error handler isn't set exception will be raised
    async def default(error: dict, api_ctx):
        if error["error"]["error_code"] in RETURN_RESULT_ERRORS:
            ...
        else:
            ...

    api = API(tokens="...", clients=AIOHTTPClient())
    api.default_api_options.error_dispatcher.add_handler(3, error_handler)  # unknown method passed
    api.default_api_options.error_dispatcher.add_handler(6, error_handler_another)  # too many requests
    api.default_api_options.error_dispatcher.set_default_error_handler(default)  # default handler

    ctx = api.get_context()

    await ctx.status.get()

asyncio.run(main())

