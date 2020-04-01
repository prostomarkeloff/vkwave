from typing import Any, Callable, TypeVar, Dict, cast

from .caster import AbstractCaster

IT = TypeVar("IT")
T = TypeVar("T")


class DefaultCaster(AbstractCaster[IT]):
    def __init__(self):
        self._user_casts: Dict[T, Callable[[Any], IT]] = {}

    def add_caster(self, typeof: T, handler: Callable[[Any], IT]):
        self._user_casts[typeof] = handler

    def cast(self, something: Any) -> IT:  # type: ignore
        cb: IT

        typeof = type(something)
        av_cast = self._user_casts.get(typeof)
        if av_cast:
            av_cast = cast(Callable[[Any], IT], av_cast)
            cb = av_cast(something)
            return cb
