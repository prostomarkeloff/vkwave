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
        additional_address: Optional[str] = None,
        metro_id: Optional[int] = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
    ) -> Union[dict, GroupsAddAddressResponse]:
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
        secret_key: Optional[str] = None,
    ) -> Union[dict, GroupsAddCallbackServerResponse]:
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
        text: Optional[str] = None,
    ) -> Union[dict, GroupsAddLinkResponse]:
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
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def ban(
        self,
        group_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
        end_date: Optional[int] = None,
        reason: Optional[int] = None,
        comment: Optional[str] = None,
        comment_visible: Optional[bool] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def create(
        self,
        title: str,
        return_raw_response: bool = False,
        description: Optional[str] = None,
        type: Optional[str] = None,
        public_category: Optional[int] = None,
        subtype: Optional[int] = None,
    ) -> Union[dict, GroupsCreateResponse]:
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

    async def delete_address(
        self,
        group_id: int,
        address_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id:
        :param address_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteAddress", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def delete_callback_server(
        self,
        group_id: int,
        server_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def delete_link(
        self,
        group_id: int,
        link_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def disable_online(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("disableOnline", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def edit(
        self,
        group_id: int,
        return_raw_response: bool = False,
        title: Optional[str] = None,
        description: Optional[str] = None,
        screen_name: Optional[str] = None,
        access: Optional[int] = None,
        website: Optional[str] = None,
        subject: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        rss: Optional[str] = None,
        event_start_date: Optional[int] = None,
        event_finish_date: Optional[int] = None,
        event_group_id: Optional[int] = None,
        public_category: Optional[int] = None,
        public_subcategory: Optional[int] = None,
        public_date: Optional[str] = None,
        wall: Optional[int] = None,
        topics: Optional[int] = None,
        photos: Optional[int] = None,
        video: Optional[int] = None,
        audio: Optional[int] = None,
        links: Optional[BaseBoolInt] = None,
        events: Optional[BaseBoolInt] = None,
        places: Optional[BaseBoolInt] = None,
        contacts: Optional[BaseBoolInt] = None,
        docs: Optional[int] = None,
        wiki: Optional[int] = None,
        messages: Optional[BaseBoolInt] = None,
        articles: Optional[bool] = None,
        addresses: Optional[bool] = None,
        age_limits: Optional[int] = None,
        market: Optional[BaseBoolInt] = None,
        market_comments: Optional[BaseBoolInt] = None,
        market_country: Optional[List[int]] = None,
        market_city: Optional[List[int]] = None,
        market_currency: Optional[int] = None,
        market_contact: Optional[int] = None,
        market_wiki: Optional[int] = None,
        obscene_filter: Optional[BaseBoolInt] = None,
        obscene_stopwords: Optional[BaseBoolInt] = None,
        obscene_words: Optional[List[str]] = None,
        main_section: Optional[int] = None,
        secondary_section: Optional[int] = None,
        country: Optional[int] = None,
        city: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def edit_address(
        self,
        group_id: int,
        address_id: int,
        return_raw_response: bool = False,
        title: Optional[str] = None,
        address: Optional[str] = None,
        additional_address: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        metro_id: Optional[int] = None,
        latitude: Optional[int] = None,
        longitude: Optional[int] = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
    ) -> Union[dict, GroupsEditAddressResponse]:
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
        secret_key: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def edit_link(
        self,
        group_id: int,
        link_id: int,
        return_raw_response: bool = False,
        text: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def edit_manager(
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
        role: Optional[str] = None,
        is_contact: Optional[BaseBoolInt] = None,
        contact_position: Optional[str] = None,
        contact_phone: Optional[str] = None,
        contact_email: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param role: - Manager role. Possible values: *'moderator',, *'editor',, *'administrator',, *'advertiser'.
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

        result = BaseOkResponse(**raw_result)
        return result

    async def enable_online(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("enableOnline", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
        extended: Optional[BaseBoolInt] = None,
        filter: Optional[List[GroupsFilter]] = None,
        fields: Optional[List[GroupsFields]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, GroupsGetResponse]:
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
            else GroupsGetObjectExtendedResponse(**raw_result)
        )
        return result

    async def get_addresses(
        self,
        group_id: int,
        return_raw_response: bool = False,
        address_ids: Optional[List[int]] = None,
        latitude: Optional[int] = None,
        longitude: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[AddressesFields]] = None,
    ) -> Union[dict, GroupsGetAddressesResponse]:
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
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[BaseUserGroupFields]] = None,
        owner_id: Optional[int] = None,
    ) -> Union[dict, GroupsGetBannedResponse]:
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
        group_ids: Optional[List[str]] = None,
        group_id: Optional[str] = None,
        fields: Optional[List[GroupsFields]] = None,
    ) -> Union[dict, GroupsGetByIdObjectLegacyResponse]:
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

        result = GroupsGetByIdObjectLegacyResponse(**raw_result)
        return result

    async def get_callback_confirmation_code(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetCallbackConfirmationCodeResponse]:
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
        server_ids: Optional[List[int]] = None,
    ) -> Union[dict, GroupsGetCallbackServersResponse]:
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
        server_id: Optional[int] = None,
    ) -> Union[dict, GroupsGetCallbackSettingsResponse]:
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
        category_id: Optional[int] = None,
        subcategory_id: Optional[int] = None,
    ) -> Union[dict, GroupsGetCatalogResponse]:
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
        extended: Optional[BaseBoolInt] = None,
        subcategories: Optional[BaseBoolInt] = None,
    ) -> Union[dict, GroupsGetCatalogInfoResponse, GroupsGetCatalogInfoExtendedResponse]:
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
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
        name_case: Optional[str] = None,
    ) -> Union[dict, GroupsGetInvitedUsersResponse]:
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
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[BaseBoolInt] = None,
    ) -> Union[dict, GroupsGetInvitesResponse, GroupsGetInvitesExtendedResponse]:
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
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetLongPollServerResponse]:
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
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetLongPollSettingsResponse]:
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
        group_id: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
        filter: Optional[str] = None,
    ) -> Union[dict, GroupsGetMembersResponse, GroupsGetMembersFieldsResponse]:
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

        result = (
            GroupsGetMembersResponse(**raw_result)
            if (not fields) and (not filter)
            else GroupsGetMembersFieldsResponse(**raw_result)
        )
        return result

    async def get_requests(
        self,
        group_id: int,
        return_raw_response: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
    ) -> Union[dict, GroupsGetRequestsResponse, GroupsGetRequestsFieldsResponse]:
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

        result = (
            GroupsGetRequestsResponse(**raw_result)
            if not fields
            else GroupsGetRequestsFieldsResponse(**raw_result)
        )
        return result

    async def get_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetSettingsResponse]:
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

    async def get_tag_list(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetTagListResponse]:
        """
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTagList", params)
        if return_raw_response:
            return raw_result

        result = GroupsGetTagListResponse(**raw_result)
        return result

    async def get_token_permissions(
        self,
        return_raw_response: bool = False,
    ) -> Union[dict, GroupsGetTokenPermissionsResponse]:
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
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def is_member(
        self,
        group_id: str,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
        user_ids: Optional[List[int]] = None,
        extended: Optional[BaseBoolInt] = None,
    ) -> Union[dict, GroupsIsMemberResponse, GroupsIsMemberExtendedResponse]:
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
        group_id: Optional[int] = None,
        not_sure: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def leave(
        self,
        group_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id: - ID or screen name of the community.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("leave", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def remove_user(
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def reorder_link(
        self,
        group_id: int,
        link_id: int,
        return_raw_response: bool = False,
        after: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result

    async def search(
        self,
        q: str,
        return_raw_response: bool = False,
        type: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        future: Optional[BaseBoolInt] = None,
        market: Optional[BaseBoolInt] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, GroupsSearchResponse]:
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
        server_id: Optional[int] = None,
        api_version: Optional[str] = None,
        message_new: Optional[BaseBoolInt] = None,
        message_reply: Optional[BaseBoolInt] = None,
        message_allow: Optional[BaseBoolInt] = None,
        message_edit: Optional[bool] = None,
        message_deny: Optional[BaseBoolInt] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[BaseBoolInt] = None,
        audio_new: Optional[BaseBoolInt] = None,
        video_new: Optional[BaseBoolInt] = None,
        wall_reply_new: Optional[BaseBoolInt] = None,
        wall_reply_edit: Optional[BaseBoolInt] = None,
        wall_reply_delete: Optional[BaseBoolInt] = None,
        wall_reply_restore: Optional[BaseBoolInt] = None,
        wall_post_new: Optional[BaseBoolInt] = None,
        wall_repost: Optional[BaseBoolInt] = None,
        board_post_new: Optional[BaseBoolInt] = None,
        board_post_edit: Optional[BaseBoolInt] = None,
        board_post_restore: Optional[BaseBoolInt] = None,
        board_post_delete: Optional[BaseBoolInt] = None,
        photo_comment_new: Optional[BaseBoolInt] = None,
        photo_comment_edit: Optional[BaseBoolInt] = None,
        photo_comment_delete: Optional[BaseBoolInt] = None,
        photo_comment_restore: Optional[BaseBoolInt] = None,
        video_comment_new: Optional[BaseBoolInt] = None,
        video_comment_edit: Optional[BaseBoolInt] = None,
        video_comment_delete: Optional[BaseBoolInt] = None,
        video_comment_restore: Optional[BaseBoolInt] = None,
        market_comment_new: Optional[BaseBoolInt] = None,
        market_comment_edit: Optional[BaseBoolInt] = None,
        market_comment_delete: Optional[BaseBoolInt] = None,
        market_comment_restore: Optional[BaseBoolInt] = None,
        market_order_new: Optional[bool] = None,
        market_order_edit: Optional[bool] = None,
        poll_vote_new: Optional[BaseBoolInt] = None,
        group_join: Optional[BaseBoolInt] = None,
        group_leave: Optional[BaseBoolInt] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        lead_forms_new: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        donut_subscription_create: Optional[bool] = None,
        donut_subscription_prolonged: Optional[bool] = None,
        donut_subscription_cancelled: Optional[bool] = None,
        donut_subscription_price_changed: Optional[bool] = None,
        donut_subscription_expired: Optional[bool] = None,
        donut_money_withdraw: Optional[bool] = None,
        donut_money_withdraw_error: Optional[bool] = None,
    ) -> Union[dict, BaseOkResponse]:
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
        :param market_order_new:
        :param market_order_edit:
        :param poll_vote_new: - A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: - Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: - Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: - User added to community blacklist
        :param user_unblock: - User removed from community blacklist
        :param lead_forms_new: - New form in lead forms
        :param like_add:
        :param like_remove:
        :param message_event:
        :param donut_subscription_create:
        :param donut_subscription_prolonged:
        :param donut_subscription_cancelled:
        :param donut_subscription_price_changed:
        :param donut_subscription_expired:
        :param donut_money_withdraw:
        :param donut_money_withdraw_error:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setCallbackSettings", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def set_long_poll_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
        enabled: Optional[BaseBoolInt] = None,
        api_version: Optional[str] = None,
        message_new: Optional[BaseBoolInt] = None,
        message_reply: Optional[BaseBoolInt] = None,
        message_allow: Optional[BaseBoolInt] = None,
        message_deny: Optional[BaseBoolInt] = None,
        message_edit: Optional[BaseBoolInt] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[BaseBoolInt] = None,
        audio_new: Optional[BaseBoolInt] = None,
        video_new: Optional[BaseBoolInt] = None,
        wall_reply_new: Optional[BaseBoolInt] = None,
        wall_reply_edit: Optional[BaseBoolInt] = None,
        wall_reply_delete: Optional[BaseBoolInt] = None,
        wall_reply_restore: Optional[BaseBoolInt] = None,
        wall_post_new: Optional[BaseBoolInt] = None,
        wall_repost: Optional[BaseBoolInt] = None,
        board_post_new: Optional[BaseBoolInt] = None,
        board_post_edit: Optional[BaseBoolInt] = None,
        board_post_restore: Optional[BaseBoolInt] = None,
        board_post_delete: Optional[BaseBoolInt] = None,
        photo_comment_new: Optional[BaseBoolInt] = None,
        photo_comment_edit: Optional[BaseBoolInt] = None,
        photo_comment_delete: Optional[BaseBoolInt] = None,
        photo_comment_restore: Optional[BaseBoolInt] = None,
        video_comment_new: Optional[BaseBoolInt] = None,
        video_comment_edit: Optional[BaseBoolInt] = None,
        video_comment_delete: Optional[BaseBoolInt] = None,
        video_comment_restore: Optional[BaseBoolInt] = None,
        market_comment_new: Optional[BaseBoolInt] = None,
        market_comment_edit: Optional[BaseBoolInt] = None,
        market_comment_delete: Optional[BaseBoolInt] = None,
        market_comment_restore: Optional[BaseBoolInt] = None,
        poll_vote_new: Optional[BaseBoolInt] = None,
        group_join: Optional[BaseBoolInt] = None,
        group_leave: Optional[BaseBoolInt] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        donut_subscription_create: Optional[bool] = None,
        donut_subscription_prolonged: Optional[bool] = None,
        donut_subscription_cancelled: Optional[bool] = None,
        donut_subscription_price_changed: Optional[bool] = None,
        donut_subscription_expired: Optional[bool] = None,
        donut_money_withdraw: Optional[bool] = None,
        donut_money_withdraw_error: Optional[bool] = None,
    ) -> Union[dict, BaseOkResponse]:
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
        :param like_add:
        :param like_remove:
        :param message_event:
        :param donut_subscription_create:
        :param donut_subscription_prolonged:
        :param donut_subscription_cancelled:
        :param donut_subscription_price_changed:
        :param donut_subscription_expired:
        :param donut_money_withdraw:
        :param donut_money_withdraw_error:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setLongPollSettings", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def set_settings(
        self,
        group_id: int,
        return_raw_response: bool = False,
        messages: Optional[bool] = None,
        bots_capabilities: Optional[bool] = None,
        bots_start_button: Optional[bool] = None,
        bots_add_to_chat: Optional[bool] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id:
        :param messages:
        :param bots_capabilities:
        :param bots_start_button:
        :param bots_add_to_chat:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setSettings", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def set_user_note(
        self,
        group_id: int,
        user_id: int,
        return_raw_response: bool = False,
        note: Optional[str] = None,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param group_id:
        :param user_id:
        :param note: - Note body
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setUserNote", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def tag_add(
        self,
        group_id: int,
        tag_name: str,
        return_raw_response: bool = False,
        tag_color: Optional[str] = None,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param group_id:
        :param tag_name:
        :param tag_color:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("tagAdd", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def tag_bind(
        self,
        group_id: int,
        tag_id: int,
        user_id: int,
        act: str,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param group_id:
        :param tag_id:
        :param user_id:
        :param act: - Describe the action
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("tagBind", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def tag_delete(
        self,
        group_id: int,
        tag_id: int,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param group_id:
        :param tag_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("tagDelete", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def tag_update(
        self,
        group_id: int,
        tag_id: int,
        tag_name: str,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseBoolResponse]:
        """
        :param group_id:
        :param tag_id:
        :param tag_name:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("tagUpdate", params)
        if return_raw_response:
            return raw_result

        result = BaseBoolResponse(**raw_result)
        return result

    async def toggle_market(
        self,
        group_id: int,
        state: str,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param group_id:
        :param state:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("toggleMarket", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def unban(
        self,
        group_id: int,
        return_raw_response: bool = False,
        owner_id: Optional[int] = None,
    ) -> Union[dict, BaseOkResponse]:
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

        result = BaseOkResponse(**raw_result)
        return result
