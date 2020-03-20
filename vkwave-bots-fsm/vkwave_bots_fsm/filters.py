from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots_fsm.fsm import State, ForWhat, FiniteStateMachine

from vkwave_bots.dispatching.filters.base_filters import BaseFilter, FilterResult


class StateFilter(BaseFilter):
    def __init__(self, fsm: FiniteStateMachine, state: State, for_what: ForWhat, always_false: bool = False):
        self.always_false = always_false
        self.fsm = fsm
        self.state = state
        self.for_what = for_what

    async def check(self, event: BaseEvent) -> FilterResult:
        if self.always_false:
            return FilterResult(False)
        current_state = await self.fsm.get_data(event, for_what=self.for_what)
        return FilterResult(current_state["__vkwave_fsm_state__"] == str(self.state))
