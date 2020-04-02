from vkwave.types.responses import *

from ._category import Category


class Status(Category):
    async def get(
        self, user_id: typing.Optional[int] = None, group_id: typing.Optional[int] = None,
    ) -> StatusGetResponse:
        """
        :param user_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param group_id:
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("get", params)
        result = StatusGetResponse(**raw_result)
        return result

    async def set(
        self, text: typing.Optional[str] = None, group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param text: - Text of the new status.
        :param group_id: - Identifier of a community to set a status in. If left blank the status is set to current user.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("set", params)
        result = OkResponse(**raw_result)
        return result
