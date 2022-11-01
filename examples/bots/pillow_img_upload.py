from io import BytesIO

from PIL import Image

from vkwave.bots import PhotoUploader, SimpleLongPollBot
from vkwave.types.objects import MessagesMessageAttachmentType

bot = SimpleLongPollBot(tokens=["токен)"], group_id=123)

photo_uploader = PhotoUploader(api_context=bot.api_context)


@bot.message_handler(
    bot.attachment_type_filter(attachment_type=MessagesMessageAttachmentType.PHOTO)
)
async def simple(event: bot.SimpleBotEvent):
    print(event.attachments[0].url)
    await event.attachments[0].save("photo.jpg")
    bytesi = BytesIO(await event.attachments[0].download())
    img = Image.open(bytesi)
    rotated: Image.Image = img.rotate(90)
    by = BytesIO()
    rotated.save(by, format="PNG")
    by.seek(0)

    resp = await photo_uploader.get_attachment_from_io(peer_id=event.peer_id, f=by, file_extension="png")
    await event.answer(attachment=resp, message="фотачьку перевернули)")


bot.run_forever()

