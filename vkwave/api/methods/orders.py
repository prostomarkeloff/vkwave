from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Orders(Category):
    async def cancel_subscription(
        self,
        user_id: int,
        subscription_id: int,
        return_raw_response: bool = False,
        pending_cancel: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OrdersCancelSubscriptionResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("cancelSubscription", params)
        if return_raw_response:
            return raw_result

        result = OrdersCancelSubscriptionResponse(**raw_result)
        return result

    async def change_state(
        self,
        order_id: int,
        action: str,
        return_raw_response: bool = False,
        app_order_id: typing.Optional[int] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OrdersChangeStateResponse]:
        """
        :param order_id: - order ID.
        :param action: - action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: - internal ID of the order in the application.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("changeState", params)
        if return_raw_response:
            return raw_result

        result = OrdersChangeStateResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OrdersGetResponse]:
        """
        :param offset:
        :param count: - number of returned orders.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = OrdersGetResponse(**raw_result)
        return result

    async def get_amount(
        self, user_id: int, votes: typing.List[str], return_raw_response: bool = False,
    ) -> typing.Union[dict, OrdersGetAmountResponse]:
        """
        :param user_id:
        :param votes:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAmount", params)
        if return_raw_response:
            return raw_result

        result = OrdersGetAmountResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        return_raw_response: bool = False,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OrdersGetByIdResponse]:
        """
        :param order_id: - order ID.
        :param order_ids: - order IDs (when information about several orders is requested).
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = OrdersGetByIdResponse(**raw_result)
        return result

    async def get_user_subscription_by_id(
        self, user_id: int, subscription_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OrdersGetUserSubscriptionByIdResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUserSubscriptionById", params)
        if return_raw_response:
            return raw_result

        result = OrdersGetUserSubscriptionByIdResponse(**raw_result)
        return result

    async def get_user_subscriptions(
        self, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OrdersGetUserSubscriptionsResponse]:
        """
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUserSubscriptions", params)
        if return_raw_response:
            return raw_result

        result = OrdersGetUserSubscriptionsResponse(**raw_result)
        return result

    async def update_subscription(
        self, user_id: int, subscription_id: int, price: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OrdersUpdateSubscriptionResponse]:
        """
        :param user_id:
        :param subscription_id:
        :param price:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateSubscription", params)
        if return_raw_response:
            return raw_result

        result = OrdersUpdateSubscriptionResponse(**raw_result)
        return result
