from abc import abstractmethod, ABC

import typing
import types


class AbstractHTTPClient(ABC):

    API_URL = "https://api.vk.com/method/{method_name}"

    @abstractmethod
    async def request(self, method_name: str, **kwargs) -> dict:
        """
        Send request to VK.
        Returns dict even if it contains error.
        """
        # TODO: custom errors for this kind of errors (connection errors, timeout, etc.)
