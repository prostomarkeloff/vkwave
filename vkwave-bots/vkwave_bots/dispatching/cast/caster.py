from abc import ABC
from abc import abstractmethod as abm
from typing import Any, Callable, Generic, Type, TypeVar

IT = TypeVar("IT")  # input type
T = TypeVar("T")


class AbstractCaster(ABC, Generic[IT]):
    @abm
    def cast(self, something: Any) -> IT:
        ...

    @abm
    def add_caster(self, typeof: Type[T], handler: Callable[[Any], IT]):
        ...
