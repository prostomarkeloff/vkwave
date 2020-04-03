from vkwave.api.methods import API
from vkwave.api.methods import APIOptionsRequestContext
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.client.default import AIOHTTPClient


def create_bot_aiohttp(token: str) -> APIOptionsRequestContext:
    # javamustdie
    client = AIOHTTPClient()
    token = BotSyncSingleToken(Token(token))
    api = API(clients=client, tokens=token)
    return api.get_context()
