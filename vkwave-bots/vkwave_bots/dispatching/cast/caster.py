from abc import ABC, abstractmethod as abm
from typing import Generic, TypeVar, Any, Type, Callable

IT = TypeVar("IT")  # input type
T = TypeVar("T")


class AbstractCaster(ABC, Generic[IT]):
    @abm
    def cast(self, something: Any) -> IT:
        ...

    @abm
    def add_caster(self, typeof: Type[T], handler: Callable[[Any], IT]):
        ...
