from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Auth(Category):
    async def check_phone(
        self,
        phone: str = None,
        client_id: typing.Optional[int] = None,
        client_secret: typing.Optional[str] = None,
        auth_by_phone: typing.Optional[bool] = None,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param phone: - Phone number.
        :param client_id: - User ID.
        :param client_secret:
        :param auth_by_phone:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("checkPhone", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def restore(
        self,
        phone: str = None,
        last_name: str = None,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AuthRestoreResponse]:
        """
        :param phone: - User phone number.
        :param last_name: - User last name.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restore", params)
        if return_raw_response:
            return raw_result

        result = AuthRestoreResponse(**raw_result)
        return result
