from vkwave_bots.dispatching.events.base import BaseEvent
from vkwave_bots_fsm.fsm import State, ForWhat, FiniteStateMachine

from vkwave_bots.dispatching.filters.base_filters import BaseFilter, FilterResult


class FsmFilter(BaseFilter):
    def __init__(self, fsm: FiniteStateMachine, state: State, for_what: ForWhat):
        self.fsm = fsm
        self.state_title = state.title
        self.for_what = for_what

    async def check(self, event: BaseEvent) -> FilterResult:
        current_state = await self.fsm.get_data(event, for_what=self.for_what)
        return FilterResult(current_state["__vkwave_fsm_state__"] == self.state_title)
