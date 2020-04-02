"""
Default implementation of HTTPClient for vkwave-client.
"""

from asyncio import AbstractEventLoop
from json import JSONDecodeError
from logging import getLogger
from typing import Optional

from aiohttp import ClientConnectionError, ClientSession
from typing_extensions import Final

from vkwave.http import AbstractHTTPClient
from vkwave.http import AIOHTTPClient as AHC_H

from .abstract import AbstractAPIClient
from .context import RequestContext, Signal
from .factory import AbstractFactory, DefaultFactory
from .types import MethodName

logger = getLogger(__name__)


async def _logging_signal_before_request(ctx: RequestContext):
    logger.debug(
        f"Doing request to '{ctx.method_name}' method with these params: {ctx.request_params}"
    )


class AIOHTTPClient(AbstractAPIClient):
    API_URL: Final = "https://api.vk.com/method/{method_name}"

    def __init__(
        self, session: Optional[ClientSession] = None, loop: Optional[AbstractEventLoop] = None,
    ):
        self._http_client = AHC_H(session=session, loop=loop)
        self._factory: AbstractFactory = DefaultFactory()

    @property
    def http_client(self) -> AbstractHTTPClient:
        return self._http_client

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
        return await self._http_client.request_json(
            "POST", self.API_URL.format(method_name=method_name), data=params
        )

    async def close(self) -> None:
        logger.debug("Closing aiohttp session...")
        await self.http_client.close()
