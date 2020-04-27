from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Groups(Category):
    async def add_address(
        self,
        group_id: int,
        title: str,
        address: str,
        country_id: int,
        city_id: int,
        latitude: int,
        longitude: int,
        return_raw_response: bool = False,
        additional_address: typing.Optional[str] = None,
        metro_id: typing.Optional[int] = None,
        phone: typing.Optional[str] = None,
        work_info_status: typing.Optional[str] = None,
        timetable: typing.Optional[str] = None,
        is_main_address: typing.Optional[bool] = None,
    ) -> typing.Union[dict, GroupsAddAddressResponse]:
        """
        :param group_id:
        :param title:
        :param address:
        :param additional_address:
        :param country_id:
        :param city_id:
        :param metro_id:
        :param latitude:
        :param longitude:
        :param phone:
        :param work_info_status:
        :param timetable:
        :param is_main_address:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addAddress", params)
        if return_raw_response:
            return raw_result

        result = GroupsAddAddressResponse(**raw_result)
        return result

    async def add_callback_server(
        self,
        group_id: int,
        url: str,
        title: str,
        return_raw_response: bool = False,
        secret_key: typing.Optional[str] = None,
    ) -> typing.Union[dict, GroupsAddCallbackServerResponse]:
        """
        :param group_id:
        :param url:
        :param title:
        :param secret_key:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addCallbackServer", params)
        if return_raw_response:
            return raw_result

        result = GroupsAddCallbackServerResponse(**raw_result)
        return result

    async def add_link(
        self,
        group_id: int,
        link: str,
        return_raw_response: bool = False,
        text: typing.Optional[str] = None,
    ) -> typing.Union[dict, GroupsAddLinkResponse]:
        """
        :param group_id: - Community ID.
        :param link: - Link URL.
        :param text: - Description text for the link.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addLink", params)
        if return_raw_response:
            return raw_result

        result = GroupsAddLinkResponse(**raw_result)
        return result

    async def approve_request(
        self, group_id: int, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("approveRequest", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def ban(
        self,
        group_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        reason: typing.Optional[int] = None,
        comment: typing.Optional[str] = None,
        comment_visible: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
        :param owner_id:
        :param end_date:
        :param reason:
        :param comment:
        :param comment_visible:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("ban", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def create(
        self,
        title: str,
        return_raw_response: bool = False,
        description: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        public_category: typing.Optional[int] = None,
        subtype: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsCreateResponse]:
        """
        :param title: - Community title.
        :param description: - Community description (ignored for 'type' = 'public').
        :param type: - Community type. Possible values: *'group' – group,, *'event' – event,, *'public' – public page
        :param public_category: - Category ID (for 'type' = 'public' only).
        :param subtype: - Public page subtype. Possible values: *'1' – place or small business,, *'2' – company, organization or website,, *'3' – famous person or group of people,, *'4' – product or work of art.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("create", params)
        if return_raw_response:
            return raw_result

        result = GroupsCreateResponse(**raw_result)
        return result

    async def delete_callback_server(
        self, group_id: int, server_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
        :param server_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteCallbackServer", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_link(
        self, group_id: int, link_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteLink", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def disable_online(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("disableOnline", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        group_id: int,
        return_raw_response: bool = False,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        screen_name: typing.Optional[str] = None,
        access: typing.Optional[BaseBoolInt] = None,
        website: typing.Optional[str] = None,
        subject: typing.Optional[BaseBoolInt] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        rss: typing.Optional[str] = None,
        event_start_date: typing.Optional[int] = None,
        event_finish_date: typing.Optional[int] = None,
        event_group_id: typing.Optional[int] = None,
        public_category: typing.Optional[int] = None,
        public_subcategory: typing.Optional[int] = None,
        public_date: typing.Optional[str] = None,
        wall: typing.Optional[BaseBoolInt] = None,
        topics: typing.Optional[BaseBoolInt] = None,
        photos: typing.Optional[BaseBoolInt] = None,
        video: typing.Optional[BaseBoolInt] = None,
        audio: typing.Optional[BaseBoolInt] = None,
        links: typing.Optional[BaseBoolInt] = None,
        events: typing.Optional[BaseBoolInt] = None,
        places: typing.Optional[BaseBoolInt] = None,
        contacts: typing.Optional[BaseBoolInt] = None,
        docs: typing.Optional[BaseBoolInt] = None,
        wiki: typing.Optional[BaseBoolInt] = None,
        messages: typing.Optional[BaseBoolInt] = None,
        articles: typing.Optional[bool] = None,
        addresses: typing.Optional[bool] = None,
        age_limits: typing.Optional[int] = None,
        market: typing.Optional[BaseBoolInt] = None,
        market_comments: typing.Optional[BaseBoolInt] = None,
        market_country: typing.Optional[typing.List[int]] = None,
        market_city: typing.Optional[typing.List[int]] = None,
        market_currency: typing.Optional[BaseBoolInt] = None,
        market_contact: typing.Optional[BaseBoolInt] = None,
        market_wiki: typing.Optional[int] = None,
        obscene_filter: typing.Optional[BaseBoolInt] = None,
        obscene_stopwords: typing.Optional[BaseBoolInt] = None,
        obscene_words: typing.Optional[typing.List[str]] = None,
        main_section: typing.Optional[int] = None,
        secondary_section: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param title: - Community title.
        :param description: - Community description.
        :param screen_name: - Community screen name.
        :param access: - Community type. Possible values: *'0' – open,, *'1' – closed,, *'2' – private.
        :param website: - Website that will be displayed in the community information field.
        :param subject: - Community subject. Possible values: , *'1' – auto/moto,, *'2' – activity holidays,, *'3' – business,, *'4' – pets,, *'5' – health,, *'6' – dating and communication, , *'7' – games,, *'8' – IT (computers and software),, *'9' – cinema,, *'10' – beauty and fashion,, *'11' – cooking,, *'12' – art and culture,, *'13' – literature,, *'14' – mobile services and internet,, *'15' – music,, *'16' – science and technology,, *'17' – real estate,, *'18' – news and media,, *'19' – security,, *'20' – education,, *'21' – home and renovations,, *'22' – politics,, *'23' – food,, *'24' – industry,, *'25' – travel,, *'26' – work,, *'27' – entertainment,, *'28' – religion,, *'29' – family,, *'30' – sports,, *'31' – insurance,, *'32' – television,, *'33' – goods and services,, *'34' – hobbies,, *'35' – finance,, *'36' – photo,, *'37' – esoterics,, *'38' – electronics and appliances,, *'39' – erotic,, *'40' – humor,, *'41' – society, humanities,, *'42' – design and graphics.
        :param email: - Organizer email (for events).
        :param phone: - Organizer phone number (for events).
        :param rss: - RSS feed address for import (available only to communities with special permission. Contact vk.com/support to get it.
        :param event_start_date: - Event start date in Unixtime format.
        :param event_finish_date: - Event finish date in Unixtime format.
        :param event_group_id: - Organizer community ID (for events only).
        :param public_category: - Public page category ID.
        :param public_subcategory: - Public page subcategory ID.
        :param public_date: - Founding date of a company or organization owning the community in "dd.mm.YYYY" format.
        :param wall: - Wall settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (groups and events only),, *'3' – closed (groups and events only).
        :param topics: - Board topics settings. Possbile values: , *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param photos: - Photos settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param video: - Video settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param audio: - Audio settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param links: - Links settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param events: - Events settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param places: - Places settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param contacts: - Contacts settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param docs: - Documents settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param wiki: - Wiki pages settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param messages: - Community messages. Possible values: *'0' — disabled,, *'1' — enabled.
        :param articles:
        :param addresses:
        :param age_limits: - Community age limits. Possible values: *'1' — no limits,, *'2' — 16+,, *'3' — 18+.
        :param market: - Market settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_comments: - market comments settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_country: - Market delivery countries.
        :param market_city: - Market delivery cities (if only one country is specified).
        :param market_currency: - Market currency settings. Possbile values: , *'643' – Russian rubles,, *'980' – Ukrainian hryvnia,, *'398' – Kazakh tenge,, *'978' – Euro,, *'840' – US dollars
        :param market_contact: - Seller contact for market. Set '0' for community messages.
        :param market_wiki: - ID of a wiki page with market description.
        :param obscene_filter: - Obscene expressions filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_stopwords: - Stopwords filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_words: - Keywords for stopwords filter.
        :param main_section:
        :param secondary_section:
        :param country: - Country of the community.
        :param city: - City of the community.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_address(
        self,
        group_id: int,
        address_id: int,
        return_raw_response: bool = False,
        title: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        additional_address: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        metro_id: typing.Optional[int] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        phone: typing.Optional[str] = None,
        work_info_status: typing.Optional[str] = None,
        timetable: typing.Optional[str] = None,
        is_main_address: typing.Optional[bool] = None,
    ) -> typing.Union[dict, GroupsEditAddressResponse]:
        """
        :param group_id:
        :param address_id:
        :param title:
        :param address:
        :param additional_address:
        :param country_id:
        :param city_id:
        :param metro_id:
        :param latitude:
        :param longitude:
        :param phone:
        :param work_info_status:
        :param timetable:
        :param is_main_address:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editAddress", params)
        if return_raw_response:
            return raw_result

        result = GroupsEditAddressResponse(**raw_result)
        return result

    async def edit_callback_server(
        self,
        group_id: int,
        server_id: int,
        url: str,
        title: str,
        return_raw_response: bool = False,
        secret_key: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
        :param server_id:
        :param url:
        :param title:
        :param secret_key:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editCallbackServer", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_link(
        self,
        group_id: int,
        link_id: int,
        return_raw_response: bool = False,
        text: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :param text: - New description text for the link.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editLink", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_manager(
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
        role: typing.Optional[str] = None,
        is_contact: typing.Optional[BaseBoolInt] = None,
        contact_position: typing.Optional[str] = None,
        contact_phone: typing.Optional[str] = None,
        contact_email: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param role: - Manager role. Possible values: *'moderator',, *'editor',, *'administrator'.
        :param is_contact: - '1' — to show the manager in Contacts block of the community.
        :param contact_position: - Position to show in Contacts block.
        :param contact_phone: - Contact phone.
        :param contact_email: - Contact e-mail.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editManager", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def enable_online(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("enableOnline", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        filter: typing.Optional[typing.List[GroupsFilter]] = None,
        fields: typing.Optional[typing.List[GroupsFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsGetResponse, GroupsGetExtendedResponse]:
        """
        :param user_id: - User ID.
        :param extended: - '1' — to return complete information about a user's communities, '0' — to return a list of community IDs without any additional fields (default),
        :param filter: - Types of communities to return: 'admin' — to return communities administered by the user , 'editor' — to return communities where the user is an administrator or editor, 'moder' — to return communities where the user is an administrator, editor, or moderator, 'groups' — to return only groups, 'publics' — to return only public pages, 'events' — to return only events
        :param fields: - Profile fields to return.
        :param offset: - Offset needed to return a specific subset of communities.
        :param count: - Number of communities to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = (
            GroupsGetResponse(**raw_result)
            if not extended
            else GroupsGetExtendedResponse(**raw_result)
        )
        return result

    async def get_addresses(
        self,
        group_id: int,
        return_raw_response: bool = False,
        address_ids: typing.Optional[typing.List[int]] = None,
        latitude: typing.Optional[int] = None,
        longitude: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[AddressesFields]] = None,
    ) -> typing.Union[dict, GroupsGetAddressesResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param address_ids:
        :param latitude: - Latitude of  the user geo position.
        :param longitude: - Longitude of the user geo position.
        :param offset: - Offset needed to return a specific subset of community addresses.
        :param count: - Number of community addresses to return.
        :param fields: - Address fields
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAddresses", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetAddressesResponse(**raw_result)
        return result

    async def get_banned(
        self,
        group_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsGetBannedResponse]:
        """
        :param group_id: - Community ID.
        :param offset: - Offset needed to return a specific subset of users.
        :param count: - Number of users to return.
        :param fields:
        :param owner_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getBanned", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetBannedResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        return_raw_response: bool = False,
        group_ids: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[GroupsFields]] = None,
    ) -> typing.Union[dict, GroupsGetByIdResponse]:
        """
        :param group_ids: - IDs or screen names of communities.
        :param group_id: - ID or screen name of the community.
        :param fields: - Group fields to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetByIdResponse(**raw_result)
        return result

    async def get_callback_confirmation_code(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, GroupsGetCallbackConfirmationCodeResponse]:
        """
        :param group_id: - Community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCallbackConfirmationCode", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetCallbackConfirmationCodeResponse(**raw_result)
        return result

    async def get_callback_servers(
        self,
        group_id: int,
        return_raw_response: bool = False,
        server_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, GroupsGetCallbackServersResponse]:
        """
        :param group_id:
        :param server_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCallbackServers", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetCallbackServersResponse(**raw_result)
        return result

    async def get_callback_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
        server_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsGetCallbackSettingsResponse]:
        """
        :param group_id: - Community ID.
        :param server_id: - Server ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCallbackSettings", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetCallbackSettingsResponse(**raw_result)
        return result

    async def get_catalog(
        self,
        return_raw_response: bool = False,
        category_id: typing.Optional[int] = None,
        subcategory_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsGetCatalogResponse]:
        """
        :param category_id: - Category id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :param subcategory_id: - Subcategory id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCatalog", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetCatalogResponse(**raw_result)
        return result

    async def get_catalog_info(
        self,
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        subcategories: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, GroupsGetCatalogInfoResponse, GroupsGetCatalogInfoExtendedResponse]:
        """
        :param extended: - 1 – to return communities count and three communities for preview. By default: 0.
        :param subcategories: - 1 – to return subcategories info. By default: 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCatalogInfo", params)
        if return_raw_response:
            return raw_result

        result = (
            GroupsGetCatalogInfoResponse(**raw_result)
            if not extended
            else GroupsGetCatalogInfoExtendedResponse(**raw_result)
        )
        return result

    async def get_invited_users(
        self,
        group_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> typing.Union[dict, GroupsGetInvitedUsersResponse]:
        """
        :param group_id: - Group ID to return invited users for.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param fields: - List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param name_case: - Case for declension of user name and surname. Possible values: *'nom' — nominative (default),, *'gen' — genitive,, *'dat' — dative,, *'acc' — accusative, , *'ins' — instrumental,, *'abl' — prepositional.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getInvitedUsers", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetInvitedUsersResponse(**raw_result)
        return result

    async def get_invites(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, GroupsGetInvitesResponse, GroupsGetInvitesExtendedResponse]:
        """
        :param offset: - Offset needed to return a specific subset of invitations.
        :param count: - Number of invitations to return.
        :param extended: - '1' — to return additional [vk.com/dev/fields_groups|fields] for communities..
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getInvites", params)
        if return_raw_response:
            return raw_result

        result = (
            GroupsGetInvitesResponse(**raw_result)
            if not extended
            else GroupsGetInvitesExtendedResponse(**raw_result)
        )
        return result

    async def get_long_poll_server(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, GroupsGetLongPollServerResponse]:
        """
        :param group_id: - Community ID
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLongPollServer", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetLongPollServerResponse(**raw_result)
        return result

    async def get_long_poll_settings(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, GroupsGetLongPollSettingsResponse]:
        """
        :param group_id: - Community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLongPollSettings", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetLongPollSettingsResponse(**raw_result)
        return result

    async def get_members(
        self,
        return_raw_response: bool = False,
        group_id: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        filter: typing.Optional[str] = None,
    ) -> typing.Union[dict, GroupsGetMembersResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param sort: - Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: - Offset needed to return a specific subset of community members.
        :param count: - Number of community members to return.
        :param fields: - List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter: - *'friends' – only friends in this community will be returned,, *'unsure' – only those who pressed 'I may attend' will be returned (if it's an event).
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMembers", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetMembersResponse(**raw_result)
        return result

    async def get_requests(
        self,
        group_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, GroupsGetRequestsResponse]:
        """
        :param group_id: - Community ID.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param fields: - Profile fields to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRequests", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetRequestsResponse(**raw_result)
        return result

    async def get_settings(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, GroupsGetSettingsResponse]:
        """
        :param group_id: - Community ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSettings", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetSettingsResponse(**raw_result)
        return result

    async def get_token_permissions(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, GroupsGetTokenPermissionsResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTokenPermissions", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetTokenPermissionsResponse(**raw_result)
        return result

    async def invite(
        self, group_id: int, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("invite", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def is_member(
        self,
        group_id: str,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, GroupsIsMemberResponse, GroupsIsMemberExtendedResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param user_id: - User ID.
        :param user_ids: - User IDs.
        :param extended: - '1' — to return an extended response with additional fields. By default: '0'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("isMember", params)
        if return_raw_response:
            return raw_result

        result = (
            GroupsIsMemberResponse(**raw_result)
            if not extended
            else GroupsIsMemberExtendedResponse(**raw_result)
        )
        return result

    async def join(
        self,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
        not_sure: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param not_sure: - Optional parameter which is taken into account when 'gid' belongs to the event: '1' — Perhaps I will attend, '0' — I will be there for sure (default), ,
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("join", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def leave(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("leave", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def remove_user(
        self, group_id: int, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeUser", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def reorder_link(
        self,
        group_id: int,
        link_id: int,
        return_raw_response: bool = False,
        after: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :param after: - ID of the link after which to place the link with 'link_id'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("reorderLink", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def search(
        self,
        q: str,
        return_raw_response: bool = False,
        type: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        future: typing.Optional[BaseBoolInt] = None,
        market: typing.Optional[BaseBoolInt] = None,
        sort: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, GroupsSearchResponse]:
        """
        :param q: - Search query string.
        :param type: - Community type. Possible values: 'group, page, event.'
        :param country_id: - Country ID.
        :param city_id: - City ID. If this parameter is transmitted, country_id is ignored.
        :param future: - '1' — to return only upcoming events. Works with the 'type' = 'event' only.
        :param market: - '1' — to return communities with enabled market only.
        :param sort: - Sort order. Possible values: *'0' — default sorting (similar the full version of the site),, *'1' — by growth speed,, *'2'— by the "day attendance/members number" ratio,, *'3' — by the "Likes number/members number" ratio,, *'4' — by the "comments number/members number" ratio,, *'5' — by the "boards entries number/members number" ratio.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of communities to return. "Note that you can not receive more than first thousand of results, regardless of 'count' and 'offset' values."
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = GroupsSearchResponse(**raw_result)
        return result

    async def set_callback_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
        server_id: typing.Optional[int] = None,
        api_version: typing.Optional[str] = None,
        message_new: typing.Optional[BaseBoolInt] = None,
        message_reply: typing.Optional[BaseBoolInt] = None,
        message_allow: typing.Optional[BaseBoolInt] = None,
        message_edit: typing.Optional[bool] = None,
        message_deny: typing.Optional[BaseBoolInt] = None,
        message_typing_state: typing.Optional[bool] = None,
        photo_new: typing.Optional[BaseBoolInt] = None,
        audio_new: typing.Optional[BaseBoolInt] = None,
        video_new: typing.Optional[BaseBoolInt] = None,
        wall_reply_new: typing.Optional[BaseBoolInt] = None,
        wall_reply_edit: typing.Optional[BaseBoolInt] = None,
        wall_reply_delete: typing.Optional[BaseBoolInt] = None,
        wall_reply_restore: typing.Optional[BaseBoolInt] = None,
        wall_post_new: typing.Optional[BaseBoolInt] = None,
        wall_repost: typing.Optional[BaseBoolInt] = None,
        board_post_new: typing.Optional[BaseBoolInt] = None,
        board_post_edit: typing.Optional[BaseBoolInt] = None,
        board_post_restore: typing.Optional[BaseBoolInt] = None,
        board_post_delete: typing.Optional[BaseBoolInt] = None,
        photo_comment_new: typing.Optional[BaseBoolInt] = None,
        photo_comment_edit: typing.Optional[BaseBoolInt] = None,
        photo_comment_delete: typing.Optional[BaseBoolInt] = None,
        photo_comment_restore: typing.Optional[BaseBoolInt] = None,
        video_comment_new: typing.Optional[BaseBoolInt] = None,
        video_comment_edit: typing.Optional[BaseBoolInt] = None,
        video_comment_delete: typing.Optional[BaseBoolInt] = None,
        video_comment_restore: typing.Optional[BaseBoolInt] = None,
        market_comment_new: typing.Optional[BaseBoolInt] = None,
        market_comment_edit: typing.Optional[BaseBoolInt] = None,
        market_comment_delete: typing.Optional[BaseBoolInt] = None,
        market_comment_restore: typing.Optional[BaseBoolInt] = None,
        poll_vote_new: typing.Optional[BaseBoolInt] = None,
        group_join: typing.Optional[BaseBoolInt] = None,
        group_leave: typing.Optional[BaseBoolInt] = None,
        group_change_settings: typing.Optional[bool] = None,
        group_change_photo: typing.Optional[bool] = None,
        group_officers_edit: typing.Optional[bool] = None,
        user_block: typing.Optional[bool] = None,
        user_unblock: typing.Optional[bool] = None,
        lead_forms_new: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param server_id: - Server ID.
        :param api_version:
        :param message_new: - A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: - A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: - Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit:
        :param message_deny: - Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_typing_state:
        :param photo_new: - New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: - New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: - New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: - New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: - Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: - A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: - A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: - New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: - New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: - New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: - Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: - Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: - Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: - New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: - A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: - A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: - A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: - New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: - A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: - A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: - A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: - New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: - A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: - A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: - A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: - A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: - Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: - Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: - User added to community blacklist
        :param user_unblock: - User removed from community blacklist
        :param lead_forms_new: - New form in lead forms
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setCallbackSettings", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_long_poll_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
        enabled: typing.Optional[BaseBoolInt] = None,
        api_version: typing.Optional[str] = None,
        message_new: typing.Optional[BaseBoolInt] = None,
        message_reply: typing.Optional[BaseBoolInt] = None,
        message_allow: typing.Optional[BaseBoolInt] = None,
        message_deny: typing.Optional[BaseBoolInt] = None,
        message_edit: typing.Optional[BaseBoolInt] = None,
        message_typing_state: typing.Optional[bool] = None,
        photo_new: typing.Optional[BaseBoolInt] = None,
        audio_new: typing.Optional[BaseBoolInt] = None,
        video_new: typing.Optional[BaseBoolInt] = None,
        wall_reply_new: typing.Optional[BaseBoolInt] = None,
        wall_reply_edit: typing.Optional[BaseBoolInt] = None,
        wall_reply_delete: typing.Optional[BaseBoolInt] = None,
        wall_reply_restore: typing.Optional[BaseBoolInt] = None,
        wall_post_new: typing.Optional[BaseBoolInt] = None,
        wall_repost: typing.Optional[BaseBoolInt] = None,
        board_post_new: typing.Optional[BaseBoolInt] = None,
        board_post_edit: typing.Optional[BaseBoolInt] = None,
        board_post_restore: typing.Optional[BaseBoolInt] = None,
        board_post_delete: typing.Optional[BaseBoolInt] = None,
        photo_comment_new: typing.Optional[BaseBoolInt] = None,
        photo_comment_edit: typing.Optional[BaseBoolInt] = None,
        photo_comment_delete: typing.Optional[BaseBoolInt] = None,
        photo_comment_restore: typing.Optional[BaseBoolInt] = None,
        video_comment_new: typing.Optional[BaseBoolInt] = None,
        video_comment_edit: typing.Optional[BaseBoolInt] = None,
        video_comment_delete: typing.Optional[BaseBoolInt] = None,
        video_comment_restore: typing.Optional[BaseBoolInt] = None,
        market_comment_new: typing.Optional[BaseBoolInt] = None,
        market_comment_edit: typing.Optional[BaseBoolInt] = None,
        market_comment_delete: typing.Optional[BaseBoolInt] = None,
        market_comment_restore: typing.Optional[BaseBoolInt] = None,
        poll_vote_new: typing.Optional[BaseBoolInt] = None,
        group_join: typing.Optional[BaseBoolInt] = None,
        group_leave: typing.Optional[BaseBoolInt] = None,
        group_change_settings: typing.Optional[bool] = None,
        group_change_photo: typing.Optional[bool] = None,
        group_officers_edit: typing.Optional[bool] = None,
        user_block: typing.Optional[bool] = None,
        user_unblock: typing.Optional[bool] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Community ID.
        :param enabled: - Sets whether Long Poll is enabled ('0' — disabled, '1' — enabled).
        :param api_version:
        :param message_new: - A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: - A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: - Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_deny: - Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit: - A message has been edited ('0' — disabled, '1' — enabled).
        :param message_typing_state:
        :param photo_new: - New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: - New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: - New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: - New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: - Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: - A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: - A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: - New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: - New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: - New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: - Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: - Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: - Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: - New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: - A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: - A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: - A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: - New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: - A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: - A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: - A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: - New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: - A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: - A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: - A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: - A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: - Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: - Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: - User added to community blacklist
        :param user_unblock: - User removed from community blacklist
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setLongPollSettings", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def unban(
        self,
        group_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id:
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
