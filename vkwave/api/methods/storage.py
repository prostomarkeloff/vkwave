from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Storage(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        user_id: Optional[int] = None,
    ) -> Union[dict, StorageGetResponse]:
        """
        :param key:
        :param keys:
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = StorageGetV5110Response(**raw_result)
        return result

    async def get_keys(
        self,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, StorageGetKeysResponse]:
        """
        :param user_id: - user id, whose variables names are returned if they were requested with a server method.
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
        value: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param key:
        :param value:
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("set", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
