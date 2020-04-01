import typing

if typing.TYPE_CHECKING:
    pass

ErrorHandlerCallable = typing.Callable[["RequestContext"], typing.Awaitable[None]]

MethodName = typing.NewType("MethodName", str)
RequestCallbackCallable = typing.Callable[[MethodName, dict], typing.Awaitable[dict]]
SignalCallbackCallable = typing.Callable[["RequestContext"], typing.Awaitable[None]]
