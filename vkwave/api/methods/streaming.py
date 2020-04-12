from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Streaming(Category):
    async def get_server_url(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, StreamingGetServerUrlResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getServerUrl", params)
        if return_raw_response:
            return raw_result

        result = StreamingGetServerUrlResponse(**raw_result)
        return result

    async def set_settings(
        self, return_raw_response: bool = False, monthly_tier: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param monthly_tier:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setSettings", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
