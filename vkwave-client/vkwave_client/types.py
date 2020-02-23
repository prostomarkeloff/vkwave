import typing

if typing.TYPE_CHECKING:
    from .context import ResultContext

ErrorHandlerCallable = typing.Callable[
    [Exception, "ResultContext"], typing.Awaitable[None]
]

MethodName = typing.NewType("MethodName", str)
RequestCallbackCallable = typing.Callable[[MethodName, dict], typing.Awaitable[dict]]
