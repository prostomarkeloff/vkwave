import typing
from enum import Enum, auto

if typing.TYPE_CHECKING:
    from ._abc import APIOptionsRequestContext

Error = typing.NewType("Error", dict)
ErrorHandlerCallable = typing.Callable[
    [Error, "APIOptionsRequestContext"],
    typing.Union[typing.Awaitable[None], typing.Awaitable[dict]],
]

# errors when we return result of error handler to the place when error occurred
RETURN_RESULT_ERRORS = [1, 6, 14]


# 1: something went wrong (try later)
# 6: too many requests (wait a little time and send request)
# 14: captcha (user's captcha handler)

# user also can add own errors to this list


class ReturnInfo(Enum):
    """Info about returning something from handler or no"""

    RETURN = auto()
    NORETURN = auto()


def get_return_info(code: int) -> ReturnInfo:
    if code in RETURN_RESULT_ERRORS:
        return ReturnInfo.RETURN
    return ReturnInfo.NORETURN


class UnsuccessAPIRequestException(Exception):
    """When ctx.result.state is not SUCCESS"""


class APIError(Exception):
    def __init__(self, code: int, message: str, request_params: dict):
        self.code = code
        self.text = message
        self.request_params = request_params
        self.message = f"[{code}] {message}"
        super().__init__(self.message)


_NO_DEFAULT_HANDLER = object()


async def _noop_default_handler(error: Error, ctx: "APIOptionsRequestContext"):
    return _NO_DEFAULT_HANDLER


class ErrorDispatcher:
    def __init__(self):
        self.handlers: typing.Dict[int, ErrorHandlerCallable] = {}
        self.default_error_handler: ErrorHandlerCallable = _noop_default_handler

    def add_handler(self, code: int, handler: ErrorHandlerCallable):
        self.handlers[code] = handler

    def set_default_error_handler(self, handler: ErrorHandlerCallable):
        self.default_error_handler = handler

    async def _run_handler(
        self,
        code: int,
        error: Error,
        return_info: ReturnInfo,
        request_context: "APIOptionsRequestContext",
    ) -> typing.Union[bool, typing.Optional[dict]]:
        handler = self.handlers.get(code)
        if not handler:
            result = await self.default_error_handler(error, request_context)
            if result is _NO_DEFAULT_HANDLER:
                return False
        handler = typing.cast(ErrorHandlerCallable, handler)
        result = await handler(error, request_context)

        if return_info is ReturnInfo.RETURN:
            return result

        return None

    async def process_error(
        self, error: Error, request_context: "APIOptionsRequestContext"
    ) -> typing.Optional[dict]:
        err = error["error"]
        code = err["error_code"]
        return_info = get_return_info(code)

        result = await self._run_handler(code, error, return_info, request_context)
        if return_info is ReturnInfo.RETURN:
            result = typing.cast(dict, result)
            return result

        raise APIError(code, err["error_msg"], err["request_params"])
