import asyncio

from vkwave.api import Token, BotSyncSingleToken, API
from vkwave.bots import PhotoUploader, WallPhotoUploader, DocUploader
from vkwave.client import AIOHTTPClient

client = AIOHTTPClient()
api = API(clients=client, tokens=BotSyncSingleToken(Token("token")),)

uploader = PhotoUploader(api.get_context())
# same with VoiceUploader etc.


async def main():
    big_attachment = await uploader.get_attachments_from_links(
        peer_id=1234,
        links=[
            "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
            "https://camo.githubusercontent.com/9c8d6519e5997860b7a4b28f74719c0c2f83142b/68747470733a2f2f692e696d6775722e636f6d2f386955334578366c2e6a7067",
            "https://user-images.githubusercontent.com/28061158/74590410-239e3300-501f-11ea-9774-27ee507a1e1e.jpg",
        ],
    )
    await api.get_context().messages.send(user_id=1234, attachment=big_attachment, random_id=0)


async def wall_upload():
    # works only with user token
    photo = await WallPhotoUploader(api.get_context()).get_attachment_from_link(
        group_id=-191949777,
        link="https://user-images.githubusercontent.com/28061158/74590410-239e3300-501f-11ea-9774-27ee507a1e1e.jpg",
    )
    await api.get_context().wall.post(owner_id=-191949777, message="432", attachments=photo)


async def doc_upload():
    doc = await DocUploader(api.get_context()).get_attachment_from_link(
        peer_id=123,
        link="https://user-images.githubusercontent.com/28061158/74590410-239e3300-501f-11ea-9774-27ee507a1e1e.jpg",
        title="my document title",
        file_extension="jpg"
    )
    await api.get_context().messages.send(user_id=1234, attachment=doc, random_id=0)


asyncio.get_event_loop().run_until_complete(main())
