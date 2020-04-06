from vkwave.api.methods import APIOptionsRequestContext
from vkwave.bots.easy import SimpleLongPollBot, TaskManager
from vkwave.bots.vkscript import execute
from vkwave.types.responses import ExecuteResponse

bot = SimpleLongPollBot(
    tokens=["123"],
    group_id=456,
)


@execute
def get_subs_names(api: APIOptionsRequestContext, group_id: int):
    subs_names = []

    subscribers = api.groups.getMembers(group_id=group_id)
    subscribers = subscribers.items

    while subscribers:
        subscriber_id = subscribers.pop()
        subscriber_data = api.users.get(user_ids=subscriber_id)
        subs_names.append(subscriber_data[0].first_name)
    return subs_names


@bot.message_handler(bot.text_filter("follow"))
async def simple(event: bot.BaseEvent):
    """
    Get name of each subscriber
    """

    check_group = 191949777

    print(get_subs_names.build(api=event.api_ctx, group_id=check_group))
    """
    var subs_names=[];
    var subscribers=API.groups.getMembers({group_id:191949777});
    var subscribers=subscribers.items;
    while(subscribers){
            var subscriber_id=subscribers.pop();
            var subscriber_data=API.users.get({user_ids:subscriber_id});
            subs_names.push(subscriber_data[0].first_name);
    };
    return subs_names;
    """

    execute_data: ExecuteResponse = await get_subs_names(api=event.api_ctx, group_id=check_group)
    print(execute_data)
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id, message=execute_data.response, random_id=0,
    )


tm = TaskManager()
tm.add_task(bot.run)
tm.run()
