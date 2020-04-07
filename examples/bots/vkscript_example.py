from vkwave.api.methods import APIOptionsRequestContext
from vkwave.bots.easy import SimpleLongPollBot, TaskManager
from vkwave.vkscript import execute
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

    for sub_id in subscribers:
        subscriber_data = api.users.get(user_ids=sub_id)
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
    var subscribers=API.groups.getMembers({group_id:1});
    var subscribers=subscribers.items;
    while(subscribers.length > 0){
        var sub_id=subscribers.pop();
        var subscriber_data=API.users.get({user_ids:sub_id});
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
