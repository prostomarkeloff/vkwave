from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Donut(Category):
    async def get_friends(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[str]] = None,
    ) -> Union[dict, GroupsGetMembersFieldsResponse]:
        """
        :param owner_id:
        :param offset:
        :param count:
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFriends", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetMembersFieldsResponse(**raw_result)
        return result

    async def get_subscription(
        self,
        owner_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, DonutGetSubscriptionResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSubscription", params)
        if return_raw_response:
            return raw_result

        result = DonutGetSubscriptionResponse(**raw_result)
        return result

    async def get_subscriptions(
        self,
        return_raw_response: bool = False,
        fields: Optional[List[BaseUserGroupFields]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, DonutGetSubscriptionsResponse]:
        """
        :param fields:
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSubscriptions", params)
        if return_raw_response:
            return raw_result

        result = DonutGetSubscriptionsResponse(**raw_result)
        return result

    async def is_don(
        self,
        owner_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("isDon", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result
