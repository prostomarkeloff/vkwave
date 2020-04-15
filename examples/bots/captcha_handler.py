# Easy bot imports
from vkwave.bots.easy import SimpleLongPollBot
from vkwave.api.methods import APIOptionsRequestContext


# Ordinary bot imports
from vkwave.client.default import AIOHTTPClient
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.bots.core.tokens.storage import TokenStorage
from vkwave.bots.core.dispatching.dp.dp import Dispatcher
from vkwave.bots.core.dispatching.extensions.longpoll_bot import BotLongpollExtension
from vkwave.bots.core.tokens.types import GroupId
from vkwave.api.methods import API
from vkwave.longpoll.bot import BotLongpoll, BotLongpollData


async def solve_captcha(captcha_link: str):
    result = input(f"Input captcha {captcha_link}:")
    return result


async def captcha_handler(error: dict, api_ctx: APIOptionsRequestContext):
    # not the greatest implementation, but you can make any

    method = None
    request_params = {}
    for param in error["error"]["request_params"]:
        if param["key"] == "method":
            method = param["value"]
            continue
        if param["key"] in ("oauth", "v"):
            continue
        request_params[param["key"]] = param["value"]

    captcha_img = error["error"]["captcha_img"]
    captcha_sid = error["error"]["captcha_sid"]

    key = await solve_captcha(captcha_img)

    request_params.update({"captcha_sid": captcha_sid, "captcha_key": key})

    await eval(f"api_ctx.{method}(**request_params)")


# Easy way

bot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)
bot.api_session.default_api_options.error_dispatcher.add_handler(14, captcha_handler)


# Not easy way


api_session = API(BotSyncSingleToken(Token("MyToken")), AIOHTTPClient())
api = api_session.get_context()
dp = Dispatcher(api_session, TokenStorage[GroupId]())
lp_extension = BotLongpollExtension(dp, BotLongpoll(api, BotLongpollData(123456789)))

api_session.default_api_options.error_dispatcher.add_handler(14, captcha_handler)




