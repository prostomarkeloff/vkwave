from vkwave_types.responses import *
from ._category import Category


class Auth(Category):
    async def check_phone(
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("checkPhone", params)
        result = OkResponse(**raw_result)
        return result

    async def restore(
        self,
        phone: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
    ) -> AuthRestoreResponse:
        """
        :param phone: - User phone number.
        :param last_name: - User last name.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("restore", params)
        result = AuthRestoreResponse(**raw_result)
        return result
