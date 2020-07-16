import os

import pytest

from dotenv import load_dotenv
from vkwave.bots.utils.uploaders import DocUploader, PhotoUploader
from vkwave.bots import create_api_session_aiohttp

load_dotenv()
TOKEN = os.getenv("TOKEN")


@pytest.fixture()
def user_id():
    return int(os.environ.get("VK_USER_ID", "578716413"))


@pytest.mark.asyncio
async def test_doc_uploader(user_id):
    async with create_api_session_aiohttp(TOKEN) as api:
        uploader = DocUploader(api)

        audio_message = await uploader.get_attachment_from_link(
            peer_id=user_id,
            link="https://preview.redd.it/k126wnojy9801.gif?format=png8&s=2cfc209601febb09fc4f31fc30d61408c9372269",
        )
        await api.messages.send(user_id=user_id, attachment=audio_message, random_id=0)


@pytest.mark.asyncio
async def test_photo_uploader(user_id):
    async with create_api_session_aiohttp(TOKEN) as api:
        uploader = PhotoUploader(api)

        big_attachment = await uploader.get_attachments_from_links(
            peer_id=user_id,
            links=[
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
            ],
        )
        await api.messages.send(user_id=user_id, attachment=big_attachment, random_id=0)
