from vkwave_types.responses import *
from ._category import Category


class Status(Category):
    def get(
        self, user_id: typing.Optional[int], group_id: typing.Optional[int],
    ) -> StatusGetResponse:
        """
        :param user_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = StatusGetResponse(**raw_result)
        return result

    def set(
        self, text: typing.Optional[str], group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param text: - Text of the new status.
        :param group_id: - Identifier of a community to set a status in. If left blank the status is set to current user.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("set", params)
        result = OkResponse(**raw_result)
        return result
