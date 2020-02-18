from abc import abstractmethod, ABC
from typing_extensions import Final

import typing

MethodName = typing.NewType("MethodName", str)


class AbstractHTTPClient(ABC):

    API_URL: Final = "https://api.vk.com/method/{method_name}"

    @abstractmethod
    async def request(self, method_name: MethodName, **kwargs) -> dict:
        """
        Sends request to VK.
        Returns dict even if it contains error.
        """

    # TODO: custom errors for this kind of errors (connection errors, timeout, etc.)

    @abstractmethod
    async def close(self) -> None:
        """
        Closes resources.
        """
