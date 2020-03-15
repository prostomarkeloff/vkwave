from .base import BaseFilter
from vkwave_bots.dispatching.events.base import BaseEvent
from typing import List


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
