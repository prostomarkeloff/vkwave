import typing
from enum import Enum, auto

from typing_extensions import final

from .types import (
    ErrorHandlerCallable,
    MethodName,
    RequestCallbackCallable,
    SignalCallbackCallable,
)


async def _noop_error_handler(ctx: "RequestContext") -> None:
    """This handler does nothing. You should replace that."""


class RequestState(Enum):
    """State of request. Probably maybe useless in a lot of situtations but sometimes..."""

    NOT_SENT = auto()
    SENT = auto()


class ResultState(Enum):
    """
    State of result.
    You must check this before operating with values in (data, exception_data, exception)
    """

    NOTHING = auto()
    SUCCESS = auto()
    HANDLED_EXCEPTION = auto()
    UNHANDLED_EXCEPTION = auto()


class Signal(Enum):
    # when any exception is occurred (but after exception handlers)
    ON_EXCEPTION = auto()
    # when we are preparing to send request
    BEFORE_REQUEST = auto()
    # when we sent request and ran exception handler (if exception occurred)
    AFTER_REQUEST = auto()


class RequestContext:
    """
    Context of request. It is being returned from `create_request` function.
    Needed to work with request specified things.
    """

    def __init__(
        self,
        request_callback: RequestCallbackCallable,
        method_name: MethodName,
        request_params: dict,
        exceptions: typing.Optional[typing.Dict[typing.Type[Exception], None]] = None,
    ):
        """
        :param request_callback: callable thing that will be called on `ctx.send_request`.
        :param method_name: name of method
        :param request_params: request params
        :param exceptions: possible exceptions while calling `request_callback`.
         There are should be only client specified exceptions.

        """
        self.state: RequestState = RequestState.NOT_SENT

        self.request_callback = request_callback
        self.request_params = request_params
        self.method_name = method_name
        self.result = ResultContext()

        self._signals: typing.Dict[Signal, typing.List[SignalCallbackCallable]] = {
            Signal.ON_EXCEPTION: [],
            Signal.BEFORE_REQUEST: [],
            Signal.AFTER_REQUEST: [],
        }

        self._exception_handlers: typing.Dict[typing.Type[Exception], ErrorHandlerCallable] = {}

        if exceptions is None:
            exceptions = {}

        # set default handlers
        for exception in exceptions:
            self._exception_handlers[exception] = _noop_error_handler

    @final
    async def _handle_exception(self, exception: Exception) -> bool:
        handler = self._exception_handlers.get(type(exception))
        if handler and handler is not _noop_error_handler:
            await handler(self)
            return True
        return False

    def signal(self, signal: Signal, callback: SignalCallbackCallable) -> None:
        self._signals[signal].append(callback)

    async def _push_signal(self, signal: Signal) -> None:
        for callback in self._signals[signal]:
            await callback(self)

    def set_exception_handler(
        self, exception: typing.Type[Exception], handler: ErrorHandlerCallable,
    ) -> None:
        if not self._exception_handlers.get(exception):
            raise ValueError("Unallowed exception")
        self._exception_handlers[exception] = handler

    @final
    async def send_request(self) -> None:
        await self._push_signal(Signal.BEFORE_REQUEST)

        try:
            result = await self.request_callback(self.method_name, self.request_params)
            self.result.state = ResultState.SUCCESS
            self.result.data = result
        except Exception as exc:
            self.result.exception = exc
            if await self._handle_exception(exc):
                self.result.state = ResultState.HANDLED_EXCEPTION
            else:
                self.result.state = ResultState.UNHANDLED_EXCEPTION
            await self._push_signal(Signal.ON_EXCEPTION)

        self.state = RequestState.SENT
        await self._push_signal(Signal.AFTER_REQUEST)


class ResultContext:
    def __init__(self):
        self.state: ResultState = ResultState.NOTHING
        self._exception: typing.Optional[Exception] = None
        self._exception_data: typing.Optional[dict] = None
        self._data: typing.Optional[dict] = None

    @property
    def exception(self) -> typing.Optional[Exception]:
        """Exception raised during calling `request_callback`"""
        return self._exception

    @exception.setter
    def exception(self, exc: Exception) -> None:
        self._exception = exc

    @property
    def exception_data(self) -> typing.Optional[dict]:
        """Data is set by exception handler."""
        return self._exception_data

    @exception_data.setter
    def exception_data(self, data: dict) -> None:
        self._exception_data = data

    @property
    def data(self) -> typing.Optional[dict]:
        """Result of `request_callback`."""
        return self._data

    @data.setter
    def data(self, data: dict) -> None:
        self._data = data
