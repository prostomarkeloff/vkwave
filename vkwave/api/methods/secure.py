from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Secure(Category):
    async def add_app_event(
        self,
        user_id: int,
        activity_id: int,
        return_raw_response: bool = False,
        value: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id: - ID of a user to save the data
        :param activity_id: - there are 2 default activities: , * 1 – level. Works similar to ,, * 2 – points, saves points amount, Any other value is for saving completed missions
        :param value: - depends on activity_id: * 1 – number, current level number,, * 2 – number, current user's points amount, , Any other value is ignored
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addAppEvent", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def check_token(
        self,
        return_raw_response: bool = False,
        token: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
    ) -> typing.Union[dict, SecureCheckTokenResponse]:
        """
        :param token: - client 'access_token'
        :param ip: - user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("checkToken", params)
        if return_raw_response:
            return raw_result

        result = SecureCheckTokenResponse(**raw_result)
        return result

    async def get_app_balance(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, SecureGetAppBalanceResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAppBalance", params)
        if return_raw_response:
            return raw_result

        result = SecureGetAppBalanceResponse(**raw_result)
        return result

    async def get_s_m_s_history(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, SecureGetSMSHistoryResponse]:
        """
        :param user_id:
        :param date_from: - filter by start date. It is set as UNIX-time.
        :param date_to: - filter by end date. It is set as UNIX-time.
        :param limit: - number of returned posts. By default — 1000.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSMSHistory", params)
        if return_raw_response:
            return raw_result

        result = SecureGetSMSHistoryResponse(**raw_result)
        return result

    async def get_transactions_history(
        self,
        return_raw_response: bool = False,
        type: typing.Optional[int] = None,
        uid_from: typing.Optional[int] = None,
        uid_to: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[dict, SecureGetTransactionsHistoryResponse]:
        """
        :param type:
        :param uid_from:
        :param uid_to:
        :param date_from:
        :param date_to:
        :param limit:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTransactionsHistory", params)
        if return_raw_response:
            return raw_result

        result = SecureGetTransactionsHistoryResponse(**raw_result)
        return result

    async def get_user_level(
        self, user_ids: typing.List[int], return_raw_response: bool = False,
    ) -> typing.Union[dict, SecureGetUserLevelResponse]:
        """
        :param user_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUserLevel", params)
        if return_raw_response:
            return raw_result

        result = SecureGetUserLevelResponse(**raw_result)
        return result

    async def give_event_sticker(
        self, user_ids: typing.List[int], achievement_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, SecureGiveEventStickerResponse]:
        """
        :param user_ids:
        :param achievement_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("giveEventSticker", params)
        if return_raw_response:
            return raw_result

        result = SecureGiveEventStickerResponse(**raw_result)
        return result

    async def send_notification(
        self,
        message: str,
        return_raw_response: bool = False,
        user_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, SecureSendNotificationResponse]:
        """
        :param user_ids:
        :param user_id:
        :param message: - notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendNotification", params)
        if return_raw_response:
            return raw_result

        result = SecureSendNotificationResponse(**raw_result)
        return result

    async def send_s_m_s_notification(
        self, user_id: int, message: BaseBoolInt, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id: - ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: - 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendSMSNotification", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_counter(
        self,
        return_raw_response: bool = False,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param counters:
        :param user_id:
        :param counter: - counter value.
        :param increment:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setCounter", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
