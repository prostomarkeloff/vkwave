"""
Default implementation of HTTPClient for vkwave-client.
"""

from asyncio import get_event_loop, AbstractEventLoop
from typing import Optional
from logging import getLogger
from json import JSONDecodeError

from typing_extensions import Final
from aiohttp import ClientSession
from aiohttp import ClientConnectionError

from .abstract import AbstractAPIClient
from .types import MethodName
from .context import RequestContext, Signal
from .factory import AbstractFactory, DefaultFactory

logger = getLogger(__name__)


async def _logging_signal_before_request(ctx: RequestContext):
    logger.debug(
        f"Doing request to '{ctx.method_name}' method with these params: {ctx.request_params}"
    )


class AIOHTTPClient(AbstractAPIClient):

    API_URL: Final = "https://api.vk.com/method/{method_name}"

    def __init__(
        self,
        session: Optional[ClientSession] = None,
        loop: Optional[AbstractEventLoop] = None,
    ):
        self._loop = loop or get_event_loop()
        self._session = session or ClientSession(loop=self._loop)
        self._factory: AbstractFactory = DefaultFactory()

    @property
    def context_factory(self) -> AbstractFactory:
        return self._factory

    def set_context_factory(self, factory: AbstractFactory) -> None:
        self._factory = factory

    def create_request(self, method_name: MethodName, params: dict) -> RequestContext:
        ctx = self.context_factory.create_context(
            request_callback=self.request_callback,
            method_name=method_name,
            request_params=params,
            exceptions={ClientConnectionError: None, JSONDecodeError: None},
        )
        ctx.signal(Signal.BEFORE_REQUEST, _logging_signal_before_request)
        return ctx

    async def request_callback(self, method_name: MethodName, params: dict) -> dict:
        async with self._session.post(
            self.API_URL.format(method_name=method_name), data=params
        ) as resp:
            return await resp.json()

    async def close(self) -> None:
        logger.debug("Closing aiohttp session...")
        await self._session.close()
