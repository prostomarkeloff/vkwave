import pytest

from vkwave.client.abstract import AbstractAPIClient
from vkwave.client.context import RequestContext, Signal
from vkwave.client.factory import AbstractFactory, DefaultFactory
from vkwave.client.types import MethodName


class SomeAPIException(Exception):
    pass


async def callback(method_name: MethodName, params: dict) -> dict:
    if raise_exception := params.pop("raise_exception"):
        raise SomeAPIException()
    else:
        return params


@pytest.fixture
def client():



    class TestAPIClient(AbstractAPIClient):
        def __init__(self):
            self._factory = DefaultFactory()

        @property
        def context_factory(self) -> AbstractFactory:
            return self._factory

        def set_context_factory(self, factory: AbstractFactory) -> None:
            self._factory = factory

        def create_request(self, method_name: MethodName, params: dict) -> RequestContext:
            return self.context_factory.create_context(
                exceptions={SomeAPIException: None},
                request_callback=callback,
                request_params=params,
                method_name=method_name,
            )

        async def close(self):
            pass


    return TestAPIClient()


@pytest.mark.asyncio
async def test_with_exception(client):
    async def exception_handler(ctx: RequestContext):
        # it's called anymore
        assert 1
        ctx.result.exception_data = {"me": "alive"}

    ctx = client.create_request(
        "anymethod", {"raise_exception": True, "something": "yes, of course"}
    )

    # we can't set exception handler(s) for unknown exceptions
    with pytest.raises(ValueError):
        ctx.set_exception_handler(RuntimeError, exception_handler)

    ctx.set_exception_handler(SomeAPIException, exception_handler)

    await ctx.send_request()

    assert ctx.result.exception_data == {"me": "alive"}
    assert ctx.result.data is None
    assert isinstance(ctx.result.exception, SomeAPIException)


@pytest.mark.asyncio
async def test_without_exception(client):
    ctx = client.create_request("anymethod", {"raise_exception": False, "hi": "there"})

    await ctx.send_request()

    assert ctx.result.exception is None
    assert ctx.result.exception_data is None
    assert ctx.result.data == {"hi": "there"}


@pytest.mark.asyncio
async def test_signals(client):
    async def signal(ctx: RequestContext):
        assert 1
        ctx.result.exception_data = {"captured": "by signal"}

    ctx = client.create_request("anymethod", {"raise_exception": True})
    ctx.signal(Signal.ON_EXCEPTION, signal)

    await ctx.send_request()

    assert ctx.result.exception is not None
    assert ctx.result.exception_data["captured"] == "by signal"
    assert ctx.result.data is None


@pytest.mark.asyncio
async def test_no_http_client(client):
    with pytest.raises(NotImplementedError):
        client.http_client
