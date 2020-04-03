from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Streaming(Category):
    async def get_server_url(
        self, raw: bool = False,
    ) -> typing.Union[dict, StreamingGetServerUrlResponse]:
        """
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getServerUrl", params)
        if raw:
            return raw_result

        result = StreamingGetServerUrlResponse(**raw_result)
        return result

    async def set_settings(
        self, monthly_tier: typing.Optional[str] = None, raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param monthly_tier:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setSettings", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result
