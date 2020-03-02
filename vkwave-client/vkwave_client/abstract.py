from abc import abstractmethod, ABC

from .types import MethodName
from .context import RequestContext

class AbstractAPIClient(ABC):
    @abstractmethod
    def create_request(self, method_name: MethodName, params: dict) -> RequestContext:
        ...

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()

    @abstractmethod
    async def close(self) -> None:
        """Close resources."""
