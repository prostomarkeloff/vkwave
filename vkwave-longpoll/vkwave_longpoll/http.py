from abc import ABC, abstractmethod
from typing import Optional
from aiohttp import ClientSession
from asyncio import AbstractEventLoop as AEL, get_event_loop

class AbstractHTTPClient(ABC):
    @abstractmethod
    async def request(self, method: str, url: str, data: Optional[dict] = None) -> dict:
        ...

class AIOHTTPClient(AbstractHTTPClient):
    def __init__(self, loop: Optional[AEL] = None):
        self.loop = loop or get_event_loop()
        self.session = ClientSession(loop=self.loop)

    async def request(self, method: str, url: str, data: Optional[dict] = None) -> dict:
        data = data or {}

        async with self.session.request(method, url, data=data) as resp:
            return await resp.json()
