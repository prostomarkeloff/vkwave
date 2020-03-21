from abc import ABC, abstractmethod
from asyncio import AbstractEventLoop as AEL
from asyncio import get_event_loop
from typing import Optional

from aiohttp import ClientSession


class AbstractHTTPClient(ABC):
    @abstractmethod
    async def request(self, method: str, url: str, data: Optional[dict] = None) -> dict:
        ...

    @abstractmethod
    async def close(self):
        ...


class AIOHTTPClient(AbstractHTTPClient):
    def __init__(self, session: Optional[ClientSession] = None, loop: Optional[AEL] = None):
        self.loop = loop or get_event_loop()
        self.session = ClientSession(loop=self.loop)

    async def close(self):
        await self.session.close()

    async def request_text(self, method: str, url: str, data: Optional[dict] = None) -> str:
        data = data or {}

        async with self.session.request(method, url, data=data) as resp:
            return await resp.text()

    async def request_json(self, method: str, url: str, data: Optional[dict] = None) -> dict:
        data = data or {}

        async with self.session.request(method, url, data=data) as resp:
            return await resp.json()
