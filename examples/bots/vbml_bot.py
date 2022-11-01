from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens=["Token"], group_id=123)


@bot.message_handler(bot.vbml_filter("+<country_code:int>(<state_code:int>)<number:int>"))
async def vbml_test(event):
    vmbl_data = event["vmbl_data"]
    country_code = vmbl_data["country_code"]
    state_code = vmbl_data["state_code"]
    number = vmbl_data["number"]
    print(country_code, state_code, number)


bot.run_forever()
