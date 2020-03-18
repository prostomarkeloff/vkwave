from vkwave_types.responses import *

from ._category import Category


class Streaming(Category):
    async def get_server_url(self,) -> StreamingGetServerUrlResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getServerUrl", params)
        result = StreamingGetServerUrlResponse(**raw_result)
        return result

    async def set_settings(
        self, monthly_tier: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param monthly_tier:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setSettings", params)
        result = OkResponse(**raw_result)
        return result
