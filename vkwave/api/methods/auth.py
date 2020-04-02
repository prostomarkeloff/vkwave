from vkwave.types.responses import *

from ._category import Category


class Auth(Category):
    async def check_phone(
        self,
        phone: str = None,
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
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("checkPhone", params)
        result = OkResponse(**raw_result)
        return result

    async def restore(self, phone: str = None, last_name: str = None,) -> AuthRestoreResponse:
        """
        :param phone: - User phone number.
        :param last_name: - User last name.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("restore", params)
        result = AuthRestoreResponse(**raw_result)
        return result
