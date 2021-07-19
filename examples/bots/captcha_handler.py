# Easy bot imports
from vkwave.bots import SimpleLongPollUserBot
from vkwave.api import APIOptionsRequestContext


# Ordinary bot imports
from vkwave.client import AIOHTTPClient
from vkwave.bots import TokenStorage, Dispatcher, BotLongpollExtension, GroupId
from vkwave.api import API, BotSyncSingleToken, Token
from vkwave.longpoll import BotLongpoll, BotLongpollData


async def solve_captcha(captcha_link: str):
    result = input(f"Input captcha {captcha_link}:")
    return result


async def captcha_handler(error: dict, api_ctx: APIOptionsRequestContext):
    # not the greatest implementation, but you can make any

    method = error["error"]["request_params"][0]["value"]
    request_params = {
        param["key"]: param["value"]
        for param in error["error"]["request_params"]
        if param["key"] not in {"oauth", "v", "method"}
    }
    key = await solve_captcha(error["error"]["captcha_img"])

    request_params.update({"captcha_sid": error["error"]["captcha_sid"], "captcha_key": key})
    return await api_ctx.api_request(method, params=request_params)


# Easy way

bot = SimpleLongPollUserBot(tokens="MyToken")
bot.api_session.api.default_api_options.error_dispatcher.add_handler(14, captcha_handler)


# Not easy way


api_session = API(BotSyncSingleToken(Token("MyToken")), AIOHTTPClient())
api = api_session.get_context()
dp = Dispatcher(api_session, TokenStorage[GroupId]())
lp_extension = BotLongpollExtension(dp, BotLongpoll(api, BotLongpollData(123456789)))

api_session.default_api_options.error_dispatcher.add_handler(14, captcha_handler)
