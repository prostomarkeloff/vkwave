from asyncio import iscoroutinefunction
from inspect import isawaitable, isfunction
from typing import Any, cast

from vkwave_bots.dispatching.cast.default import DefaultCaster

from .callback import AsyncFuncCallback, BaseCallback, SyncFuncCallback


class CallbackCaster(DefaultCaster[BaseCallback]):
    def cast(self, something: Any) -> BaseCallback:
        av_cast = super().cast(something)
        if av_cast:
            return av_cast

        cb: BaseCallback
        if iscoroutinefunction(something) or isawaitable(something):
            cb = AsyncFuncCallback(something)
            return cb
        if isfunction(something):
            cb = SyncFuncCallback(something)
            return cb
        if isinstance(something, str):
            return SyncFuncCallback(lambda event: something)

        raise NotImplementedError("There is no cast for this type")


caster = CallbackCaster()
