from typing import List

from vkwave.bots.core.dispatching.events.base import BaseEvent

from .base import BaseFilter


class FilterManager:
    def __init__(self):
        self.filters: List[BaseFilter] = []

    def add_filter(self, filter: BaseFilter):
        self.filters.append(filter)

    async def execute_filters(self, event: BaseEvent) -> bool:
        """Return true if all filters succeed."""
        result: bool = True
        for filter in self.filters:
            f_result = await filter.check(event)
            if not f_result:
                return False
        return result
