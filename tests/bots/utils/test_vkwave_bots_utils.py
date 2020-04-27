import os

import pytest

from vkwave.bots.utils.uploaders import DocUploader, PhotoUploader
from vkwave.easy import create_bot_aiohttp


@pytest.fixture()
def token():
    return os.environ.get("TOKEN")


@pytest.fixture()
def user_id():
    return int(os.environ.get("VK_USER_ID", "578716413"))


@pytest.mark.asyncio
async def test_doc_uploader(token, user_id):
    if not token:
        pytest.skip("no token")
    async with create_bot_aiohttp(token) as api:
        uploader = DocUploader(api)

        # сексульно дышим кеше в лс
        audio_message = await uploader.get_attachment_from_link(
            peer_id=user_id,
            link="https://preview.redd.it/k126wnojy9801.gif?format=png8&s=2cfc209601febb09fc4f31fc30d61408c9372269",
        )
        await api.messages.send(user_id=user_id, attachment=audio_message, random_id=0)


@pytest.mark.asyncio
async def test_photo_uploader(token, user_id):
    if not token:
        pytest.skip("no token")
    async with create_bot_aiohttp(token) as api:
        uploader = PhotoUploader(api)

        # сексульно кидаем вквейв кеше в лс
        big_attachment = await uploader.get_attachments_from_links(
            peer_id=user_id,
            links=[
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
                "https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg",
            ],
        )
        await api.messages.send(user_id=user_id, attachment=big_attachment, random_id=0)
