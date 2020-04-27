from abc import ABC, abstractmethod
from typing import Dict

from vkwave.bots.core.tokens.types import GroupId


class AbstractGetConfirmationStrategy(ABC):
    @abstractmethod
    async def get_confirmation(self, group_id: GroupId) -> str:
        ...


class NotImplementedGetConfirmationStrategy(AbstractGetConfirmationStrategy):
    async def get_confirmation(self, group_id: GroupId) -> str:
        raise NotImplementedError


class ConfirmationStorage:
    def __init__(self):
        self.confirmations: Dict[GroupId, str] = {}
        self.strategy: AbstractGetConfirmationStrategy = NotImplementedGetConfirmationStrategy()

    def add_confirmation(self, group_id: GroupId, confirmation: str):
        self.confirmations[group_id] = confirmation

    async def get_confirmation(self, group_id: GroupId) -> str:
        cached = self.confirmations.get(group_id)
        if cached:
            return cached
        confirmation = await self.strategy.get_confirmation(group_id)
        self.add_confirmation(group_id, confirmation)
        return confirmation
