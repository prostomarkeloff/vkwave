from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.bots.core.dispatching.filters.builtin import BaseFilter, FilterResult
from vkwave.bots.fsm.fsm import FiniteStateMachine, ForWhat, State
from vkwave.bots.storage.types import Key

ANY_STATE = "__any_state__"


class StateFilter(BaseFilter):
    def __init__(
        self, fsm: FiniteStateMachine, state: State, for_what: ForWhat, always_false: bool = False,
    ):
        self.always_false = always_false
        self.fsm = fsm
        self.state = state
        self.for_what = for_what

    async def check(self, event: BaseEvent) -> FilterResult:
        if self.state == ANY_STATE:
            return FilterResult(True)
        if self.always_false:
            from_id = event.object.object.message.from_id
            peer_id = event.object.object.message.peer_id
            template = "__vkwave_{for_what}_{peer_id}_{from_id}__"
            is_pm = from_id == peer_id

            user_in_chat_state = template.format(
                for_what="userInChat", peer_id=peer_id, from_id=from_id
            )
            if is_pm:
                user_state = template.format(for_what="user", peer_id=from_id, from_id=from_id)
            else:
                user_state = template.format(for_what="chat", peer_id=peer_id, from_id=peer_id)

            return FilterResult(
                not (
                    await self.fsm.storage.contains(Key(user_in_chat_state))
                    or await self.fsm.storage.contains(Key(user_state))
                )
            )
        current_state = await self.fsm.get_data(event, for_what=self.for_what)
        return FilterResult(
            current_state is not None and current_state["__vkwave_fsm_state__"] == str(self.state)
        )
