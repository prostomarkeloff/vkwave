from vkwave_types.responses import *
from ._category import Category


class Secure(Category):
    def add_app_event(
        self,
        user_id: typing.Optional[int] = None,
        activity_id: typing.Optional[int] = None,
        value: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param user_id: - ID of a user to save the data
        :param activity_id: - there are 2 default activities: , * 1 – level. Works similar to ,, * 2 – points, saves points amount, Any other value is for saving completed missions
        :param value: - depends on activity_id: * 1 – number, current level number,, * 2 – number, current user's points amount, , Any other value is ignored
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addAppEvent", params)
        result = OkResponse(**raw_result)
        return result

    def check_token(
        self, token: typing.Optional[str] = None, ip: typing.Optional[str] = None,
    ) -> SecureCheckTokenResponse:
        """
        :param token: - client 'access_token'
        :param ip: - user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("checkToken", params)
        result = SecureCheckTokenResponse(**raw_result)
        return result

    def get_app_balance(self,) -> SecureGetAppBalanceResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAppBalance", params)
        result = SecureGetAppBalanceResponse(**raw_result)
        return result

    def get_s_m_s_history(
        self,
        user_id: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> SecureGetSMSHistoryResponse:
        """
        :param user_id:
        :param date_from: - filter by start date. It is set as UNIX-time.
        :param date_to: - filter by end date. It is set as UNIX-time.
        :param limit: - number of returned posts. By default — 1000.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSMSHistory", params)
        result = SecureGetSMSHistoryResponse(**raw_result)
        return result

    def get_transactions_history(
        self,
        type: typing.Optional[int] = None,
        uid_from: typing.Optional[int] = None,
        uid_to: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> SecureGetTransactionsHistoryResponse:
        """
        :param type:
        :param uid_from:
        :param uid_to:
        :param date_from:
        :param date_to:
        :param limit:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTransactionsHistory", params)
        result = SecureGetTransactionsHistoryResponse(**raw_result)
        return result

    def get_user_level(
        self, user_ids: typing.Optional[typing.List[int]] = None,
    ) -> SecureGetUserLevelResponse:
        """
        :param user_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUserLevel", params)
        result = SecureGetUserLevelResponse(**raw_result)
        return result

    def give_event_sticker(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        achievement_id: typing.Optional[int] = None,
    ) -> SecureGiveEventStickerResponse:
        """
        :param user_ids:
        :param achievement_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("giveEventSticker", params)
        result = SecureGiveEventStickerResponse(**raw_result)
        return result

    def send_notification(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
    ) -> SecureSendNotificationResponse:
        """
        :param user_ids:
        :param user_id:
        :param message: - notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("sendNotification", params)
        result = SecureSendNotificationResponse(**raw_result)
        return result

    def send_s_m_s_notification(
        self,
        user_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param user_id: - ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: - 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("sendSMSNotification", params)
        result = OkResponse(**raw_result)
        return result

    def set_counter(
        self,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param counters:
        :param user_id:
        :param counter: - counter value.
        :param increment:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setCounter", params)
        result = OkResponse(**raw_result)
        return result
