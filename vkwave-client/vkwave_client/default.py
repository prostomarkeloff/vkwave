"""
Default implementation of HTTPClient for vkwave-client.
"""

from aiohttp import ClientSession
from asyncio import get_event_loop, AbstractEventLoop

from .abstract import AbstractHTTPClient, MethodName

from typing import Optional


class AIOHTTPClient(AbstractHTTPClient):
    def __init__(
        self,
        session: Optional[ClientSession] = None,
        loop: Optional[AbstractEventLoop] = None,
    ):
        self._loop = loop or get_event_loop()
        self._session = session or ClientSession(loop=self._loop)

    async def request(self, method_name: MethodName, **kwargs) -> dict:
        async with self._session.post(
            self.API_URL.format(method_name=method_name), data=kwargs
        ) as resp:
            return await resp.json()

    async def close(self) -> None:
        await self._session.close()
