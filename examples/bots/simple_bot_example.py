from vkwave.bots.easy import SimpleBot


bot = SimpleBot(
    token="12345",
    group_id=1234,
)


@bot.message_handler(bot.text_filter("hello"))
async def simple(event: bot.BaseEvent):
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id, message="hello from vkwave!", random_id=0,
    )


@bot.message_handler(bot.command_filter(commands=["start"]))
async def start(event: bot.BaseEvent):
    user_data = (
        await bot.api_context.users.get(user_ids=event.object.object.message.peer_id)
    ).response[0]
    user_name = user_data.first_name
    await event.api_ctx.messages.send(
        peer_id=event.object.object.message.peer_id,
        message=f"You just started, {user_name}",
        random_id=0,
    )


bot.run()
