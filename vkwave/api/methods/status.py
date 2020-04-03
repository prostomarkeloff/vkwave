from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Status(Category):
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, StatusGetResponse]:
        """
        :param user_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param group_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = StatusGetResponse(**raw_result)
        return result

    async def set(
        self,
        text: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param text: - Text of the new status.
        :param group_id: - Identifier of a community to set a status in. If left blank the status is set to current user.
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("set", params)
        if raw:
            return raw_result

        result = OkResponse(**raw_result)
        return result
