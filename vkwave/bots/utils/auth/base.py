from abc import ABC, abstractmethod

from typing import Optional
from .types import OAuthResponse


class BaseAuth(ABC):
    @abstractmethod
    async def auth(
        self,
        login: str,
        password: str,
        two_auth: bool = False,
        two_auth_code: Optional[int] = None
    ) -> OAuthResponse:
        ...
