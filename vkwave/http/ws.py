from abc import ABC, abstractmethod
from asyncio import AbstractEventLoop as AEL, get_event_loop
from typing import Optional, AsyncGenerator

import aiohttp
from aiohttp import ClientSession


class AbstractWSClient(ABC):
    @abstractmethod
    async def connect(self, url: str):
        ...

    @abstractmethod
    async def stream_bytes(self) -> AsyncGenerator[None, bytes]:
        ...

    @abstractmethod
    async def stream_str(self) -> AsyncGenerator[None, str]:
        ...

    @abstractmethod
    async def stream_json(self) -> AsyncGenerator[None, dict]:
        ...

    @abstractmethod
    async def close(self):
        ...


class AIOHTTPWSClient(AbstractWSClient):
    def __init__(self, session: Optional[ClientSession] = None, loop: Optional[AEL] = None):
        self.loop = loop or get_event_loop()
        self.session = session or ClientSession(loop=self.loop)
        self._ws_conn: Optional[aiohttp.ClientWebSocketResponse] = None

    async def connect(self, url: str):
        self._ws_conn = self.session.ws_connect(url, autoping=False)

    async def stream_bytes(self) -> AsyncGenerator[None, bytes]:
        while True:
            msg = await self._ws_conn.receive()
            yield msg.data

    async def stream_str(self) -> AsyncGenerator[None, str]:
        while True:
            msg = await self._ws_conn.receive_str()
            yield msg

    async def stream_json(self) -> AsyncGenerator[None, dict]:
        while True:
            msg = await self._ws_conn.receive_json()
            yield msg

    async def close(self):
        if self._ws_conn and not self._ws_conn.closed:
            await self._ws_conn.close()
        await self.session.close()
