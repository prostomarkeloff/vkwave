from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

from vkwave.api.methods._abc import APIOptionsRequestContext
from vkwave.bots.core.types.bot_type import BotType
from vkwave.types.bot_events import BaseBotEvent
from vkwave.types.user_events import BaseUserEvent

T = TypeVar("T")


class BaseEvent(ABC, Generic[T]):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(bot_type={self.bot_type}, object={self.object}, api_ctx={self.api_ctx})"

    @abstractmethod
    def __setitem__(self, key: Any, item: Any) -> None:
        ...

    @abstractmethod
    def __getitem__(self, key: Any) -> Any:
        ...

    @property
    @abstractmethod
    def bot_type(self) -> BotType:
        ...

    @property
    @abstractmethod
    def object(self) -> T:
        ...

    @property
    @abstractmethod
    def api_ctx(self) -> APIOptionsRequestContext:
        ...


class Event(BaseEvent[T]):
    def __init__(self):
        self._user_data: Dict[Any, Any] = {}

    @property
    def user_data(self):
        return self._user_data

    @user_data.setter
    def user_data(self, value: Dict[Any, Any]):
        self._user_data = value

    def __setitem__(self, key: Any, item: Any) -> None:
        self._user_data[key] = item

    def __getitem__(self, key: Any) -> Any:
        return self._user_data[key]


class UserEvent(Event[BaseUserEvent]):
    def __init__(self, object: BaseUserEvent, api_ctx: APIOptionsRequestContext):
        super().__init__()
        self._bot_type = BotType.USER
        self._object = object
        self._api_ctx = api_ctx

    @property
    def bot_type(self) -> BotType:
        return self._bot_type

    @property
    def object(self) -> BaseUserEvent:
        return self._object

    @property
    def api_ctx(self) -> APIOptionsRequestContext:
        return self._api_ctx


class BotEvent(Event[BaseBotEvent]):
    def __init__(self, object: BaseBotEvent, api_ctx: APIOptionsRequestContext):
        super().__init__()
        self._bot_type = BotType.BOT
        self._object = object
        self._api_ctx = api_ctx

    @property
    def bot_type(self) -> BotType:
        return self._bot_type

    @property
    def object(self) -> BaseBotEvent:
        return self._object

    @property
    def api_ctx(self) -> APIOptionsRequestContext:
        return self._api_ctx
