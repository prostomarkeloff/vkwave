from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Ads(Category):
    async def add_office_users(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsAddOfficeUsersResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addOfficeUsers", params)
        if return_raw_response:
            return raw_result

        result = AdsAddOfficeUsersResponse(**raw_result)
        return result

    async def check_link(
        self,
        account_id: int,
        link_type: str,
        link_url: str,
        return_raw_response: bool = False,
        campaign_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsCheckLinkResponse]:
        """
        :param account_id: - Advertising account ID.
        :param link_type: - Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
        :param link_url: - Object URL.
        :param campaign_id: - Campaign ID
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("checkLink", params)
        if return_raw_response:
            return raw_result

        result = AdsCheckLinkResponse(**raw_result)
        return result

    async def create_ads(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsCreateAdsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createAds", params)
        if return_raw_response:
            return raw_result

        result = AdsCreateAdsResponse(**raw_result)
        return result

    async def create_campaigns(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsCreateCampaignsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createCampaigns", params)
        if return_raw_response:
            return raw_result

        result = AdsCreateCampaignsResponse(**raw_result)
        return result

    async def create_clients(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsCreateClientsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createClients", params)
        if return_raw_response:
            return raw_result

        result = AdsCreateClientsResponse(**raw_result)
        return result

    async def create_target_group(
        self,
        account_id: int,
        name: str,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
        lifetime: typing.Optional[int] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdsCreateTargetGroupResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param name: - Name of the target group — a string up to 64 characters long.
        :param lifetime: - 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param target_pixel_id:
        :param target_pixel_rules:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createTargetGroup", params)
        if return_raw_response:
            return raw_result

        result = AdsCreateTargetGroupResponse(**raw_result)
        return result

    async def delete_ads(
        self, account_id: int, ids: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsDeleteAdsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with ad IDs.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteAds", params)
        if return_raw_response:
            return raw_result

        result = AdsDeleteAdsResponse(**raw_result)
        return result

    async def delete_campaigns(
        self, account_id: int, ids: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsDeleteCampaignsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted campaigns.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteCampaigns", params)
        if return_raw_response:
            return raw_result

        result = AdsDeleteCampaignsResponse(**raw_result)
        return result

    async def delete_clients(
        self, account_id: int, ids: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsDeleteClientsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted clients.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteClients", params)
        if return_raw_response:
            return raw_result

        result = AdsDeleteClientsResponse(**raw_result)
        return result

    async def delete_target_group(
        self,
        account_id: int,
        target_group_id: int,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Group ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteTargetGroup", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get_accounts(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetAccountsResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAccounts", params)
        if return_raw_response:
            return raw_result

        result = AdsGetAccountsResponse(**raw_result)
        return result

    async def get_ads(
        self,
        account_id: int,
        return_raw_response: bool = False,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[BaseBoolInt] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsGetAdsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset. Used in the same cases as 'limit' parameter.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAds", params)
        if return_raw_response:
            return raw_result

        result = AdsGetAdsResponse(**raw_result)
        return result

    async def get_ads_layout(
        self,
        account_id: int,
        return_raw_response: bool = False,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[BaseBoolInt] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsGetAdsLayoutResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown. *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset. Used in the same cases as 'limit' parameter.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAdsLayout", params)
        if return_raw_response:
            return raw_result

        result = AdsGetAdsLayoutResponse(**raw_result)
        return result

    async def get_ads_targeting(
        self,
        account_id: int,
        return_raw_response: bool = False,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[BaseBoolInt] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsGetAdsTargetingResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ad_ids: - Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: - Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: - 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: - flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: - Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: - Offset needed to return a specific subset of results.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAdsTargeting", params)
        if return_raw_response:
            return raw_result

        result = AdsGetAdsTargetingResponse(**raw_result)
        return result

    async def get_budget(
        self, account_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetBudgetResponse]:
        """
        :param account_id: - Advertising account ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getBudget", params)
        if return_raw_response:
            return raw_result

        result = AdsGetBudgetResponse(**raw_result)
        return result

    async def get_campaigns(
        self,
        account_id: int,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[BaseBoolInt] = None,
        campaign_ids: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdsGetCampaignsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: - Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
        :param campaign_ids: - Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCampaigns", params)
        if return_raw_response:
            return raw_result

        result = AdsGetCampaignsResponse(**raw_result)
        return result

    async def get_categories(
        self, return_raw_response: bool = False, lang: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdsGetCategoriesResponse]:
        """
        :param lang: - Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCategories", params)
        if return_raw_response:
            return raw_result

        result = AdsGetCategoriesResponse(**raw_result)
        return result

    async def get_clients(
        self, account_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetClientsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getClients", params)
        if return_raw_response:
            return raw_result

        result = AdsGetClientsResponse(**raw_result)
        return result

    async def get_demographics(
        self,
        account_id: int,
        ids_type: str,
        ids: BaseBoolInt,
        period: str,
        date_from: BaseBoolInt,
        date_to: BaseBoolInt,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetDemographicsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: - IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: - Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: - Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: - Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getDemographics", params)
        if return_raw_response:
            return raw_result

        result = AdsGetDemographicsResponse(**raw_result)
        return result

    async def get_flood_stats(
        self, account_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetFloodStatsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFloodStats", params)
        if return_raw_response:
            return raw_result

        result = AdsGetFloodStatsResponse(**raw_result)
        return result

    async def get_office_users(
        self, account_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetOfficeUsersResponse]:
        """
        :param account_id: - Advertising account ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getOfficeUsers", params)
        if return_raw_response:
            return raw_result

        result = AdsGetOfficeUsersResponse(**raw_result)
        return result

    async def get_posts_reach(
        self, account_id: int, ids_type: str, ids: BaseBoolInt, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetPostsReachResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: - IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPostsReach", params)
        if return_raw_response:
            return raw_result

        result = AdsGetPostsReachResponse(**raw_result)
        return result

    async def get_rejection_reason(
        self, account_id: int, ad_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetRejectionReasonResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ad_id: - Ad ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRejectionReason", params)
        if return_raw_response:
            return raw_result

        result = AdsGetRejectionReasonResponse(**raw_result)
        return result

    async def get_statistics(
        self,
        account_id: int,
        ids_type: str,
        ids: BaseBoolInt,
        period: str,
        date_from: BaseBoolInt,
        date_to: BaseBoolInt,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetStatisticsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns,, *client — clients,, *office — account.
        :param ids: - IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: - Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: - Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: - Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getStatistics", params)
        if return_raw_response:
            return raw_result

        result = AdsGetStatisticsResponse(**raw_result)
        return result

    async def get_suggestions(
        self,
        section: str,
        return_raw_response: bool = False,
        ids: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        cities: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdsGetSuggestionsResponse]:
        """
        :param section: - Section, suggestions are retrieved in. Available values: *countries — request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions — requested list of regions. 'country' parameter is required. *cities — requested list of cities. 'country' parameter is required. *districts — requested list of districts. 'cities' parameter is required. *stations — requested list of subway stations. 'cities' parameter is required. *streets — requested list of streets. 'cities' parameter is required. *schools — requested list of educational organizations. 'cities' parameter is required. *interests — requested list of interests. *positions — requested list of positions (professions). *group_types — requested list of group types. *religions — requested list of religious commitments. *browsers — requested list of browsers and mobile devices.
        :param ids: - Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: - Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: - ID of the country objects are searched in.
        :param cities: - IDs of cities where objects are searched in, separated with a comma.
        :param lang: - Language of the returned string values. Supported languages: *ru — Russian,, *ua — Ukrainian,, *en — English.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSuggestions", params)
        if return_raw_response:
            return raw_result

        result = AdsGetSuggestionsResponse(**raw_result)
        return result

    async def get_target_groups(
        self,
        account_id: int,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, AdsGetTargetGroupsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: - '1' — to return pixel code.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTargetGroups", params)
        if return_raw_response:
            return raw_result

        result = AdsGetTargetGroupsResponse(**raw_result)
        return result

    async def get_targeting_stats(
        self,
        account_id: int,
        link_url: str,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
        criteria: typing.Optional[str] = None,
        ad_id: typing.Optional[int] = None,
        ad_format: typing.Optional[BaseBoolInt] = None,
        ad_platform: typing.Optional[BaseBoolInt] = None,
        ad_platform_no_wall: typing.Optional[str] = None,
        ad_platform_no_ad_network: typing.Optional[str] = None,
        link_domain: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdsGetTargetingStatsResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getTargetingStats", params)
        if return_raw_response:
            return raw_result

        result = AdsGetTargetingStatsResponse(**raw_result)
        return result

    async def get_upload_u_r_l(
        self, ad_format: int, return_raw_response: bool = False, icon: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsGetUploadURLResponse]:
        """
        :param ad_format: - Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
        :param icon:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUploadURL", params)
        if return_raw_response:
            return raw_result

        result = AdsGetUploadURLResponse(**raw_result)
        return result

    async def get_video_upload_u_r_l(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsGetVideoUploadURLResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getVideoUploadURL", params)
        if return_raw_response:
            return raw_result

        result = AdsGetVideoUploadURLResponse(**raw_result)
        return result

    async def import_target_contacts(
        self,
        account_id: int,
        target_group_id: int,
        contacts: str,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdsImportTargetContactsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Target group ID.
        :param contacts: - List of phone numbers, emails or user IDs separated with a comma.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("importTargetContacts", params)
        if return_raw_response:
            return raw_result

        result = AdsImportTargetContactsResponse(**raw_result)
        return result

    async def remove_office_users(
        self, account_id: int, ids: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsRemoveOfficeUsersResponse]:
        """
        :param account_id: - Advertising account ID.
        :param ids: - Serialized JSON array with IDs of deleted managers.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeOfficeUsers", params)
        if return_raw_response:
            return raw_result

        result = AdsRemoveOfficeUsersResponse(**raw_result)
        return result

    async def update_ads(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsUpdateAdsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateAds", params)
        if return_raw_response:
            return raw_result

        result = AdsUpdateAdsResponse(**raw_result)
        return result

    async def update_campaigns(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsUpdateCampaignsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateCampaigns", params)
        if return_raw_response:
            return raw_result

        result = AdsUpdateCampaignsResponse(**raw_result)
        return result

    async def update_clients(
        self, account_id: int, data: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, AdsUpdateClientsResponse]:
        """
        :param account_id: - Advertising account ID.
        :param data: - Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateClients", params)
        if return_raw_response:
            return raw_result

        result = AdsUpdateClientsResponse(**raw_result)
        return result

    async def update_target_group(
        self,
        account_id: int,
        target_group_id: int,
        name: str,
        return_raw_response: bool = False,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        lifetime: typing.Optional[BaseBoolInt] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param account_id: - Advertising account ID.
        :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: - Group ID.
        :param name: - New name of the target group — a string up to 64 characters long.
        :param domain: - Domain of the site where user accounting code will be placed.
        :param lifetime: - 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' – automatic exclusion is off.
        :param target_pixel_id:
        :param target_pixel_rules:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("updateTargetGroup", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
