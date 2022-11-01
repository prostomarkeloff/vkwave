from vkwave.bots import BotEvent, EventTypeFilter, SimpleLongPollBot
from vkwave.bots.fsm import ANY_STATE, FiniteStateMachine, ForWhat, State, StateFilter
from vkwave.types.bot_events import BotEventType

bot = SimpleLongPollBot("123", group_id=123)


fsm = FiniteStateMachine()
bot.router.registrar.add_default_filter(StateFilter(fsm, ..., ..., always_false=True))
bot.router.registrar.add_default_filter(
    EventTypeFilter(BotEventType.MESSAGE_NEW.value)
)  # we don't want to write it in all handlers.


class MyState:
    name = State("name")
    age = State("age")


# starting interview (has default filter that will reject messages if state exists)
@bot.message_handler(bot.text_filter("start"))
async def simple_handler(event: BotEvent):
    await fsm.set_state(event=event, state=MyState.name, for_what=ForWhat.FOR_USER)
    return "Input your name"


#  exiting interview (work with any state because of `state=ANY_STATE`)
@bot.message_handler(
    bot.text_filter("exit"), StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER)
)
async def simple_handler2(event: BotEvent):
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return "You are quited!"


@bot.message_handler(StateFilter(fsm=fsm, state=MyState.name, for_what=ForWhat.FOR_USER),)
async def simple_handler(event: BotEvent):
    await fsm.set_state(
        event=event,
        state=MyState.age,
        for_what=ForWhat.FOR_USER,
        extra_state_data={"name": event.object.object.message.text},
    )
    # extra_state_data is totally equal to fsm.add_data(..., state_data={"name": event.object.object.message.text})

    return "Input your age"


@bot.message_handler(StateFilter(fsm=fsm, state=MyState.age, for_what=ForWhat.FOR_USER),)
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


bot.run_forever()
