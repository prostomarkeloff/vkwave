from abc import ABC, abstractmethod


class BaseTwoAuth(ABC):
    @abstractmethod
    async def get_code(self) -> int:
        ...
