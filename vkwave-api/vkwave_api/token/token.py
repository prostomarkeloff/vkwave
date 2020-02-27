"""
Working with API tokens.
"""
import random

from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import NewType

Token = NewType("Token", str)


class TokenType(Enum):
    USER = auto()
    BOT = auto()

# TODO: to consider about `get_token_async`.
class ABCToken(ABC):
    """
    This class represents abstract token subject.
    You should inherit from it if you want to create own abstraction over token.
    """

    typeof: TokenType

    @abstractmethod
    def get_token(self, *args, **kwargs) -> Token:
        """
        Return the 'str' representation of token.
        """

class SingleUserToken(ABCToken):

    typeof = TokenType.USER

    def __init__(self, token: Token):
        self._token = token

    def get_token(self, *args, **kwargs) -> Token:
        return self._token
