from vkwave_types.responses import *
from ._category import Category


class Storage(Category):
    def get(
        self,
        key: typing.Optional[str],
        keys: typing.Optional[typing.List[str]],
        user_id: typing.Optional[int],
        global_: typing.Optional[bool],
    ) -> dict:
        """
        :param key:
        :param keys:
        :param user_id:
        :param global_:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = dict(**raw_result)
        return result

    def get_keys(
        self,
        user_id: typing.Optional[int],
        global_: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> StorageGetKeysResponse:
        """
        :param user_id: - user id, whose variables names are returned if they were requested with a server method.
        :param global_:
        :param offset:
        :param count: - amount of variable names the info needs to be collected from.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getKeys", params)
        result = StorageGetKeysResponse(**raw_result)
        return result

    def set(
        self,
        key: typing.Optional[str],
        value: typing.Optional[str],
        user_id: typing.Optional[int],
        global_: typing.Optional[bool],
    ) -> OkResponse:
        """
        :param key:
        :param value:
        :param user_id:
        :param global_:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("set", params)
        result = OkResponse(**raw_result)
        return result
