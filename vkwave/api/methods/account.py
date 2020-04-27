from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Account(Category):
    async def ban(
        self, return_raw_response: bool = False, owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("ban", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def change_password(
        self,
        new_password: str,
        return_raw_response: bool = False,
        restore_sid: typing.Optional[str] = None,
        change_password_hash: typing.Optional[str] = None,
        old_password: typing.Optional[str] = None,
    ) -> typing.Union[dict, AccountChangePasswordResponse]:
        """
        :param restore_sid: - Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: - Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: - Current user password.
        :param new_password: - New password that will be set as a current
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("changePassword", params)
        if return_raw_response:
            return raw_result

        result = AccountChangePasswordResponse(**raw_result)
        return result

    async def get_active_offers(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, AccountGetActiveOffersResponse]:
        """
        :param offset:
        :param count: - Number of results to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getActiveOffers", params)
        if return_raw_response:
            return raw_result

        result = AccountGetActiveOffersResponse(**raw_result)
        return result

    async def get_app_permissions(
        self, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AccountGetAppPermissionsResponse]:
        """
        :param user_id: - User ID whose settings information shall be got. By default: current user.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAppPermissions", params)
        if return_raw_response:
            return raw_result

        result = AccountGetAppPermissionsResponse(**raw_result)
        return result

    async def get_banned(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, AccountGetBannedResponse]:
        """
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getBanned", params)
        if return_raw_response:
            return raw_result

        result = AccountGetBannedResponse(**raw_result)
        return result

    async def get_counters(
        self, return_raw_response: bool = False, filter: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, AccountGetCountersResponse]:
        """
        :param filter: - Counters to be returned.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCounters", params)
        if return_raw_response:
            return raw_result

        result = AccountGetCountersResponse(**raw_result)
        return result

    async def get_info(
        self, return_raw_response: bool = False, fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, AccountGetInfoResponse]:
        """
        :param fields: - Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getInfo", params)
        if return_raw_response:
            return raw_result

        result = AccountGetInfoResponse(**raw_result)
        return result

    async def get_profile_info(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, AccountGetProfileInfoResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getProfileInfo", params)
        if return_raw_response:
            return raw_result

        result = AccountGetProfileInfoResponse(**raw_result)
        return result

    async def get_push_settings(
        self, return_raw_response: bool = False, device_id: typing.Optional[str] = None,
    ) -> typing.Union[dict, AccountGetPushSettingsResponse]:
        """
        :param device_id: - Unique device ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPushSettings", params)
        if return_raw_response:
            return raw_result

        result = AccountGetPushSettingsResponse(**raw_result)
        return result

    async def register_device(
        self,
        token: str,
        device_id: str,
        return_raw_response: bool = False,
        device_model: typing.Optional[str] = None,
        device_year: typing.Optional[int] = None,
        system_version: typing.Optional[str] = None,
        settings: typing.Optional[str] = None,
        sandbox: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param token: - Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: - String name of device model.
        :param device_year: - Device year.
        :param device_id: - Unique device ID.
        :param system_version: - String version of device operating system.
        :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("registerDevice", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def save_profile_info(
        self,
        return_raw_response: bool = False,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        maiden_name: typing.Optional[str] = None,
        screen_name: typing.Optional[str] = None,
        cancel_request_id: typing.Optional[int] = None,
        sex: typing.Optional[int] = None,
        relation: typing.Optional[BaseBoolInt] = None,
        relation_partner_id: typing.Optional[int] = None,
        bdate: typing.Optional[str] = None,
        bdate_visibility: typing.Optional[BaseBoolInt] = None,
        home_town: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[dict, AccountSaveProfileInfoResponse]:
        """
        :param first_name: - User first name.
        :param last_name: - User last name.
        :param maiden_name: - User maiden name (female only)
        :param screen_name: - User screen name.
        :param cancel_request_id: - ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: - User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: - User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: - ID of the relationship partner.
        :param bdate: - User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: - Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: - User home town.
        :param country_id: - User country.
        :param city_id: - User city.
        :param status: - Status text.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("saveProfileInfo", params)
        if return_raw_response:
            return raw_result

        result = AccountSaveProfileInfoResponse(**raw_result)
        return result

    async def set_info(
        self,
        return_raw_response: bool = False,
        name: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param name: - Setting name.
        :param value: - Setting value.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setInfo", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_name_in_menu(
        self, user_id: int, return_raw_response: bool = False, name: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id: - User ID.
        :param name: - Application screen name.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setNameInMenu", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_offline(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setOffline", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_online(
        self, return_raw_response: bool = False, voip: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param voip: - '1' if videocalls are available for current device.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setOnline", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_push_settings(
        self,
        device_id: str,
        return_raw_response: bool = False,
        settings: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        value: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param device_id: - Unique device ID.
        :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
        :param key: - Notification key.
        :param value: - New value for the key in a [vk.com/dev/push_settings|special format].
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setPushSettings", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_silence_mode(
        self,
        return_raw_response: bool = False,
        device_id: typing.Optional[str] = None,
        time: typing.Optional[int] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        sound: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param device_id: - Unique device ID.
        :param time: - Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: - '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setSilenceMode", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def unban(
        self, return_raw_response: bool = False, owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unban", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def unregister_device(
        self,
        return_raw_response: bool = False,
        device_id: typing.Optional[str] = None,
        sandbox: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param device_id: - Unique device ID.
        :param sandbox:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unregisterDevice", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
