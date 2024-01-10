from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Donut(Category):
    async def get_friends(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, GroupsGetMembersFieldsResponse]:
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

        return GroupsGetMembersFieldsResponse(**raw_result)

    async def get_subscription(
        self,
        owner_id: int,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, DonutGetSubscriptionResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSubscription", params)
        if return_raw_response:
            return raw_result

        return DonutGetSubscriptionResponse(**raw_result)

    async def get_subscriptions(
        self,
        return_raw_response: bool = False,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DonutGetSubscriptionsResponse]:
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

        return DonutGetSubscriptionsResponse(**raw_result)

    async def is_don(
        self,
        owner_id: int,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseBoolResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("isDon", params)
        return raw_result if return_raw_response else BaseBoolResponse(**raw_result)
