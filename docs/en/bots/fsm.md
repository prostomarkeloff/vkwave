# FSM

Этот модуль имплементирует [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) для ботов.


FSM разделяет пользовательские состояния, состояния в чатах и состояния пользователя в чате, для выбора
одного из них вы должны указать `for_what` аргумент в методах fsm.


Состояние для одного пользователя в личных сообщениях - `ForWhat.FOR_USER`

Для всех пользователей в чате - `ForWhat.FOR_CHAT`

Для одного пользователя в чате - `ForWhat.FOR_USER_IN_CHAT`


Чтобы хендлеры без `StateFilter` могли быть выбраны корректно, нужно установить следующий стандартный фильтр.
```python
router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
```

Пример опроса с именем и возрастом.

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


# начинаем интервью
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "start",
)
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


#  выход из опроса (срабатывает на любой стейт `state=ANY_STATE`)
@router.registrar.with_decorator(
    lambda event: event.object.object.message.text == "exit",
    StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER)
)
async def simple_handler(event: BotEvent):
    # Проверяем есть ли юзер в базе
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
    # extra_state_data работает так же как fsm.add_data(..., state_data={"name": event.object.object.message.text})

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
 
    # завершаем опрос и удаляем юзера
    # `fsm.finish` делает это
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return f"Your data - {user_data}"
```

В конце опроса вы получите нечто похожее:
```
Your data - {'__vkwave_fsm_state__': '<vkwave.bots_fsm.fsm.State object at 0x0000021C19D61A90>', 'name': 'Nick', 'age': '46'}
```
