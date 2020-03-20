# vkwave-bots-fsm

This module is implementation of [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)
for bots

fsm divides user states, chat states and user in chat states,
for selecting one of the above options you can set ```for_what```
argument in fsm methods.

One user in personal message - ```ForWhat.FOR_USER```

State for all chat - ```ForWhat.FOR_CHAT```

For one user in chat - ```ForWhat.FOR_USER_IN_CHAT```

So fsm doesn't reacted on handlers without ```StateFilter``` you can set default_filter - 
```router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))```.

Because of this, if user have state, routes will not reacted on event.

Example of simple interview with asking name and age.
```python
fsm = FiniteStateMachine()
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
router.registrar.add_default_filter(EventTypeFilter(BotEventType.MESSAGE_NEW.value))


class MyState:
    name = State("name")
    age = State("age")


#  starting interview 
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "start",
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


#  exiting interview (work with any state because of state=ANY_STATE)
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
    #  extra_state_data equal to fsm.add_data(..., state_data={"name": event.object.object.message.text})

    return f"Input your age"


@router.registrar.with_decorator(
    StateFilter(fsm=fsm, state=MyState.age, for_what=ForWhat.FOR_USER),
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
 
    #  deleting all user state data
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return f"Your data - {user_data}"
```

It returns smth like
```
Your data - {'__vkwave_fsm_state__': '<vkwave_bots_fsm.fsm.State object at 0x0000021C19D61A90>', 'name': 'Nick', 'age': '46'}
```