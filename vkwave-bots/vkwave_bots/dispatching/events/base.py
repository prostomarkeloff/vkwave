from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Dict

from vkwave_bots.types.bot_type import BotType
from vkwave_types.bot_events import BaseBotEvent
from vkwave_types.user_events import BaseUserEvent
from vkwave_api.methods._abc import APIOptionsRequestContext

T = TypeVar("T")


class BaseEvent(ABC, Generic[T]):
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
        self.__user_data: Dict[Any, Any] = {}

    def __setitem__(self, key: Any, item: Any) -> None:
        self.__user_data[key] = item

    def __getitem__(self, key: Any) -> Any:
        return self.__user_data[key]


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
