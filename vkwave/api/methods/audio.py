from vkwave.types.extension_responses import *

from ._category import Category
from ._utils import get_params


class Audio(Category):
    """
    To use audio api:
        1) obtain token through direct auth with client_secret and client_id of app that is allowed to use audio api
        2) set appropriate user agent for ClientSession (for instance for official vk app: VKAndroidApp/6.51)
    """

    async def get(
        self,
        owner_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        audio_ids: typing.Optional[typing.List[int]] = None,
        need_user: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AudioGetResponse]:
        """
        :param owner_id: - music owner
        :param album_id:
        :param audio_ids: - list of audio id
        :param need_user: - 1 or 0
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = AudioGetResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        audios: typing.List[str],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AudioGetByIdResponse]:
        """
        :param audios: - List of audios in following format: "<owner_id>_<audio_id>"
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = AudioGetByIdResponse(**raw_result)
        return result
