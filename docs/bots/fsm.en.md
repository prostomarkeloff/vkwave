# FSM

This module implements [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) for bots.


FSM splits user's states, states of chats and states of user in chat, to select one of them you must pass argument `for_what` in FSM's methods.


State of one user in private chats - `ForWhat.FOR_USER`

State of chat - `ForWhat.FOR_CHAT`

State of one user in multi-user chats - `ForWhat.FOR_USER_IN_CHAT`


To choose handlers without `StateFilter` may be selected correctly, you should set default set.

```python
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
```

Example poll with asking name and age.

```python
from vkwave.bots import EventTypeFilter, BotEvent
from vkwave.types.bot_events import BotEventType
from vkwave.bots.fsm import FiniteStateMachine, StateFilter, ForWhat, State, ANY_STATE

fsm = FiniteStateMachine()
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
router.registrar.add_default_filter(EventTypeFilter(BotEventType.MESSAGE_NEW.value))  # we don't want to write it in all handlers.


class MyState:
    name = State("name")
    age = State("age")


# starting poll
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "start",
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


#  exiting from poll (works on any state)
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "exit",
    StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER)
)
async def simple_handler(event: BotEvent):
    # Check if we have the user in database
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return "You are quited!"


@router.registrar.with_decorator(
    StateFilter(fsm=fsm, state=MyState.name, for_what=ForWhat.FOR_USER),
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(
        event=event,
        state=MyState.age,
        for_what=ForWhat.FOR_USER,
        extra_state_data={"name": event.object.object.message.text},
    )
    # extra_state_data works as fsm.add_data(..., state_data={"name": event.object.object.message.text})

    return "Input your age"


@router.registrar.with_decorator(
    StateFilter(fsm=fsm, state=MyState.age, for_what=ForWhat.FOR_USER),
)
async def simple_handler(event: BotEvent):
    if not event.object.object.message.text.isdigit():
        return f"Please, send only positive numbers!"
    await fsm.add_data(
        event=event,
        for_what=ForWhat.FOR_USER,
        state_data={"age": event.object.object.message.text},
    )
    user_data = await fsm.get_data(event=event, for_what=ForWhat.FOR_USER)
 
    # finish poll and delete the user
    # `fsm.finish` will do it
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return f"Your data - {user_data}"
```

You will get somthing like this:
```
Your data - {'__vkwave_fsm_state__': '<vkwave.bots_fsm.fsm.State object at 0x0000021C19D61A90>', 'name': 'Nick', 'age': '46'}
```
