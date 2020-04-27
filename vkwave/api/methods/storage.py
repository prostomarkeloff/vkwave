from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Storage(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param key:
        :param keys:
        :param user_id:
        :param global_:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = dict(**raw_result)
        return result

    async def get_keys(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, StorageGetKeysResponse]:
        """
        :param user_id: - user id, whose variables names are returned if they were requested with a server method.
        :param global_:
        :param offset:
        :param count: - amount of variable names the info needs to be collected from.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getKeys", params)
        if return_raw_response:
            return raw_result

        result = StorageGetKeysResponse(**raw_result)
        return result

    async def set(
        self,
        key: str,
        return_raw_response: bool = False,
        value: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        global_: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param key:
        :param value:
        :param user_id:
        :param global_:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("set", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
