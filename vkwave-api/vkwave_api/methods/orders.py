from vkwave_types.responses import *
from ._category import Category


class Orders(Category):
    def cancel_subscription(
        self,
        user_id: typing.Optional[int] = None,
        subscription_id: typing.Optional[int] = None,
        pending_cancel: typing.Optional[bool] = None,
    ) -> OrdersCancelSubscriptionResponse:
        """
        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("cancelSubscription", params)
        result = OrdersCancelSubscriptionResponse(**raw_result)
        return result

    def change_state(
        self,
        order_id: typing.Optional[int] = None,
        action: typing.Optional[str] = None,
        app_order_id: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
    ) -> OrdersChangeStateResponse:
        """
        :param order_id: - order ID.
        :param action: - action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: - internal ID of the order in the application.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("changeState", params)
        result = OrdersChangeStateResponse(**raw_result)
        return result

    def get(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
    ) -> OrdersGetResponse:
        """
        :param offset:
        :param count: - number of returned orders.
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = OrdersGetResponse(**raw_result)
        return result

    def get_amount(
        self,
        user_id: typing.Optional[int] = None,
        votes: typing.Optional[typing.List[str]] = None,
    ) -> OrdersGetAmountResponse:
        """
        :param user_id:
        :param votes:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAmount", params)
        result = OrdersGetAmountResponse(**raw_result)
        return result

    def get_by_id(
        self,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[bool] = None,
    ) -> OrdersGetByIdResponse:
        """
        :param order_id: - order ID.
        :param order_ids: - order IDs (when information about several orders is requested).
        :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = OrdersGetByIdResponse(**raw_result)
        return result

    def get_user_subscription_by_id(
        self,
        user_id: typing.Optional[int] = None,
        subscription_id: typing.Optional[int] = None,
    ) -> OrdersGetUserSubscriptionByIdResponse:
        """
        :param user_id:
        :param subscription_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUserSubscriptionById", params)
        result = OrdersGetUserSubscriptionByIdResponse(**raw_result)
        return result

    def get_user_subscriptions(
        self, user_id: typing.Optional[int] = None,
    ) -> OrdersGetUserSubscriptionsResponse:
        """
        :param user_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUserSubscriptions", params)
        result = OrdersGetUserSubscriptionsResponse(**raw_result)
        return result

    def update_subscription(
        self,
        user_id: typing.Optional[int] = None,
        subscription_id: typing.Optional[int] = None,
        price: typing.Optional[int] = None,
    ) -> OrdersUpdateSubscriptionResponse:
        """
        :param user_id:
        :param subscription_id:
        :param price:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("updateSubscription", params)
        result = OrdersUpdateSubscriptionResponse(**raw_result)
        return result
