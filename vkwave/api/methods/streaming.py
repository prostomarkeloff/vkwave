from vkwave.types.responses import *

from ._category import Category


class Streaming(Category):
    async def get_server_url(self,) -> StreamingGetServerUrlResponse:
        """
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getServerUrl", params)
        result = StreamingGetServerUrlResponse(**raw_result)
        return result

    async def set_settings(self, monthly_tier: typing.Optional[str] = None,) -> OkResponse:
        """
        :param monthly_tier:
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("setSettings", params)
        result = OkResponse(**raw_result)
        return result
