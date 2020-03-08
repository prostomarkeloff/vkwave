from vkwave_types.responses import *
from ._category import Category


class Auth(Category):
    def check_phone(
        self,
        phone: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        client_secret: typing.Optional[str] = None,
        auth_by_phone: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param phone: - Phone number.
        :param client_id: - User ID.
        :param client_secret:
        :param auth_by_phone:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("checkPhone", params)
        result = OkResponse(**raw_result)
        return result

    def restore(
        self,
        phone: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
    ) -> AuthRestoreResponse:
        """
        :param phone: - User phone number.
        :param last_name: - User last name.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("restore", params)
        result = AuthRestoreResponse(**raw_result)
        return result
