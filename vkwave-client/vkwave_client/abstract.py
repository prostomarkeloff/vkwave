from abc import abstractmethod, ABC

from .types import MethodName
from .context import RequestContext


class AbstractAPIClient(ABC):
    @abstractmethod
    def create_request(self, method_name: MethodName, **params) -> RequestContext:
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close resources."""
