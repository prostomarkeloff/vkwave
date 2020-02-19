from .responses import *


def account_ban(owner_id: int,) -> OkResponse:
    """
    :param owner_id:
    :return:
    """
    pass


def account_change_password(
    restore_sid: str, change_password_hash: str, old_password: str, new_password: str,
) -> AccountChangePasswordResponse:
    """
    :param restore_sid: - Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
    :param change_password_hash: - Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
    :param old_password: - Current user password.
    :param new_password: - New password that will be set as a current
    :return:
    """
    pass


def account_get_active_offers(
    offset: int, count: int,
) -> AccountGetActiveOffersResponse:
    """
    :param offset:
    :param count: - Number of results to return.
    :return:
    """
    pass


def account_get_app_permissions(user_id: int,) -> AccountGetAppPermissionsResponse:
    """
    :param user_id: - User ID whose settings information shall be got. By default: current user.
    :return:
    """
    pass


def account_get_banned(offset: int, count: int,) -> AccountGetBannedResponse:
    """
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of results to return.
    :return:
    """
    pass


def account_get_counters(filter: list,) -> AccountGetCountersResponse:
    """
    :param filter: - Counters to be returned.
    :return:
    """
    pass


def account_get_info(fields: list,) -> AccountGetInfoResponse:
    """
    :param fields: - Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
    :return:
    """
    pass


def account_get_profile_info() -> AccountGetProfileInfoResponse:
    """
    :return:
    """
    pass


def account_get_push_settings(device_id: str,) -> AccountGetPushSettingsResponse:
    """
    :param device_id: - Unique device ID.
    :return:
    """
    pass


def account_register_device(
    token: str,
    device_model: str,
    device_year: int,
    device_id: str,
    system_version: str,
    settings: str,
    sandbox: bool,
) -> OkResponse:
    """
    :param token: - Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
    :param device_model: - String name of device model.
    :param device_year: - Device year.
    :param device_id: - Unique device ID.
    :param system_version: - String version of device operating system.
    :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
    :param sandbox:
    :return:
    """
    pass


def account_save_profile_info(
    first_name: str,
    last_name: str,
    maiden_name: str,
    screen_name: str,
    cancel_request_id: int,
    sex: int,
    relation: int,
    relation_partner_id: int,
    bdate: str,
    bdate_visibility: int,
    home_town: str,
    country_id: int,
    city_id: int,
    status: str,
) -> AccountSaveProfileInfoResponse:
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
    :return:
    """
    pass


def account_set_info(name: str, value: str,) -> OkResponse:
    """
    :param name: - Setting name.
    :param value: - Setting value.
    :return:
    """
    pass


def account_set_name_in_menu(user_id: int, name: str,) -> OkResponse:
    """
    :param user_id: - User ID.
    :param name: - Application screen name.
    :return:
    """
    pass


def account_set_offline() -> OkResponse:
    """
    :return:
    """
    pass


def account_set_online(voip: bool,) -> OkResponse:
    """
    :param voip: - '1' if videocalls are available for current device.
    :return:
    """
    pass


def account_set_push_settings(
    device_id: str, settings: str, key: str, value: list,
) -> OkResponse:
    """
    :param device_id: - Unique device ID.
    :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
    :param key: - Notification key.
    :param value: - New value for the key in a [vk.com/dev/push_settings|special format].
    :return:
    """
    pass


def account_set_silence_mode(
    device_id: str, time: int, peer_id: int, sound: int,
) -> OkResponse:
    """
    :param device_id: - Unique device ID.
    :param time: - Time in seconds for what notifications should be disabled. '-1' to disable forever.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
    :param sound: - '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
    :return:
    """
    pass


def account_unban(owner_id: int,) -> OkResponse:
    """
    :param owner_id:
    :return:
    """
    pass


def account_unregister_device(device_id: str, sandbox: bool,) -> OkResponse:
    """
    :param device_id: - Unique device ID.
    :param sandbox:
    :return:
    """
    pass


def ads_add_office_users(account_id: int, data: str,) -> AdsAddOfficeUsersResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
    :return:
    """
    pass


def ads_check_link(
    account_id: int, link_type: str, link_url: str, campaign_id: int,
) -> AdsCheckLinkResponse:
    """
    :param account_id: - Advertising account ID.
    :param link_type: - Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
    :param link_url: - Object URL.
    :param campaign_id: - Campaign ID
    :return:
    """
    pass


def ads_create_ads(account_id: int, data: str,) -> AdsCreateAdsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
    :return:
    """
    pass


def ads_create_campaigns(account_id: int, data: str,) -> AdsCreateCampaignsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
    :return:
    """
    pass


def ads_create_clients(account_id: int, data: str,) -> AdsCreateClientsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
    :return:
    """
    pass


def ads_create_target_group(
    account_id: int,
    client_id: int,
    name: str,
    lifetime: int,
    target_pixel_id: int,
    target_pixel_rules: str,
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
    pass


def ads_delete_ads(account_id: int, ids: str,) -> AdsDeleteAdsResponse:
    """
    :param account_id: - Advertising account ID.
    :param ids: - Serialized JSON array with ad IDs.
    :return:
    """
    pass


def ads_delete_campaigns(account_id: int, ids: str,) -> AdsDeleteCampaignsResponse:
    """
    :param account_id: - Advertising account ID.
    :param ids: - Serialized JSON array with IDs of deleted campaigns.
    :return:
    """
    pass


def ads_delete_clients(account_id: int, ids: str,) -> AdsDeleteClientsResponse:
    """
    :param account_id: - Advertising account ID.
    :param ids: - Serialized JSON array with IDs of deleted clients.
    :return:
    """
    pass


def ads_delete_target_group(
    account_id: int, client_id: int, target_group_id: int,
) -> OkResponse:
    """
    :param account_id: - Advertising account ID.
    :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
    :param target_group_id: - Group ID.
    :return:
    """
    pass


def ads_get_accounts() -> AdsGetAccountsResponse:
    """
    :return:
    """
    pass


def ads_get_ads(
    account_id: int,
    ad_ids: str,
    campaign_ids: str,
    client_id: int,
    include_deleted: bool,
    limit: int,
    offset: int,
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
    pass


def ads_get_ads_layout(
    account_id: int,
    ad_ids: str,
    campaign_ids: str,
    client_id: int,
    include_deleted: bool,
    limit: int,
    offset: int,
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
    pass


def ads_get_ads_targeting(
    account_id: int,
    ad_ids: str,
    campaign_ids: str,
    client_id: int,
    include_deleted: bool,
    limit: int,
    offset: int,
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
    pass


def ads_get_budget(account_id: int,) -> AdsGetBudgetResponse:
    """
    :param account_id: - Advertising account ID.
    :return:
    """
    pass


def ads_get_campaigns(
    account_id: int, client_id: int, include_deleted: bool, campaign_ids: str,
) -> AdsGetCampaignsResponse:
    """
    :param account_id: - Advertising account ID.
    :param client_id: - 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
    :param include_deleted: - Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
    :param campaign_ids: - Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
    :return:
    """
    pass


def ads_get_categories(lang: str,) -> AdsGetCategoriesResponse:
    """
    :param lang: - Language. The full list of supported languages is [vk.com/dev/api_requests|here].
    :return:
    """
    pass


def ads_get_clients(account_id: int,) -> AdsGetClientsResponse:
    """
    :param account_id: - Advertising account ID.
    :return:
    """
    pass


def ads_get_demographics(
    account_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str,
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
    pass


def ads_get_flood_stats(account_id: int,) -> AdsGetFloodStatsResponse:
    """
    :param account_id: - Advertising account ID.
    :return:
    """
    pass


def ads_get_office_users(account_id: int,) -> AdsGetOfficeUsersResponse:
    """
    :param account_id: - Advertising account ID.
    :return:
    """
    pass


def ads_get_posts_reach(
    account_id: int, ids_type: str, ids: str,
) -> AdsGetPostsReachResponse:
    """
    :param account_id: - Advertising account ID.
    :param ids_type: - Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
    :param ids: - IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
    :return:
    """
    pass


def ads_get_rejection_reason(
    account_id: int, ad_id: int,
) -> AdsGetRejectionReasonResponse:
    """
    :param account_id: - Advertising account ID.
    :param ad_id: - Ad ID.
    :return:
    """
    pass


def ads_get_statistics(
    account_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str,
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
    pass


def ads_get_suggestions(
    section: str, ids: str, q: str, country: int, cities: str, lang: str,
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
    pass


def ads_get_target_groups(
    account_id: int, client_id: int, extended: bool,
) -> AdsGetTargetGroupsResponse:
    """
    :param account_id: - Advertising account ID.
    :param client_id: - 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
    :param extended: - '1' — to return pixel code.
    :return:
    """
    pass


def ads_get_targeting_stats(
    account_id: int,
    client_id: int,
    criteria: str,
    ad_id: int,
    ad_format: int,
    ad_platform: str,
    ad_platform_no_wall: str,
    ad_platform_no_ad_network: str,
    link_url: str,
    link_domain: str,
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
    pass


def ads_get_upload_u_r_l(ad_format: int, icon: int,) -> AdsGetUploadURLResponse:
    """
    :param ad_format: - Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
    :param icon:
    :return:
    """
    pass


def ads_get_video_upload_u_r_l() -> AdsGetVideoUploadURLResponse:
    """
    :return:
    """
    pass


def ads_import_target_contacts(
    account_id: int, client_id: int, target_group_id: int, contacts: str,
) -> AdsImportTargetContactsResponse:
    """
    :param account_id: - Advertising account ID.
    :param client_id: - 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
    :param target_group_id: - Target group ID.
    :param contacts: - List of phone numbers, emails or user IDs separated with a comma.
    :return:
    """
    pass


def ads_remove_office_users(account_id: int, ids: str,) -> AdsRemoveOfficeUsersResponse:
    """
    :param account_id: - Advertising account ID.
    :param ids: - Serialized JSON array with IDs of deleted managers.
    :return:
    """
    pass


def ads_update_ads(account_id: int, data: str,) -> AdsUpdateAdsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
    :return:
    """
    pass


def ads_update_campaigns(account_id: int, data: str,) -> AdsUpdateCampaignsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
    :return:
    """
    pass


def ads_update_clients(account_id: int, data: str,) -> AdsUpdateClientsResponse:
    """
    :param account_id: - Advertising account ID.
    :param data: - Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
    :return:
    """
    pass


def ads_update_target_group(
    account_id: int,
    client_id: int,
    target_group_id: int,
    name: str,
    domain: str,
    lifetime: int,
    target_pixel_id: int,
    target_pixel_rules: str,
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
    pass


def app_widgets_update(code: str, type: str,) -> BaseOkResponse:
    """
    :param code:
    :param type:
    :return:
    """
    pass


def apps_delete_app_requests() -> OkResponse:
    """
    :return:
    """
    pass


def apps_get(
    app_id: int,
    app_ids: list,
    platform: str,
    extended: bool,
    return_friends: bool,
    fields: list,
    name_case: str,
) -> AppsGetResponse:
    """
    :param app_id: - Application ID
    :param app_ids: - List of application ID
    :param platform: - platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
    :param extended:
    :param return_friends:
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
    :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')
    :return:
    """
    pass


def apps_get_catalog(
    sort: str,
    offset: int,
    count: int,
    platform: str,
    extended: bool,
    return_friends: bool,
    fields: list,
    name_case: str,
    q: str,
    genre_id: int,
    filter: str,
) -> AppsGetCatalogResponse:
    """
    :param sort: - Sort order: 'popular_today' — popular for one day (default), 'visitors' — by visitors number , 'create_date' — by creation date, 'growth_rate' — by growth rate, 'popular_week' — popular for one week
    :param offset: - Offset required to return a specific subset of apps.
    :param count: - Number of apps to return.
    :param platform:
    :param extended: - '1' — to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' — not to return additional fields (default).
    :param return_friends:
    :param fields:
    :param name_case:
    :param q: - Search query string.
    :param genre_id:
    :param filter: - 'installed' — to return list of installed apps (only for mobile platform).
    :return:
    """
    pass


def apps_get_friends_list(
    extended: bool, count: int, offset: int, type: str, fields: list,
) -> AppsGetFriendsListResponse:
    """
    :param extended:
    :param count: - List size.
    :param offset:
    :param type: - List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
    :param fields: - Additional profile fields, see [vk.com/dev/fields|description].
    :return:
    """
    pass


def apps_get_leaderboard(
    type: str, global_: bool, extended: bool,
) -> AppsGetLeaderboardResponse:
    """
    :param type: - Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
    :param global_: - Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
    :param extended: - 1 — to return additional info about users
    :return:
    """
    pass


def apps_get_scopes(type: str,) -> AppsGetScopesResponse:
    """
    :param type:
    :return:
    """
    pass


def apps_get_score(user_id: int,) -> AppsGetScoreResponse:
    """
    :param user_id:
    :return:
    """
    pass


def apps_send_request(
    user_id: int, text: str, type: str, name: str, key: str, separate: bool,
) -> AppsSendRequestResponse:
    """
    :param user_id: - id of the user to send a request
    :param text: - request text
    :param type: - request type. Values: 'invite' – if the request is sent to a user who does not have the app installed,, 'request' – if a user has already installed the app
    :param name:
    :param key: - special string key to be sent with the request
    :param separate:
    :return:
    """
    pass


def auth_check_phone(
    phone: str, client_id: int, client_secret: str, auth_by_phone: bool,
) -> OkResponse:
    """
    :param phone: - Phone number.
    :param client_id: - User ID.
    :param client_secret:
    :param auth_by_phone:
    :return:
    """
    pass


def auth_restore(phone: str, last_name: str,) -> AuthRestoreResponse:
    """
    :param phone: - User phone number.
    :param last_name: - User last name.
    :return:
    """
    pass


def board_add_topic(
    group_id: int, title: str, text: str, from_group: bool, attachments: list,
) -> BoardAddTopicResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param title: - Topic title.
    :param text: - Text of the topic.
    :param from_group: - For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
    :param attachments: - List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
    :return:
    """
    pass


def board_close_topic(group_id: int, topic_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :return:
    """
    pass


def board_create_comment(
    group_id: int,
    topic_id: int,
    message: str,
    attachments: list,
    from_group: bool,
    sticker_id: int,
    guid: str,
) -> BoardCreateCommentResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - ID of the topic to be commented on.
    :param message: - (Required if 'attachments' is not set.) Text of the comment.
    :param attachments: - (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
    :param from_group: - '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
    :param sticker_id: - Sticker ID.
    :param guid: - Unique identifier to avoid repeated comments.
    :return:
    """
    pass


def board_delete_comment(group_id: int, topic_id: int, comment_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :param comment_id: - Comment ID.
    :return:
    """
    pass


def board_delete_topic(group_id: int, topic_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :return:
    """
    pass


def board_edit_comment(
    group_id: int, topic_id: int, comment_id: int, message: str, attachments: list,
) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :param comment_id: - ID of the comment on the topic.
    :param message: - (Required if 'attachments' is not set). New comment text.
    :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
    :return:
    """
    pass


def board_edit_topic(group_id: int, topic_id: int, title: str,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :param title: - New title of the topic.
    :return:
    """
    pass


def board_fix_topic(group_id: int, topic_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :return:
    """
    pass


def board_get_comments(
    group_id: int,
    topic_id: int,
    need_likes: bool,
    start_comment_id: int,
    offset: int,
    count: int,
    extended: bool,
    sort: str,
) -> BoardGetCommentsResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :param need_likes: - '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
    :param start_comment_id:
    :param offset: - Offset needed to return a specific subset of comments.
    :param count: - Number of comments to return.
    :param extended: - '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
    :param sort: - Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,
    :return:
    """
    pass


def board_get_topics(
    group_id: int,
    topic_ids: list,
    order: int,
    offset: int,
    count: int,
    extended: bool,
    preview: int,
    preview_length: int,
) -> BoardGetTopicsResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_ids: - IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
    :param order: - Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
    :param offset: - Offset needed to return a specific subset of topics.
    :param count: - Number of topics to return.
    :param extended: - '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
    :param preview: - '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
    :param preview_length: - Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
    :return:
    """
    pass


def board_open_topic(group_id: int, topic_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :return:
    """
    pass


def board_restore_comment(group_id: int, topic_id: int, comment_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :param comment_id: - Comment ID.
    :return:
    """
    pass


def board_unfix_topic(group_id: int, topic_id: int,) -> OkResponse:
    """
    :param group_id: - ID of the community that owns the discussion board.
    :param topic_id: - Topic ID.
    :return:
    """
    pass


def database_get_chairs(
    faculty_id: int, offset: int, count: int,
) -> DatabaseGetChairsResponse:
    """
    :param faculty_id: - id of the faculty to get chairs from
    :param offset: - offset required to get a certain subset of chairs
    :param count: - amount of chairs to get
    :return:
    """
    pass


def database_get_cities(
    country_id: int, region_id: int, q: str, need_all: bool, offset: int, count: int,
) -> DatabaseGetCitiesResponse:
    """
    :param country_id: - Country ID.
    :param region_id: - Region ID.
    :param q: - Search query.
    :param need_all: - '1' — to return all cities in the country, '0' — to return major cities in the country (default),
    :param offset: - Offset needed to return a specific subset of cities.
    :param count: - Number of cities to return.
    :return:
    """
    pass


def database_get_cities_by_id(city_ids: list,) -> DatabaseGetCitiesByIdResponse:
    """
    :param city_ids: - City IDs.
    :return:
    """
    pass


def database_get_countries(
    need_all: bool, code: str, offset: int, count: int,
) -> DatabaseGetCountriesResponse:
    """
    :param need_all: - '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
    :param code: - Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
    :param offset: - Offset needed to return a specific subset of countries.
    :param count: - Number of countries to return.
    :return:
    """
    pass


def database_get_countries_by_id(
    country_ids: list,
) -> DatabaseGetCountriesByIdResponse:
    """
    :param country_ids: - Country IDs.
    :return:
    """
    pass


def database_get_faculties(
    university_id: int, offset: int, count: int,
) -> DatabaseGetFacultiesResponse:
    """
    :param university_id: - University ID.
    :param offset: - Offset needed to return a specific subset of faculties.
    :param count: - Number of faculties to return.
    :return:
    """
    pass


def database_get_metro_stations(
    city_id: int, offset: int, count: int, extended: bool,
) -> DatabaseGetMetroStationsResponse:
    """
    :param city_id:
    :param offset:
    :param count:
    :param extended:
    :return:
    """
    pass


def database_get_metro_stations_by_id(
    station_ids: list,
) -> DatabaseGetMetroStationsByIdResponse:
    """
    :param station_ids:
    :return:
    """
    pass


def database_get_regions(
    country_id: int, q: str, offset: int, count: int,
) -> DatabaseGetRegionsResponse:
    """
    :param country_id: - Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
    :param q: - Search query.
    :param offset: - Offset needed to return specific subset of regions.
    :param count: - Number of regions to return.
    :return:
    """
    pass


def database_get_school_classes(country_id: int,) -> DatabaseGetSchoolClassesResponse:
    """
    :param country_id: - Country ID.
    :return:
    """
    pass


def database_get_schools(
    q: str, city_id: int, offset: int, count: int,
) -> DatabaseGetSchoolsResponse:
    """
    :param q: - Search query.
    :param city_id: - City ID.
    :param offset: - Offset needed to return a specific subset of schools.
    :param count: - Number of schools to return.
    :return:
    """
    pass


def database_get_universities(
    q: str, country_id: int, city_id: int, offset: int, count: int,
) -> DatabaseGetUniversitiesResponse:
    """
    :param q: - Search query.
    :param country_id: - Country ID.
    :param city_id: - City ID.
    :param offset: - Offset needed to return a specific subset of universities.
    :param count: - Number of universities to return.
    :return:
    """
    pass


def docs_add(owner_id: int, doc_id: int, access_key: str,) -> DocsAddResponse:
    """
    :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
    :param doc_id: - Document ID.
    :param access_key: - Access key. This parameter is required if 'access_key' was returned with the document's data.
    :return:
    """
    pass


def docs_delete(owner_id: int, doc_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
    :param doc_id: - Document ID.
    :return:
    """
    pass


def docs_edit(owner_id: int, doc_id: int, title: str, tags: list,) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param doc_id: - Document ID.
    :param title: - Document title.
    :param tags: - Document tags.
    :return:
    """
    pass


def docs_get(count: int, offset: int, type: int, owner_id: int,) -> DocsGetResponse:
    """
    :param count: - Number of documents to return. By default, all documents.
    :param offset: - Offset needed to return a specific subset of documents.
    :param type:
    :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
    :return:
    """
    pass


def docs_get_by_id(docs: list,) -> DocsGetByIdResponse:
    """
    :param docs: - Document IDs. Example: , "66748_91488,66748_91455",
    :return:
    """
    pass


def docs_get_messages_upload_server(
    type: str, peer_id: int,
) -> BaseGetUploadServerResponse:
    """
    :param type: - Document type.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
    :return:
    """
    pass


def docs_get_types(owner_id: int,) -> DocsGetTypesResponse:
    """
    :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
    :return:
    """
    pass


def docs_get_upload_server(group_id: int,) -> DocsGetUploadServer:
    """
    :param group_id: - Community ID (if the document will be uploaded to the community).
    :return:
    """
    pass


def docs_get_wall_upload_server(group_id: int,) -> BaseGetUploadServerResponse:
    """
    :param group_id: - Community ID (if the document will be uploaded to the community).
    :return:
    """
    pass


def docs_save(file: str, title: str, tags: str,) -> DocsSaveResponse:
    """
    :param file: - This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
    :param title: - Document title.
    :param tags: - Document tags.
    :return:
    """
    pass


def docs_search(
    q: str, search_own: bool, count: int, offset: int,
) -> DocsSearchResponse:
    """
    :param q: - Search query string.
    :param search_own:
    :param count: - Number of results to return.
    :param offset: - Offset needed to return a specific subset of results.
    :return:
    """
    pass


def fave_add_article(url: str,) -> BaseBoolResponse:
    """
    :param url:
    :return:
    """
    pass


def fave_add_link(link: str,) -> OkResponse:
    """
    :param link: - Link URL.
    :return:
    """
    pass


def fave_add_page(user_id: int, group_id: int,) -> OkResponse:
    """
    :param user_id:
    :param group_id:
    :return:
    """
    pass


def fave_add_post(owner_id: int, id: int, access_key: str,) -> OkResponse:
    """
    :param owner_id:
    :param id:
    :param access_key:
    :return:
    """
    pass


def fave_add_product(owner_id: int, id: int, access_key: str,) -> OkResponse:
    """
    :param owner_id:
    :param id:
    :param access_key:
    :return:
    """
    pass


def fave_add_tag(name: str,) -> FaveAddTagResponse:
    """
    :param name:
    :return:
    """
    pass


def fave_add_video(owner_id: int, id: int, access_key: str,) -> OkResponse:
    """
    :param owner_id:
    :param id:
    :param access_key:
    :return:
    """
    pass


def fave_edit_tag(id: int, name: str,) -> OkResponse:
    """
    :param id:
    :param name:
    :return:
    """
    pass


def fave_get(
    extended: bool,
    item_type: str,
    tag_id: int,
    offset: int,
    count: int,
    fields: str,
    is_from_snackbar: bool,
) -> FaveGetResponse:
    """
    :param extended: - '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
    :param item_type:
    :param tag_id: - Tag ID.
    :param offset: - Offset needed to return a specific subset of users.
    :param count: - Number of users to return.
    :param fields:
    :param is_from_snackbar:
    :return:
    """
    pass


def fave_get_pages(
    offset: int, count: int, type: str, fields: list, tag_id: int,
) -> FaveGetPagesResponse:
    """
    :param offset:
    :param count:
    :param type:
    :param fields:
    :param tag_id:
    :return:
    """
    pass


def fave_get_tags() -> FaveGetTagsResponse:
    """
    :return:
    """
    pass


def fave_mark_seen() -> BaseBoolResponse:
    """
    :return:
    """
    pass


def fave_remove_article(owner_id: int, article_id: int,) -> BaseBoolResponse:
    """
    :param owner_id:
    :param article_id:
    :return:
    """
    pass


def fave_remove_link(link_id: str, link: str,) -> OkResponse:
    """
    :param link_id: - Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
    :param link: - Link URL
    :return:
    """
    pass


def fave_remove_page(user_id: int, group_id: int,) -> OkResponse:
    """
    :param user_id:
    :param group_id:
    :return:
    """
    pass


def fave_remove_post(owner_id: int, id: int,) -> OkResponse:
    """
    :param owner_id:
    :param id:
    :return:
    """
    pass


def fave_remove_product(owner_id: int, id: int,) -> OkResponse:
    """
    :param owner_id:
    :param id:
    :return:
    """
    pass


def fave_remove_tag(id: int,) -> OkResponse:
    """
    :param id:
    :return:
    """
    pass


def fave_reorder_tags(ids: list,) -> OkResponse:
    """
    :param ids:
    :return:
    """
    pass


def fave_set_page_tags(user_id: int, group_id: int, tag_ids: list,) -> OkResponse:
    """
    :param user_id:
    :param group_id:
    :param tag_ids:
    :return:
    """
    pass


def fave_set_tags(
    item_type: str,
    item_owner_id: int,
    item_id: int,
    tag_ids: list,
    link_id: str,
    link_url: str,
) -> OkResponse:
    """
    :param item_type:
    :param item_owner_id:
    :param item_id:
    :param tag_ids:
    :param link_id:
    :param link_url:
    :return:
    """
    pass


def fave_track_page_interaction(user_id: int, group_id: int,) -> OkResponse:
    """
    :param user_id:
    :param group_id:
    :return:
    """
    pass


def friends_add(user_id: int, text: str, follow: bool,) -> FriendsAddResponse:
    """
    :param user_id: - ID of the user whose friend request will be approved or to whom a friend request will be sent.
    :param text: - Text of the message (up to 500 characters) for the friend request, if any.
    :param follow: - '1' to pass an incoming request to followers list.
    :return:
    """
    pass


def friends_add_list(name: str, user_ids: list,) -> FriendsAddListResponse:
    """
    :param name: - Name of the friend list.
    :param user_ids: - IDs of users to be added to the friend list.
    :return:
    """
    pass


def friends_are_friends(user_ids: list, need_sign: bool,) -> FriendsAreFriendsResponse:
    """
    :param user_ids: - IDs of the users whose friendship status to check.
    :param need_sign: - '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
    :return:
    """
    pass


def friends_delete(user_id: int,) -> FriendsDeleteResponse:
    """
    :param user_id: - ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
    :return:
    """
    pass


def friends_delete_all_requests() -> OkResponse:
    """
    :return:
    """
    pass


def friends_delete_list(list_id: int,) -> OkResponse:
    """
    :param list_id: - ID of the friend list to delete.
    :return:
    """
    pass


def friends_edit(user_id: int, list_ids: list,) -> OkResponse:
    """
    :param user_id: - ID of the user whose friend list is to be edited.
    :param list_ids: - IDs of the friend lists to which to add the user.
    :return:
    """
    pass


def friends_edit_list(
    name: str, list_id: int, user_ids: list, add_user_ids: list, delete_user_ids: list,
) -> OkResponse:
    """
    :param name: - Name of the friend list.
    :param list_id: - Friend list ID.
    :param user_ids: - IDs of users in the friend list.
    :param add_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
    :param delete_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
    :return:
    """
    pass


def friends_get(
    user_id: int,
    order: str,
    list_id: int,
    count: int,
    offset: int,
    fields: list,
    name_case: str,
    ref: str,
) -> FriendsGetResponse:
    """
    :param user_id: - User ID. By default, the current user ID.
    :param order: - Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
    :param list_id: - ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
    :param count: - Number of friends to return.
    :param offset: - Offset needed to return a specific subset of friends.
    :param fields: - Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
    :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :param ref:
    :return:
    """
    pass


def friends_get_app_users() -> FriendsGetAppUsersResponse:
    """
    :return:
    """
    pass


def friends_get_by_phones(phones: list, fields: list,) -> FriendsGetByPhonesResponse:
    """
    :param phones: - List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
    :return:
    """
    pass


def friends_get_lists(user_id: int, return_system: bool,) -> FriendsGetListsResponse:
    """
    :param user_id: - User ID.
    :param return_system: - '1' — to return system friend lists. By default: '0'.
    :return:
    """
    pass


def friends_get_mutual(
    source_uid: int,
    target_uid: int,
    target_uids: list,
    order: str,
    count: int,
    offset: int,
) -> FriendsGetMutualResponse:
    """
    :param source_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
    :param target_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
    :param target_uids: - IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
    :param order: - Sort order: 'random' — random order
    :param count: - Number of mutual friends to return.
    :param offset: - Offset needed to return a specific subset of mutual friends.
    :return:
    """
    pass


def friends_get_online(
    user_id: int,
    list_id: int,
    online_mobile: bool,
    order: str,
    count: int,
    offset: int,
) -> FriendsGetOnlineResponse:
    """
    :param user_id: - User ID.
    :param list_id: - Friend list ID. If this parameter is not set, information about all online friends is returned.
    :param online_mobile: - '1' — to return an additional 'online_mobile' field, '0' — (default),
    :param order: - Sort order: 'random' — random order
    :param count: - Number of friends to return.
    :param offset: - Offset needed to return a specific subset of friends.
    :return:
    """
    pass


def friends_get_recent(count: int,) -> FriendsGetRecentResponse:
    """
    :param count: - Number of recently added friends to return.
    :return:
    """
    pass


def friends_get_requests(
    offset: int,
    count: int,
    extended: bool,
    need_mutual: bool,
    out: bool,
    sort: int,
    need_viewed: bool,
    suggested: bool,
    ref: str,
    fields: list,
) -> FriendsGetRequestsResponse:
    """
    :param offset: - Offset needed to return a specific subset of friend requests.
    :param count: - Number of friend requests to return (default 100, maximum 1000).
    :param extended: - '1' — to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
    :param need_mutual: - '1' — to return a list of mutual friends (up to 20), if any
    :param out: - '1' — to return outgoing requests, '0' — to return incoming requests (default)
    :param sort: - Sort order: '1' — by number of mutual friends, '0' — by date
    :param need_viewed:
    :param suggested: - '1' — to return a list of suggested friends, '0' — to return friend requests (default)
    :param ref:
    :param fields:
    :return:
    """
    pass


def friends_get_suggestions(
    filter: list, count: int, offset: int, fields: list, name_case: str,
) -> FriendsGetSuggestionsResponse:
    """
    :param filter: - Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
    :param count: - Number of suggestions to return.
    :param offset: - Offset needed to return a specific subset of suggestions.
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
    :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :return:
    """
    pass


def friends_search(
    user_id: int, q: str, fields: list, name_case: str, offset: int, count: int,
) -> FriendsSearchResponse:
    """
    :param user_id: - User ID.
    :param q: - Search query string (e.g., 'Vasya Babich').
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
    :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :param offset: - Offset needed to return a specific subset of friends.
    :param count: - Number of friends to return.
    :return:
    """
    pass


def gifts_get(user_id: int, count: int, offset: int,) -> GiftsGetResponse:
    """
    :param user_id: - User ID.
    :param count: - Number of gifts to return.
    :param offset: - Offset needed to return a specific subset of results.
    :return:
    """
    pass


def groups_add_address(
    group_id: int,
    title: str,
    address: str,
    additional_address: str,
    country_id: int,
    city_id: int,
    metro_id: int,
    latitude: int,
    longitude: int,
    phone: str,
    work_info_status: str,
    timetable: str,
    is_main_address: bool,
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
    pass


def groups_add_callback_server(
    group_id: int, url: str, title: str, secret_key: str,
) -> GroupsAddCallbackServerResponse:
    """
    :param group_id:
    :param url:
    :param title:
    :param secret_key:
    :return:
    """
    pass


def groups_add_link(group_id: int, link: str, text: str,) -> GroupsAddLinkResponse:
    """
    :param group_id: - Community ID.
    :param link: - Link URL.
    :param text: - Description text for the link.
    :return:
    """
    pass


def groups_approve_request(group_id: int, user_id: int,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param user_id: - User ID.
    :return:
    """
    pass


def groups_ban(
    group_id: int,
    owner_id: int,
    end_date: int,
    reason: int,
    comment: str,
    comment_visible: bool,
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
    pass


def groups_create(
    title: str, description: str, type: str, public_category: int, subtype: int,
) -> GroupsCreateResponse:
    """
    :param title: - Community title.
    :param description: - Community description (ignored for 'type' = 'public').
    :param type: - Community type. Possible values: *'group' – group,, *'event' – event,, *'public' – public page
    :param public_category: - Category ID (for 'type' = 'public' only).
    :param subtype: - Public page subtype. Possible values: *'1' – place or small business,, *'2' – company, organization or website,, *'3' – famous person or group of people,, *'4' – product or work of art.
    :return:
    """
    pass


def groups_delete_callback_server(group_id: int, server_id: int,) -> OkResponse:
    """
    :param group_id:
    :param server_id:
    :return:
    """
    pass


def groups_delete_link(group_id: int, link_id: int,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param link_id: - Link ID.
    :return:
    """
    pass


def groups_disable_online(group_id: int,) -> OkResponse:
    """
    :param group_id:
    :return:
    """
    pass


def groups_edit(
    group_id: int,
    title: str,
    description: str,
    screen_name: str,
    access: int,
    website: str,
    subject: str,
    email: str,
    phone: str,
    rss: str,
    event_start_date: int,
    event_finish_date: int,
    event_group_id: int,
    public_category: int,
    public_subcategory: int,
    public_date: str,
    wall: int,
    topics: int,
    photos: int,
    video: int,
    audio: int,
    links: bool,
    events: bool,
    places: bool,
    contacts: bool,
    docs: int,
    wiki: int,
    messages: bool,
    articles: bool,
    addresses: bool,
    age_limits: int,
    market: bool,
    market_comments: bool,
    market_country: list,
    market_city: list,
    market_currency: int,
    market_contact: int,
    market_wiki: int,
    obscene_filter: bool,
    obscene_stopwords: bool,
    obscene_words: list,
    main_section: int,
    secondary_section: int,
    country: int,
    city: int,
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
    pass


def groups_edit_address(
    group_id: int,
    address_id: int,
    title: str,
    address: str,
    additional_address: str,
    country_id: int,
    city_id: int,
    metro_id: int,
    latitude: int,
    longitude: int,
    phone: str,
    work_info_status: str,
    timetable: str,
    is_main_address: bool,
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
    pass


def groups_edit_callback_server(
    group_id: int, server_id: int, url: str, title: str, secret_key: str,
) -> OkResponse:
    """
    :param group_id:
    :param server_id:
    :param url:
    :param title:
    :param secret_key:
    :return:
    """
    pass


def groups_edit_link(group_id: int, link_id: int, text: str,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param link_id: - Link ID.
    :param text: - New description text for the link.
    :return:
    """
    pass


def groups_edit_manager(
    group_id: int,
    user_id: int,
    role: str,
    is_contact: bool,
    contact_position: str,
    contact_phone: str,
    contact_email: str,
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
    pass


def groups_enable_online(group_id: int,) -> OkResponse:
    """
    :param group_id:
    :return:
    """
    pass


def groups_get(
    user_id: int, extended: bool, filter: list, fields: list, offset: int, count: int,
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
    pass


def groups_get_addresses(
    group_id: int,
    address_ids: list,
    latitude: int,
    longitude: int,
    offset: int,
    count: int,
    fields: list,
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
    pass


def groups_get_banned(
    group_id: int, offset: int, count: int, fields: list, owner_id: int,
) -> GroupsGetBannedResponse:
    """
    :param group_id: - Community ID.
    :param offset: - Offset needed to return a specific subset of users.
    :param count: - Number of users to return.
    :param fields:
    :param owner_id:
    :return:
    """
    pass


def groups_get_by_id(
    group_ids: list, group_id: str, fields: list,
) -> GroupsGetByIdResponse:
    """
    :param group_ids: - IDs or screen names of communities.
    :param group_id: - ID or screen name of the community.
    :param fields: - Group fields to return.
    :return:
    """
    pass


def groups_get_callback_confirmation_code(
    group_id: int,
) -> GroupsGetCallbackConfirmationCodeResponse:
    """
    :param group_id: - Community ID.
    :return:
    """
    pass


def groups_get_callback_servers(
    group_id: int, server_ids: list,
) -> GroupsGetCallbackServersResponse:
    """
    :param group_id:
    :param server_ids:
    :return:
    """
    pass


def groups_get_callback_settings(
    group_id: int, server_id: int,
) -> GroupsGetCallbackSettingsResponse:
    """
    :param group_id: - Community ID.
    :param server_id: - Server ID.
    :return:
    """
    pass


def groups_get_catalog(
    category_id: int, subcategory_id: int,
) -> GroupsGetCatalogResponse:
    """
    :param category_id: - Category id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
    :param subcategory_id: - Subcategory id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
    :return:
    """
    pass


def groups_get_catalog_info(
    extended: bool, subcategories: bool,
) -> GroupsGetCatalogInfoResponse:
    """
    :param extended: - 1 – to return communities count and three communities for preview. By default: 0.
    :param subcategories: - 1 – to return subcategories info. By default: 0.
    :return:
    """
    pass


def groups_get_invited_users(
    group_id: int, offset: int, count: int, fields: list, name_case: str,
) -> GroupsGetInvitedUsersResponse:
    """
    :param group_id: - Group ID to return invited users for.
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of results to return.
    :param fields: - List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
    :param name_case: - Case for declension of user name and surname. Possible values: *'nom' — nominative (default),, *'gen' — genitive,, *'dat' — dative,, *'acc' — accusative, , *'ins' — instrumental,, *'abl' — prepositional.
    :return:
    """
    pass


def groups_get_invites(
    offset: int, count: int, extended: bool,
) -> GroupsGetInvitesResponse:
    """
    :param offset: - Offset needed to return a specific subset of invitations.
    :param count: - Number of invitations to return.
    :param extended: - '1' — to return additional [vk.com/dev/fields_groups|fields] for communities..
    :return:
    """
    pass


def groups_get_long_poll_server(group_id: int,) -> GroupsGetLongPollServerResponse:
    """
    :param group_id: - Community ID
    :return:
    """
    pass


def groups_get_long_poll_settings(group_id: int,) -> GroupsGetLongPollSettingsResponse:
    """
    :param group_id: - Community ID.
    :return:
    """
    pass


def groups_get_members(
    group_id: str, sort: str, offset: int, count: int, fields: list, filter: str,
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
    pass


def groups_get_requests(
    group_id: int, offset: int, count: int, fields: list,
) -> GroupsGetRequestsResponse:
    """
    :param group_id: - Community ID.
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of results to return.
    :param fields: - Profile fields to return.
    :return:
    """
    pass


def groups_get_settings(group_id: int,) -> GroupsGetSettingsResponse:
    """
    :param group_id: - Community ID.
    :return:
    """
    pass


def groups_get_token_permissions() -> GroupsGetTokenPermissionsResponse:
    """
    :return:
    """
    pass


def groups_invite(group_id: int, user_id: int,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param user_id: - User ID.
    :return:
    """
    pass


def groups_is_member(
    group_id: str, user_id: int, user_ids: list, extended: bool,
) -> GroupsIsMemberResponse:
    """
    :param group_id: - ID or screen name of the community.
    :param user_id: - User ID.
    :param user_ids: - User IDs.
    :param extended: - '1' — to return an extended response with additional fields. By default: '0'.
    :return:
    """
    pass


def groups_join(group_id: int, not_sure: str,) -> OkResponse:
    """
    :param group_id: - ID or screen name of the community.
    :param not_sure: - Optional parameter which is taken into account when 'gid' belongs to the event: '1' — Perhaps I will attend, '0' — I will be there for sure (default), ,
    :return:
    """
    pass


def groups_leave(group_id: int,) -> OkResponse:
    """
    :param group_id: - ID or screen name of the community.
    :return:
    """
    pass


def groups_remove_user(group_id: int, user_id: int,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param user_id: - User ID.
    :return:
    """
    pass


def groups_reorder_link(group_id: int, link_id: int, after: int,) -> OkResponse:
    """
    :param group_id: - Community ID.
    :param link_id: - Link ID.
    :param after: - ID of the link after which to place the link with 'link_id'.
    :return:
    """
    pass


def groups_search(
    q: str,
    type: str,
    country_id: int,
    city_id: int,
    future: bool,
    market: bool,
    sort: int,
    offset: int,
    count: int,
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
    pass


def groups_set_callback_settings(
    group_id: int,
    server_id: int,
    api_version: str,
    message_new: bool,
    message_reply: bool,
    message_allow: bool,
    message_edit: bool,
    message_deny: bool,
    message_typing_state: bool,
    photo_new: bool,
    audio_new: bool,
    video_new: bool,
    wall_reply_new: bool,
    wall_reply_edit: bool,
    wall_reply_delete: bool,
    wall_reply_restore: bool,
    wall_post_new: bool,
    wall_repost: bool,
    board_post_new: bool,
    board_post_edit: bool,
    board_post_restore: bool,
    board_post_delete: bool,
    photo_comment_new: bool,
    photo_comment_edit: bool,
    photo_comment_delete: bool,
    photo_comment_restore: bool,
    video_comment_new: bool,
    video_comment_edit: bool,
    video_comment_delete: bool,
    video_comment_restore: bool,
    market_comment_new: bool,
    market_comment_edit: bool,
    market_comment_delete: bool,
    market_comment_restore: bool,
    poll_vote_new: bool,
    group_join: bool,
    group_leave: bool,
    group_change_settings: bool,
    group_change_photo: bool,
    group_officers_edit: bool,
    user_block: bool,
    user_unblock: bool,
    lead_forms_new: bool,
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
    pass


def groups_set_long_poll_settings(
    group_id: int,
    enabled: bool,
    api_version: str,
    message_new: bool,
    message_reply: bool,
    message_allow: bool,
    message_deny: bool,
    message_edit: bool,
    message_typing_state: bool,
    photo_new: bool,
    audio_new: bool,
    video_new: bool,
    wall_reply_new: bool,
    wall_reply_edit: bool,
    wall_reply_delete: bool,
    wall_reply_restore: bool,
    wall_post_new: bool,
    wall_repost: bool,
    board_post_new: bool,
    board_post_edit: bool,
    board_post_restore: bool,
    board_post_delete: bool,
    photo_comment_new: bool,
    photo_comment_edit: bool,
    photo_comment_delete: bool,
    photo_comment_restore: bool,
    video_comment_new: bool,
    video_comment_edit: bool,
    video_comment_delete: bool,
    video_comment_restore: bool,
    market_comment_new: bool,
    market_comment_edit: bool,
    market_comment_delete: bool,
    market_comment_restore: bool,
    poll_vote_new: bool,
    group_join: bool,
    group_leave: bool,
    group_change_settings: bool,
    group_change_photo: bool,
    group_officers_edit: bool,
    user_block: bool,
    user_unblock: bool,
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
    pass


def groups_unban(group_id: int, owner_id: int,) -> OkResponse:
    """
    :param group_id:
    :param owner_id:
    :return:
    """
    pass


def leads_check_user(
    lead_id: int,
    test_result: int,
    test_mode: bool,
    auto_start: bool,
    age: int,
    country: str,
) -> LeadsCheckUserResponse:
    """
    :param lead_id: - Lead ID.
    :param test_result: - Value to be return in 'result' field when test mode is used.
    :param test_mode:
    :param auto_start:
    :param age: - User age.
    :param country: - User country code.
    :return:
    """
    pass


def leads_complete(vk_sid: str, secret: str, comment: str,) -> LeadsCompleteResponse:
    """
    :param vk_sid: - Session obtained as GET parameter when session started.
    :param secret: - Secret key from the lead testing interface.
    :param comment: - Comment text.
    :return:
    """
    pass


def leads_get_stats(
    lead_id: int, secret: str, date_start: str, date_end: str,
) -> LeadsGetStatsResponse:
    """
    :param lead_id: - Lead ID.
    :param secret: - Secret key obtained from the lead testing interface.
    :param date_start: - Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
    :param date_end: - Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
    :return:
    """
    pass


def leads_get_users(
    offer_id: int, secret: str, offset: int, count: int, status: int, reverse: bool,
) -> LeadsGetUsersResponse:
    """
    :param offer_id: - Offer ID.
    :param secret: - Secret key obtained in the lead testing interface.
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of results to return.
    :param status: - Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
    :param reverse: - Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
    :return:
    """
    pass


def leads_metric_hit(data: str,) -> LeadsMetricHitResponse:
    """
    :param data: - Metric data obtained in the lead interface.
    :return:
    """
    pass


def leads_start(
    lead_id: int, secret: str, uid: int, aid: int, test_mode: bool, force: bool,
) -> LeadsStartResponse:
    """
    :param lead_id: - Lead ID.
    :param secret: - Secret key from the lead testing interface.
    :param uid:
    :param aid:
    :param test_mode:
    :param force:
    :return:
    """
    pass


def likes_add(
    type: str, owner_id: int, item_id: int, access_key: str,
) -> LikesAddResponse:
    """
    :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
    :param owner_id: - ID of the user or community that owns the object.
    :param item_id: - Object ID.
    :param access_key: - Access key required for an object owned by a private entity.
    :return:
    """
    pass


def likes_delete(type: str, owner_id: int, item_id: int,) -> LikesDeleteResponse:
    """
    :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
    :param owner_id: - ID of the user or community that owns the object.
    :param item_id: - Object ID.
    :return:
    """
    pass


def likes_get_list(
    type: str,
    owner_id: int,
    item_id: int,
    page_url: str,
    filter: str,
    friends_only: int,
    extended: bool,
    offset: int,
    count: int,
    skip_own: bool,
) -> LikesGetListResponse:
    """
    :param type: - , Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
    :param owner_id: - ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
    :param item_id: - Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
    :param page_url: - URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
    :param filter: - Filters to apply: 'likes' — returns information about all users who liked the object (default), 'copies' — returns information only about users who told their friends about the object
    :param friends_only: - Specifies which users are returned: '1' — to return only the current user's friends, '0' — to return all users (default)
    :param extended: - Specifies whether extended information will be returned. '1' — to return extended information about users and communities from the 'Likes' list, '0' — to return no additional information (default)
    :param offset: - Offset needed to select a specific subset of users.
    :param count: - Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
    :param skip_own:
    :return:
    """
    pass


def likes_is_liked(
    user_id: int, type: str, owner_id: int, item_id: int,
) -> LikesIsLikedResponse:
    """
    :param user_id: - User ID.
    :param type: - Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion
    :param owner_id: - ID of the user or community that owns the object.
    :param item_id: - Object ID.
    :return:
    """
    pass


def market_add(
    owner_id: int,
    name: str,
    description: str,
    category_id: int,
    price: int,
    old_price: int,
    deleted: bool,
    main_photo_id: int,
    photo_ids: list,
    url: str,
) -> MarketAddResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param name: - Item name.
    :param description: - Item description.
    :param category_id: - Item category ID.
    :param price: - Item price.
    :param old_price:
    :param deleted: - Item status ('1' — deleted, '0' — not deleted).
    :param main_photo_id: - Cover photo ID.
    :param photo_ids: - IDs of additional photos.
    :param url: - Url for button in market item.
    :return:
    """
    pass


def market_add_album(
    owner_id: int, title: str, photo_id: int, main_album: bool,
) -> MarketAddAlbumResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param title: - Collection title.
    :param photo_id: - Cover photo ID.
    :param main_album: - Set as main ('1' – set, '0' – no).
    :return:
    """
    pass


def market_add_to_album(owner_id: int, item_id: int, album_ids: list,) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :param album_ids: - Collections IDs to add item to.
    :return:
    """
    pass


def market_create_comment(
    owner_id: int,
    item_id: int,
    message: str,
    attachments: list,
    from_group: bool,
    reply_to_comment: int,
    sticker_id: int,
    guid: str,
) -> MarketCreateCommentResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :param message: - Comment text (required if 'attachments' parameter is not specified)
    :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
    :param from_group: - '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
    :param reply_to_comment: - ID of a comment to reply with current comment to.
    :param sticker_id: - Sticker ID.
    :param guid: - Random value to avoid resending one comment.
    :return:
    """
    pass


def market_delete(owner_id: int, item_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :return:
    """
    pass


def market_delete_album(owner_id: int, album_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of an collection owner community.
    :param album_id: - Collection ID.
    :return:
    """
    pass


def market_delete_comment(
    owner_id: int, comment_id: int,
) -> MarketDeleteCommentResponse:
    """
    :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
    :param comment_id: - comment id
    :return:
    """
    pass


def market_edit(
    owner_id: int,
    item_id: int,
    name: str,
    description: str,
    category_id: int,
    price: int,
    deleted: bool,
    main_photo_id: int,
    photo_ids: list,
    url: str,
) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :param name: - Item name.
    :param description: - Item description.
    :param category_id: - Item category ID.
    :param price: - Item price.
    :param deleted: - Item status ('1' — deleted, '0' — not deleted).
    :param main_photo_id: - Cover photo ID.
    :param photo_ids: - IDs of additional photos.
    :param url: - Url for button in market item.
    :return:
    """
    pass


def market_edit_album(
    owner_id: int, album_id: int, title: str, photo_id: int, main_album: bool,
) -> OkResponse:
    """
    :param owner_id: - ID of an collection owner community.
    :param album_id: - Collection ID.
    :param title: - Collection title.
    :param photo_id: - Cover photo id
    :param main_album: - Set as main ('1' – set, '0' – no).
    :return:
    """
    pass


def market_edit_comment(
    owner_id: int, comment_id: int, message: str, attachments: list,
) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param comment_id: - Comment ID.
    :param message: - New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
    :param attachments: - Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
    :return:
    """
    pass


def market_get(
    owner_id: int, album_id: int, count: int, offset: int, extended: bool,
) -> MarketGetResponse:
    """
    :param owner_id: - ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
    :param album_id:
    :param count: - Number of items to return.
    :param offset: - Offset needed to return a specific subset of results.
    :param extended: - '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
    :return:
    """
    pass


def market_get_album_by_id(
    owner_id: int, album_ids: list,
) -> MarketGetAlbumByIdResponse:
    """
    :param owner_id: - identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
    :param album_ids: - collections identifiers to obtain data from
    :return:
    """
    pass


def market_get_albums(
    owner_id: int, offset: int, count: int,
) -> MarketGetAlbumsResponse:
    """
    :param owner_id: - ID of an items owner community.
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of items to return.
    :return:
    """
    pass


def market_get_by_id(item_ids: list, extended: bool,) -> MarketGetByIdResponse:
    """
    :param item_ids: - Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
    :param extended: - '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
    :return:
    """
    pass


def market_get_categories(count: int, offset: int,) -> MarketGetCategoriesResponse:
    """
    :param count: - Number of results to return.
    :param offset: - Offset needed to return a specific subset of results.
    :return:
    """
    pass


def market_get_comments(
    owner_id: int,
    item_id: int,
    need_likes: bool,
    start_comment_id: int,
    offset: int,
    count: int,
    sort: str,
    extended: bool,
    fields: list,
) -> MarketGetCommentsResponse:
    """
    :param owner_id: - ID of an item owner community
    :param item_id: - Item ID.
    :param need_likes: - '1' — to return likes info.
    :param start_comment_id: - ID of a comment to start a list from (details below).
    :param offset:
    :param count: - Number of results to return.
    :param sort: - Sort order ('asc' — from old to new, 'desc' — from new to old)
    :param extended: - '1' — comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
    :param fields: - List of additional profile fields to return. See the [vk.com/dev/fields|details]
    :return:
    """
    pass


def market_remove_from_album(
    owner_id: int, item_id: int, album_ids: list,
) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :param album_ids: - Collections IDs to remove item from.
    :return:
    """
    pass


def market_reorder_albums(
    owner_id: int, album_id: int, before: int, after: int,
) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param album_id: - Collection ID.
    :param before: - ID of a collection to place current collection before it.
    :param after: - ID of a collection to place current collection after it.
    :return:
    """
    pass


def market_reorder_items(
    owner_id: int, album_id: int, item_id: int, before: int, after: int,
) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param album_id: - ID of a collection to reorder items in. Set 0 to reorder full items list.
    :param item_id: - Item ID.
    :param before: - ID of an item to place current item before it.
    :param after: - ID of an item to place current item after it.
    :return:
    """
    pass


def market_report(owner_id: int, item_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Item ID.
    :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
    :return:
    """
    pass


def market_report_comment(owner_id: int, comment_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param comment_id: - Comment ID.
    :param reason: - Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
    :return:
    """
    pass


def market_restore(owner_id: int, item_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of an item owner community.
    :param item_id: - Deleted item ID.
    :return:
    """
    pass


def market_restore_comment(
    owner_id: int, comment_id: int,
) -> MarketRestoreCommentResponse:
    """
    :param owner_id: - identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
    :param comment_id: - deleted comment id
    :return:
    """
    pass


def market_search(
    owner_id: int,
    album_id: int,
    q: str,
    price_from: int,
    price_to: int,
    tags: list,
    sort: int,
    rev: int,
    offset: int,
    count: int,
    extended: bool,
    status: int,
) -> MarketSearchResponse:
    """
    :param owner_id: - ID of an items owner community.
    :param album_id:
    :param q: - Search query, for example "pink slippers".
    :param price_from: - Minimum item price value.
    :param price_to: - Maximum item price value.
    :param tags: - Comma-separated tag IDs list.
    :param sort:
    :param rev: - '0' — do not use reverse order, '1' — use reverse order
    :param offset: - Offset needed to return a specific subset of results.
    :param count: - Number of items to return.
    :param extended: - '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
    :param status:
    :return:
    """
    pass


def messages_add_chat_user(chat_id: int, user_id: int,) -> OkResponse:
    """
    :param chat_id: - Chat ID.
    :param user_id: - ID of the user to be added to the chat.
    :return:
    """
    pass


def messages_allow_messages_from_group(group_id: int, key: str,) -> OkResponse:
    """
    :param group_id: - Group ID.
    :param key:
    :return:
    """
    pass


def messages_create_chat(user_ids: list, title: str,) -> MessagesCreateChatResponse:
    """
    :param user_ids: - IDs of the users to be added to the chat.
    :param title: - Chat title.
    :return:
    """
    pass


def messages_delete(
    message_ids: list, spam: bool, group_id: int, delete_for_all: bool,
) -> MessagesDeleteResponse:
    """
    :param message_ids: - Message IDs.
    :param spam: - '1' — to mark message as spam.
    :param group_id: - Group ID (for group messages with user access token)
    :param delete_for_all: - '1' — delete message for for all.
    :return:
    """
    pass


def messages_delete_chat_photo(
    chat_id: int, group_id: int,
) -> MessagesDeleteChatPhotoResponse:
    """
    :param chat_id: - Chat ID.
    :param group_id:
    :return:
    """
    pass


def messages_delete_conversation(
    user_id: int, peer_id: int, group_id: int,
) -> MessagesDeleteConversationResponse:
    """
    :param user_id: - User ID. To clear a chat history use 'chat_id'
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param group_id: - Group ID (for group messages with user access token)
    :return:
    """
    pass


def messages_deny_messages_from_group(group_id: int,) -> OkResponse:
    """
    :param group_id: - Group ID.
    :return:
    """
    pass


def messages_edit(
    peer_id: int,
    message: str,
    message_id: int,
    lat: int,
    long: int,
    attachment: str,
    keep_forward_messages: bool,
    keep_snippets: bool,
    group_id: int,
    dont_parse_links: bool,
) -> MessagesEditResponse:
    """
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param message: - (Required if 'attachments' is not set.) Text of the message.
    :param message_id:
    :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
    :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
    :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
    :param keep_forward_messages: - '1' — to keep forwarded, messages.
    :param keep_snippets: - '1' — to keep attached snippets.
    :param group_id: - Group ID (for group messages with user access token)
    :param dont_parse_links:
    :return:
    """
    pass


def messages_edit_chat(chat_id: int, title: str,) -> OkResponse:
    """
    :param chat_id: - Chat ID.
    :param title: - New title of the chat.
    :return:
    """
    pass


def messages_get_by_conversation_message_id(
    peer_id: int,
    conversation_message_ids: list,
    extended: bool,
    fields: list,
    group_id: int,
) -> MessagesGetByConversationMessageIdResponse:
    """
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param conversation_message_ids: - Conversation message IDs.
    :param extended: - Information whether the response should be extended
    :param fields: - Profile fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_by_id(
    message_ids: list, preview_length: int, extended: bool, fields: list, group_id: int,
) -> MessagesGetByIdResponse:
    """
    :param message_ids: - Message IDs.
    :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
    :param extended: - Information whether the response should be extended
    :param fields: - Profile fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_chat_preview(
    peer_id: int, link: str, fields: list,
) -> MessagesGetChatPreviewResponse:
    """
    :param peer_id:
    :param link: - Invitation link.
    :param fields: - Profile fields to return.
    :return:
    """
    pass


def messages_get_conversation_members(
    peer_id: int, fields: list, group_id: int,
) -> MessagesGetConversationMembersResponse:
    """
    :param peer_id: - Peer ID.
    :param fields: - Profile fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_conversations(
    offset: int,
    count: int,
    filter: str,
    extended: bool,
    start_message_id: int,
    fields: list,
    group_id: int,
) -> MessagesGetConversationsResponse:
    """
    :param offset: - Offset needed to return a specific subset of conversations.
    :param count: - Number of conversations to return.
    :param filter: - Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
    :param extended: - '1' — return extra information about users and communities
    :param start_message_id: - ID of the message from what to return dialogs.
    :param fields: - Profile and communities fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_conversations_by_id(
    peer_ids: list, extended: bool, fields: list, group_id: int,
) -> MessagesGetConversationsByIdResponse:
    """
    :param peer_ids: - Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param extended: - Return extended properties
    :param fields: - Profile and communities fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_history(
    offset: int,
    count: int,
    user_id: int,
    peer_id: int,
    start_message_id: int,
    rev: int,
    extended: bool,
    fields: list,
    group_id: int,
) -> MessagesGetHistoryResponse:
    """
    :param offset: - Offset needed to return a specific subset of messages.
    :param count: - Number of messages to return.
    :param user_id: - ID of the user whose message history you want to return.
    :param peer_id:
    :param start_message_id: - Starting message ID from which to return history.
    :param rev: - Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
    :param extended: - Information whether the response should be extended
    :param fields: - Profile fields to return.
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_get_history_attachments(
    peer_id: int,
    media_type: str,
    start_from: str,
    count: int,
    photo_sizes: bool,
    fields: list,
    group_id: int,
    preserve_order: bool,
    max_forwards_level: int,
) -> MessagesGetHistoryAttachmentsResponse:
    """
    :param peer_id: - Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
    :param media_type: - Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
    :param start_from: - Message ID to start return results from.
    :param count: - Number of objects to return.
    :param photo_sizes: - '1' — to return photo sizes in a
    :param fields: - Additional profile [vk.com/dev/fields|fields] to return. 
    :param group_id: - Group ID (for group messages with group access token)
    :param preserve_order:
    :param max_forwards_level:
    :return:
    """
    pass


def messages_get_invite_link(
    peer_id: int, reset: bool, group_id: int,
) -> MessagesGetInviteLinkResponse:
    """
    :param peer_id: - Destination ID.
    :param reset: - 1 — to generate new link (revoke previous), 0 — to return previous link.
    :param group_id: - Group ID
    :return:
    """
    pass


def messages_get_last_activity(user_id: int,) -> MessagesGetLastActivityResponse:
    """
    :param user_id: - User ID.
    :return:
    """
    pass


def messages_get_long_poll_history(
    ts: int,
    pts: int,
    preview_length: int,
    onlines: bool,
    fields: list,
    events_limit: int,
    msgs_limit: int,
    max_msg_id: int,
    group_id: int,
    lp_version: int,
    last_n: int,
    credentials: bool,
) -> MessagesGetLongPollHistoryResponse:
    """
    :param ts: - Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
    :param pts: - Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
    :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
    :param onlines: - '1' — to return history with online users only.
    :param fields: - Additional profile [vk.com/dev/fields|fields] to return.
    :param events_limit: - Maximum number of events to return.
    :param msgs_limit: - Maximum number of messages to return.
    :param max_msg_id: - Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
    :param group_id: - Group ID (for group messages with user access token)
    :param lp_version:
    :param last_n:
    :param credentials:
    :return:
    """
    pass


def messages_get_long_poll_server(
    need_pts: bool, group_id: int, lp_version: int,
) -> MessagesGetLongPollServerResponse:
    """
    :param need_pts: - '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
    :param group_id: - Group ID (for group messages with user access token)
    :param lp_version: - Long poll version
    :return:
    """
    pass


def messages_is_messages_from_group_allowed(
    group_id: int, user_id: int,
) -> MessagesIsMessagesFromGroupAllowedResponse:
    """
    :param group_id: - Group ID.
    :param user_id: - User ID.
    :return:
    """
    pass


def messages_join_chat_by_invite_link(
    link: str,
) -> MessagesJoinChatByInviteLinkResponse:
    """
    :param link: - Invitation link.
    :return:
    """
    pass


def messages_mark_as_answered_conversation(
    peer_id: int, answered: bool, group_id: int,
) -> OkResponse:
    """
    :param peer_id: - ID of conversation to mark as important.
    :param answered: - '1' — to mark as answered, '0' — to remove the mark
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_mark_as_important(
    message_ids: list, important: int,
) -> MessagesMarkAsImportantResponse:
    """
    :param message_ids: - IDs of messages to mark as important.
    :param important: - '1' — to add a star (mark as important), '0' — to remove the star
    :return:
    """
    pass


def messages_mark_as_important_conversation(
    peer_id: int, important: bool, group_id: int,
) -> OkResponse:
    """
    :param peer_id: - ID of conversation to mark as important.
    :param important: - '1' — to add a star (mark as important), '0' — to remove the star
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_mark_as_read(
    message_ids: list, peer_id: int, start_message_id: int, group_id: int,
) -> OkResponse:
    """
    :param message_ids: - IDs of messages to mark as read.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param start_message_id: - Message ID to start from.
    :param group_id: - Group ID (for group messages with user access token)
    :return:
    """
    pass


def messages_pin(peer_id: int, message_id: int,) -> MessagesPinResponse:
    """
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
    :param message_id:
    :return:
    """
    pass


def messages_remove_chat_user(
    chat_id: int, user_id: int, member_id: int,
) -> OkResponse:
    """
    :param chat_id: - Chat ID.
    :param user_id: - ID of the user to be removed from the chat.
    :param member_id:
    :return:
    """
    pass


def messages_restore(message_id: int, group_id: int,) -> OkResponse:
    """
    :param message_id: - ID of a previously-deleted message to restore.
    :param group_id: - Group ID (for group messages with user access token)
    :return:
    """
    pass


def messages_search(
    q: str,
    peer_id: int,
    date: int,
    preview_length: int,
    offset: int,
    count: int,
    extended: bool,
    fields: list,
    group_id: int,
) -> MessagesSearchResponse:
    """
    :param q: - Search query string.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param date: - Date to search message before in Unixtime.
    :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
    :param offset: - Offset needed to return a specific subset of messages.
    :param count: - Number of messages to return.
    :param extended:
    :param fields:
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_search_conversations(
    q: str, count: int, extended: bool, fields: list, group_id: int,
) -> MessagesSearchConversationsResponse:
    """
    :param q: - Search query string.
    :param count: - Maximum number of results.
    :param extended: - '1' — return extra information about users and communities
    :param fields: - Profile fields to return.
    :param group_id: - Group ID (for group messages with user access token)
    :return:
    """
    pass


def messages_send(
    user_id: int,
    random_id: int,
    peer_id: int,
    domain: str,
    chat_id: int,
    user_ids: list,
    message: str,
    lat: int,
    long: int,
    attachment: str,
    reply_to: int,
    forward_messages: list,
    forward: str,
    sticker_id: int,
    group_id: int,
    keyboard: str,
    payload: str,
    dont_parse_links: bool,
    disable_mentions: bool,
) -> MessagesSendResponse:
    """
    :param user_id: - User ID (by default — current user).
    :param random_id: - Unique identifier to avoid resending the message.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param domain: - User's short address (for example, 'illarionov').
    :param chat_id: - ID of conversation the message will relate to.
    :param user_ids: - IDs of message recipients (if new conversation shall be started).
    :param message: - (Required if 'attachments' is not set.) Text of the message.
    :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
    :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
    :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
    :param reply_to:
    :param forward_messages: - ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
    :param forward:
    :param sticker_id: - Sticker id.
    :param group_id: - Group ID (for group messages with group access token)
    :param keyboard:
    :param payload:
    :param dont_parse_links:
    :param disable_mentions:
    :return:
    """
    pass


def messages_set_activity(
    user_id: int, type: str, peer_id: int, group_id: int,
) -> OkResponse:
    """
    :param user_id: - User ID.
    :param type: - 'typing' — user has started to type.
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
    :param group_id: - Group ID (for group messages with group access token)
    :return:
    """
    pass


def messages_set_chat_photo(file: str,) -> MessagesSetChatPhotoResponse:
    """
    :param file: - Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
    :return:
    """
    pass


def messages_unpin(peer_id: int, group_id: int,) -> OkResponse:
    """
    :param peer_id:
    :param group_id:
    :return:
    """
    pass


def newsfeed_add_ban(user_ids: list, group_ids: list,) -> OkResponse:
    """
    :param user_ids:
    :param group_ids:
    :return:
    """
    pass


def newsfeed_delete_ban(user_ids: list, group_ids: list,) -> OkResponse:
    """
    :param user_ids:
    :param group_ids:
    :return:
    """
    pass


def newsfeed_delete_list(list_id: int,) -> OkResponse:
    """
    :param list_id:
    :return:
    """
    pass


def newsfeed_get(
    filters: list,
    return_banned: bool,
    start_time: int,
    end_time: int,
    max_photos: int,
    source_ids: str,
    start_from: str,
    count: int,
    fields: list,
    section: str,
) -> NewsfeedGetResponse:
    """
    :param filters: - Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends, 'note' — new notes
    :param return_banned: - '1' — to return news items from banned sources
    :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
    :param max_photos: - Maximum number of photos to return. By default, '5'.
    :param source_ids: - Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
    :param start_from: - identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
    :param count: - Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
    :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
    :param section:
    :return:
    """
    pass


def newsfeed_get_banned(
    extended: bool, fields: list, name_case: str,
) -> NewsfeedGetBannedResponse:
    """
    :param extended: - '1' — return extra information about users and communities
    :param fields: - Profile fields to return.
    :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :return:
    """
    pass


def newsfeed_get_comments(
    count: int,
    filters: list,
    reposts: str,
    start_time: int,
    end_time: int,
    last_comments_count: int,
    start_from: str,
    fields: list,
) -> NewsfeedGetCommentsResponse:
    """
    :param count: - Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
    :param filters: - Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
    :param reposts: - Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
    :param start_time: - Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a comment to return. By default, the current time.
    :param last_comments_count:
    :param start_from: - Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
    :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
    :return:
    """
    pass


def newsfeed_get_lists(list_ids: list, extended: bool,) -> NewsfeedGetListsResponse:
    """
    :param list_ids: - numeric list identifiers.
    :param extended: - Return additional list info
    :return:
    """
    pass


def newsfeed_get_mentions(
    owner_id: int, start_time: int, end_time: int, offset: int, count: int,
) -> NewsfeedGetMentionsResponse:
    """
    :param owner_id: - Owner ID.
    :param start_time: - Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a post to return. By default, the current time.
    :param offset: - Offset needed to return a specific subset of posts.
    :param count: - Number of posts to return.
    :return:
    """
    pass


def newsfeed_get_recommended(
    start_time: int,
    end_time: int,
    max_photos: int,
    start_from: str,
    count: int,
    fields: list,
) -> NewsfeedGetRecommendedResponse:
    """
    :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
    :param max_photos: - Maximum number of photos to return. By default, '5'.
    :param start_from: - 'new_from' value obtained in previous call.
    :param count: - Number of news items to return.
    :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
    :return:
    """
    pass


def newsfeed_get_suggested_sources(
    offset: int, count: int, shuffle: bool, fields: list,
) -> NewsfeedGetSuggestedSourcesResponse:
    """
    :param offset: - offset required to choose a particular subset of communities or users.
    :param count: - amount of communities or users to return.
    :param shuffle: - shuffle the returned list or not.
    :param fields: - list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
    :return:
    """
    pass


def newsfeed_ignore_item(type: str, owner_id: int, item_id: int,) -> OkResponse:
    """
    :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
    :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
    :param item_id: - Item identifier
    :return:
    """
    pass


def newsfeed_save_list(
    list_id: int, title: str, source_ids: list, no_reposts: bool,
) -> NewsfeedSaveListResponse:
    """
    :param list_id: - numeric list identifier (if not sent, will be set automatically).
    :param title: - list name.
    :param source_ids: - users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
    :param no_reposts: - reposts display on and off ('1' is for off).
    :return:
    """
    pass


def newsfeed_search(
    q: str,
    extended: bool,
    count: int,
    latitude: int,
    longitude: int,
    start_time: int,
    end_time: int,
    start_from: str,
    fields: list,
) -> NewsfeedSearchResponse:
    """
    :param q: - Search query string (e.g., 'New Year').
    :param extended: - '1' — to return additional information about the user or community that placed the post.
    :param count: - Number of posts to return.
    :param latitude: - Geographical latitude point (in degrees, -90 to 90) within which to search.
    :param longitude: - Geographical longitude point (in degrees, -180 to 180) within which to search.
    :param start_time: - Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a news item to return. By default, the current time.
    :param start_from:
    :param fields: - Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
    :return:
    """
    pass


def newsfeed_unignore_item(type: str, owner_id: int, item_id: int,) -> OkResponse:
    """
    :param type: - Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
    :param owner_id: - Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
    :param item_id: - Item identifier
    :return:
    """
    pass


def newsfeed_unsubscribe(type: str, owner_id: int, item_id: int,) -> OkResponse:
    """
    :param type: - Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
    :param owner_id: - Object owner ID.
    :param item_id: - Object ID.
    :return:
    """
    pass


def notes_add(
    title: str, text: str, privacy_view: list, privacy_comment: list,
) -> NotesAddResponse:
    """
    :param title: - Note title.
    :param text: - Note text.
    :param privacy_view:
    :param privacy_comment:
    :return:
    """
    pass


def notes_create_comment(
    note_id: int, owner_id: int, reply_to: int, message: str, guid: str,
) -> NotesCreateCommentResponse:
    """
    :param note_id: - Note ID.
    :param owner_id: - Note owner ID.
    :param reply_to: - ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
    :param message: - Comment text.
    :param guid:
    :return:
    """
    pass


def notes_delete(note_id: int,) -> OkResponse:
    """
    :param note_id: - Note ID.
    :return:
    """
    pass


def notes_delete_comment(comment_id: int, owner_id: int,) -> OkResponse:
    """
    :param comment_id: - Comment ID.
    :param owner_id: - Note owner ID.
    :return:
    """
    pass


def notes_edit(
    note_id: int, title: str, text: str, privacy_view: list, privacy_comment: list,
) -> OkResponse:
    """
    :param note_id: - Note ID.
    :param title: - Note title.
    :param text: - Note text.
    :param privacy_view:
    :param privacy_comment:
    :return:
    """
    pass


def notes_edit_comment(comment_id: int, owner_id: int, message: str,) -> OkResponse:
    """
    :param comment_id: - Comment ID.
    :param owner_id: - Note owner ID.
    :param message: - New comment text.
    :return:
    """
    pass


def notes_get(
    note_ids: list, user_id: int, offset: int, count: int, sort: int,
) -> NotesGetResponse:
    """
    :param note_ids: - Note IDs.
    :param user_id: - Note owner ID.
    :param offset:
    :param count: - Number of notes to return.
    :param sort:
    :return:
    """
    pass


def notes_get_by_id(
    note_id: int, owner_id: int, need_wiki: bool,
) -> NotesGetByIdResponse:
    """
    :param note_id: - Note ID.
    :param owner_id: - Note owner ID.
    :param need_wiki:
    :return:
    """
    pass


def notes_get_comments(
    note_id: int, owner_id: int, sort: int, offset: int, count: int,
) -> NotesGetCommentsResponse:
    """
    :param note_id: - Note ID.
    :param owner_id: - Note owner ID.
    :param sort:
    :param offset:
    :param count: - Number of comments to return.
    :return:
    """
    pass


def notes_restore_comment(comment_id: int, owner_id: int,) -> OkResponse:
    """
    :param comment_id: - Comment ID.
    :param owner_id: - Note owner ID.
    :return:
    """
    pass


def notifications_get(
    count: int, start_from: str, filters: list, start_time: int, end_time: int,
) -> NotificationsGetResponse:
    """
    :param count: - Number of notifications to return.
    :param start_from:
    :param filters: - Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
    :param start_time: - Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
    :param end_time: - Latest timestamp (in Unix time) of a notification to return. By default, the current time.
    :return:
    """
    pass


def notifications_mark_as_viewed() -> NotificationsMarkAsViewedResponse:
    """
    :return:
    """
    pass


def notifications_send_message(
    user_ids: list, message: str, fragment: str, group_id: int,
) -> NotificationsSendMessageResponse:
    """
    :param user_ids:
    :param message:
    :param fragment:
    :param group_id:
    :return:
    """
    pass


def orders_cancel_subscription(
    user_id: int, subscription_id: int, pending_cancel: bool,
) -> OrdersCancelSubscriptionResponse:
    """
    :param user_id:
    :param subscription_id:
    :param pending_cancel:
    :return:
    """
    pass


def orders_change_state(
    order_id: int, action: str, app_order_id: int, test_mode: bool,
) -> OrdersChangeStateResponse:
    """
    :param order_id: - order ID.
    :param action: - action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
    :param app_order_id: - internal ID of the order in the application.
    :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
    :return:
    """
    pass


def orders_get(offset: int, count: int, test_mode: bool,) -> OrdersGetResponse:
    """
    :param offset:
    :param count: - number of returned orders.
    :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
    :return:
    """
    pass


def orders_get_amount(user_id: int, votes: list,) -> OrdersGetAmountResponse:
    """
    :param user_id:
    :param votes:
    :return:
    """
    pass


def orders_get_by_id(
    order_id: int, order_ids: list, test_mode: bool,
) -> OrdersGetByIdResponse:
    """
    :param order_id: - order ID.
    :param order_ids: - order IDs (when information about several orders is requested).
    :param test_mode: - if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
    :return:
    """
    pass


def orders_get_user_subscription_by_id(
    user_id: int, subscription_id: int,
) -> OrdersGetUserSubscriptionByIdResponse:
    """
    :param user_id:
    :param subscription_id:
    :return:
    """
    pass


def orders_get_user_subscriptions(user_id: int,) -> OrdersGetUserSubscriptionsResponse:
    """
    :param user_id:
    :return:
    """
    pass


def orders_update_subscription(
    user_id: int, subscription_id: int, price: int,
) -> OrdersUpdateSubscriptionResponse:
    """
    :param user_id:
    :param subscription_id:
    :param price:
    :return:
    """
    pass


def pages_clear_cache(url: str,) -> OkResponse:
    """
    :param url: - Address of the page where you need to refesh the cached version
    :return:
    """
    pass


def pages_get(
    owner_id: int,
    page_id: int,
    global_: bool,
    site_preview: bool,
    title: str,
    need_source: bool,
    need_html: bool,
) -> PagesGetResponse:
    """
    :param owner_id: - Page owner ID.
    :param page_id: - Wiki page ID.
    :param global_: - '1' — to return information about a global wiki page
    :param site_preview: - '1' — resulting wiki page is a preview for the attached link
    :param title: - Wiki page title.
    :param need_source:
    :param need_html: - '1' — to return the page as HTML,
    :return:
    """
    pass


def pages_get_history(
    page_id: int, group_id: int, user_id: int,
) -> PagesGetHistoryResponse:
    """
    :param page_id: - Wiki page ID.
    :param group_id: - ID of the community that owns the wiki page.
    :param user_id:
    :return:
    """
    pass


def pages_get_titles(group_id: int,) -> PagesGetTitlesResponse:
    """
    :param group_id: - ID of the community that owns the wiki page.
    :return:
    """
    pass


def pages_get_version(
    version_id: int, group_id: int, user_id: int, need_html: bool,
) -> PagesGetVersionResponse:
    """
    :param version_id:
    :param group_id: - ID of the community that owns the wiki page.
    :param user_id:
    :param need_html: - '1' — to return the page as HTML
    :return:
    """
    pass


def pages_parse_wiki(text: str, group_id: int,) -> PagesParseWikiResponse:
    """
    :param text: - Text of the wiki page.
    :param group_id: - ID of the group in the context of which this markup is interpreted.
    :return:
    """
    pass


def pages_save(
    text: str, page_id: int, group_id: int, user_id: int, title: str,
) -> PagesSaveResponse:
    """
    :param text: - Text of the wiki page in wiki-format.
    :param page_id: - Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
    :param group_id: - ID of the community that owns the wiki page.
    :param user_id: - User ID
    :param title: - Wiki page title.
    :return:
    """
    pass


def pages_save_access(
    page_id: int, group_id: int, user_id: int, view: int, edit: int,
) -> PagesSaveAccessResponse:
    """
    :param page_id: - Wiki page ID.
    :param group_id: - ID of the community that owns the wiki page.
    :param user_id:
    :param view: - Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
    :param edit: - Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
    :return:
    """
    pass


def photos_confirm_tag(owner_id: int, photo_id: str, tag_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param tag_id: - Tag ID.
    :return:
    """
    pass


def photos_copy(owner_id: int, photo_id: int, access_key: str,) -> PhotosCopyResponse:
    """
    :param owner_id: - photo's owner ID
    :param photo_id: - photo ID
    :param access_key: - for private photos
    :return:
    """
    pass


def photos_create_album(
    title: str,
    group_id: int,
    description: str,
    privacy_view: list,
    privacy_comment: list,
    upload_by_admins_only: bool,
    comments_disabled: bool,
) -> PhotosCreateAlbumResponse:
    """
    :param title: - Album title.
    :param group_id: - ID of the community in which the album will be created.
    :param description: - Album description.
    :param privacy_view:
    :param privacy_comment:
    :param upload_by_admins_only:
    :param comments_disabled:
    :return:
    """
    pass


def photos_create_comment(
    owner_id: int,
    photo_id: int,
    message: str,
    attachments: list,
    from_group: bool,
    reply_to_comment: int,
    sticker_id: int,
    access_key: str,
    guid: str,
) -> PhotosCreateCommentResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param message: - Comment text.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
    :param from_group: - '1' — to post a comment from the community
    :param reply_to_comment:
    :param sticker_id:
    :param access_key:
    :param guid:
    :return:
    """
    pass


def photos_delete(owner_id: int, photo_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :return:
    """
    pass


def photos_delete_album(album_id: int, group_id: int,) -> OkResponse:
    """
    :param album_id: - Album ID.
    :param group_id: - ID of the community that owns the album.
    :return:
    """
    pass


def photos_delete_comment(
    owner_id: int, comment_id: int,
) -> PhotosDeleteCommentResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param comment_id: - Comment ID.
    :return:
    """
    pass


def photos_edit(
    owner_id: int,
    photo_id: int,
    caption: str,
    latitude: int,
    longitude: int,
    place_str: str,
    foursquare_id: str,
    delete_place: bool,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param caption: - New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
    :param latitude:
    :param longitude:
    :param place_str:
    :param foursquare_id:
    :param delete_place:
    :return:
    """
    pass


def photos_edit_album(
    album_id: int,
    title: str,
    description: str,
    owner_id: int,
    privacy_view: list,
    privacy_comment: list,
    upload_by_admins_only: bool,
    comments_disabled: bool,
) -> OkResponse:
    """
    :param album_id: - ID of the photo album to be edited.
    :param title: - New album title.
    :param description: - New album description.
    :param owner_id: - ID of the user or community that owns the album.
    :param privacy_view:
    :param privacy_comment:
    :param upload_by_admins_only:
    :param comments_disabled:
    :return:
    """
    pass


def photos_edit_comment(
    owner_id: int, comment_id: int, message: str, attachments: list,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param comment_id: - Comment ID.
    :param message: - New text of the comment.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
    :return:
    """
    pass


def photos_get(
    owner_id: int,
    album_id: str,
    photo_ids: list,
    rev: bool,
    extended: bool,
    feed_type: str,
    feed: int,
    photo_sizes: bool,
    offset: int,
    count: int,
) -> PhotosGetResponse:
    """
    :param owner_id: - ID of the user or community that owns the photos. Use a negative value to designate a community ID.
    :param album_id: - Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
    :param photo_ids: - Photo IDs.
    :param rev: - Sort order: '1' — reverse chronological, '0' — chronological
    :param extended: - '1' — to return additional 'likes', 'comments', and 'tags' fields, '0' — (default)
    :param feed_type: - Type of feed obtained in 'feed' field of the method.
    :param feed: - unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
    :param photo_sizes: - '1' — to return photo sizes in a [vk.com/dev/photo_sizes|special format]
    :param offset:
    :param count:
    :return:
    """
    pass


def photos_get_albums(
    owner_id: int,
    album_ids: list,
    offset: int,
    count: int,
    need_system: bool,
    need_covers: bool,
    photo_sizes: bool,
) -> PhotosGetAlbumsResponse:
    """
    :param owner_id: - ID of the user or community that owns the albums.
    :param album_ids: - Album IDs.
    :param offset: - Offset needed to return a specific subset of albums.
    :param count: - Number of albums to return.
    :param need_system: - '1' — to return system albums with negative IDs
    :param need_covers: - '1' — to return an additional 'thumb_src' field, '0' — (default)
    :param photo_sizes: - '1' — to return photo sizes in a
    :return:
    """
    pass


def photos_get_albums_count(
    user_id: int, group_id: int,
) -> PhotosGetAlbumsCountResponse:
    """
    :param user_id: - User ID.
    :param group_id: - Community ID.
    :return:
    """
    pass


def photos_get_all(
    owner_id: int,
    extended: bool,
    offset: int,
    count: int,
    photo_sizes: bool,
    no_service_albums: bool,
    need_hidden: bool,
    skip_hidden: bool,
) -> PhotosGetAllResponse:
    """
    :param owner_id: - ID of a user or community that owns the photos. Use a negative value to designate a community ID.
    :param extended: - '1' — to return detailed information about photos
    :param offset: - Offset needed to return a specific subset of photos. By default, '0'.
    :param count: - Number of photos to return.
    :param photo_sizes: - '1' – to return image sizes in [vk.com/dev/photo_sizes|special format].
    :param no_service_albums: - '1' – to return photos only from standard albums, '0' – to return all photos including those in service albums, e.g., 'My wall photos' (default)
    :param need_hidden: - '1' – to show information about photos being hidden from the block above the wall.
    :param skip_hidden: - '1' – not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
    :return:
    """
    pass


def photos_get_all_comments(
    owner_id: int, album_id: int, need_likes: bool, offset: int, count: int,
) -> PhotosGetAllCommentsResponse:
    """
    :param owner_id: - ID of the user or community that owns the album(s).
    :param album_id: - Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
    :param need_likes: - '1' — to return an additional 'likes' field, '0' — (default)
    :param offset: - Offset needed to return a specific subset of comments. By default, '0'.
    :param count: - Number of comments to return. By default, '20'. Maximum value, '100'.
    :return:
    """
    pass


def photos_get_by_id(
    photos: list, extended: bool, photo_sizes: bool,
) -> PhotosGetByIdResponse:
    """
    :param photos: - IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
    :param extended: - '1' — to return additional fields, '0' — (default)
    :param photo_sizes: - '1' — to return photo sizes in a
    :return:
    """
    pass


def photos_get_chat_upload_server(
    chat_id: int, crop_x: int, crop_y: int, crop_width: int,
) -> BaseGetUploadServerResponse:
    """
    :param chat_id: - ID of the chat for which you want to upload a cover photo.
    :param crop_x:
    :param crop_y:
    :param crop_width: - Width (in pixels) of the photo after cropping.
    :return:
    """
    pass


def photos_get_comments(
    owner_id: int,
    photo_id: int,
    need_likes: bool,
    start_comment_id: int,
    offset: int,
    count: int,
    sort: str,
    access_key: str,
    extended: bool,
    fields: list,
) -> PhotosGetCommentsResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param need_likes: - '1' — to return an additional 'likes' field, '0' — (default)
    :param start_comment_id:
    :param offset: - Offset needed to return a specific subset of comments. By default, '0'.
    :param count: - Number of comments to return.
    :param sort: - Sort order: 'asc' — old first, 'desc' — new first
    :param access_key:
    :param extended:
    :param fields:
    :return:
    """
    pass


def photos_get_market_album_upload_server(
    group_id: int,
) -> BaseGetUploadServerResponse:
    """
    :param group_id: - Community ID.
    :return:
    """
    pass


def photos_get_market_upload_server(
    group_id: int, main_photo: bool, crop_x: int, crop_y: int, crop_width: int,
) -> PhotosGetMarketUploadServerResponse:
    """
    :param group_id: - Community ID.
    :param main_photo: - '1' if you want to upload the main item photo.
    :param crop_x: - X coordinate of the crop left upper corner.
    :param crop_y: - Y coordinate of the crop left upper corner.
    :param crop_width: - Width of the cropped photo in px.
    :return:
    """
    pass


def photos_get_messages_upload_server(
    peer_id: int,
) -> PhotosGetMessagesUploadServerResponse:
    """
    :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
    :return:
    """
    pass


def photos_get_new_tags(offset: int, count: int,) -> PhotosGetNewTagsResponse:
    """
    :param offset: - Offset needed to return a specific subset of photos.
    :param count: - Number of photos to return.
    :return:
    """
    pass


def photos_get_owner_cover_photo_upload_server(
    group_id: int, crop_x: int, crop_y: int, crop_x2: int, crop_y2: int,
) -> BaseGetUploadServerResponse:
    """
    :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
    :param crop_x: - X coordinate of the left-upper corner
    :param crop_y: - Y coordinate of the left-upper corner
    :param crop_x2: - X coordinate of the right-bottom corner
    :param crop_y2: - Y coordinate of the right-bottom corner
    :return:
    """
    pass


def photos_get_owner_photo_upload_server(owner_id: int,) -> BaseGetUploadServerResponse:
    """
    :param owner_id: - identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
    :return:
    """
    pass


def photos_get_tags(
    owner_id: int, photo_id: int, access_key: str,
) -> PhotosGetTagsResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param access_key:
    :return:
    """
    pass


def photos_get_upload_server(
    group_id: int, album_id: int,
) -> PhotosGetUploadServerResponse:
    """
    :param group_id: - ID of community that owns the album (if the photo will be uploaded to a community album).
    :param album_id:
    :return:
    """
    pass


def photos_get_user_photos(
    user_id: int, offset: int, count: int, extended: bool, sort: str,
) -> PhotosGetUserPhotosResponse:
    """
    :param user_id: - User ID.
    :param offset: - Offset needed to return a specific subset of photos. By default, '0'.
    :param count: - Number of photos to return. Maximum value is 1000.
    :param extended: - '1' — to return an additional 'likes' field, '0' — (default)
    :param sort: - Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
    :return:
    """
    pass


def photos_get_wall_upload_server(group_id: int,) -> PhotosGetWallUploadServerResponse:
    """
    :param group_id: - ID of community to whose wall the photo will be uploaded.
    :return:
    """
    pass


def photos_make_cover(owner_id: int, photo_id: int, album_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param album_id: - Album ID.
    :return:
    """
    pass


def photos_move(owner_id: int, target_album_id: int, photo_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param target_album_id: - ID of the album to which the photo will be moved.
    :param photo_id: - Photo ID.
    :return:
    """
    pass


def photos_put_tag(
    owner_id: int, photo_id: int, user_id: int, x: int, y: int, x2: int, y2: int,
) -> PhotosPutTagResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param user_id: - ID of the user to be tagged.
    :param x: - Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
    :param y: - Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
    :param x2: - Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
    :param y2: - Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
    :return:
    """
    pass


def photos_remove_tag(owner_id: int, photo_id: int, tag_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param tag_id: - Tag ID.
    :return:
    """
    pass


def photos_reorder_albums(
    owner_id: int, album_id: int, before: int, after: int,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the album.
    :param album_id: - Album ID.
    :param before: - ID of the album before which the album in question shall be placed.
    :param after: - ID of the album after which the album in question shall be placed.
    :return:
    """
    pass


def photos_reorder_photos(
    owner_id: int, photo_id: int, before: int, after: int,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param before: - ID of the photo before which the photo in question shall be placed.
    :param after: - ID of the photo after which the photo in question shall be placed.
    :return:
    """
    pass


def photos_report(owner_id: int, photo_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
    :return:
    """
    pass


def photos_report_comment(owner_id: int, comment_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param comment_id: - ID of the comment being reported.
    :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
    :return:
    """
    pass


def photos_restore(owner_id: int, photo_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param photo_id: - Photo ID.
    :return:
    """
    pass


def photos_restore_comment(
    owner_id: int, comment_id: int,
) -> PhotosRestoreCommentResponse:
    """
    :param owner_id: - ID of the user or community that owns the photo.
    :param comment_id: - ID of the deleted comment.
    :return:
    """
    pass


def photos_save(
    album_id: int,
    group_id: int,
    server: int,
    photos_list: str,
    hash: str,
    latitude: int,
    longitude: int,
    caption: str,
) -> PhotosSaveResponse:
    """
    :param album_id: - ID of the album to save photos to.
    :param group_id: - ID of the community to save photos to.
    :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param photos_list: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param latitude: - Geographical latitude, in degrees (from '-90' to '90').
    :param longitude: - Geographical longitude, in degrees (from '-180' to '180').
    :param caption: - Text describing the photo. 2048 digits max.
    :return:
    """
    pass


def photos_save_market_album_photo(
    group_id: int, photo: str, server: int, hash: str,
) -> PhotosSaveMarketAlbumPhotoResponse:
    """
    :param group_id: - Community ID.
    :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :return:
    """
    pass


def photos_save_market_photo(
    group_id: int, photo: str, server: int, hash: str, crop_data: str, crop_hash: str,
) -> PhotosSaveMarketPhotoResponse:
    """
    :param group_id: - Community ID.
    :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param server: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param crop_data: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param crop_hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :return:
    """
    pass


def photos_save_messages_photo(
    photo: str, server: int, hash: str,
) -> PhotosSaveMessagesPhotoResponse:
    """
    :param photo: - Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
    :param server:
    :param hash:
    :return:
    """
    pass


def photos_save_owner_cover_photo(
    hash: str, photo: str,
) -> PhotosSaveOwnerCoverPhotoResponse:
    """
    :param hash: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :param photo: - Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
    :return:
    """
    pass


def photos_save_owner_photo(
    server: str, hash: str, photo: str,
) -> PhotosSaveOwnerPhotoResponse:
    """
    :param server: - parameter returned after [vk.com/dev/upload_files|photo upload].
    :param hash: - parameter returned after [vk.com/dev/upload_files|photo upload].
    :param photo: - parameter returned after [vk.com/dev/upload_files|photo upload].
    :return:
    """
    pass


def photos_save_wall_photo(
    user_id: int,
    group_id: int,
    photo: str,
    server: int,
    hash: str,
    latitude: int,
    longitude: int,
    caption: str,
) -> PhotosSaveWallPhotoResponse:
    """
    :param user_id: - ID of the user on whose wall the photo will be saved.
    :param group_id: - ID of community on whose wall the photo will be saved.
    :param photo: - Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
    :param server:
    :param hash:
    :param latitude: - Geographical latitude, in degrees (from '-90' to '90').
    :param longitude: - Geographical longitude, in degrees (from '-180' to '180').
    :param caption: - Text describing the photo. 2048 digits max.
    :return:
    """
    pass


def photos_search(
    q: str,
    lat: int,
    long: int,
    start_time: int,
    end_time: int,
    sort: int,
    offset: int,
    count: int,
    radius: int,
) -> PhotosSearchResponse:
    """
    :param q: - Search query string.
    :param lat: - Geographical latitude, in degrees (from '-90' to '90').
    :param long: - Geographical longitude, in degrees (from '-180' to '180').
    :param start_time:
    :param end_time:
    :param sort: - Sort order:
    :param offset: - Offset needed to return a specific subset of photos.
    :param count: - Number of photos to return.
    :param radius: - Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
    :return:
    """
    pass


def polls_add_vote(
    owner_id: int, poll_id: int, answer_ids: list, is_board: bool,
) -> PollsAddVoteResponse:
    """
    :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
    :param poll_id: - Poll ID.
    :param answer_ids:
    :param is_board:
    :return:
    """
    pass


def polls_create(
    question: str,
    is_anonymous: bool,
    is_multiple: bool,
    end_date: int,
    owner_id: int,
    add_answers: str,
    photo_id: int,
    background_id: str,
) -> PollsCreateResponse:
    """
    :param question: - question text
    :param is_anonymous: - '1' – anonymous poll, participants list is hidden,, '0' – public poll, participants list is available,, Default value is '0'.
    :param is_multiple:
    :param end_date:
    :param owner_id: - If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
    :param add_answers: - available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
    :param photo_id:
    :param background_id:
    :return:
    """
    pass


def polls_delete_vote(
    owner_id: int, poll_id: int, answer_id: int, is_board: bool,
) -> PollsDeleteVoteResponse:
    """
    :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
    :param poll_id: - Poll ID.
    :param answer_id: - Answer ID.
    :param is_board:
    :return:
    """
    pass


def polls_edit(
    owner_id: int,
    poll_id: int,
    question: str,
    add_answers: str,
    edit_answers: str,
    delete_answers: str,
    end_date: int,
    photo_id: int,
    background_id: str,
) -> OkResponse:
    """
    :param owner_id: - poll owner id
    :param poll_id: - edited poll's id
    :param question: - new question text
    :param add_answers: - answers list, for example: , "["yes","no","maybe"]"
    :param edit_answers: - object containing answers that need to be edited,, key – answer id, value – new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
    :param delete_answers: - list of answer ids to be deleted. For example: "[382967099, 382967103]"
    :param end_date:
    :param photo_id:
    :param background_id:
    :return:
    """
    pass


def polls_get_by_id(
    owner_id: int,
    is_board: bool,
    poll_id: int,
    extended: bool,
    friends_count: int,
    fields: list,
    name_case: str,
) -> PollsGetByIdResponse:
    """
    :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
    :param is_board: - '1' – poll is in a board, '0' – poll is on a wall. '0' by default.
    :param poll_id: - Poll ID.
    :param extended:
    :param friends_count:
    :param fields:
    :param name_case:
    :return:
    """
    pass


def polls_get_voters(
    owner_id: int,
    poll_id: int,
    answer_ids: list,
    is_board: bool,
    friends_only: bool,
    offset: int,
    count: int,
    fields: list,
    name_case: str,
) -> PollsGetVotersResponse:
    """
    :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
    :param poll_id: - Poll ID.
    :param answer_ids: - Answer IDs.
    :param is_board:
    :param friends_only: - '1' — to return only current user's friends, '0' — to return all users (default),
    :param offset: - Offset needed to return a specific subset of voters. '0' — (default)
    :param count: - Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' — (default)
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
    :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :return:
    """
    pass


def pretty_cards_create(
    owner_id: int,
    photo: str,
    title: str,
    link: str,
    price: str,
    price_old: str,
    button: str,
) -> PrettyCardsCreateResponse:
    """
    :param owner_id:
    :param photo:
    :param title:
    :param link:
    :param price:
    :param price_old:
    :param button:
    :return:
    """
    pass


def pretty_cards_delete(owner_id: int, card_id: int,) -> PrettyCardsDeleteResponse:
    """
    :param owner_id:
    :param card_id:
    :return:
    """
    pass


def pretty_cards_edit(
    owner_id: int,
    card_id: int,
    photo: str,
    title: str,
    link: str,
    price: str,
    price_old: str,
    button: str,
) -> PrettyCardsEditResponse:
    """
    :param owner_id:
    :param card_id:
    :param photo:
    :param title:
    :param link:
    :param price:
    :param price_old:
    :param button:
    :return:
    """
    pass


def pretty_cards_get(owner_id: int, offset: int, count: int,) -> PrettyCardsGetResponse:
    """
    :param owner_id:
    :param offset:
    :param count:
    :return:
    """
    pass


def pretty_cards_get_by_id(
    owner_id: int, card_ids: list,
) -> PrettyCardsGetByIdResponse:
    """
    :param owner_id:
    :param card_ids:
    :return:
    """
    pass


def pretty_cards_get_upload_u_r_l() -> PrettyCardsGetUploadURLResponse:
    """
    :return:
    """
    pass


def search_get_hints(
    q: str, offset: int, limit: int, filters: list, fields: list, search_global: bool,
) -> SearchGetHintsResponse:
    """
    :param q: - Search query string.
    :param offset: - Offset for querying specific result subset
    :param limit: - Maximum number of results to return.
    :param filters:
    :param fields:
    :param search_global:
    :return:
    """
    pass


def secure_add_app_event(user_id: int, activity_id: int, value: int,) -> OkResponse:
    """
    :param user_id: - ID of a user to save the data
    :param activity_id: - there are 2 default activities: , * 1 – level. Works similar to ,, * 2 – points, saves points amount, Any other value is for saving completed missions
    :param value: - depends on activity_id: * 1 – number, current level number,, * 2 – number, current user's points amount, , Any other value is ignored
    :return:
    """
    pass


def secure_check_token(token: str, ip: str,) -> SecureCheckTokenResponse:
    """
    :param token: - client 'access_token'
    :param ip: - user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
    :return:
    """
    pass


def secure_get_app_balance() -> SecureGetAppBalanceResponse:
    """
    :return:
    """
    pass


def secure_get_s_m_s_history(
    user_id: int, date_from: int, date_to: int, limit: int,
) -> SecureGetSMSHistoryResponse:
    """
    :param user_id:
    :param date_from: - filter by start date. It is set as UNIX-time.
    :param date_to: - filter by end date. It is set as UNIX-time.
    :param limit: - number of returned posts. By default — 1000.
    :return:
    """
    pass


def secure_get_transactions_history(
    type: int, uid_from: int, uid_to: int, date_from: int, date_to: int, limit: int,
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
    pass


def secure_get_user_level(user_ids: list,) -> SecureGetUserLevelResponse:
    """
    :param user_ids:
    :return:
    """
    pass


def secure_give_event_sticker(
    user_ids: list, achievement_id: int,
) -> SecureGiveEventStickerResponse:
    """
    :param user_ids:
    :param achievement_id:
    :return:
    """
    pass


def secure_send_notification(
    user_ids: list, user_id: int, message: str,
) -> SecureSendNotificationResponse:
    """
    :param user_ids:
    :param user_id:
    :param message: - notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
    :return:
    """
    pass


def secure_send_s_m_s_notification(user_id: int, message: str,) -> OkResponse:
    """
    :param user_id: - ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
    :param message: - 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
    :return:
    """
    pass


def secure_set_counter(
    counters: list, user_id: int, counter: int, increment: bool,
) -> OkResponse:
    """
    :param counters:
    :param user_id:
    :param counter: - counter value.
    :param increment:
    :return:
    """
    pass


def stats_get(
    group_id: int,
    app_id: int,
    timestamp_from: int,
    timestamp_to: int,
    interval: str,
    intervals_count: int,
    filters: list,
    stats_groups: list,
    extended: bool,
) -> StatsGetResponse:
    """
    :param group_id: - Community ID.
    :param app_id: - Application ID.
    :param timestamp_from:
    :param timestamp_to:
    :param interval:
    :param intervals_count:
    :param filters:
    :param stats_groups:
    :param extended:
    :return:
    """
    pass


def stats_get_post_reach(owner_id: str, post_id: int,) -> StatsGetPostReachResponse:
    """
    :param owner_id: - post owner community id. Specify with "-" sign.
    :param post_id: - wall post id. Note that stats are available only for '300' last (newest) posts on a community wall.
    :return:
    """
    pass


def stats_track_visitor(id: str,) -> OkResponse:
    """
    :param id:
    :return:
    """
    pass


def status_get(user_id: int, group_id: int,) -> StatusGetResponse:
    """
    :param user_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param group_id:
    :return:
    """
    pass


def status_set(text: str, group_id: int,) -> OkResponse:
    """
    :param text: - Text of the new status.
    :param group_id: - Identifier of a community to set a status in. If left blank the status is set to current user.
    :return:
    """
    pass


def storage_get(key: str, keys: list, user_id: int, global_: bool,) -> dict:
    """
    :param key:
    :param keys:
    :param user_id:
    :param global_:
    :return:
    """
    pass


def storage_get_keys(
    user_id: int, global_: bool, offset: int, count: int,
) -> StorageGetKeysResponse:
    """
    :param user_id: - user id, whose variables names are returned if they were requested with a server method.
    :param global_:
    :param offset:
    :param count: - amount of variable names the info needs to be collected from.
    :return:
    """
    pass


def storage_set(key: str, value: str, user_id: int, global_: bool,) -> OkResponse:
    """
    :param key:
    :param value:
    :param user_id:
    :param global_:
    :return:
    """
    pass


def stories_ban_owner(owners_ids: list,) -> OkResponse:
    """
    :param owners_ids: - List of sources IDs
    :return:
    """
    pass


def stories_delete(owner_id: int, story_id: int,) -> OkResponse:
    """
    :param owner_id: - Story owner's ID. Current user id is used by default.
    :param story_id: - Story ID.
    :return:
    """
    pass


def stories_get(owner_id: int, extended: bool,) -> StoriesGetResponse:
    """
    :param owner_id: - Owner ID.
    :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
    :return:
    """
    pass


def stories_get_banned(extended: bool, fields: list,) -> StoriesGetBannedResponse:
    """
    :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
    :param fields: - Additional fields to return
    :return:
    """
    pass


def stories_get_by_id(
    stories: list, extended: bool, fields: list,
) -> StoriesGetByIdResponse:
    """
    :param stories: - Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
    :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
    :param fields: - Additional fields to return
    :return:
    """
    pass


def stories_get_photo_upload_server(
    add_to_news: bool,
    user_ids: list,
    reply_to_story: str,
    link_text: str,
    link_url: str,
    group_id: int,
) -> StoriesGetPhotoUploadServerResponse:
    """
    :param add_to_news: - 1 — to add the story to friend's feed.
    :param user_ids: - List of users IDs who can see the story.
    :param reply_to_story: - ID of the story to reply with the current.
    :param link_text: - Link text (for community's stories only).
    :param link_url: - Link URL. Internal links on https://vk.com only.
    :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
    :return:
    """
    pass


def stories_get_replies(
    owner_id: int, story_id: int, access_key: str, extended: bool, fields: list,
) -> StoriesGetRepliesResponse:
    """
    :param owner_id: - Story owner ID.
    :param story_id: - Story ID.
    :param access_key: - Access key for the private object.
    :param extended: - '1' — to return additional fields for users and communities. Default value is 0.
    :param fields: - Additional fields to return
    :return:
    """
    pass


def stories_get_stats(owner_id: int, story_id: int,) -> StoriesGetStatsResponse:
    """
    :param owner_id: - Story owner ID. 
    :param story_id: - Story ID.
    :return:
    """
    pass


def stories_get_video_upload_server(
    add_to_news: bool,
    user_ids: list,
    reply_to_story: str,
    link_text: str,
    link_url: str,
    group_id: int,
) -> StoriesGetVideoUploadServerResponse:
    """
    :param add_to_news: - 1 — to add the story to friend's feed.
    :param user_ids: - List of users IDs who can see the story.
    :param reply_to_story: - ID of the story to reply with the current.
    :param link_text: - Link text (for community's stories only).
    :param link_url: - Link URL. Internal links on https://vk.com only.
    :param group_id: - ID of the community to upload the story (should be verified or with the "fire" icon).
    :return:
    """
    pass


def stories_get_viewers(
    owner_id: int, story_id: int, count: int, offset: int, extended: bool,
) -> StoriesGetViewersResponse:
    """
    :param owner_id: - Story owner ID.
    :param story_id: - Story ID.
    :param count: - Maximum number of results.
    :param offset: - Offset needed to return a specific subset of results.
    :param extended: - '1' — to return detailed information about photos
    :return:
    """
    pass


def stories_hide_all_replies(owner_id: int, group_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user whose replies should be hidden.
    :param group_id:
    :return:
    """
    pass


def stories_hide_reply(owner_id: int, story_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user whose replies should be hidden.
    :param story_id: - Story ID.
    :return:
    """
    pass


def stories_unban_owner(owners_ids: list,) -> OkResponse:
    """
    :param owners_ids: - List of hidden sources to show stories from.
    :return:
    """
    pass


def streaming_get_server_url() -> StreamingGetServerUrlResponse:
    """
    :return:
    """
    pass


def streaming_set_settings(monthly_tier: str,) -> OkResponse:
    """
    :param monthly_tier:
    :return:
    """
    pass


def users_get(user_ids: list, fields: list, name_case: str,) -> UsersGetResponse:
    """
    :param user_ids: - User IDs or screen names ('screen_name'). By default, current user ID.
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities',
    :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :return:
    """
    pass


def users_get_followers(
    user_id: int, offset: int, count: int, fields: list, name_case: str,
) -> UsersGetFollowersResponse:
    """
    :param user_id: - User ID.
    :param offset: - Offset needed to return a specific subset of followers.
    :param count: - Number of followers to return.
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
    :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
    :return:
    """
    pass


def users_get_subscriptions(
    user_id: int, extended: bool, offset: int, count: int, fields: list,
) -> UsersGetSubscriptionsResponse:
    """
    :param user_id: - User ID.
    :param extended: - '1' — to return a combined list of users and communities, '0' — to return separate lists of users and communities (default)
    :param offset: - Offset needed to return a specific subset of subscriptions.
    :param count: - Number of users and communities to return.
    :param fields:
    :return:
    """
    pass


def users_is_app_user(user_id: int,) -> UsersIsAppUserResponse:
    """
    :param user_id:
    :return:
    """
    pass


def users_report(user_id: int, type: str, comment: str,) -> OkResponse:
    """
    :param user_id: - ID of the user about whom a complaint is being made.
    :param type: - Type of complaint: 'porn' – pornography, 'spam' – spamming, 'insult' – abusive behavior, 'advertisement' – disruptive advertisements
    :param comment: - Comment describing the complaint.
    :return:
    """
    pass


def users_search(
    q: str,
    sort: int,
    offset: int,
    count: int,
    fields: list,
    city: int,
    country: int,
    hometown: str,
    university_country: int,
    university: int,
    university_year: int,
    university_faculty: int,
    university_chair: int,
    sex: int,
    status: int,
    age_from: int,
    age_to: int,
    birth_day: int,
    birth_month: int,
    birth_year: int,
    online: bool,
    has_photo: bool,
    school_country: int,
    school_city: int,
    school_class: int,
    school: int,
    school_year: int,
    religion: str,
    interests: str,
    company: str,
    position: str,
    group_id: int,
    from_list: list,
) -> UsersSearchResponse:
    """
    :param q: - Search query string (e.g., 'Vasya Babich').
    :param sort: - Sort order: '1' — by date registered, '0' — by rating
    :param offset: - Offset needed to return a specific subset of users.
    :param count: - Number of users to return.
    :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
    :param city: - City ID.
    :param country: - Country ID.
    :param hometown: - City name in a string.
    :param university_country: - ID of the country where the user graduated.
    :param university: - ID of the institution of higher education.
    :param university_year: - Year of graduation from an institution of higher education.
    :param university_faculty: - Faculty ID.
    :param university_chair: - Chair ID.
    :param sex: - '1' — female, '2' — male, '0' — any (default)
    :param status: - Relationship status: '1' — Not married, '2' — In a relationship, '3' — Engaged, '4' — Married, '5' — It's complicated, '6' — Actively searching, '7' — In love
    :param age_from: - Minimum age.
    :param age_to: - Maximum age.
    :param birth_day: - Day of birth.
    :param birth_month: - Month of birth.
    :param birth_year: - Year of birth.
    :param online: - '1' — online only, '0' — all users
    :param has_photo: - '1' — with photo only, '0' — all users
    :param school_country: - ID of the country where users finished school.
    :param school_city: - ID of the city where users finished school.
    :param school_class:
    :param school: - ID of the school.
    :param school_year: - School graduation year.
    :param religion: - Users' religious affiliation.
    :param interests: - Users' interests.
    :param company: - Name of the company where users work.
    :param position: - Job position.
    :param group_id: - ID of a community to search in communities.
    :param from_list:
    :return:
    """
    pass


def utils_check_link(url: str,) -> UtilsCheckLinkResponse:
    """
    :param url: - Link to check (e.g., 'http://google.com').
    :return:
    """
    pass


def utils_delete_from_last_shortened(key: str,) -> OkResponse:
    """
    :param key: - Link key (characters after vk.cc/).
    :return:
    """
    pass


def utils_get_last_shortened_links(
    count: int, offset: int,
) -> UtilsGetLastShortenedLinksResponse:
    """
    :param count: - Number of links to return.
    :param offset: - Offset needed to return a specific subset of links.
    :return:
    """
    pass


def utils_get_link_stats(
    key: str,
    source: str,
    access_key: str,
    interval: str,
    intervals_count: int,
    extended: bool,
) -> UtilsGetLinkStatsResponse:
    """
    :param key: - Link key (characters after vk.cc/).
    :param source: - Source of scope
    :param access_key: - Access key for private link stats.
    :param interval: - Interval.
    :param intervals_count: - Number of intervals to return.
    :param extended: - 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
    :return:
    """
    pass


def utils_get_server_time() -> UtilsGetServerTimeResponse:
    """
    :return:
    """
    pass


def utils_get_short_link(url: str, private: bool,) -> UtilsGetShortLinkResponse:
    """
    :param url: - URL to be shortened.
    :param private: - 1 — private stats, 0 — public stats.
    :return:
    """
    pass


def utils_resolve_screen_name(screen_name: str,) -> UtilsResolveScreenNameResponse:
    """
    :param screen_name: - Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
    :return:
    """
    pass


def video_add(target_id: int, video_id: int, owner_id: int,) -> OkResponse:
    """
    :param target_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
    :param video_id: - Video ID.
    :param owner_id: - ID of the user or community that owns the video. Use a negative value to designate a community ID.
    :return:
    """
    pass


def video_add_album(group_id: int, title: str, privacy: list,) -> VideoAddAlbumResponse:
    """
    :param group_id: - Community ID (if the album will be created in a community).
    :param title: - Album title.
    :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
    :return:
    """
    pass


def video_add_to_album(
    target_id: int, album_id: int, album_ids: list, owner_id: int, video_id: int,
) -> OkResponse:
    """
    :param target_id:
    :param album_id:
    :param album_ids:
    :param owner_id:
    :param video_id:
    :return:
    """
    pass


def video_create_comment(
    owner_id: int,
    video_id: int,
    message: str,
    attachments: list,
    from_group: bool,
    reply_to_comment: int,
    sticker_id: int,
    guid: str,
) -> VideoCreateCommentResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param video_id: - Video ID.
    :param message: - New comment text.
    :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
    :param from_group: - '1' — to post the comment from a community name (only if 'owner_id'<0)
    :param reply_to_comment:
    :param sticker_id:
    :param guid:
    :return:
    """
    pass


def video_delete(video_id: int, owner_id: int, target_id: int,) -> OkResponse:
    """
    :param video_id: - Video ID.
    :param owner_id: - ID of the user or community that owns the video.
    :param target_id:
    :return:
    """
    pass


def video_delete_album(group_id: int, album_id: int,) -> OkResponse:
    """
    :param group_id: - Community ID (if the album is owned by a community).
    :param album_id: - Album ID.
    :return:
    """
    pass


def video_delete_comment(owner_id: int, comment_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param comment_id: - ID of the comment to be deleted.
    :return:
    """
    pass


def video_edit(
    owner_id: int,
    video_id: int,
    name: str,
    desc: str,
    privacy_view: list,
    privacy_comment: list,
    no_comments: bool,
    repeat: bool,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param video_id: - Video ID.
    :param name: - New video title.
    :param desc: - New video description.
    :param privacy_view: - Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
    :param privacy_comment: - Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
    :param no_comments: - Disable comments for the group video.
    :param repeat: - '1' — to repeat the playback of the video, '0' — to play the video once,
    :return:
    """
    pass


def video_edit_album(
    group_id: int, album_id: int, title: str, privacy: list,
) -> OkResponse:
    """
    :param group_id: - Community ID (if the album edited is owned by a community).
    :param album_id: - Album ID.
    :param title: - New album title.
    :param privacy: - new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
    :return:
    """
    pass


def video_edit_comment(
    owner_id: int, comment_id: int, message: str, attachments: list,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param comment_id: - Comment ID.
    :param message: - New comment text.
    :param attachments: - List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
    :return:
    """
    pass


def video_get(
    owner_id: int, videos: list, album_id: int, count: int, offset: int, extended: bool,
) -> VideoGetResponse:
    """
    :param owner_id: - ID of the user or community that owns the video(s).
    :param videos: - Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
    :param album_id: - ID of the album containing the video(s).
    :param count: - Number of videos to return.
    :param offset: - Offset needed to return a specific subset of videos.
    :param extended: - '1' — to return an extended response with additional fields
    :return:
    """
    pass


def video_get_album_by_id(owner_id: int, album_id: int,) -> VideoGetAlbumByIdResponse:
    """
    :param owner_id: - identifier of a user or community to add a video to. Use a negative value to designate a community ID.
    :param album_id: - Album ID.
    :return:
    """
    pass


def video_get_albums(
    owner_id: int, offset: int, count: int, extended: bool, need_system: bool,
) -> VideoGetAlbumsResponse:
    """
    :param owner_id: - ID of the user or community that owns the video album(s).
    :param offset: - Offset needed to return a specific subset of video albums.
    :param count: - Number of video albums to return.
    :param extended: - '1' — to return additional information about album privacy settings for the current user
    :param need_system:
    :return:
    """
    pass


def video_get_albums_by_video(
    target_id: int, owner_id: int, video_id: int, extended: bool,
) -> VideoGetAlbumsByVideoResponse:
    """
    :param target_id:
    :param owner_id:
    :param video_id:
    :param extended:
    :return:
    """
    pass


def video_get_comments(
    owner_id: int,
    video_id: int,
    need_likes: bool,
    start_comment_id: int,
    offset: int,
    count: int,
    sort: str,
    extended: bool,
    fields: list,
) -> VideoGetCommentsResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param video_id: - Video ID.
    :param need_likes: - '1' — to return an additional 'likes' field
    :param start_comment_id:
    :param offset: - Offset needed to return a specific subset of comments.
    :param count: - Number of comments to return.
    :param sort: - Sort order: 'asc' — oldest comment first, 'desc' — newest comment first
    :param extended:
    :param fields:
    :return:
    """
    pass


def video_remove_from_album(
    target_id: int, album_id: int, album_ids: list, owner_id: int, video_id: int,
) -> OkResponse:
    """
    :param target_id:
    :param album_id:
    :param album_ids:
    :param owner_id:
    :param video_id:
    :return:
    """
    pass


def video_reorder_albums(
    owner_id: int, album_id: int, before: int, after: int,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the albums..
    :param album_id: - Album ID.
    :param before: - ID of the album before which the album in question shall be placed.
    :param after: - ID of the album after which the album in question shall be placed.
    :return:
    """
    pass


def video_reorder_videos(
    target_id: int,
    album_id: int,
    owner_id: int,
    video_id: int,
    before_owner_id: int,
    before_video_id: int,
    after_owner_id: int,
    after_video_id: int,
) -> OkResponse:
    """
    :param target_id: - ID of the user or community that owns the album with videos.
    :param album_id: - ID of the video album.
    :param owner_id: - ID of the user or community that owns the video.
    :param video_id: - ID of the video.
    :param before_owner_id: - ID of the user or community that owns the video before which the video in question shall be placed.
    :param before_video_id: - ID of the video before which the video in question shall be placed.
    :param after_owner_id: - ID of the user or community that owns the video after which the photo in question shall be placed.
    :param after_video_id: - ID of the video after which the photo in question shall be placed.
    :return:
    """
    pass


def video_report(
    owner_id: int, video_id: int, reason: int, comment: str, search_query: str,
) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param video_id: - Video ID.
    :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
    :param comment: - Comment describing the complaint.
    :param search_query: - (If the video was found in search results.) Search query string.
    :return:
    """
    pass


def video_report_comment(owner_id: int, comment_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param comment_id: - ID of the comment being reported.
    :param reason: - Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
    :return:
    """
    pass


def video_restore(video_id: int, owner_id: int,) -> OkResponse:
    """
    :param video_id: - Video ID.
    :param owner_id: - ID of the user or community that owns the video.
    :return:
    """
    pass


def video_restore_comment(
    owner_id: int, comment_id: int,
) -> VideoRestoreCommentResponse:
    """
    :param owner_id: - ID of the user or community that owns the video.
    :param comment_id: - ID of the deleted comment.
    :return:
    """
    pass


def video_save(
    name: str,
    description: str,
    is_private: bool,
    wallpost: bool,
    link: str,
    group_id: int,
    album_id: int,
    privacy_view: list,
    privacy_comment: list,
    no_comments: bool,
    repeat: bool,
    compression: bool,
) -> VideoSaveResponse:
    """
    :param name: - Name of the video.
    :param description: - Description of the video.
    :param is_private: - '1' — to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' — not to designate the video as private
    :param wallpost: - '1' — to post the saved video on a user's wall, '0' — not to post the saved video on a user's wall
    :param link: - URL for embedding the video from an external website.
    :param group_id: - ID of the community in which the video will be saved. By default, the current user's page.
    :param album_id: - ID of the album to which the saved video will be added.
    :param privacy_view:
    :param privacy_comment:
    :param no_comments:
    :param repeat: - '1' — to repeat the playback of the video, '0' — to play the video once,
    :param compression:
    :return:
    """
    pass


def video_search(
    q: str,
    sort: int,
    hd: int,
    adult: bool,
    filters: list,
    search_own: bool,
    offset: int,
    longer: int,
    shorter: int,
    count: int,
    extended: bool,
) -> VideoSearchResponse:
    """
    :param q: - Search query string (e.g., 'The Beatles').
    :param sort: - Sort order: '1' — by duration, '2' — by relevance, '0' — by date added
    :param hd: - If not null, only searches for high-definition videos.
    :param adult: - '1' — to disable the Safe Search filter, '0' — to enable the Safe Search filter
    :param filters: - Filters to apply: 'youtube' — return YouTube videos only, 'vimeo' — return Vimeo videos only, 'short' — return short videos only, 'long' — return long videos only
    :param search_own:
    :param offset: - Offset needed to return a specific subset of videos.
    :param longer:
    :param shorter:
    :param count: - Number of videos to return.
    :param extended:
    :return:
    """
    pass


def wall_close_comments(owner_id: int, post_id: int,) -> BaseBoolResponse:
    """
    :param owner_id:
    :param post_id:
    :return:
    """
    pass


def wall_create_comment(
    owner_id: int,
    post_id: int,
    from_group: int,
    message: str,
    reply_to_comment: int,
    attachments: list,
    sticker_id: int,
    guid: str,
) -> WallCreateCommentResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID.
    :param from_group: - Group ID.
    :param message: - (Required if 'attachments' is not set.) Text of the comment.
    :param reply_to_comment: - ID of comment to reply.
    :param attachments: - (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
    :param sticker_id: - Sticker ID.
    :param guid: - Unique identifier to avoid repeated comments.
    :return:
    """
    pass


def wall_delete(owner_id: int, post_id: int,) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param post_id: - ID of the post to be deleted.
    :return:
    """
    pass


def wall_delete_comment(owner_id: int, comment_id: int,) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param comment_id: - Comment ID.
    :return:
    """
    pass


def wall_edit(
    owner_id: int,
    post_id: int,
    friends_only: bool,
    message: str,
    attachments: list,
    services: str,
    signed: bool,
    publish_date: int,
    lat: int,
    long: int,
    place_id: int,
    mark_as_ads: bool,
    close_comments: bool,
    poster_bkg_id: int,
    poster_bkg_owner_id: int,
    poster_bkg_access_hash: str,
) -> WallEditResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param post_id:
    :param friends_only:
    :param message: - (Required if 'attachments' is not set.) Text of the post.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
    :param services:
    :param signed:
    :param publish_date:
    :param lat:
    :param long:
    :param place_id:
    :param mark_as_ads:
    :param close_comments:
    :param poster_bkg_id:
    :param poster_bkg_owner_id:
    :param poster_bkg_access_hash:
    :return:
    """
    pass


def wall_edit_ads_stealth(
    owner_id: int,
    post_id: int,
    message: str,
    attachments: list,
    signed: bool,
    lat: int,
    long: int,
    place_id: int,
    link_button: str,
    link_title: str,
    link_image: str,
    link_video: str,
) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID. Used for publishing of scheduled and suggested posts.
    :param message: - (Required if 'attachments' is not set.) Text of the post.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
    :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
    :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
    :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
    :param place_id: - ID of the location where the user was tagged.
    :param link_button: - Link button ID
    :param link_title: - Link title
    :param link_image: - Link image url
    :param link_video: - Link video ID in format "<owner_id>_<media_id>"
    :return:
    """
    pass


def wall_edit_comment(
    owner_id: int, comment_id: int, message: str, attachments: list,
) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param comment_id: - Comment ID.
    :param message: - New comment text.
    :param attachments: - List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
    :return:
    """
    pass


def wall_get(
    owner_id: int,
    domain: str,
    offset: int,
    count: int,
    filter: str,
    extended: bool,
    fields: list,
) -> WallGetResponse:
    """
    :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
    :param domain: - User or community short address.
    :param offset: - Offset needed to return a specific subset of posts.
    :param count: - Number of posts to return (maximum 100).
    :param filter: - Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall
    :param extended: - '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
    :param fields:
    :return:
    """
    pass


def wall_get_by_id(
    posts: list, extended: bool, copy_history_depth: int, fields: list,
) -> WallGetByIdResponse:
    """
    :param posts: - User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
    :param extended: - '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
    :param copy_history_depth: - Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
    :param fields:
    :return:
    """
    pass


def wall_get_comments(
    owner_id: int,
    post_id: int,
    need_likes: bool,
    start_comment_id: int,
    offset: int,
    count: int,
    sort: str,
    preview_length: int,
    extended: bool,
    fields: list,
    comment_id: int,
    thread_items_count: int,
) -> WallGetCommentsResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID.
    :param need_likes: - '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
    :param start_comment_id:
    :param offset: - Offset needed to return a specific subset of comments.
    :param count: - Number of comments to return (maximum 100).
    :param sort: - Sort order: 'asc' — chronological, 'desc' — reverse chronological
    :param preview_length: - Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
    :param extended:
    :param fields:
    :param comment_id: - Comment ID.
    :param thread_items_count: - Count items in threads.
    :return:
    """
    pass


def wall_get_reposts(
    owner_id: int, post_id: int, offset: int, count: int,
) -> WallGetRepostsResponse:
    """
    :param owner_id: - User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID.
    :param offset: - Offset needed to return a specific subset of reposts.
    :param count: - Number of reposts to return.
    :return:
    """
    pass


def wall_open_comments(owner_id: int, post_id: int,) -> BaseBoolResponse:
    """
    :param owner_id:
    :param post_id:
    :return:
    """
    pass


def wall_pin(owner_id: int, post_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID.
    :return:
    """
    pass


def wall_post(
    owner_id: int,
    friends_only: bool,
    from_group: bool,
    message: str,
    attachments: list,
    services: str,
    signed: bool,
    publish_date: int,
    lat: int,
    long: int,
    place_id: int,
    post_id: int,
    guid: str,
    mark_as_ads: bool,
    close_comments: bool,
    mute_notifications: bool,
) -> WallPostResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param friends_only: - '1' — post will be available to friends only, '0' — post will be available to all users (default)
    :param from_group: - For a community: '1' — post will be published by the community, '0' — post will be published by the user (default)
    :param message: - (Required if 'attachments' is not set.) Text of the post.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
    :param services: - List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
    :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
    :param publish_date: - Publication date (in Unix time). If used, posting will be delayed until the set time.
    :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
    :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
    :param place_id: - ID of the location where the user was tagged.
    :param post_id: - Post ID. Used for publishing of scheduled and suggested posts.
    :param guid:
    :param mark_as_ads:
    :param close_comments:
    :param mute_notifications:
    :return:
    """
    pass


def wall_post_ads_stealth(
    owner_id: int,
    message: str,
    attachments: list,
    signed: bool,
    lat: int,
    long: int,
    place_id: int,
    guid: str,
    link_button: str,
    link_title: str,
    link_image: str,
    link_video: str,
) -> WallPostAdsStealthResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param message: - (Required if 'attachments' is not set.) Text of the post.
    :param attachments: - (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
    :param signed: - Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
    :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
    :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
    :param place_id: - ID of the location where the user was tagged.
    :param guid: - Unique identifier to avoid duplication the same post.
    :param link_button: - Link button ID
    :param link_title: - Link title
    :param link_image: - Link image url
    :param link_video: - Link video ID in format "<owner_id>_<media_id>"
    :return:
    """
    pass


def wall_report_comment(owner_id: int, comment_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the wall.
    :param comment_id: - Comment ID.
    :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
    :return:
    """
    pass


def wall_report_post(owner_id: int, post_id: int, reason: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the wall.
    :param post_id: - Post ID.
    :param reason: - Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
    :return:
    """
    pass


def wall_repost(
    object: str,
    message: str,
    group_id: int,
    mark_as_ads: bool,
    mute_notifications: bool,
) -> WallRepostResponse:
    """
    :param object: - ID of the object to be reposted on the wall. Example: "wall66748_3675"
    :param message: - Comment to be added along with the reposted object.
    :param group_id: - Target community ID when reposting to a community.
    :param mark_as_ads:
    :param mute_notifications:
    :return:
    """
    pass


def wall_restore(owner_id: int, post_id: int,) -> OkResponse:
    """
    :param owner_id: - User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
    :param post_id: - ID of the post to be restored.
    :return:
    """
    pass


def wall_restore_comment(owner_id: int, comment_id: int,) -> OkResponse:
    """
    :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
    :param comment_id: - Comment ID.
    :return:
    """
    pass


def wall_search(
    owner_id: int,
    domain: str,
    query: str,
    owners_only: bool,
    count: int,
    offset: int,
    extended: bool,
    fields: list,
) -> WallSearchResponse:
    """
    :param owner_id: - user or community id. "Remember that for a community 'owner_id' must be negative."
    :param domain: - user or community screen name.
    :param query: - search query string.
    :param owners_only: - '1' – returns only page owner's posts.
    :param count: - count of posts to return.
    :param offset: - Offset needed to return a specific subset of posts.
    :param extended: - show extended post info.
    :param fields:
    :return:
    """
    pass


def wall_unpin(owner_id: int, post_id: int,) -> OkResponse:
    """
    :param owner_id: - ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
    :param post_id: - Post ID.
    :return:
    """
    pass


def widgets_get_comments(
    widget_api_id: int,
    url: str,
    page_id: str,
    order: str,
    fields: list,
    offset: int,
    count: int,
) -> WidgetsGetCommentsResponse:
    """
    :param widget_api_id:
    :param url:
    :param page_id:
    :param order:
    :param fields:
    :param offset:
    :param count:
    :return:
    """
    pass


def widgets_get_pages(
    widget_api_id: int, order: str, period: str, offset: int, count: int,
) -> WidgetsGetPagesResponse:
    """
    :param widget_api_id:
    :param order:
    :param period:
    :param offset:
    :param count:
    :return:
    """
    pass
