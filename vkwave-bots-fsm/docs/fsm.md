# vkwave-bots-fsm

This module is implementation of [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
for bots

fsm divides user states, chat states and user in chat states,
for selecting one of the above options you can set ```for_what```
argument in fsm methods.

```python3
from vkwave_bots_fsm.fsm import FiniteStateMachine, State, ForWhat
from vkwave_bots_fsm.filter import FsmFilter

fsm = FiniteStateMachine()
router = DefaultRouter()

class MyState:
    name = State("name")
    age = State("age")


@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "start",
    EventTypeFilter(BotEventType.MESSAGE_NEW.value),
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


@router.registrar.with_decorator(
    FsmFilter(fsm=fsm, state=MyState.name, for_what=ForWhat.FOR_USER),
    EventTypeFilter(BotEventType.MESSAGE_NEW),
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(
        event=event,
        state=MyState.age,
        for_what=ForWhat.FOR_USER,
        extra_state_data={"name": event.object.object.message.text},
    )

    return f"Input your age"


@router.registrar.with_decorator(
    FsmFilter(fsm=fsm, state=MyState.age, for_what=ForWhat.FOR_USER),
    EventTypeFilter(BotEventType.MESSAGE_NEW),
)
async def simple_handler(event: BotEvent):
    if not event.object.object.message.text.isdigit():
        return f"Only digits!"
    await fsm.add_data(
        event=event,
        for_what=ForWhat.FOR_USER,
        state_data={"age": event.object.object.message.text},
    )
    user_data = await fsm.get_data(event=event, for_what=ForWhat.FOR_USER)
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return f"Your data - {user_data}"
```

It returns smth like
```
Your data - {'__vkwave_fsm_state__': '<vkwave_bots_fsm.fsm.State object at 0x0000021C19D61A90>', 'name': 'Nick', 'age': '46'}
```