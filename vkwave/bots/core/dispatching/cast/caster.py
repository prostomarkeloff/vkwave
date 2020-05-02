from abc import ABC
from abc import abstractmethod as abm
from typing import Any, Callable, Generic, Optional, TypeVar

IT = TypeVar("IT")  # input type
T = TypeVar("T")


class AbstractCaster(ABC, Generic[IT]):
    @abm
    def from_casters(self, something: Any) -> Optional[IT]:
        ...

    def cast(self, something: Any) -> IT:
        result = self.from_casters(something) or self.default(something)
        if result is None:
            raise NotImplementedError("There is not cast for this object")
        return result

    @abm
    def default(self, something: Any) -> Optional[IT]:
        ...

    @abm
    def add_caster(self, handler: Callable[[Any], IT]):
        ...
