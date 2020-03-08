from vkwave_types.responses import *
from ._category import Category


class Groups(Category):
    def add_address(
        self,
        group_id: typing.Optional[int],
        title: typing.Optional[str],
        address: typing.Optional[str],
        additional_address: typing.Optional[str],
        country_id: typing.Optional[int],
        city_id: typing.Optional[int],
        metro_id: typing.Optional[int],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        phone: typing.Optional[str],
        work_info_status: typing.Optional[str],
        timetable: typing.Optional[str],
        is_main_address: typing.Optional[bool],
    ) -> GroupsAddAddressResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addAddress", params)
        result = GroupsAddAddressResponse(**raw_result)
        return result

    def add_callback_server(
        self,
        group_id: typing.Optional[int],
        url: typing.Optional[str],
        title: typing.Optional[str],
        secret_key: typing.Optional[str],
    ) -> GroupsAddCallbackServerResponse:
        """
        :param group_id:
        :param url:
        :param title:
        :param secret_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addCallbackServer", params)
        result = GroupsAddCallbackServerResponse(**raw_result)
        return result

    def add_link(
        self,
        group_id: typing.Optional[int],
        link: typing.Optional[str],
        text: typing.Optional[str],
    ) -> GroupsAddLinkResponse:
        """
        :param group_id: - Community ID.
        :param link: - Link URL.
        :param text: - Description text for the link.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addLink", params)
        result = GroupsAddLinkResponse(**raw_result)
        return result

    def approve_request(
        self, group_id: typing.Optional[int], user_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("approveRequest", params)
        result = OkResponse(**raw_result)
        return result

    def ban(
        self,
        group_id: typing.Optional[int],
        owner_id: typing.Optional[int],
        end_date: typing.Optional[int],
        reason: typing.Optional[int],
        comment: typing.Optional[str],
        comment_visible: typing.Optional[bool],
    ) -> OkResponse:
        """
        :param group_id:
        :param owner_id:
        :param end_date:
        :param reason:
        :param comment:
        :param comment_visible:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("ban", params)
        result = OkResponse(**raw_result)
        return result

    def create(
        self,
        title: typing.Optional[str],
        description: typing.Optional[str],
        type: typing.Optional[str],
        public_category: typing.Optional[int],
        subtype: typing.Optional[int],
    ) -> GroupsCreateResponse:
        """
        :param title: - Community title.
        :param description: - Community description (ignored for 'type' = 'public').
        :param type: - Community type. Possible values: *'group' – group,, *'event' – event,, *'public' – public page
        :param public_category: - Category ID (for 'type' = 'public' only).
        :param subtype: - Public page subtype. Possible values: *'1' – place or small business,, *'2' – company, organization or website,, *'3' – famous person or group of people,, *'4' – product or work of art.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("create", params)
        result = GroupsCreateResponse(**raw_result)
        return result

    def delete_callback_server(
        self, group_id: typing.Optional[int], server_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id:
        :param server_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteCallbackServer", params)
        result = OkResponse(**raw_result)
        return result

    def delete_link(
        self, group_id: typing.Optional[int], link_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteLink", params)
        result = OkResponse(**raw_result)
        return result

    def disable_online(self, group_id: typing.Optional[int],) -> OkResponse:
        """
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("disableOnline", params)
        result = OkResponse(**raw_result)
        return result

    def edit(
        self,
        group_id: typing.Optional[int],
        title: typing.Optional[str],
        description: typing.Optional[str],
        screen_name: typing.Optional[str],
        access: typing.Optional[int],
        website: typing.Optional[str],
        subject: typing.Optional[str],
        email: typing.Optional[str],
        phone: typing.Optional[str],
        rss: typing.Optional[str],
        event_start_date: typing.Optional[int],
        event_finish_date: typing.Optional[int],
        event_group_id: typing.Optional[int],
        public_category: typing.Optional[int],
        public_subcategory: typing.Optional[int],
        public_date: typing.Optional[str],
        wall: typing.Optional[int],
        topics: typing.Optional[int],
        photos: typing.Optional[int],
        video: typing.Optional[int],
        audio: typing.Optional[int],
        links: typing.Optional[bool],
        events: typing.Optional[bool],
        places: typing.Optional[bool],
        contacts: typing.Optional[bool],
        docs: typing.Optional[int],
        wiki: typing.Optional[int],
        messages: typing.Optional[bool],
        articles: typing.Optional[bool],
        addresses: typing.Optional[bool],
        age_limits: typing.Optional[int],
        market: typing.Optional[bool],
        market_comments: typing.Optional[bool],
        market_country: typing.Optional[typing.List[int]],
        market_city: typing.Optional[typing.List[int]],
        market_currency: typing.Optional[int],
        market_contact: typing.Optional[int],
        market_wiki: typing.Optional[int],
        obscene_filter: typing.Optional[bool],
        obscene_stopwords: typing.Optional[bool],
        obscene_words: typing.Optional[typing.List[str]],
        main_section: typing.Optional[int],
        secondary_section: typing.Optional[int],
        country: typing.Optional[int],
        city: typing.Optional[int],
    ) -> OkResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def edit_address(
        self,
        group_id: typing.Optional[int],
        address_id: typing.Optional[int],
        title: typing.Optional[str],
        address: typing.Optional[str],
        additional_address: typing.Optional[str],
        country_id: typing.Optional[int],
        city_id: typing.Optional[int],
        metro_id: typing.Optional[int],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        phone: typing.Optional[str],
        work_info_status: typing.Optional[str],
        timetable: typing.Optional[str],
        is_main_address: typing.Optional[bool],
    ) -> GroupsEditAddressResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editAddress", params)
        result = GroupsEditAddressResponse(**raw_result)
        return result

    def edit_callback_server(
        self,
        group_id: typing.Optional[int],
        server_id: typing.Optional[int],
        url: typing.Optional[str],
        title: typing.Optional[str],
        secret_key: typing.Optional[str],
    ) -> OkResponse:
        """
        :param group_id:
        :param server_id:
        :param url:
        :param title:
        :param secret_key:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editCallbackServer", params)
        result = OkResponse(**raw_result)
        return result

    def edit_link(
        self,
        group_id: typing.Optional[int],
        link_id: typing.Optional[int],
        text: typing.Optional[str],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :param text: - New description text for the link.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editLink", params)
        result = OkResponse(**raw_result)
        return result

    def edit_manager(
        self,
        group_id: typing.Optional[int],
        user_id: typing.Optional[int],
        role: typing.Optional[str],
        is_contact: typing.Optional[bool],
        contact_position: typing.Optional[str],
        contact_phone: typing.Optional[str],
        contact_email: typing.Optional[str],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :param role: - Manager role. Possible values: *'moderator',, *'editor',, *'administrator'.
        :param is_contact: - '1' — to show the manager in Contacts block of the community.
        :param contact_position: - Position to show in Contacts block.
        :param contact_phone: - Contact phone.
        :param contact_email: - Contact e-mail.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("editManager", params)
        result = OkResponse(**raw_result)
        return result

    def enable_online(self, group_id: typing.Optional[int],) -> OkResponse:
        """
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("enableOnline", params)
        result = OkResponse(**raw_result)
        return result

    def get(
        self,
        user_id: typing.Optional[int],
        extended: typing.Optional[bool],
        filter: typing.Optional[typing.List[GroupsFilter]],
        fields: typing.Optional[typing.List[GroupsFields]],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> GroupsGetResponse:
        """
        :param user_id: - User ID.
        :param extended: - '1' — to return complete information about a user's communities, '0' — to return a list of community IDs without any additional fields (default),
        :param filter: - Types of communities to return: 'admin' — to return communities administered by the user , 'editor' — to return communities where the user is an administrator or editor, 'moder' — to return communities where the user is an administrator, editor, or moderator, 'groups' — to return only groups, 'publics' — to return only public pages, 'events' — to return only events
        :param fields: - Profile fields to return.
        :param offset: - Offset needed to return a specific subset of communities.
        :param count: - Number of communities to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = GroupsGetResponse(**raw_result)
        return result

    def get_addresses(
        self,
        group_id: typing.Optional[int],
        address_ids: typing.Optional[typing.List[int]],
        latitude: typing.Optional[int],
        longitude: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[AddressesFields]],
    ) -> GroupsGetAddressesResponse:
        """
        :param group_id: - ID or screen name of the community.
        :param address_ids:
        :param latitude: - Latitude of  the user geo position.
        :param longitude: - Longitude of the user geo position.
        :param offset: - Offset needed to return a specific subset of community addresses.
        :param count: - Number of community addresses to return.
        :param fields: - Address fields
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAddresses", params)
        result = GroupsGetAddressesResponse(**raw_result)
        return result

    def get_banned(
        self,
        group_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[BaseUserGroupFields]],
        owner_id: typing.Optional[int],
    ) -> GroupsGetBannedResponse:
        """
        :param group_id: - Community ID.
        :param offset: - Offset needed to return a specific subset of users.
        :param count: - Number of users to return.
        :param fields:
        :param owner_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getBanned", params)
        result = GroupsGetBannedResponse(**raw_result)
        return result

    def get_by_id(
        self,
        group_ids: typing.Optional[typing.List[str]],
        group_id: typing.Optional[str],
        fields: typing.Optional[typing.List[GroupsFields]],
    ) -> GroupsGetByIdResponse:
        """
        :param group_ids: - IDs or screen names of communities.
        :param group_id: - ID or screen name of the community.
        :param fields: - Group fields to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = GroupsGetByIdResponse(**raw_result)
        return result

    def get_callback_confirmation_code(
        self, group_id: typing.Optional[int],
    ) -> GroupsGetCallbackConfirmationCodeResponse:
        """
        :param group_id: - Community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCallbackConfirmationCode", params)
        result = GroupsGetCallbackConfirmationCodeResponse(**raw_result)
        return result

    def get_callback_servers(
        self,
        group_id: typing.Optional[int],
        server_ids: typing.Optional[typing.List[int]],
    ) -> GroupsGetCallbackServersResponse:
        """
        :param group_id:
        :param server_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCallbackServers", params)
        result = GroupsGetCallbackServersResponse(**raw_result)
        return result

    def get_callback_settings(
        self, group_id: typing.Optional[int], server_id: typing.Optional[int],
    ) -> GroupsGetCallbackSettingsResponse:
        """
        :param group_id: - Community ID.
        :param server_id: - Server ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCallbackSettings", params)
        result = GroupsGetCallbackSettingsResponse(**raw_result)
        return result

    def get_catalog(
        self, category_id: typing.Optional[int], subcategory_id: typing.Optional[int],
    ) -> GroupsGetCatalogResponse:
        """
        :param category_id: - Category id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :param subcategory_id: - Subcategory id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCatalog", params)
        result = GroupsGetCatalogResponse(**raw_result)
        return result

    def get_catalog_info(
        self, extended: typing.Optional[bool], subcategories: typing.Optional[bool],
    ) -> GroupsGetCatalogInfoResponse:
        """
        :param extended: - 1 – to return communities count and three communities for preview. By default: 0.
        :param subcategories: - 1 – to return subcategories info. By default: 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCatalogInfo", params)
        result = GroupsGetCatalogInfoResponse(**raw_result)
        return result

    def get_invited_users(
        self,
        group_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[UsersFields]],
        name_case: typing.Optional[str],
    ) -> GroupsGetInvitedUsersResponse:
        """
        :param group_id: - Group ID to return invited users for.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param fields: - List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param name_case: - Case for declension of user name and surname. Possible values: *'nom' — nominative (default),, *'gen' — genitive,, *'dat' — dative,, *'acc' — accusative, , *'ins' — instrumental,, *'abl' — prepositional.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getInvitedUsers", params)
        result = GroupsGetInvitedUsersResponse(**raw_result)
        return result

    def get_invites(
        self,
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> GroupsGetInvitesResponse:
        """
        :param offset: - Offset needed to return a specific subset of invitations.
        :param count: - Number of invitations to return.
        :param extended: - '1' — to return additional [vk.com/dev/fields_groups|fields] for communities..
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getInvites", params)
        result = GroupsGetInvitesResponse(**raw_result)
        return result

    def get_long_poll_server(
        self, group_id: typing.Optional[int],
    ) -> GroupsGetLongPollServerResponse:
        """
        :param group_id: - Community ID
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLongPollServer", params)
        result = GroupsGetLongPollServerResponse(**raw_result)
        return result

    def get_long_poll_settings(
        self, group_id: typing.Optional[int],
    ) -> GroupsGetLongPollSettingsResponse:
        """
        :param group_id: - Community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getLongPollSettings", params)
        result = GroupsGetLongPollSettingsResponse(**raw_result)
        return result

    def get_members(
        self,
        group_id: typing.Optional[str],
        sort: typing.Optional[str],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[UsersFields]],
        filter: typing.Optional[str],
    ) -> GroupsGetMembersResponse:
        """
        :param group_id: - ID or screen name of the community.
        :param sort: - Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: - Offset needed to return a specific subset of community members.
        :param count: - Number of community members to return.
        :param fields: - List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter: - *'friends' – only friends in this community will be returned,, *'unsure' – only those who pressed 'I may attend' will be returned (if it's an event).
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMembers", params)
        result = GroupsGetMembersResponse(**raw_result)
        return result

    def get_requests(
        self,
        group_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[UsersFields]],
    ) -> GroupsGetRequestsResponse:
        """
        :param group_id: - Community ID.
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :param fields: - Profile fields to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRequests", params)
        result = GroupsGetRequestsResponse(**raw_result)
        return result

    def get_settings(
        self, group_id: typing.Optional[int],
    ) -> GroupsGetSettingsResponse:
        """
        :param group_id: - Community ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSettings", params)
        result = GroupsGetSettingsResponse(**raw_result)
        return result

    def get_token_permissions(self,) -> GroupsGetTokenPermissionsResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTokenPermissions", params)
        result = GroupsGetTokenPermissionsResponse(**raw_result)
        return result

    def invite(
        self, group_id: typing.Optional[int], user_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("invite", params)
        result = OkResponse(**raw_result)
        return result

    def is_member(
        self,
        group_id: typing.Optional[str],
        user_id: typing.Optional[int],
        user_ids: typing.Optional[typing.List[int]],
        extended: typing.Optional[bool],
    ) -> GroupsIsMemberResponse:
        """
        :param group_id: - ID or screen name of the community.
        :param user_id: - User ID.
        :param user_ids: - User IDs.
        :param extended: - '1' — to return an extended response with additional fields. By default: '0'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("isMember", params)
        result = GroupsIsMemberResponse(**raw_result)
        return result

    def join(
        self, group_id: typing.Optional[int], not_sure: typing.Optional[str],
    ) -> OkResponse:
        """
        :param group_id: - ID or screen name of the community.
        :param not_sure: - Optional parameter which is taken into account when 'gid' belongs to the event: '1' — Perhaps I will attend, '0' — I will be there for sure (default), ,
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("join", params)
        result = OkResponse(**raw_result)
        return result

    def leave(self, group_id: typing.Optional[int],) -> OkResponse:
        """
        :param group_id: - ID or screen name of the community.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("leave", params)
        result = OkResponse(**raw_result)
        return result

    def remove_user(
        self, group_id: typing.Optional[int], user_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param user_id: - User ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeUser", params)
        result = OkResponse(**raw_result)
        return result

    def reorder_link(
        self,
        group_id: typing.Optional[int],
        link_id: typing.Optional[int],
        after: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id: - Community ID.
        :param link_id: - Link ID.
        :param after: - ID of the link after which to place the link with 'link_id'.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("reorderLink", params)
        result = OkResponse(**raw_result)
        return result

    def search(
        self,
        q: typing.Optional[str],
        type: typing.Optional[str],
        country_id: typing.Optional[int],
        city_id: typing.Optional[int],
        future: typing.Optional[bool],
        market: typing.Optional[bool],
        sort: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> GroupsSearchResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("search", params)
        result = GroupsSearchResponse(**raw_result)
        return result

    def set_callback_settings(
        self,
        group_id: typing.Optional[int],
        server_id: typing.Optional[int],
        api_version: typing.Optional[str],
        message_new: typing.Optional[bool],
        message_reply: typing.Optional[bool],
        message_allow: typing.Optional[bool],
        message_edit: typing.Optional[bool],
        message_deny: typing.Optional[bool],
        message_typing_state: typing.Optional[bool],
        photo_new: typing.Optional[bool],
        audio_new: typing.Optional[bool],
        video_new: typing.Optional[bool],
        wall_reply_new: typing.Optional[bool],
        wall_reply_edit: typing.Optional[bool],
        wall_reply_delete: typing.Optional[bool],
        wall_reply_restore: typing.Optional[bool],
        wall_post_new: typing.Optional[bool],
        wall_repost: typing.Optional[bool],
        board_post_new: typing.Optional[bool],
        board_post_edit: typing.Optional[bool],
        board_post_restore: typing.Optional[bool],
        board_post_delete: typing.Optional[bool],
        photo_comment_new: typing.Optional[bool],
        photo_comment_edit: typing.Optional[bool],
        photo_comment_delete: typing.Optional[bool],
        photo_comment_restore: typing.Optional[bool],
        video_comment_new: typing.Optional[bool],
        video_comment_edit: typing.Optional[bool],
        video_comment_delete: typing.Optional[bool],
        video_comment_restore: typing.Optional[bool],
        market_comment_new: typing.Optional[bool],
        market_comment_edit: typing.Optional[bool],
        market_comment_delete: typing.Optional[bool],
        market_comment_restore: typing.Optional[bool],
        poll_vote_new: typing.Optional[bool],
        group_join: typing.Optional[bool],
        group_leave: typing.Optional[bool],
        group_change_settings: typing.Optional[bool],
        group_change_photo: typing.Optional[bool],
        group_officers_edit: typing.Optional[bool],
        user_block: typing.Optional[bool],
        user_unblock: typing.Optional[bool],
        lead_forms_new: typing.Optional[bool],
    ) -> OkResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setCallbackSettings", params)
        result = OkResponse(**raw_result)
        return result

    def set_long_poll_settings(
        self,
        group_id: typing.Optional[int],
        enabled: typing.Optional[bool],
        api_version: typing.Optional[str],
        message_new: typing.Optional[bool],
        message_reply: typing.Optional[bool],
        message_allow: typing.Optional[bool],
        message_deny: typing.Optional[bool],
        message_edit: typing.Optional[bool],
        message_typing_state: typing.Optional[bool],
        photo_new: typing.Optional[bool],
        audio_new: typing.Optional[bool],
        video_new: typing.Optional[bool],
        wall_reply_new: typing.Optional[bool],
        wall_reply_edit: typing.Optional[bool],
        wall_reply_delete: typing.Optional[bool],
        wall_reply_restore: typing.Optional[bool],
        wall_post_new: typing.Optional[bool],
        wall_repost: typing.Optional[bool],
        board_post_new: typing.Optional[bool],
        board_post_edit: typing.Optional[bool],
        board_post_restore: typing.Optional[bool],
        board_post_delete: typing.Optional[bool],
        photo_comment_new: typing.Optional[bool],
        photo_comment_edit: typing.Optional[bool],
        photo_comment_delete: typing.Optional[bool],
        photo_comment_restore: typing.Optional[bool],
        video_comment_new: typing.Optional[bool],
        video_comment_edit: typing.Optional[bool],
        video_comment_delete: typing.Optional[bool],
        video_comment_restore: typing.Optional[bool],
        market_comment_new: typing.Optional[bool],
        market_comment_edit: typing.Optional[bool],
        market_comment_delete: typing.Optional[bool],
        market_comment_restore: typing.Optional[bool],
        poll_vote_new: typing.Optional[bool],
        group_join: typing.Optional[bool],
        group_leave: typing.Optional[bool],
        group_change_settings: typing.Optional[bool],
        group_change_photo: typing.Optional[bool],
        group_officers_edit: typing.Optional[bool],
        user_block: typing.Optional[bool],
        user_unblock: typing.Optional[bool],
    ) -> OkResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("setLongPollSettings", params)
        result = OkResponse(**raw_result)
        return result

    def unban(
        self, group_id: typing.Optional[int], owner_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param group_id:
        :param owner_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("unban", params)
        result = OkResponse(**raw_result)
        return result
