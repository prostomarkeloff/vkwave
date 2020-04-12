from typing import Any, Callable, List, Optional, TypeVar, cast

from .caster import AbstractCaster

IT = TypeVar("IT")
T = TypeVar("T")


class DefaultCaster(AbstractCaster[IT]):
    def __init__(self):
        self._user_casts: List[Callable[[Any], IT]] = []

    def add_caster(self, handler: Callable[[Any], IT]):
        self._user_casts.append(handler)

    def from_casters(self, something: Any) -> Optional[IT]:
        for handler in self._user_casts:
            result = handler(something)
            if result is not None:
                return result
        return None
