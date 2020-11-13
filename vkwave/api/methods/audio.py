from vkwave.types.extension_responses import *

from ._category import Category
from ._utils import get_params


class Audio(Category):
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
