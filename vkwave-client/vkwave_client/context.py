from enum import auto, Enum
from .types import MethodName, ErrorHandlerCallable, RequestCallbackCallable
from typing_extensions import final

import typing


async def _noop_error_handler(err: Exception, ctx: "ResultContext") -> None:
    pass


class RequestState(Enum):
    NOT_SENT = auto()
    SENT = auto()


class ResultState(Enum):
    NOTHING = auto()
    SUCCESS = auto()
    HANDLED_EXCEPTION = auto()
    UNHANDLED_EXCEPTION = auto()


class RequestContext:
    def __init__(
        self,
        request_callback: RequestCallbackCallable,
        method_name: MethodName,
        request_params: dict,
        exceptions: typing.Optional[typing.Dict[typing.Type[Exception], None,]] = None,
    ):
        self.state: RequestState = RequestState.NOT_SENT

        self._request_callback = request_callback
        self._request_params = request_params
        self._method_name = method_name
        self.result = ResultContext()

        self._exception_handlers: typing.Dict[
            typing.Type[Exception], ErrorHandlerCallable
        ] = {}

        if exceptions is None:
            exceptions = {}
        for exception in exceptions:
            self._exception_handlers[exception] = _noop_error_handler

    @final
    async def _handle_exception(self, exception: Exception) -> bool:
        handler = self._exception_handlers[type(exception)]
        if handler is not _noop_error_handler:
            await handler(exception, self.result)
            return True
        return False

    def set_exception_handler(
        self, exception: typing.Type[Exception], handler: ErrorHandlerCallable,
    ) -> None:
        if not self._exception_handlers.get(exception):
            raise ValueError("Unallowed exception")
        self._exception_handlers[exception] = handler

    @final
    async def send_request(self) -> None:
        try:
            result = await self._request_callback(
                self._method_name, self._request_params
            )
            self.result.state = ResultState.SUCCESS
            self.result.data = result
        except Exception as exc:
            self.result.exception = exc
            if await self._handle_exception(exc):
                self.result.state = ResultState.HANDLED_EXCEPTION
            else:
                self.result.state = ResultState.UNHANDLED_EXCEPTION
        self.state = RequestState.SENT


class ResultContext:
    def __init__(self):
        self.state: ResultState = ResultState.NOTHING
        self._exception: typing.Optional[Exception] = None
        self._exception_data: typing.Optional[dict] = None
        self._data: typing.Optional[dict] = None

    @property
    def exception(self) -> typing.Optional[Exception]:
        return self._exception

    @exception.setter
    def exception(self, exc: Exception) -> None:
        self._exception = exc

    @property
    def exception_data(self) -> typing.Optional[dict]:
        return self._exception_data

    @exception_data.setter
    def exception_data(self, data: dict) -> None:
        self._exception_data = data

    @property
    def data(self) -> typing.Optional[dict]:
        return self._data

    @data.setter
    def data(self, data: dict) -> None:
        self._data = data
