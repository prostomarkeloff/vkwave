from vkwave_types.responses import *
from ._category import Category


class Storage(Category):
    async def get(
        self,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
    ) -> dict:
        """
        :param key:
        :param keys:
        :param user_id:
        :param global_:
        :return:
        """

        params = {}
        for key_, value in locals().items():
            if key_ not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key_] = value

        raw_result = await self.api_request("get", params)
        result = dict(**raw_result)
        return result

    async def get_keys(
        self,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> StorageGetKeysResponse:
        """
        :param user_id: - user id, whose variables names are returned if they were requested with a server method.
        :param global_:
        :param offset:
        :param count: - amount of variable names the info needs to be collected from.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getKeys", params)
        result = StorageGetKeysResponse(**raw_result)
        return result

    async def set(
        self,
        key: str = None,
        value: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param key:
        :param value:
        :param user_id:
        :param global_:
        :return:
        """

        params = {}
        for key_, value_ in locals().items():
            if key_ not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value = ",".join(str(item) for item in value_)
                params[key_] = value_

        raw_result = await self.api_request("set", params)
        result = OkResponse(**raw_result)
        return result
