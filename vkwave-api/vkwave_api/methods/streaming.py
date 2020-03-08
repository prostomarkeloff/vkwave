from vkwave_types.responses import *
from ._category import Category


class Streaming(Category):
    def get_server_url(self,) -> StreamingGetServerUrlResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getServerUrl", params)
        result = StreamingGetServerUrlResponse(**raw_result)
        return result

    def set_settings(self, monthly_tier: typing.Optional[str] = None,) -> OkResponse:
        """
        :param monthly_tier:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setSettings", params)
        result = OkResponse(**raw_result)
        return result
