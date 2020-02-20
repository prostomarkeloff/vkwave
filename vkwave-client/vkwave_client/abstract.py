import typing
from abc import abstractmethod, ABC

from typing_extensions import final

from .types import MethodName
from .context import RequestContext


class AbstractAPIClient(ABC):
    @abstractmethod
    def request(self, method_name: MethodName, **params) -> RequestContext:
        ...

    @abstractmethod
    async def request_callback(self, method_name: MethodName, params: dict) -> dict:
        """
        Send request to something and return dict.
        Can raise exceptions.
        """

    @abstractmethod
    async def close(self) -> None:
        """Close resources."""
