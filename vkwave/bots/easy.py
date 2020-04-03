from vkwave.api.methods import API
from vkwave.api.token.token import BotSyncSingleToken, Token
from vkwave.client.default import AIOHTTPClient


class _APIContextManager:
    def __init__(self, token: str):
        self.client = AIOHTTPClient()
        self.token = BotSyncSingleToken(Token(token))
        self.api = API(clients=self.client, tokens=self.token)

    async def __aenter__(self):
        return self.api.get_context()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.client.close()


def create_bot_aiohttp(token: str) -> _APIContextManager:
    return _APIContextManager(token)
