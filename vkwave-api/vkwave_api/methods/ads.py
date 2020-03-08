from vkwave_types.responses import *
from ._category import Category


class Ads(Category):
    def add_office_users(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsAddOfficeUsersResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addOfficeUsers", params)
        result = AdsAddOfficeUsersResponse(**raw_result)
        return result

    def check_link(
        self,
        account_id: typing.Optional[int],
        link_type: typing.Optional[str],
        link_url: typing.Optional[str],
        campaign_id: typing.Optional[int],
    ) -> AdsCheckLinkResponse:
        """
        :param account_id: - Advertising account ID.
        :param link_type: - Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
        :param link_url: - Object URL.
        :param campaign_id: - Campaign ID
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("checkLink", params)
        result = AdsCheckLinkResponse(**raw_result)
        return result

    def create_ads(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsCreateAdsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createAds", params)
        result = AdsCreateAdsResponse(**raw_result)
        return result

    def create_campaigns(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsCreateCampaignsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createCampaigns", params)
        result = AdsCreateCampaignsResponse(**raw_result)
        return result

    def create_clients(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsCreateClientsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createClients", params)
        result = AdsCreateClientsResponse(**raw_result)
        return result

    def create_target_group(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        name: typing.Optional[str],
        lifetime: typing.Optional[int],
        target_pixel_id: typing.Optional[int],
        target_pixel_rules: typing.Optional[str],
    ) -> AdsCreateTargetGroupResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param name: - Name of the target group — a string up to 64 characters long.
        :param lifetime: - 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param target_pixel_id:
        :param target_pixel_rules:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("createTargetGroup", params)
        result = AdsCreateTargetGroupResponse(**raw_result)
        return result

    def delete_ads(
        self, account_id: typing.Optional[int], ids: typing.Optional[str],
    ) -> AdsDeleteAdsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with ad IDs.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteAds", params)
        result = AdsDeleteAdsResponse(**raw_result)
        return result

    def delete_campaigns(
        self, account_id: typing.Optional[int], ids: typing.Optional[str],
    ) -> AdsDeleteCampaignsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted campaigns.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteCampaigns", params)
        result = AdsDeleteCampaignsResponse(**raw_result)
        return result

    def delete_clients(
        self, account_id: typing.Optional[int], ids: typing.Optional[str],
    ) -> AdsDeleteClientsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted clients.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteClients", params)
        result = AdsDeleteClientsResponse(**raw_result)
        return result

    def delete_target_group(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        target_group_id: typing.Optional[int],
    ) -> OkResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Group ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteTargetGroup", params)
        result = OkResponse(**raw_result)
        return result

    def get_accounts(self,) -> AdsGetAccountsResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAccounts", params)
        result = AdsGetAccountsResponse(**raw_result)
        return result

    def get_ads(
        self,
        account_id: typing.Optional[int],
        ad_ids: typing.Optional[str],
        campaign_ids: typing.Optional[str],
        client_id: typing.Optional[int],
        include_deleted: typing.Optional[bool],
        limit: typing.Optional[int],
        offset: typing.Optional[int],
    ) -> AdsGetAdsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset. Used in the same cases as 'limit' parameter.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAds", params)
        result = AdsGetAdsResponse(**raw_result)
        return result

    def get_ads_layout(
        self,
        account_id: typing.Optional[int],
        ad_ids: typing.Optional[str],
        campaign_ids: typing.Optional[str],
        client_id: typing.Optional[int],
        include_deleted: typing.Optional[bool],
        limit: typing.Optional[int],
        offset: typing.Optional[int],
    ) -> AdsGetAdsLayoutResponse:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown. *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset. Used in the same cases as 'limit' parameter.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAdsLayout", params)
        result = AdsGetAdsLayoutResponse(**raw_result)
        return result

    def get_ads_targeting(
        self,
        account_id: typing.Optional[int],
        ad_ids: typing.Optional[str],
        campaign_ids: typing.Optional[str],
        client_id: typing.Optional[int],
        include_deleted: typing.Optional[bool],
        limit: typing.Optional[int],
        offset: typing.Optional[int],
    ) -> AdsGetAdsTargetingResponse:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset needed to return a specific subset of results.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getAdsTargeting", params)
        result = AdsGetAdsTargetingResponse(**raw_result)
        return result

    def get_budget(self, account_id: typing.Optional[int],) -> AdsGetBudgetResponse:
        """
        :param account_id: - Advertising account ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getBudget", params)
        result = AdsGetBudgetResponse(**raw_result)
        return result

    def get_campaigns(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        include_deleted: typing.Optional[bool],
        campaign_ids: typing.Optional[str],
    ) -> AdsGetCampaignsResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
        :param campaign_ids: - Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCampaigns", params)
        result = AdsGetCampaignsResponse(**raw_result)
        return result

    def get_categories(self, lang: typing.Optional[str],) -> AdsGetCategoriesResponse:
        """
        :param lang: - Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCategories", params)
        result = AdsGetCategoriesResponse(**raw_result)
        return result

    def get_clients(self, account_id: typing.Optional[int],) -> AdsGetClientsResponse:
        """
        :param account_id: - Advertising account ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getClients", params)
        result = AdsGetClientsResponse(**raw_result)
        return result

    def get_demographics(
        self,
        account_id: typing.Optional[int],
        ids_type: typing.Optional[str],
        ids: typing.Optional[str],
        period: typing.Optional[str],
        date_from: typing.Optional[str],
        date_to: typing.Optional[str],
    ) -> AdsGetDemographicsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: - IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: - Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: - Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: - Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getDemographics", params)
        result = AdsGetDemographicsResponse(**raw_result)
        return result

    def get_flood_stats(
        self, account_id: typing.Optional[int],
    ) -> AdsGetFloodStatsResponse:
        """
        :param account_id: - Advertising account ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getFloodStats", params)
        result = AdsGetFloodStatsResponse(**raw_result)
        return result

    def get_office_users(
        self, account_id: typing.Optional[int],
    ) -> AdsGetOfficeUsersResponse:
        """
        :param account_id: - Advertising account ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getOfficeUsers", params)
        result = AdsGetOfficeUsersResponse(**raw_result)
        return result

    def get_posts_reach(
        self,
        account_id: typing.Optional[int],
        ids_type: typing.Optional[str],
        ids: typing.Optional[str],
    ) -> AdsGetPostsReachResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: - IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getPostsReach", params)
        result = AdsGetPostsReachResponse(**raw_result)
        return result

    def get_rejection_reason(
        self, account_id: typing.Optional[int], ad_id: typing.Optional[int],
    ) -> AdsGetRejectionReasonResponse:
        """
        :param account_id: - Advertising account ID.
        :param ad_id: - Ad ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRejectionReason", params)
        result = AdsGetRejectionReasonResponse(**raw_result)
        return result

    def get_statistics(
        self,
        account_id: typing.Optional[int],
        ids_type: typing.Optional[str],
        ids: typing.Optional[str],
        period: typing.Optional[str],
        date_from: typing.Optional[str],
        date_to: typing.Optional[str],
    ) -> AdsGetStatisticsResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns,, *client — clients,, *office — account.
        :param ids: - IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: - Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: - Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: - Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getStatistics", params)
        result = AdsGetStatisticsResponse(**raw_result)
        return result

    def get_suggestions(
        self,
        section: typing.Optional[str],
        ids: typing.Optional[str],
        q: typing.Optional[str],
        country: typing.Optional[int],
        cities: typing.Optional[str],
        lang: typing.Optional[str],
    ) -> AdsGetSuggestionsResponse:
        """
        :param section: - Section, suggestions are retrieved in. Available values: *countries — request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions — requested list of regions. 'country' parameter is required. *cities — requested list of cities. 'country' parameter is required. *districts — requested list of districts. 'cities' parameter is required. *stations — requested list of subway stations. 'cities' parameter is required. *streets — requested list of streets. 'cities' parameter is required. *schools — requested list of educational organizations. 'cities' parameter is required. *interests — requested list of interests. *positions — requested list of positions (professions). *group_types — requested list of group types. *religions — requested list of religious commitments. *browsers — requested list of browsers and mobile devices.
        :param ids: - Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: - Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: - ID of the country objects are searched in.
        :param cities: - IDs of cities where objects are searched in, separated with a comma.
        :param lang: - Language of the returned string values. Supported languages: *ru — Russian,, *ua — Ukrainian,, *en — English.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSuggestions", params)
        result = AdsGetSuggestionsResponse(**raw_result)
        return result

    def get_target_groups(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> AdsGetTargetGroupsResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: - '1' — to return pixel code.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTargetGroups", params)
        result = AdsGetTargetGroupsResponse(**raw_result)
        return result

    def get_targeting_stats(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        criteria: typing.Optional[str],
        ad_id: typing.Optional[int],
        ad_format: typing.Optional[int],
        ad_platform: typing.Optional[str],
        ad_platform_no_wall: typing.Optional[str],
        ad_platform_no_ad_network: typing.Optional[str],
        link_url: typing.Optional[str],
        link_domain: typing.Optional[str],
    ) -> AdsGetTargetingStatsResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id:
        :param criteria: - Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param ad_id: - ID of an ad which targeting parameters shall be analyzed.
        :param ad_format: - Ad format. Possible values: *'1' — image and text,, *'2' — big image,, *'3' — exclusive format,, *'4' — community, square image,, *'7' — special app format,, *'8' — special community format,, *'9' — post in community,, *'10' — app board.
        :param ad_platform: - Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' — VK and partner sites,, *'1' — VK only. (for 'ad_format' = '9'), *'all' — all platforms,, *'desktop' — desktop version,, *'mobile' — mobile version and apps.
        :param ad_platform_no_wall:
        :param ad_platform_no_ad_network:
        :param link_url: - URL for the advertised object.
        :param link_domain: - Domain of the advertised object.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getTargetingStats", params)
        result = AdsGetTargetingStatsResponse(**raw_result)
        return result

    def get_upload_u_r_l(
        self, ad_format: typing.Optional[int], icon: typing.Optional[int],
    ) -> AdsGetUploadURLResponse:
        """
        :param ad_format: - Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
        :param icon:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUploadURL", params)
        result = AdsGetUploadURLResponse(**raw_result)
        return result

    def get_video_upload_u_r_l(self,) -> AdsGetVideoUploadURLResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getVideoUploadURL", params)
        result = AdsGetVideoUploadURLResponse(**raw_result)
        return result

    def import_target_contacts(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        target_group_id: typing.Optional[int],
        contacts: typing.Optional[str],
    ) -> AdsImportTargetContactsResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Target group ID.
        :param contacts: - List of phone numbers, emails or user IDs separated with a comma.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("importTargetContacts", params)
        result = AdsImportTargetContactsResponse(**raw_result)
        return result

    def remove_office_users(
        self, account_id: typing.Optional[int], ids: typing.Optional[str],
    ) -> AdsRemoveOfficeUsersResponse:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted managers.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("removeOfficeUsers", params)
        result = AdsRemoveOfficeUsersResponse(**raw_result)
        return result

    def update_ads(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsUpdateAdsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("updateAds", params)
        result = AdsUpdateAdsResponse(**raw_result)
        return result

    def update_campaigns(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsUpdateCampaignsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("updateCampaigns", params)
        result = AdsUpdateCampaignsResponse(**raw_result)
        return result

    def update_clients(
        self, account_id: typing.Optional[int], data: typing.Optional[str],
    ) -> AdsUpdateClientsResponse:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("updateClients", params)
        result = AdsUpdateClientsResponse(**raw_result)
        return result

    def update_target_group(
        self,
        account_id: typing.Optional[int],
        client_id: typing.Optional[int],
        target_group_id: typing.Optional[int],
        name: typing.Optional[str],
        domain: typing.Optional[str],
        lifetime: typing.Optional[int],
        target_pixel_id: typing.Optional[int],
        target_pixel_rules: typing.Optional[str],
    ) -> OkResponse:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Group ID.
        :param name: - New name of the target group — a string up to 64 characters long.
        :param domain: - Domain of the site where user accounting code will be placed.
        :param lifetime: - 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' – automatic exclusion is off.
        :param target_pixel_id:
        :param target_pixel_rules:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("updateTargetGroup", params)
        result = OkResponse(**raw_result)
        return result
