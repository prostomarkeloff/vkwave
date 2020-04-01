# FSM

This module is implementation of [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
for bots.

FSM divides user states, chat states and user in chat states,
for selecting one of these options you can choose `for_what` argument in fsm methods.

One user in personal message - `ForWhat.FOR_USER`

State for all chat - `ForWhat.FOR_CHAT`

For one user in chat - `ForWhat.FOR_USER_IN_CHAT`

Event state's set already, handlers without `StateFilter` may be chosen. We will fix it via default filter that returns `False` if any state exists.
```python
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
```

Example of simple interview with asking name and age of user.

```python
fsm = FiniteStateMachine()
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
router.registrar.add_default_filter(EventTypeFilter(BotEventType.MESSAGE_NEW.value))  # we don't want to write it in all handlers.


class MyState:
    name = State("name")
    age = State("age")


# starting interview (has default filter that will reject messages if state exists)
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "start",
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


#  exiting interview (work with any state because of `state=ANY_STATE`)
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "exit",
    StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER)
)
async def simple_handler(event: BotEvent):
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
    # extra_state_data is totally equal to fsm.add_data(..., state_data={"name": event.object.object.message.text})

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
 
    # we finish interview and... we should delete user's state from storage.
    # `fsm.finish` will do it by itself.
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return f"Your data - {user_data}"
```

In the end of interview it will write down to you something like that:
```
Your data - {'__vkwave_fsm_state__': '<vkwave.bots_fsm.fsm.State object at 0x0000021C19D61A90>', 'name': 'Nick', 'age': '46'}
```
