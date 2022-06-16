import enum
import inspect
import typing

from pydantic import BaseModel, Field


class AccountAccountCounters(BaseModel):
    app_requests: typing.Optional[int] = Field(
        None,
        description='New app requests number'
    )
    events: typing.Optional[int] = Field(
        None,
        description='New events number'
    )
    faves: typing.Optional[int] = Field(
        None,
        description='New faves number'
    )
    friends: typing.Optional[int] = Field(
        None,
        description='New friends requests number'
    )
    friends_recommendations: typing.Optional[int] = Field(
        None,
        description='New friends recommendations number'
    )
    friends_suggestions: typing.Optional[int] = Field(
        None,
        description='New friends suggestions number'
    )
    gifts: typing.Optional[int] = Field(
        None,
        description='New gifts number'
    )
    groups: typing.Optional[int] = Field(
        None,
        description='New groups number'
    )
    memories: typing.Optional[int] = Field(
        None,
        description='New memories number'
    )
    menu_clips_badge: typing.Optional[int] = Field(
        None,
        description=''
    )
    menu_discover_badge: typing.Optional[int] = Field(
        None,
        description=''
    )
    messages: typing.Optional[int] = Field(
        None,
        description='New messages number'
    )
    notes: typing.Optional[int] = Field(
        None,
        description='New notes number'
    )
    notifications: typing.Optional[int] = Field(
        None,
        description='New notifications number'
    )
    photos: typing.Optional[int] = Field(
        None,
        description='New photo tags number'
    )
    sdk: typing.Optional[int] = Field(
        None,
        description='New sdk number'
    )


class AccountInfo(BaseModel):
    _2fa_required: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Two factor authentication is enabled'
    )
    country: typing.Optional[str] = Field(
        None,
        description='Country code'
    )
    https_required: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether HTTPS-only is enabled'
    )
    intro: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether user has been processed intro'
    )
    lang: typing.Optional[int] = Field(
        None,
        description='Language ID'
    )
    link_redirects: typing.Optional[typing.Any] = Field(
        None,
        description=''
    )
    mini_apps_ads_slot_id: typing.Optional[int] = Field(
        None,
        description='Ads slot id for MyTarget'
    )
    no_wall_replies: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether wall comments should be hidden'
    )
    own_posts_default: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether only owners posts should be shown'
    )
    qr_promotion: typing.Optional[int] = Field(
        None,
        description=''
    )
    show_vk_apps_intro: typing.Optional[bool] = Field(
        None,
        description=''
    )
    subscriptions: typing.Optional["AccountSubscriptions"] = Field(
        None,
        description=''
    )
    wishlists_ae_promo_banner_show: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )


class AccountNameRequest(BaseModel):
    first_name: typing.Optional[str] = Field(
        None,
        description='First name in request'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Request ID needed to cancel the request'
    )
    lang: typing.Optional[str] = Field(
        None,
        description='Text to display to user'
    )
    last_name: typing.Optional[str] = Field(
        None,
        description='Last name in request'
    )
    link_href: typing.Optional[str] = Field(
        None,
        description='href for link in lang field'
    )
    link_label: typing.Optional[str] = Field(
        None,
        description='label to display for link in lang field'
    )
    status: typing.Optional["AccountNameRequestStatus"] = Field(
        None,
        description=''
    )


class AccountNameRequestStatus(enum.Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class LinkType(enum.Enum):
    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class AccountOffer(BaseModel):
    currency_amount: typing.Optional[float] = Field(
        None,
        description='Currency amount'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Offer description'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Offer ID'
    )
    img: typing.Optional[str] = Field(
        None,
        description='URL of the preview image'
    )
    instruction: typing.Optional[str] = Field(
        None,
        description='Instruction how to process the offer'
    )
    instruction_html: typing.Optional[str] = Field(
        None,
        description='Instruction how to process the offer (HTML format)'
    )
    link_id: typing.Optional[int] = Field(
        None,
        description='Link id'
    )
    link_type: typing.Optional["LinkType"] = Field(
        None,
        description='Link type'
    )
    price: typing.Optional[int] = Field(
        None,
        description='Offer price'
    )
    short_description: typing.Optional[str] = Field(
        None,
        description='Offer short description'
    )
    tag: typing.Optional[str] = Field(
        None,
        description='Offer tag'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Offer title'
    )


class AccountPushConversations(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Items count'
    )
    items: typing.Optional[typing.List["AccountPushConversationsItem"]] = Field(
        None,
        description=''
    )


class AccountPushConversationsItem(BaseModel):
    disabled_mass_mentions: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the mass mentions (like @all, @online) are disabled. Can be affected by disabled_mentions'
    )
    disabled_mentions: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the mentions are disabled'
    )
    disabled_until: int = Field(
        None,
        description='Time until that notifications are disabled in seconds'
    )
    peer_id: int = Field(
        None,
        description='Peer ID'
    )
    sound: "BaseBoolInt" = Field(
        None,
        description='Information whether the sound are enabled'
    )


class AccountPushParams(BaseModel):
    app_request: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        None,
        description=''
    )
    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        None,
        description=''
    )
    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    friend_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    friend_found: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    group_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    group_invite: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        None,
        description=''
    )
    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        None,
        description=''
    )
    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        None,
        description=''
    )
    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        None,
        description=''
    )
    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )
    wall_publish: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        None,
        description=''
    )


class AccountPushParamsMode(enum.Enum):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
    ON = "on"
    OFF = "off"


class AccountPushParamsSettings(enum.Enum):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


class AccountPushSettings(BaseModel):
    conversations: typing.Optional["AccountPushConversations"] = Field(
        None,
        description=''
    )
    disabled: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether notifications are disabled'
    )
    disabled_until: typing.Optional[int] = Field(
        None,
        description='Time until that notifications are disabled in Unixtime'
    )
    settings: typing.Optional["AccountPushParams"] = Field(
        None,
        description=''
    )


AccountSubscriptions = typing.List[int]


class UsersUserMin(BaseModel):
    can_access_closed: typing.Optional[bool] = None
    deactivated: typing.Optional[str] = Field(
        None,
        description='Returns if a profile is deleted or blocked'
    )
    first_name: typing.Optional[str] = Field(
        None,
        description='User first name'
    )
    hidden: typing.Optional[int] = Field(
        None,
        description='Returns if a profile is hidden.'
    )
    id: int = Field(
        None,
        description='User ID'
    )
    is_closed: typing.Optional[bool] = Field(
        None,
        description=''
    )
    last_name: typing.Optional[str] = Field(
        None,
        description='User last name'
    )


class UsersUserSettingsXtr(BaseModel):
    bdate: typing.Optional[str] = Field(
        None,
        description='Users date of birth'
    )
    bdate_visibility: typing.Optional[int] = Field(
        None,
        description='Information whether users birthdate are hidden'
    )
    city: typing.Optional["BaseCity"] = Field(
        None,
        description=''
    )
    connections: typing.Optional["UsersUserConnections"] = Field(
        None,
        description=''
    )
    country: typing.Optional["BaseCountry"] = Field(
        None,
        description=''
    )
    first_name: typing.Optional[str] = Field(
        None,
        description='User first name'
    )
    home_town: str = Field(
        None,
        description='Users hometown'
    )
    interests: typing.Optional["AccountUserSettingsInterests"] = Field(
        None,
        description=''
    )
    languages: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    last_name: typing.Optional[str] = Field(
        None,
        description='User last name'
    )
    maiden_name: typing.Optional[str] = Field(
        None,
        description='User maiden name'
    )
    name_request: typing.Optional["AccountNameRequest"] = Field(
        None,
        description=''
    )
    personal: typing.Optional["UsersPersonal"] = Field(
        None,
        description=''
    )
    phone: typing.Optional[str] = Field(
        None,
        description='User phone number with some hidden digits'
    )
    relation: typing.Optional["UsersUserRelation"] = Field(
        None,
        description='User relationship status'
    )
    relation_partner: typing.Optional["UsersUserMin"] = Field(
        None,
        description=''
    )
    relation_pending: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether relation status is pending'
    )
    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = Field(
        None,
        description=''
    )
    screen_name: typing.Optional[str] = Field(
        None,
        description='Domain name of the users page'
    )
    sex: typing.Optional["BaseSex"] = Field(
        None,
        description='User sex'
    )
    status: str = Field(
        None,
        description='User status'
    )
    status_audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    is_service_account: typing.Optional[bool] = Field(
        None,
        description='flag about service account'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the user with 200 pixels in width'
    )


class AccountUserSettingsInterest(BaseModel):
    title: str = Field(
        None,
        description=''
    )
    value: str = Field(
        None,
        description=''
    )


class AccountUserSettingsInterests(BaseModel):
    about: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    activities: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    books: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    games: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    interests: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    movies: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    music: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    quotes: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )
    tv: typing.Optional["AccountUserSettingsInterest"] = Field(
        None,
        description=''
    )


class AddressesFields(enum.Enum):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    METRO_STATION_ID = "metro_station_id"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(BaseModel):
    client_id: typing.Optional[str] = Field(
        None,
        description='Client ID'
    )
    role: typing.Optional["AdsAccessRole"] = Field(
        None,
        description=''
    )


class AdsAccount(BaseModel):
    access_role: "AdsAccessRole" = Field(
        None,
        description=''
    )
    account_id: int = Field(
        None,
        description='Account ID'
    )
    account_name: str = Field(
        None,
        description='Account name'
    )
    account_status: "BaseBoolInt" = Field(
        None,
        description='Information whether account is active'
    )
    account_type: "AdsAccountType" = Field(
        None,
        description=''
    )
    can_view_budget: bool = Field(
        None,
        description='Can user view account budget'
    )


class AdsAccountType(enum.Enum):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(BaseModel):
    ad_format: int = Field(
        None,
        description='Ad format'
    )
    ad_platform: typing.Optional[typing.Union[int, str]] = Field(
        None,
        description='Ad platform'
    )
    all_limit: int = Field(
        None,
        description='Total limit'
    )
    approved: "AdsAdApproved" = Field(
        None,
        description=''
    )
    autobidding_max_cost: typing.Optional[int] = Field(
        None,
        description='Max cost of target actions for autobidding, kopecks'
    )
    campaign_id: int = Field(
        None,
        description='Campaign ID'
    )
    category1_id: typing.Optional[int] = Field(
        None,
        description='Category ID'
    )
    category2_id: typing.Optional[int] = Field(
        None,
        description='Additional category ID'
    )
    cost_type: "AdsAdCostType" = Field(
        None,
        description=''
    )
    cpa: typing.Optional[int] = Field(
        None,
        description='Cost of an action, kopecks'
    )
    cpc: typing.Optional[int] = Field(
        None,
        description='Cost of a click, kopecks'
    )
    cpm: typing.Optional[int] = Field(
        None,
        description='Cost of 1000 impressions, kopecks'
    )
    disclaimer_medical: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether disclaimer is enabled'
    )
    disclaimer_specialist: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether disclaimer is enabled'
    )
    disclaimer_supplements: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether disclaimer is enabled'
    )
    id: int = Field(
        None,
        description='Ad ID'
    )
    impressions_limit: typing.Optional[int] = Field(
        None,
        description='Impressions limit'
    )
    impressions_limited: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether impressions are limited'
    )
    name: str = Field(
        None,
        description='Ad title'
    )
    ocpm: typing.Optional[int] = Field(
        None,
        description='Cost of 1000 impressions optimized, kopecks'
    )
    status: "AdsAdStatus" = Field(
        None,
        description=''
    )
    video: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the ad is a video'
    )


class AdsAdApproved(enum.IntEnum):
    not_moderated = 0
    pending_moderation = 1
    approved = 2
    rejected = 3


class AdsAdCostType(enum.IntEnum):
    per_clicks = 0
    per_impressions = 1
    per_actions = 2
    per_impressions_optimized = 3


class AdsAdLayout(BaseModel):
    ad_format: int = Field(
        None,
        description='Ad format'
    )
    campaign_id: int = Field(
        None,
        description='Campaign ID'
    )
    cost_type: "AdsAdCostType" = Field(
        None,
        description=''
    )
    description: str = Field(
        None,
        description='Ad description'
    )
    id: str = Field(
        None,
        description='Ad ID'
    )
    image_src: str = Field(
        None,
        description='Image URL'
    )
    image_src_2x: typing.Optional[str] = Field(
        None,
        description='URL of the preview image in double size'
    )
    link_domain: typing.Optional[str] = Field(
        None,
        description='Domain of advertised object'
    )
    link_url: str = Field(
        None,
        description='URL of advertised object'
    )
    preview_link: typing.Optional[str] = Field(
        None,
        description='link to preview an ad as it is shown on the website'
    )
    title: str = Field(
        None,
        description='Ad title'
    )
    video: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the ad is a video'
    )


class AdsAdStatus(enum.IntEnum):
    stopped = 0
    started = 1
    deleted = 2


class AdsCampaign(BaseModel):
    ads_count: typing.Optional[int] = Field(
        None,
        description='Amount of active ads in campaign'
    )
    all_limit: str = Field(
        None,
        description='Campaigns total limit, rubles'
    )
    create_time: typing.Optional[int] = Field(
        None,
        description='Campaign create time, as Unixtime'
    )
    day_limit: str = Field(
        None,
        description='Campaigns day limit, rubles'
    )
    goal_type: typing.Optional[int] = Field(
        None,
        description='Campaign goal type'
    )
    id: int = Field(
        None,
        description='Campaign ID'
    )
    is_cbo_enabled: typing.Optional[bool] = Field(
        None,
        description='Shows if Campaign Budget Optimization is on'
    )
    name: str = Field(
        None,
        description='Campaign title'
    )
    start_time: int = Field(
        None,
        description='Campaign start time, as Unixtime'
    )
    status: "AdsCampaignStatus" = Field(
        None,
        description=''
    )
    stop_time: int = Field(
        None,
        description='Campaign stop time, as Unixtime'
    )
    type: "AdsCampaignType" = Field(
        None,
        description=''
    )
    update_time: typing.Optional[int] = Field(
        None,
        description='Campaign update time, as Unixtime'
    )
    user_goal_type: typing.Optional[int] = Field(
        None,
        description='Campaign user goal type'
    )
    views_limit: typing.Optional[int] = Field(
        None,
        description='Limit of views per user per campaign'
    )


class AdsCampaignStatus(enum.IntEnum):
    stopped = 0
    started = 1
    deleted = 2


class AdsCampaignType(enum.Enum):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


class AdsCategory(BaseModel):
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )
    subcategories: typing.Optional[typing.List["AdsCategory"]] = Field(
        None,
        description=''
    )


class AdsClient(BaseModel):
    all_limit: str = Field(
        None,
        description='Clients total limit, rubles'
    )
    day_limit: str = Field(
        None,
        description='Clients day limit, rubles'
    )
    id: int = Field(
        None,
        description='Client ID'
    )
    name: str = Field(
        None,
        description='Client name'
    )


class AdsCreateAdStatus(BaseModel):
    error_code: typing.Optional[int] = Field(
        None,
        description='Error code'
    )
    error_desc: typing.Optional[str] = Field(
        None,
        description='Error description'
    )
    id: int = Field(
        None,
        description='Ad ID'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Stealth Post ID'
    )


class AdsCreateCampaignStatus(BaseModel):
    error_code: typing.Optional[int] = Field(
        None,
        description='Error code'
    )
    error_desc: typing.Optional[str] = Field(
        None,
        description='Error description'
    )
    id: int = Field(
        None,
        description='Campaign ID'
    )


class AdsCriteria(BaseModel):
    age_from: typing.Optional[int] = Field(
        None,
        description='Age from'
    )
    age_to: typing.Optional[int] = Field(
        None,
        description='Age to'
    )
    apps: typing.Optional[str] = Field(
        None,
        description='Apps IDs'
    )
    apps_not: typing.Optional[str] = Field(
        None,
        description='Apps IDs to except'
    )
    birthday: typing.Optional[int] = Field(
        None,
        description='Days to birthday'
    )
    cities: typing.Optional[str] = Field(
        None,
        description='Cities IDs'
    )
    cities_not: typing.Optional[str] = Field(
        None,
        description='Cities IDs to except'
    )
    country: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )
    districts: typing.Optional[str] = Field(
        None,
        description='Districts IDs'
    )
    groups: typing.Optional[str] = Field(
        None,
        description='Communities IDs'
    )
    interest_categories: typing.Optional[str] = Field(
        None,
        description='Interests categories IDs'
    )
    interests: typing.Optional[str] = Field(
        None,
        description='Interests'
    )
    paying: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user has proceeded VK payments before'
    )
    positions: typing.Optional[str] = Field(
        None,
        description='Positions IDs'
    )
    religions: typing.Optional[str] = Field(
        None,
        description='Religions IDs'
    )
    retargeting_groups: typing.Optional[str] = Field(
        None,
        description='Retargeting groups IDs'
    )
    retargeting_groups_not: typing.Optional[str] = Field(
        None,
        description='Retargeting groups IDs to except'
    )
    school_from: typing.Optional[int] = Field(
        None,
        description='School graduation year from'
    )
    school_to: typing.Optional[int] = Field(
        None,
        description='School graduation year to'
    )
    schools: typing.Optional[str] = Field(
        None,
        description='Schools IDs'
    )
    sex: typing.Optional["AdsCriteriaSex"] = Field(
        None,
        description=''
    )
    stations: typing.Optional[str] = Field(
        None,
        description='Stations IDs'
    )
    statuses: typing.Optional[str] = Field(
        None,
        description='Relationship statuses'
    )
    streets: typing.Optional[str] = Field(
        None,
        description='Streets IDs'
    )
    travellers: typing.Optional["BasePropertyExists"] = Field(
        None,
        description='Travellers only'
    )
    uni_from: typing.Optional[int] = Field(
        None,
        description='University graduation year from'
    )
    uni_to: typing.Optional[int] = Field(
        None,
        description='University graduation year to'
    )
    user_browsers: typing.Optional[str] = Field(
        None,
        description='Browsers'
    )
    user_devices: typing.Optional[str] = Field(
        None,
        description='Devices'
    )
    user_os: typing.Optional[str] = Field(
        None,
        description='Operating systems'
    )


class AdsCriteriaSex(enum.IntEnum):
    any = 0
    male = 1
    female = 2


class AdsDemoStats(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    stats: typing.Optional["AdsDemostatsFormat"] = Field(
        None,
        description=''
    )
    type: typing.Optional["AdsObjectType"] = Field(
        None,
        description=''
    )


class AdsDemostatsFormat(BaseModel):
    age: typing.Optional[typing.List["AdsStatsAge"]] = Field(
        None,
        description=''
    )
    cities: typing.Optional[typing.List["AdsStatsCities"]] = Field(
        None,
        description=''
    )
    day: typing.Optional[str] = Field(
        None,
        description='Day as YYYY-MM-DD'
    )
    month: typing.Optional[str] = Field(
        None,
        description='Month as YYYY-MM'
    )
    overall: typing.Optional[int] = Field(
        None,
        description='1 if period=overall'
    )
    sex: typing.Optional[typing.List["AdsStatsSex"]] = Field(
        None,
        description=''
    )
    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = Field(
        None,
        description=''
    )


class AdsFloodStats(BaseModel):
    left: int = Field(
        None,
        description='Requests left'
    )
    refresh: int = Field(
        None,
        description='Time to refresh in seconds'
    )


class AdsLinkStatus(BaseModel):
    description: str = Field(
        None,
        description='Reject reason'
    )
    redirect_url: str = Field(
        None,
        description='URL'
    )
    status: str = Field(
        None,
        description='Link status'
    )


class LookalikeRequestStatus(enum.Enum):
    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class LookalikeRequestSourceType(enum.Enum):
    RETARGETING_GROUP = "retargeting_group"


class AdsLookalikeRequest(BaseModel):
    audience_count: typing.Optional[int] = Field(
        None,
        description='Lookalike request seed audience size'
    )
    create_time: int = Field(
        None,
        description='Lookalike request create time, as Unixtime'
    )
    id: int = Field(
        None,
        description='Lookalike request ID'
    )
    save_audience_levels: typing.Optional[typing.List["AdsLookalikeRequestSaveAudienceLevel"]] = Field(
        None,
        description=''
    )
    scheduled_delete_time: typing.Optional[int] = Field(
        None,
        description='Time by which lookalike request would be deleted, as Unixtime'
    )
    source_name: typing.Optional[str] = Field(
        None,
        description='Lookalike request seed name (retargeting group name)'
    )
    source_retargeting_group_id: typing.Optional[int] = Field(
        None,
        description='Retargeting group id, which was used as lookalike seed'
    )
    source_type: typing.Optional["LookalikeRequestSourceType"] = Field(
        None,
        description='Lookalike request source type'
    )
    status: typing.Optional["LookalikeRequestStatus"] = Field(
        None,
        description='Lookalike request status'
    )
    update_time: int = Field(
        None,
        description='Lookalike request update time, as Unixtime'
    )


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    audience_count: typing.Optional[int] = Field(
        None,
        description='Saved audience audience size for according level'
    )
    level: typing.Optional[int] = Field(
        None,
        description='Save audience level id, which is used in save audience queries'
    )


class AdsMusician(BaseModel):
    avatar: typing.Optional[str] = Field(
        None,
        description='Music artist photo'
    )
    id: int = Field(
        None,
        description='Targeting music artist ID'
    )
    name: str = Field(
        None,
        description='Music artist name'
    )


class AdsObjectType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(BaseModel):
    paragraph: typing.Optional[str] = Field(
        None,
        description='Rules paragraph'
    )


class AdsPromotedPostReach(BaseModel):
    hide: int = Field(
        None,
        description='Hides amount'
    )
    id: int = Field(
        None,
        description='Object ID from ids parameter'
    )
    join_group: int = Field(
        None,
        description='Community joins'
    )
    links: int = Field(
        None,
        description='Link clicks'
    )
    reach_subscribers: int = Field(
        None,
        description='Subscribers reach'
    )
    reach_total: int = Field(
        None,
        description='Total reach'
    )
    report: int = Field(
        None,
        description='Reports amount'
    )
    to_group: int = Field(
        None,
        description='Community clicks'
    )
    unsubscribe: int = Field(
        None,
        description='Unsubscribe events amount'
    )
    video_views_100p: typing.Optional[int] = Field(
        None,
        description='Video views for 100 percent'
    )
    video_views_25p: typing.Optional[int] = Field(
        None,
        description='Video views for 25 percent'
    )
    video_views_3s: typing.Optional[int] = Field(
        None,
        description='Video views for 3 seconds'
    )
    video_views_50p: typing.Optional[int] = Field(
        None,
        description='Video views for 50 percent'
    )
    video_views_75p: typing.Optional[int] = Field(
        None,
        description='Video views for 75 percent'
    )
    video_views_start: typing.Optional[int] = Field(
        None,
        description='Video starts'
    )


class AdsRejectReason(BaseModel):
    comment: typing.Optional[str] = Field(
        None,
        description='Comment text'
    )
    rules: typing.Optional[typing.List["AdsRules"]] = Field(
        None,
        description=''
    )


class AdsRules(BaseModel):
    paragraphs: typing.Optional[typing.List["AdsParagraphs"]] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description='Comment'
    )


class AdsStats(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    stats: typing.Optional["AdsStatsFormat"] = Field(
        None,
        description=''
    )
    type: typing.Optional["AdsObjectType"] = Field(
        None,
        description=''
    )
    views_times: typing.Optional["AdsStatsViewsTimes"] = Field(
        None,
        description=''
    )


class AdsStatsAge(BaseModel):
    clicks_rate: typing.Optional[float] = Field(
        None,
        description='Clicks rate'
    )
    impressions_rate: typing.Optional[float] = Field(
        None,
        description='Impressions rate'
    )
    value: typing.Optional[str] = Field(
        None,
        description='Age interval'
    )


class AdsStatsCities(BaseModel):
    clicks_rate: typing.Optional[float] = Field(
        None,
        description='Clicks rate'
    )
    impressions_rate: typing.Optional[float] = Field(
        None,
        description='Impressions rate'
    )
    name: typing.Optional[str] = Field(
        None,
        description='City name'
    )
    value: typing.Optional[int] = Field(
        None,
        description='City ID'
    )


class AdsStatsFormat(BaseModel):
    clicks: typing.Optional[int] = Field(
        None,
        description='Clicks number'
    )
    day: typing.Optional[str] = Field(
        None,
        description='Day as YYYY-MM-DD'
    )
    impressions: typing.Optional[int] = Field(
        None,
        description='Impressions number'
    )
    join_rate: typing.Optional[int] = Field(
        None,
        description='Events number'
    )
    link_external_clicks: typing.Optional[int] = Field(
        None,
        description='External clicks number'
    )
    month: typing.Optional[str] = Field(
        None,
        description='Month as YYYY-MM'
    )
    overall: typing.Optional[int] = Field(
        None,
        description='1 if period=overall'
    )
    reach: typing.Optional[int] = Field(
        None,
        description='Reach '
    )
    spent: typing.Optional[int] = Field(
        None,
        description='Spent funds'
    )
    video_clicks_site: typing.Optional[int] = Field(
        None,
        description='Clickthoughs to the advertised site'
    )
    video_views: typing.Optional[int] = Field(
        None,
        description='Video views number'
    )
    video_views_full: typing.Optional[int] = Field(
        None,
        description='Video views (full video)'
    )
    video_views_half: typing.Optional[int] = Field(
        None,
        description='Video views (half of video)'
    )


class AdsStatsSex(BaseModel):
    clicks_rate: typing.Optional[float] = Field(
        None,
        description='Clicks rate'
    )
    impressions_rate: typing.Optional[float] = Field(
        None,
        description='Impressions rate'
    )
    value: typing.Optional["AdsStatsSexValue"] = Field(
        None,
        description=''
    )


class AdsStatsSexAge(BaseModel):
    clicks_rate: typing.Optional[float] = Field(
        None,
        description='Clicks rate'
    )
    impressions_rate: typing.Optional[float] = Field(
        None,
        description='Impressions rate'
    )
    value: typing.Optional[str] = Field(
        None,
        description='Sex and age interval'
    )


class AdsStatsSexValue(enum.Enum):
    F = "f"
    M = "m"


class AdsStatsViewsTimes(BaseModel):
    views_ads_times_1: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_10: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_11_plus: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_2: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_3: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_4: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_5: typing.Optional[str] = Field(
        None,
        description=''
    )
    views_ads_times_6: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_7: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_8: typing.Optional[int] = Field(
        None,
        description=''
    )
    views_ads_times_9: typing.Optional[int] = Field(
        None,
        description=''
    )


class AdsTargSettings(AdsCriteria):
    campaign_id: typing.Optional[int] = Field(
        None,
        description='Campaign ID'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Ad ID'
    )


class AdsTargStats(BaseModel):
    audience_count: int = Field(
        None,
        description='Audience'
    )
    recommended_cpc: typing.Optional[float] = Field(
        None,
        description='Recommended CPC value for 50% reach (old format)'
    )
    recommended_cpc_50: typing.Optional[float] = Field(
        None,
        description='Recommended CPC value for 50% reach'
    )
    recommended_cpc_70: typing.Optional[float] = Field(
        None,
        description='Recommended CPC value for 70% reach'
    )
    recommended_cpc_90: typing.Optional[float] = Field(
        None,
        description='Recommended CPC value for 90% reach'
    )
    recommended_cpm: typing.Optional[float] = Field(
        None,
        description='Recommended CPM value for 50% reach (old format)'
    )
    recommended_cpm_50: typing.Optional[float] = Field(
        None,
        description='Recommended CPM value for 50% reach'
    )
    recommended_cpm_70: typing.Optional[float] = Field(
        None,
        description='Recommended CPM value for 70% reach'
    )
    recommended_cpm_90: typing.Optional[float] = Field(
        None,
        description='Recommended CPM value for 90% reach'
    )


class AdsTargSuggestions(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Object name'
    )


class AdsTargSuggestionsCities(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Object name'
    )
    parent: typing.Optional[str] = Field(
        None,
        description='Parent object'
    )


class AdsTargSuggestionsRegions(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Object name'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Object type'
    )


class AdsTargSuggestionsSchools(BaseModel):
    desc: typing.Optional[str] = Field(
        None,
        description='Full school title'
    )
    id: typing.Optional[int] = Field(
        None,
        description='School ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='School title'
    )
    parent: typing.Optional[str] = Field(
        None,
        description='City name'
    )
    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = Field(
        None,
        description=''
    )


class AdsTargSuggestionsSchoolsType(enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(BaseModel):
    audience_count: typing.Optional[int] = Field(
        None,
        description='Audience'
    )
    domain: typing.Optional[str] = Field(
        None,
        description='Site domain'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Group ID'
    )
    lifetime: typing.Optional[int] = Field(
        None,
        description='Number of days for user to be in group'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Group name'
    )
    pixel: typing.Optional[str] = Field(
        None,
        description='Pixel code'
    )


class AdsUpdateOfficeUsersResult(BaseModel):
    error: typing.Optional["BaseError"] = Field(
        None,
        description=''
    )
    is_success: bool = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class AdsUserSpecification(BaseModel):
    client_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    grant_access_to_all_clients: typing.Optional[bool] = Field(
        None,
        description=''
    )
    role: "AdsAccessRolePublic" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )
    view_budget: typing.Optional[bool] = Field(
        None,
        description=''
    )


class AdsUserSpecificationCutted(BaseModel):
    client_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    role: "AdsAccessRolePublic" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )
    view_budget: typing.Optional[bool] = Field(
        None,
        description=''
    )


class AdsUsers(BaseModel):
    accesses: typing.List["AdsAccesses"] = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class AdswebGetAdCategoriesResponseCategoriesCategory(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    name: str = Field(
        None,
        description=''
    )


class AdswebGetAdUnitsResponseAdUnitsAdUnit(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    site_id: int = Field(
        None,
        description=''
    )


class AdswebGetFraudHistoryResponseEntriesEntry(BaseModel):
    day: str = Field(
        None,
        description=''
    )
    site_id: int = Field(
        None,
        description=''
    )


class AdswebGetSitesResponseSitesSite(BaseModel):
    domains: typing.Optional[str] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    status_moder: typing.Optional[str] = Field(
        None,
        description=''
    )
    status_user: typing.Optional[str] = Field(
        None,
        description=''
    )


class AdswebGetStatisticsResponseItemsItem(BaseModel):
    ad_unit_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    day_max: typing.Optional[str] = Field(
        None,
        description=''
    )
    day_min: typing.Optional[str] = Field(
        None,
        description=''
    )
    days_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    hour_max: typing.Optional[str] = Field(
        None,
        description=''
    )
    hour_min: typing.Optional[str] = Field(
        None,
        description=''
    )
    hours_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    month_max: typing.Optional[str] = Field(
        None,
        description=''
    )
    month_min: typing.Optional[str] = Field(
        None,
        description=''
    )
    months_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    overall_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    site_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class AppWidgetsPhoto(BaseModel):
    id: str = Field(
        None,
        description='Image ID'
    )
    images: typing.List["BaseImage"] = Field(
        None,
        description=''
    )


class AppWidgetsPhotos(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description=''
    )
    items: typing.Optional[typing.List["AppWidgetsPhoto"]] = Field(
        None,
        description=''
    )


class AppsAppMin(BaseModel):
    author_owner_id: typing.Optional[int] = Field(
        None,
        description='Application authors ID'
    )
    background_loader_color: typing.Optional[str] = Field(
        None,
        description='Hex color code without hash sign'
    )
    icon_139: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 139 px in width'
    )
    icon_150: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 150 px in width'
    )
    icon_278: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 278 px in width'
    )
    icon_576: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 576 px in width'
    )
    icon_75: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 75 px in width'
    )
    id: int = Field(
        None,
        description='Application ID'
    )
    is_installed: typing.Optional[bool] = Field(
        None,
        description='Is application installed'
    )
    loader_icon: typing.Optional[str] = Field(
        None,
        description='SVG data'
    )
    title: str = Field(
        None,
        description='Application title'
    )
    type: "AppsAppType" = Field(
        None,
        description=''
    )


class AppsApp(AppsAppMin):
    author_url: typing.Optional[str] = Field(
        None,
        description='Application authors URL'
    )
    banner_1120: typing.Optional[str] = Field(
        None,
        description='URL of the app banner with 1120 px in width'
    )
    banner_560: typing.Optional[str] = Field(
        None,
        description='URL of the app banner with 560 px in width'
    )
    catalog_position: typing.Optional[int] = Field(
        None,
        description='Catalog position'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Application description'
    )
    friends: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    genre: typing.Optional[str] = Field(
        None,
        description='Genre name'
    )
    genre_id: typing.Optional[int] = Field(
        None,
        description='Genre ID'
    )
    icon_16: typing.Optional[str] = Field(
        None,
        description='URL of the app icon with 16 px in width'
    )
    international: typing.Optional[bool] = Field(
        None,
        description='Information whether the application is multilanguage'
    )
    is_in_catalog: typing.Optional[int] = Field(
        None,
        description='Information whether application is in mobile catalog'
    )
    is_new: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Is new flag'
    )
    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = Field(
        None,
        description=''
    )
    members_count: typing.Optional[int] = Field(
        None,
        description='Members number'
    )
    platform_id: typing.Optional[str] = Field(
        None,
        description='Application ID in store'
    )
    published_date: typing.Optional[int] = Field(
        None,
        description='Date when the application has been published in Unixtime'
    )
    push_enabled: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Is push enabled'
    )
    screen_name: typing.Optional[str] = Field(
        None,
        description='Screen name'
    )
    screen_orientation: typing.Optional[int] = Field(
        None,
        description='Screen orientation'
    )
    section: typing.Optional[str] = Field(
        None,
        description='Application section name'
    )


class AppsAppLeaderboardType(enum.IntEnum):
    not_supported = 0
    levels = 1
    points = 2


class AppsAppType(enum.Enum):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsCatalogList(BaseModel):
    count: int = Field(
        None,
        description='Total number'
    )
    items: typing.List["AppsApp"] = Field(
        None,
        description=''
    )
    profiles: typing.Optional[typing.List["UsersUserMin"]] = Field(
        None,
        description=''
    )


class AppsLeaderboard(BaseModel):
    level: typing.Optional[int] = Field(
        None,
        description='Level'
    )
    points: typing.Optional[int] = Field(
        None,
        description='Points number'
    )
    score: typing.Optional[int] = Field(
        None,
        description='Score number'
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class ScopeName(enum.Enum):
    FRIENDS = "friends"
    PHOTOS = "photos"
    VIDEO = "video"
    PAGES = "pages"
    STATUS = "status"
    NOTES = "notes"
    WALL = "wall"
    DOCS = "docs"
    GROUPS = "groups"
    STATS = "stats"
    MARKET = "market"


class AppsScope(BaseModel):
    name: typing.Optional["ScopeName"] = Field(
        None,
        description='Scope name'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Scope title'
    )


class AudioAudio(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the audio'
    )
    album_id: typing.Optional[int] = Field(
        None,
        description='Album ID'
    )
    artist: str = Field(
        None,
        description='Artist name'
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when uploaded'
    )
    duration: int = Field(
        None,
        description='Duration in seconds'
    )
    genre_id: typing.Optional[int] = Field(
        None,
        description='Genre ID'
    )
    id: int = Field(
        None,
        description='Audio ID'
    )
    owner_id: int = Field(
        None,
        description='Audio owners ID'
    )
    performer: typing.Optional[str] = Field(
        None,
        description='Performer name'
    )
    title: str = Field(
        None,
        description='Title'
    )
    url: typing.Optional[str] = Field(
        None,
        description='URL of mp3 file'
    )


class BaseBoolInt(enum.IntEnum):
    NO = 0
    YES = 1


class BaseCity(BaseModel):
    id: int = Field(
        None,
        description='City ID'
    )
    title: str = Field(
        None,
        description='City title'
    )


class BaseCommentsInfo(BaseModel):
    can_close: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    can_open: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    can_post: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment the post'
    )
    count: typing.Optional[int] = Field(
        None,
        description='Comments number'
    )
    donut: typing.Optional["WallWallpostCommentsDonut"] = Field(
        None,
        description=''
    )
    groups_can_post: typing.Optional[bool] = Field(
        None,
        description='Information whether groups can comment the post'
    )


class BaseCountry(BaseModel):
    id: int = Field(
        None,
        description='Country ID'
    )
    title: str = Field(
        None,
        description='Country title'
    )


class BaseCropPhoto(BaseModel):
    crop: "BaseCropPhotoCrop" = Field(
        None,
        description=''
    )
    photo: "PhotosPhoto" = Field(
        None,
        description=''
    )
    rect: "BaseCropPhotoRect" = Field(
        None,
        description=''
    )


class BaseCropPhotoCrop(BaseModel):
    x: float = Field(
        None,
        description='Coordinate X of the left upper corner'
    )
    x2: float = Field(
        None,
        description='Coordinate X of the right lower corner'
    )
    y: float = Field(
        None,
        description='Coordinate Y of the left upper corner'
    )
    y2: float = Field(
        None,
        description='Coordinate Y of the right lower corner'
    )


class BaseCropPhotoRect(BaseModel):
    x: float = Field(
        None,
        description='Coordinate X of the left upper corner'
    )
    x2: float = Field(
        None,
        description='Coordinate X of the right lower corner'
    )
    y: float = Field(
        None,
        description='Coordinate Y of the left upper corner'
    )
    y2: float = Field(
        None,
        description='Coordinate Y of the right lower corner'
    )


class BaseError(BaseModel):
    error_code: int = Field(
        None,
        description='Error code'
    )
    error_msg: typing.Optional[str] = Field(
        None,
        description='Error message'
    )
    error_subcode: typing.Optional[int] = Field(
        None,
        description='Error subcode'
    )
    error_text: typing.Optional[str] = Field(
        None,
        description='Localized error message'
    )
    request_params: typing.Optional[typing.List["BaseRequestParam"]] = Field(
        None,
        description=''
    )


class BaseGeo(BaseModel):
    coordinates: typing.Optional["BaseGeoCoordinates"] = Field(
        None,
        description=''
    )
    place: typing.Optional["BasePlace"] = Field(
        None,
        description=''
    )
    showmap: typing.Optional[int] = Field(
        None,
        description='Information whether a map is showed'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Place type'
    )


class BaseGeoCoordinates(BaseModel):
    latitude: float = Field(
        None,
        description=''
    )
    longitude: float = Field(
        None,
        description=''
    )


class BaseGradientPoint(BaseModel):
    color: str = Field(
        None,
        description='Hex color code without #'
    )
    position: float = Field(
        None,
        description='Point position'
    )


class BaseImage(BaseModel):
    height: int = Field(
        None,
        description='Image height'
    )
    id: typing.Optional[str] = Field(
        None,
        description=''
    )
    url: str = Field(
        None,
        description='Image url'
    )
    width: int = Field(
        None,
        description='Image width'
    )


class BaseLikes(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Likes number'
    )
    user_likes: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user likes the photo'
    )


class BaseLikesInfo(BaseModel):
    can_like: "BaseBoolInt" = Field(
        None,
        description='Information whether current user can like the post'
    )
    can_publish: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can repost'
    )
    count: int = Field(
        None,
        description='Likes number'
    )
    user_likes: int = Field(
        None,
        description='Information whether current uer has liked the post'
    )


class BaseLink(BaseModel):
    application: typing.Optional["BaseLinkApplication"] = Field(
        None,
        description=''
    )
    button: typing.Optional["BaseLinkButton"] = Field(
        None,
        description=''
    )
    caption: typing.Optional[str] = Field(
        None,
        description='Link caption'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Link description'
    )
    id: typing.Optional[str] = Field(
        None,
        description='Link ID'
    )
    is_external: typing.Optional[bool] = Field(
        None,
        description='Information whether the current link is external'
    )
    is_favorite: typing.Optional[bool] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    preview_page: typing.Optional[str] = Field(
        None,
        description='String ID of the page with article preview'
    )
    preview_url: typing.Optional[str] = Field(
        None,
        description='URL of the page with article preview'
    )
    product: typing.Optional["BaseLinkProduct"] = Field(
        None,
        description=''
    )
    rating: typing.Optional["BaseLinkRating"] = Field(
        None,
        description=''
    )
    target_object: typing.Optional["LinkTargetObject"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description='Link title'
    )
    url: str = Field(
        None,
        description='Link URL'
    )
    video: typing.Optional["VideoVideo"] = Field(
        None,
        description='Video from link'
    )


class BaseLinkApplication(BaseModel):
    app_id: typing.Optional[float] = Field(
        None,
        description='Application Id'
    )
    store: typing.Optional["BaseLinkApplicationStore"] = Field(
        None,
        description=''
    )


class BaseLinkApplicationStore(BaseModel):
    id: typing.Optional[float] = Field(
        None,
        description='Store Id'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Store name'
    )


class BaseLinkButton(BaseModel):
    action: typing.Optional["BaseLinkButtonAction"] = Field(
        None,
        description='Button action'
    )
    album_id: typing.Optional[int] = Field(
        None,
        description='Video album id'
    )
    block_id: typing.Optional[str] = Field(
        None,
        description='Target block id'
    )
    curator_id: typing.Optional[int] = Field(
        None,
        description='curator id'
    )
    icon: typing.Optional[str] = Field(
        None,
        description='Button icon name, e.g. phone or gift'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Owner id'
    )
    section_id: typing.Optional[str] = Field(
        None,
        description='Target section id'
    )
    style: typing.Optional["BaseLinkButtonStyle"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description='Button title'
    )


class BaseLinkButtonAction(BaseModel):
    consume_reason: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: "BaseLinkButtonActionType" = Field(
        None,
        description=''
    )
    url: typing.Optional[str] = Field(
        None,
        description='Action URL'
    )


class BaseLinkButtonActionType(enum.Enum):
    OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class BaseLinkProduct(BaseModel):
    merchant: typing.Optional[str] = Field(
        None,
        description=''
    )
    orders_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    price: "MarketPrice" = Field(
        None,
        description=''
    )


class BaseLinkProductCategory(BaseModel):
    pass


class BaseLinkProductStatus(enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRating(BaseModel):
    reviews_count: typing.Optional[int] = Field(
        None,
        description='Count of reviews'
    )
    stars: typing.Optional[float] = Field(
        None,
        description='Count of stars'
    )


class BaseMessageError(BaseModel):
    code: typing.Optional[int] = Field(
        None,
        description='Error code'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Error message'
    )


class BaseObject(BaseModel):
    id: int = Field(
        None,
        description='Object ID'
    )
    title: str = Field(
        None,
        description='Object title'
    )


class BaseObjectCount(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Items count'
    )


class BaseObjectWithName(BaseModel):
    id: int = Field(
        None,
        description='Object ID'
    )
    name: str = Field(
        None,
        description='Object name'
    )


class BasePlace(BaseModel):
    address: typing.Optional[str] = Field(
        None,
        description='Place address'
    )
    checkins: typing.Optional[int] = Field(
        None,
        description='Checkins number'
    )
    city: typing.Optional[str] = Field(
        None,
        description='City name'
    )
    country: typing.Optional[str] = Field(
        None,
        description='Country name'
    )
    created: typing.Optional[int] = Field(
        None,
        description='Date of the place creation in Unixtime'
    )
    icon: typing.Optional[str] = Field(
        None,
        description='URL of the places icon'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Place ID'
    )
    latitude: typing.Optional[float] = Field(
        None,
        description='Place latitude'
    )
    longitude: typing.Optional[float] = Field(
        None,
        description='Place longitude'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Place title'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Place type'
    )


class BasePropertyExists(enum.IntEnum):
    property_exists = 1


class BaseRepostsInfo(BaseModel):
    count: int = Field(
        None,
        description='Total reposts counter. Sum of wall and mail reposts counters'
    )
    mail_count: typing.Optional[int] = Field(
        None,
        description='Mail reposts counter'
    )
    user_reposted: typing.Optional[int] = Field(
        None,
        description='Information whether current user has reposted the post'
    )
    wall_count: typing.Optional[int] = Field(
        None,
        description='Wall reposts counter'
    )


class BaseRequestParam(BaseModel):
    key: typing.Optional[str] = Field(
        None,
        description='Parameter name'
    )
    value: typing.Optional[str] = Field(
        None,
        description='Parameter value'
    )


class BaseSex(enum.IntEnum):
    unknown = 0
    female = 1
    male = 2


class BaseStickerOld(BaseModel):
    height: typing.Optional[int] = Field(
        None,
        description='Height in px'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Sticker ID'
    )
    is_allowed: typing.Optional[bool] = Field(
        None,
        description='Information whether the sticker is allowed'
    )
    photo_128: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 128 px in height'
    )
    photo_256: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 256 px in height'
    )
    photo_352: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 352 px in height'
    )
    photo_512: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 512 px in height'
    )
    photo_64: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 64 px in height'
    )
    product_id: typing.Optional[int] = Field(
        None,
        description='Pack ID'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Width in px'
    )


class BaseStickerNew(BaseModel):
    animation_url: typing.Optional[str] = Field(
        None,
        description='URL of sticker animation script'
    )
    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = Field(
        None,
        description='Array of sticker animation script objects'
    )
    images: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description=''
    )
    images_with_background: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description=''
    )
    is_allowed: typing.Optional[bool] = Field(
        None,
        description='Information whether the sticker is allowed'
    )
    product_id: typing.Optional[int] = Field(
        None,
        description='Pack ID'
    )
    sticker_id: typing.Optional[int] = Field(
        None,
        description='Sticker ID'
    )


class BaseSticker(BaseStickerOld, BaseStickerNew):
    pass


class AnimationScriptType(enum.Enum):
    LIGHT = "light"
    DARK = "dark"


class BaseStickerAnimation(BaseModel):
    type: typing.Optional["AnimationScriptType"] = Field(
        None,
        description='Type of animation script'
    )
    url: typing.Optional[str] = Field(
        None,
        description='URL of animation script'
    )


BaseStickersList = typing.List["BaseStickerNew"]


class BaseUploadServer(BaseModel):
    upload_url: str = Field(
        None,
        description='Upload URL'
    )


class BaseUserGroupFields(enum.Enum):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COUNTRY = "country"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    FIRST_NAME = "first_name"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_GEN = "first_name_gen"
    LAST_NAME = "last_name"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_GEN = "last_name_gen"
    CAN_SUBSCRIBE_STORIES = "can_subscribe_stories"
    IS_SUBSCRIBED_STORIES = "is_subscribed_stories"
    VK_ADMIN_STATUS = "vk_admin_status"
    CAN_UPLOAD_STORY = "can_upload_story"


class BaseUserId(BaseModel):
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class BoardDefaultOrder(enum.IntEnum):
    desc_updated = 1
    desc_created = 2
    asc_updated = -1
    asc_created = -2


class BoardTopic(BaseModel):
    comments: typing.Optional[int] = Field(
        None,
        description='Comments number'
    )
    created: typing.Optional[int] = Field(
        None,
        description='Date when the topic has been created in Unixtime'
    )
    created_by: typing.Optional[int] = Field(
        None,
        description='Creator ID'
    )
    first_comment: typing.Optional[str] = Field(
        None,
        description='First comment text'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Topic ID'
    )
    is_closed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the topic is closed'
    )
    is_fixed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the topic is fixed'
    )
    last_comment: typing.Optional[str] = Field(
        None,
        description='Last comment text'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Topic title'
    )
    updated: typing.Optional[int] = Field(
        None,
        description='Date when the topic has been updated in Unixtime'
    )
    updated_by: typing.Optional[int] = Field(
        None,
        description='ID of user who updated the topic'
    )


class BoardTopicComment(BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        None,
        description=''
    )
    can_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can edit the comment'
    )
    date: int = Field(
        None,
        description='Date when the comment has been added in Unixtime'
    )
    from_id: int = Field(
        None,
        description='Author ID'
    )
    id: int = Field(
        None,
        description='Comment ID'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    real_offset: typing.Optional[int] = Field(
        None,
        description='Real position of the comment'
    )
    text: str = Field(
        None,
        description='Comment text'
    )


class CallbackBase(BaseModel):
    event_id: str = Field(
        None,
        description='Unique event id. If it passed twice or more - you should ignore it.'
    )
    group_id: int = Field(
        None,
        description=''
    )
    secret: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: "CallbackType" = Field(
        None,
        description=''
    )


class CallbackBoardPostDelete(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    topic_id: int = Field(
        None,
        description=''
    )
    topic_owner_id: int = Field(
        None,
        description=''
    )


class CallbackConfirmation(CallbackBase):
    type: typing.Optional["CallbackType"] = Field(
        None,
        description=''
    )


class CallbackDonutMoneyWithdraw(BaseModel):
    amount: float = Field(
        None,
        description=''
    )
    amount_without_fee: float = Field(
        None,
        description=''
    )


class CallbackDonutMoneyWithdrawError(BaseModel):
    reason: str = Field(
        None,
        description=''
    )


class CallbackDonutSubscriptionCancelled(BaseModel):
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackDonutSubscriptionCreate(BaseModel):
    amount: int = Field(
        None,
        description=''
    )
    amount_without_fee: float = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackDonutSubscriptionExpired(BaseModel):
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    amount_diff: typing.Optional[float] = Field(
        None,
        description=''
    )
    amount_diff_without_fee: typing.Optional[float] = Field(
        None,
        description=''
    )
    amount_new: int = Field(
        None,
        description=''
    )
    amount_old: int = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackDonutSubscriptionProlonged(BaseModel):
    amount: int = Field(
        None,
        description=''
    )
    amount_without_fee: float = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackGroupChangePhoto(BaseModel):
    photo: "PhotosPhoto" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackGroupChangeSettings(BaseModel):
    self: "BaseBoolInt" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackGroupJoin(BaseModel):
    join_type: "CallbackGroupJoinType" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackGroupJoinType(enum.Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    self: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackGroupMarket(enum.IntEnum):
    disabled = 0
    open = 1


class CallbackGroupOfficerRole(enum.IntEnum):
    none = 0
    moderator = 1
    editor = 2
    administrator = 3


class CallbackGroupOfficersEdit(BaseModel):
    admin_id: int = Field(
        None,
        description=''
    )
    level_new: "CallbackGroupOfficerRole" = Field(
        None,
        description=''
    )
    level_old: "CallbackGroupOfficerRole" = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackGroupSettingsChanges(BaseModel):
    access: typing.Optional["GroupsGroupIsClosed"] = Field(
        None,
        description=''
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        None,
        description=''
    )
    description: typing.Optional[str] = Field(
        None,
        description=''
    )
    enable_audio: typing.Optional["GroupsGroupAudio"] = Field(
        None,
        description=''
    )
    enable_market: typing.Optional["CallbackGroupMarket"] = Field(
        None,
        description=''
    )
    enable_photo: typing.Optional["GroupsGroupPhotos"] = Field(
        None,
        description=''
    )
    enable_status_default: typing.Optional["GroupsGroupWall"] = Field(
        None,
        description=''
    )
    enable_video: typing.Optional["GroupsGroupVideo"] = Field(
        None,
        description=''
    )
    public_category: typing.Optional[int] = Field(
        None,
        description=''
    )
    public_subcategory: typing.Optional[int] = Field(
        None,
        description=''
    )
    screen_name: typing.Optional[str] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )
    website: typing.Optional[str] = Field(
        None,
        description=''
    )


class CallbackLikeAddRemoveObjectType(enum.Enum):
    VIDEO = "video"
    PHOTO = "photo"
    POST = "post"
    COMMENT = "comment"
    NOTE = "note"
    TOPIC_COMMENT = "topic_comment"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    MARKET = "market"
    MARKET_COMMENT = "market_comment"


class CallbackLikeAddRemove(BaseModel):
    liker_id: int = Field(
        None,
        description=''
    )
    object_id: int = Field(
        None,
        description=''
    )
    object_owner_id: int = Field(
        None,
        description=''
    )
    object_type: typing.Optional["CallbackLikeAddRemoveObjectType"] = Field(
        None,
        description=''
    )
    post_id: int = Field(
        None,
        description=''
    )
    thread_reply_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class CallbackMarketComment(BaseModel):
    date: int = Field(
        None,
        description=''
    )
    from_id: int = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    market_owner_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    photo_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description=''
    )


class CallbackMarketCommentDelete(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    item_id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackMessageAllow(CallbackBase):
    object: "CallbackMessageAllowObject" = Field(
        None,
        description=''
    )
    type: typing.Optional["CallbackType"] = Field(
        None,
        description=''
    )


class CallbackMessageAllowObject(BaseModel):
    key: str = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackMessageDeny(BaseModel):
    user_id: int = Field(
        None,
        description=''
    )


class CallbackMessageEdit(CallbackBase):
    object: "MessagesMessage" = Field(
        None,
        description=''
    )
    type: typing.Optional["CallbackType"] = Field(
        None,
        description=''
    )


class CallbackMessageNew(CallbackBase):
    object: "CallbackMessageObject" = Field(
        None,
        description=''
    )
    type: typing.Optional["CallbackType"] = Field(
        None,
        description=''
    )


class CallbackMessageObject(BaseModel):
    client_info: typing.Optional["ClientInfoForBots"] = Field(
        None,
        description=''
    )
    message: typing.Optional["MessagesMessage"] = Field(
        None,
        description=''
    )


class CallbackMessageReply(CallbackBase):
    object: "MessagesMessage" = Field(
        None,
        description=''
    )
    type: typing.Optional["CallbackType"] = Field(
        None,
        description=''
    )


class CallbackPhotoComment(BaseModel):
    date: int = Field(
        None,
        description=''
    )
    from_id: int = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    photo_owner_id: int = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description=''
    )


class CallbackPhotoCommentDelete(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    photo_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackPollVoteNew(BaseModel):
    option_id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    poll_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackQrScan(BaseModel):
    data: str = Field(
        None,
        description=''
    )
    reread: bool = Field(
        None,
        description=''
    )
    subtype: str = Field(
        None,
        description=''
    )
    type: str = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackType(enum.Enum):
    AUDIO_NEW = "audio_new"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    CONFIRMATION = "confirmation"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


class CallbackUserBlock(BaseModel):
    admin_id: int = Field(
        None,
        description=''
    )
    comment: typing.Optional[str] = Field(
        None,
        description=''
    )
    reason: int = Field(
        None,
        description=''
    )
    unblock_date: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackUserUnblock(BaseModel):
    admin_id: int = Field(
        None,
        description=''
    )
    by_end_date: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallbackVideoComment(BaseModel):
    date: int = Field(
        None,
        description=''
    )
    from_id: int = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description=''
    )
    video_owner_id: int = Field(
        None,
        description=''
    )


class CallbackVideoCommentDelete(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )
    video_id: int = Field(
        None,
        description=''
    )


class CallbackWallCommentDelete(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    post_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class CallsCall(BaseModel):
    duration: typing.Optional[int] = Field(
        None,
        description='Call duration'
    )
    initiator_id: int = Field(
        None,
        description='Caller initiator'
    )
    participants: typing.Optional["CallsParticipants"] = Field(
        None,
        description=''
    )
    receiver_id: int = Field(
        None,
        description='Caller receiver'
    )
    state: "CallsEndState" = Field(
        None,
        description=''
    )
    time: int = Field(
        None,
        description='Timestamp for call'
    )
    video: typing.Optional[bool] = Field(
        None,
        description='Was this call initiated as video call'
    )


class CallsEndState(enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Participants count'
    )
    list: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )


class ClientInfoForBots(BaseModel):
    button_actions: typing.Optional[typing.List["MessagesTemplateActionTypeNames"]] = Field(
        None,
        description=''
    )
    carousel: typing.Optional[bool] = Field(
        None,
        description='client has support carousel'
    )
    inline_keyboard: typing.Optional[bool] = Field(
        None,
        description='client has support inline keyboard'
    )
    keyboard: typing.Optional[bool] = Field(
        None,
        description='client has support keyboard'
    )
    lang_id: typing.Optional[int] = Field(
        None,
        description='client or user language id'
    )


class CommentThread(BaseModel):
    can_post: typing.Optional[bool] = Field(
        None,
        description='Information whether current user can comment the post'
    )
    count: int = Field(
        None,
        description='Comments number'
    )
    groups_can_post: typing.Optional[bool] = Field(
        None,
        description='Information whether groups can comment the post'
    )
    items: typing.Optional[typing.List["WallWallComment"]] = Field(
        None,
        description=''
    )
    show_reply_button: typing.Optional[bool] = Field(
        None,
        description='Information whether recommended to display reply button'
    )


class DatabaseCity(BaseObject):
    area: typing.Optional[str] = Field(
        None,
        description='Area title'
    )
    important: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the city is included in important cities list'
    )
    region: typing.Optional[str] = Field(
        None,
        description='Region title'
    )


class DatabaseCityById(BaseObject):
    pass


class DatabaseFaculty(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Faculty ID'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Faculty title'
    )


class DatabaseRegion(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Region ID'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Region title'
    )


class DatabaseSchool(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='School ID'
    )
    title: typing.Optional[str] = Field(
        None,
        description='School title'
    )


class DatabaseStation(BaseModel):
    city_id: typing.Optional[int] = Field(
        None,
        description='City ID'
    )
    color: typing.Optional[str] = Field(
        None,
        description='Hex color code without #'
    )
    id: int = Field(
        None,
        description='Station ID'
    )
    name: str = Field(
        None,
        description='Station name'
    )


class DatabaseUniversity(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='University ID'
    )
    title: typing.Optional[str] = Field(
        None,
        description='University title'
    )


class DocsDoc(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the document'
    )
    date: int = Field(
        None,
        description='Date when file has been uploaded in Unixtime'
    )
    ext: str = Field(
        None,
        description='File extension'
    )
    id: int = Field(
        None,
        description='Document ID'
    )
    is_licensed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description='Document owner ID'
    )
    preview: typing.Optional["DocsDocPreview"] = Field(
        None,
        description=''
    )
    size: int = Field(
        None,
        description='File size in bites'
    )
    tags: typing.Optional[typing.List[str]] = Field(
        None,
        description='Document tags'
    )
    title: str = Field(
        None,
        description='Document title'
    )
    type: int = Field(
        None,
        description='Document type'
    )
    url: typing.Optional[str] = Field(
        None,
        description='File URL'
    )


class DocsDocAttachmentType(enum.Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = Field(
        None,
        description=''
    )
    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["DocsDocPreviewPhoto"] = Field(
        None,
        description=''
    )
    video: typing.Optional["DocsDocPreviewVideo"] = Field(
        None,
        description=''
    )


class DocsDocPreviewAudioMsg(BaseModel):
    duration: int = Field(
        None,
        description='Audio message duration in seconds'
    )
    link_mp3: str = Field(
        None,
        description='MP3 file URL'
    )
    link_ogg: str = Field(
        None,
        description='OGG file URL'
    )
    waveform: typing.List[int] = Field(
        None,
        description=''
    )


class DocsDocPreviewGraffiti(BaseModel):
    height: int = Field(
        None,
        description='Graffiti height'
    )
    src: str = Field(
        None,
        description='Graffiti file URL'
    )
    width: int = Field(
        None,
        description='Graffiti width'
    )


class DocsDocPreviewPhoto(BaseModel):
    sizes: typing.Optional[typing.List["DocsDocPreviewPhotoSizes"]] = Field(
        None,
        description=''
    )


class DocsDocPreviewPhotoSizes(BaseModel):
    height: int = Field(
        None,
        description='Height in px'
    )
    src: str = Field(
        None,
        description='URL of the image'
    )
    type: "PhotosPhotoSizesType" = Field(
        None,
        description=''
    )
    width: int = Field(
        None,
        description='Width in px'
    )


class DocsDocPreviewVideo(BaseModel):
    file_size: int = Field(
        None,
        description='Video file size in bites'
    )
    height: int = Field(
        None,
        description='Videos height in pixels'
    )
    src: str = Field(
        None,
        description='Video URL'
    )
    width: int = Field(
        None,
        description='Videos width in pixels'
    )


class DocsDocTypes(BaseModel):
    count: int = Field(
        None,
        description='Number of docs'
    )
    id: int = Field(
        None,
        description='Doc type ID'
    )
    name: str = Field(
        None,
        description='Doc type title'
    )


class DonutDonatorSubscriptionInfoStatus(enum.Enum):
    ACTIVE = "active"
    EXPIRING = "expiring"


class DonutDonatorSubscriptionInfo(BaseModel):
    amount: int = Field(
        None,
        description=''
    )
    next_payment_date: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    status: typing.Optional["DonutDonatorSubscriptionInfoStatus"] = Field(
        None,
        description=''
    )


class EventsEventAttach(BaseModel):
    address: typing.Optional[str] = Field(
        None,
        description='address of event'
    )
    button_text: str = Field(
        None,
        description='text of attach'
    )
    friends: typing.List[int] = Field(
        None,
        description='array of friends ids'
    )
    id: int = Field(
        None,
        description='event ID'
    )
    is_favorite: bool = Field(
        None,
        description='is favorite'
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        None,
        description='Current users member status'
    )
    text: str = Field(
        None,
        description='text of attach'
    )
    time: typing.Optional[int] = Field(
        None,
        description='event start time'
    )


class FaveBookmark(BaseModel):
    added_date: int = Field(
        None,
        description='Timestamp, when this item was bookmarked'
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    post: typing.Optional["WallWallpostFull"] = Field(
        None,
        description=''
    )
    product: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    seen: bool = Field(
        None,
        description='Has user seen this item'
    )
    tags: typing.List["FaveTag"] = Field(
        None,
        description=''
    )
    type: "FaveBookmarkType" = Field(
        None,
        description='Item type'
    )
    video: typing.Optional["VideoVideoFull"] = Field(
        None,
        description=''
    )


class FaveBookmarkType(enum.Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(BaseModel):
    description: str = Field(
        None,
        description='Some info about user or group'
    )
    group: typing.Optional["GroupsGroupFull"] = Field(
        None,
        description=''
    )
    tags: typing.List["FaveTag"] = Field(
        None,
        description=''
    )
    type: "FavePageType" = Field(
        None,
        description='Item type'
    )
    updated_date: typing.Optional[int] = Field(
        None,
        description='Timestamp, when this page was bookmarked'
    )
    user: typing.Optional["UsersUserFull"] = Field(
        None,
        description=''
    )


class FavePageType(enum.Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Tag id'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Tag name'
    )


class FriendsFriendStatus(BaseModel):
    friend_status: "FriendsFriendStatusStatus" = Field(
        None,
        description=''
    )
    sign: typing.Optional[str] = Field(
        None,
        description='MD5 hash for the result validation'
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    is_request_unread: typing.Optional[bool] = Field(
        None,
        description='Is friend request from other user unread'
    )


class FriendsFriendStatusStatus(enum.IntEnum):
    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3


class FriendsFriendsList(BaseModel):
    id: int = Field(
        None,
        description='List ID'
    )
    name: str = Field(
        None,
        description='List title'
    )


class FriendsMutualFriend(BaseModel):
    common_count: typing.Optional[int] = Field(
        None,
        description='Total mutual friends number'
    )
    common_friends: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class FriendsRequests(BaseModel):
    _from: typing.Optional[str] = Field(
        None,
        description='ID of the user by whom friend has been suggested'
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class FriendsRequestsMutual(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Total mutual friends number'
    )
    users: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )


class FriendsRequestsXtrMessage(BaseModel):
    _from: typing.Optional[str] = Field(
        None,
        description='ID of the user by whom friend has been suggested'
    )
    message: typing.Optional[str] = Field(
        None,
        description='Message sent with a request'
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class UsersUser(UsersUserMin):
    friend_status: typing.Optional["FriendsFriendStatusStatus"] = Field(
        None,
        description=''
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        None,
        description=''
    )
    online: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user is online'
    )
    online_app: typing.Optional[int] = Field(
        None,
        description='Application ID'
    )
    online_info: typing.Optional["UsersOnlineInfo"] = Field(
        None,
        description=''
    )
    online_mobile: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user is online in mobile site or application'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the user with 100 pixels in width'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the user with 50 pixels in width'
    )
    screen_name: typing.Optional[str] = Field(
        None,
        description='Domain name of the users page'
    )
    sex: typing.Optional["BaseSex"] = Field(
        None,
        description='User sex'
    )
    trending: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user has a "fire" pictogram.'
    )
    verified: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user is verified'
    )


class UsersUserFull(UsersUser):
    about: typing.Optional[str] = Field(
        None,
        description=''
    )
    access_key: typing.Optional[str] = Field(
        None,
        description=''
    )
    activities: typing.Optional[str] = Field(
        None,
        description=''
    )
    activity: typing.Optional[str] = Field(
        None,
        description='Users status'
    )
    bdate: typing.Optional[str] = Field(
        None,
        description='Users date of birth'
    )
    blacklisted: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user is in the requested users blacklist.'
    )
    blacklisted_by_me: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the requested user is in current users blacklist'
    )
    books: typing.Optional[str] = Field(
        None,
        description=''
    )
    can_be_invited_group: typing.Optional[bool] = Field(
        None,
        description='Information whether current user can be invited to the community'
    )
    can_call: typing.Optional[bool] = Field(
        None,
        description='Information whether current user can call'
    )
    can_call_from_group: typing.Optional[bool] = Field(
        None,
        description='Information whether group can call user'
    )
    can_post: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can post on the users wall'
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can see other users audio on the wall'
    )
    can_see_audio: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can see the users audio'
    )
    can_see_gifts: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can see the users gifts'
    )
    can_see_wishes: typing.Optional[bool] = Field(
        None,
        description='Information whether current user can see the users wishes'
    )
    can_send_friend_request: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can send a friend request'
    )
    can_subscribe_podcasts: typing.Optional[bool] = Field(
        None,
        description='Owner in whitelist or not'
    )
    can_subscribe_posts: typing.Optional[bool] = Field(
        None,
        description='Can subscribe to wall'
    )
    can_upload_doc: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    can_write_private_message: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can write private message'
    )
    career: typing.Optional[typing.List["UsersCareer"]] = Field(
        None,
        description=''
    )
    city: typing.Optional["BaseCity"] = Field(
        None,
        description=''
    )
    clips_count: typing.Optional[int] = Field(
        None,
        description='Number of users clips'
    )
    common_count: typing.Optional[int] = Field(
        None,
        description='Number of common friends with current user'
    )
    contact_id: typing.Optional[int] = Field(
        None,
        description='Contact person ID'
    )
    contact_name: typing.Optional[str] = Field(
        None,
        description='User contact name'
    )
    counters: typing.Optional["UsersUserCounters"] = Field(
        None,
        description=''
    )
    country: typing.Optional["BaseCountry"] = Field(
        None,
        description=''
    )
    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        None,
        description=''
    )
    descriptions: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    domain: typing.Optional[str] = Field(
        None,
        description='Domain name of the users page'
    )
    education_form: typing.Optional[str] = Field(
        None,
        description='Education form'
    )
    education_status: typing.Optional[str] = Field(
        None,
        description='Users education status'
    )
    email: typing.Optional[str] = Field(
        None,
        description=''
    )
    exports: typing.Optional["UsersExports"] = Field(
        None,
        description=''
    )
    facebook: typing.Optional[str] = Field(
        None,
        description=''
    )
    facebook_name: typing.Optional[str] = Field(
        None,
        description=''
    )
    faculty: typing.Optional[int] = Field(
        None,
        description='Faculty ID'
    )
    faculty_name: typing.Optional[str] = Field(
        None,
        description='Faculty name'
    )
    first_name_abl: typing.Optional[str] = Field(
        None,
        description='Users first name in prepositional case'
    )
    first_name_acc: typing.Optional[str] = Field(
        None,
        description='Users first name in accusative case'
    )
    first_name_dat: typing.Optional[str] = Field(
        None,
        description='Users first name in dative case'
    )
    first_name_gen: typing.Optional[str] = Field(
        None,
        description='Users first name in genitive case'
    )
    first_name_ins: typing.Optional[str] = Field(
        None,
        description='Users first name in instrumental case'
    )
    first_name_nom: typing.Optional[str] = Field(
        None,
        description='Users first name in nominative case'
    )
    followers_count: typing.Optional[int] = Field(
        None,
        description='Number of users followers'
    )
    games: typing.Optional[str] = Field(
        None,
        description=''
    )
    graduation: typing.Optional[int] = Field(
        None,
        description='Graduation year'
    )
    has_mobile: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user specified his phone number'
    )
    has_photo: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user has main photo'
    )
    has_unseen_stories: typing.Optional[bool] = Field(
        None,
        description=''
    )
    hash: typing.Optional[str] = Field(
        None,
        description=''
    )
    home_phone: typing.Optional[str] = Field(
        None,
        description='Users additional phone number'
    )
    home_town: typing.Optional[str] = Field(
        None,
        description='User hometown'
    )
    instagram: typing.Optional[str] = Field(
        None,
        description=''
    )
    interests: typing.Optional[str] = Field(
        None,
        description=''
    )
    is_favorite: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the requested user is in faves of current user'
    )
    is_friend: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the user is a friend of current user'
    )
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the requested user is hidden from current users newsfeed'
    )
    is_message_request: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_no_index: typing.Optional[bool] = Field(
        None,
        description='Access to user profile is restricted for search engines'
    )
    is_service: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_subscribed_podcasts: typing.Optional[bool] = Field(
        None,
        description='Information whether current user is subscribed to podcasts'
    )
    is_video_live_notifications_blocked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    language: typing.Optional[str] = Field(
        None,
        description=''
    )
    last_name_abl: typing.Optional[str] = Field(
        None,
        description='Users last name in prepositional case'
    )
    last_name_acc: typing.Optional[str] = Field(
        None,
        description='Users last name in accusative case'
    )
    last_name_dat: typing.Optional[str] = Field(
        None,
        description='Users last name in dative case'
    )
    last_name_gen: typing.Optional[str] = Field(
        None,
        description='Users last name in genitive case'
    )
    last_name_ins: typing.Optional[str] = Field(
        None,
        description='Users last name in instrumental case'
    )
    last_name_nom: typing.Optional[str] = Field(
        None,
        description='Users last name in nominative case'
    )
    last_seen: typing.Optional["UsersLastSeen"] = Field(
        None,
        description=''
    )
    lists: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    livejournal: typing.Optional[str] = Field(
        None,
        description=''
    )
    maiden_name: typing.Optional[str] = Field(
        None,
        description='User maiden name'
    )
    military: typing.Optional[typing.List["UsersMilitary"]] = Field(
        None,
        description=''
    )
    mobile_phone: typing.Optional[str] = Field(
        None,
        description='Users mobile phone number'
    )
    movies: typing.Optional[str] = Field(
        None,
        description=''
    )
    music: typing.Optional[str] = Field(
        None,
        description=''
    )
    nickname: typing.Optional[str] = Field(
        None,
        description='User nickname'
    )
    occupation: typing.Optional["UsersOccupation"] = Field(
        None,
        description=''
    )
    owner_state: typing.Optional["OwnerState"] = Field(
        None,
        description=''
    )
    personal: typing.Optional["UsersPersonal"] = Field(
        None,
        description=''
    )
    photo: typing.Optional[str] = Field(
        None,
        description=''
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the user with 200 pixels in width'
    )
    photo_200_orig: typing.Optional[str] = Field(
        None,
        description='URL of users photo with 200 pixels in width'
    )
    photo_400: typing.Optional[str] = Field(
        None,
        description=''
    )
    photo_400_orig: typing.Optional[str] = Field(
        None,
        description='URL of users photo with 400 pixels in width'
    )
    photo_big: typing.Optional[str] = Field(
        None,
        description=''
    )
    photo_id: typing.Optional[str] = Field(
        None,
        description='ID of the users main photo'
    )
    photo_max: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the user with maximum width'
    )
    photo_max_orig: typing.Optional[str] = Field(
        None,
        description='URL of users photo of maximum size'
    )
    photo_max_size: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    photo_medium: typing.Optional["PhotosPhotoFalseable"] = Field(
        None,
        description=''
    )
    photo_medium_rec: typing.Optional["PhotosPhotoFalseable"] = Field(
        None,
        description=''
    )
    photo_rec: typing.Optional["PhotosPhotoFalseable"] = Field(
        None,
        description=''
    )
    quotes: typing.Optional[str] = Field(
        None,
        description=''
    )
    relation: typing.Optional["UsersUserRelation"] = Field(
        None,
        description='User relationship status'
    )
    relation_partner: typing.Optional["UsersUserMin"] = Field(
        None,
        description=''
    )
    relatives: typing.Optional[typing.List["UsersRelative"]] = Field(
        None,
        description=''
    )
    schools: typing.Optional[typing.List["UsersSchool"]] = Field(
        None,
        description=''
    )
    service_description: typing.Optional[str] = Field(
        None,
        description=''
    )
    site: typing.Optional[str] = Field(
        None,
        description='Users website'
    )
    skype: typing.Optional[str] = Field(
        None,
        description=''
    )
    status: typing.Optional[str] = Field(
        None,
        description='Users status'
    )
    status_audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    stories_archive_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    test: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    timezone: typing.Optional[float] = Field(
        None,
        description='Users timezone'
    )
    tv: typing.Optional[str] = Field(
        None,
        description=''
    )
    twitter: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional["UsersUserType"] = Field(
        None,
        description=''
    )
    universities: typing.Optional[typing.List["UsersUniversity"]] = Field(
        None,
        description=''
    )
    university: typing.Optional[int] = Field(
        None,
        description='University ID'
    )
    university_group_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    university_name: typing.Optional[str] = Field(
        None,
        description='University name'
    )
    video_live: typing.Optional["VideoLiveInfo"] = Field(
        None,
        description=''
    )
    video_live_count: typing.Optional[int] = Field(
        None,
        description='Number of users live streams'
    )
    video_live_level: typing.Optional[int] = Field(
        None,
        description='User level in live streams achievements'
    )
    wall_comments: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment wall posts'
    )
    wall_default: typing.Optional[str] = Field(
        None,
        description=''
    )


class FriendsUserXtrPhone(UsersUserFull):
    phone: typing.Optional[str] = Field(
        None,
        description='User phone'
    )


class GiftsGift(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Date when gist has been sent in Unixtime'
    )
    from_id: typing.Optional[int] = Field(
        None,
        description='Gift sender ID'
    )
    gift: typing.Optional["GiftsLayout"] = Field(
        None,
        description=''
    )
    gift_hash: typing.Optional[str] = Field(
        None,
        description='Hash'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Gift ID'
    )
    message: typing.Optional[str] = Field(
        None,
        description='Comment text'
    )
    privacy: typing.Optional["GiftsGiftPrivacy"] = Field(
        None,
        description=''
    )


class GiftsGiftPrivacy(enum.IntEnum):
    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2


class GiftsLayout(BaseModel):
    build_id: typing.Optional[str] = Field(
        None,
        description='ID of the build of constructor gift'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Gift ID'
    )
    is_stickers_style: typing.Optional[bool] = Field(
        None,
        description='Information whether gift represents a stickers style'
    )
    keywords: typing.Optional[str] = Field(
        None,
        description='Keywords used for search'
    )
    stickers_product_id: typing.Optional[int] = Field(
        None,
        description='ID of the sticker pack, if the gift is representing one'
    )
    thumb_256: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 256 px in width'
    )
    thumb_48: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 48 px in width'
    )
    thumb_512: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 512 px in width'
    )
    thumb_96: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 96 px in width'
    )


class GroupsAddress(BaseModel):
    additional_address: typing.Optional[str] = Field(
        None,
        description='Additional address to the place (6 floor, left door)'
    )
    address: typing.Optional[str] = Field(
        None,
        description='String address to the place (Nevsky, 28)'
    )
    city_id: typing.Optional[int] = Field(
        None,
        description='City id of address'
    )
    country_id: typing.Optional[int] = Field(
        None,
        description='Country id of address'
    )
    distance: typing.Optional[int] = Field(
        None,
        description='Distance from the point'
    )
    id: int = Field(
        None,
        description='Address id'
    )
    latitude: typing.Optional[float] = Field(
        None,
        description='Address latitude'
    )
    longitude: typing.Optional[float] = Field(
        None,
        description='Address longitude'
    )
    metro_station_id: typing.Optional[int] = Field(
        None,
        description='Metro id of address'
    )
    phone: typing.Optional[str] = Field(
        None,
        description='Address phone'
    )
    place_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    time_offset: typing.Optional[int] = Field(
        None,
        description='Time offset int minutes from utc time'
    )
    timetable: typing.Optional["GroupsAddressTimetable"] = Field(
        None,
        description='Week timetable for the address'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Title of the place (Zinger, etc)'
    )
    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = Field(
        None,
        description='Status of information about timetable'
    )


class GroupsAddressTimetable(BaseModel):
    fri: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for friday'
    )
    mon: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for monday'
    )
    sat: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for saturday'
    )
    sun: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for sunday'
    )
    thu: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for thursday'
    )
    tue: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for tuesday'
    )
    wed: typing.Optional["GroupsAddressTimetableDay"] = Field(
        None,
        description='Timetable for wednesday'
    )


class GroupsAddressTimetableDay(BaseModel):
    break_close_time: typing.Optional[int] = Field(
        None,
        description='Close time of the break in minutes'
    )
    break_open_time: typing.Optional[int] = Field(
        None,
        description='Start time of the break in minutes'
    )
    close_time: int = Field(
        None,
        description='Close time in minutes'
    )
    open_time: int = Field(
        None,
        description='Open time in minutes'
    )


class GroupsAddressWorkInfoStatus(enum.Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
    is_enabled: bool = Field(
        None,
        description='Information whether addresses is enabled'
    )
    main_address_id: typing.Optional[int] = Field(
        None,
        description='Main address id for group'
    )


class GroupsBanInfo(BaseModel):
    admin_id: typing.Optional[int] = Field(
        None,
        description='Administrator ID'
    )
    comment: typing.Optional[str] = Field(
        None,
        description='Comment for a ban'
    )
    comment_visible: typing.Optional[bool] = Field(
        None,
        description='Show comment for user'
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when user has been added to blacklist in Unixtime'
    )
    end_date: typing.Optional[int] = Field(
        None,
        description='Date when user will be removed from blacklist in Unixtime'
    )
    is_closed: typing.Optional[bool] = Field(
        None,
        description=''
    )
    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        None,
        description=''
    )


class GroupsBanInfoReason(enum.IntEnum):
    other = 0
    spam = 1
    verbal_abuse = 2
    strong_language = 3
    flood = 4


class GroupsOwnerXtrBanInfo(BaseModel):
    ban_info: typing.Optional["GroupsBanInfo"] = Field(
        None,
        description=''
    )
    group: typing.Optional["GroupsGroup"] = Field(
        None,
        description='Information about group if type = group'
    )
    profile: typing.Optional["UsersUser"] = Field(
        None,
        description='Information about group if type = profile'
    )
    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = Field(
        None,
        description=''
    )


class GroupsBannedItem(GroupsOwnerXtrBanInfo):
    pass


class GroupsCallbackServerStatus(enum.Enum):
    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class GroupsCallbackServer(BaseModel):
    creator_id: int = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    secret_key: str = Field(
        None,
        description=''
    )
    status: typing.Optional["GroupsCallbackServerStatus"] = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description=''
    )
    url: str = Field(
        None,
        description=''
    )


class GroupsCallbackSettings(BaseModel):
    api_version: typing.Optional[str] = Field(
        None,
        description='API version used for the events'
    )
    events: typing.Optional["GroupsLongPollEvents"] = Field(
        None,
        description=''
    )


class GroupsContactsItem(BaseModel):
    desc: typing.Optional[str] = Field(
        None,
        description='Contact description'
    )
    email: typing.Optional[str] = Field(
        None,
        description='Contact email'
    )
    phone: typing.Optional[str] = Field(
        None,
        description='Contact phone'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class GroupsCountersGroup(BaseModel):
    addresses: typing.Optional[int] = Field(
        None,
        description='Addresses number'
    )
    albums: typing.Optional[int] = Field(
        None,
        description='Photo albums number'
    )
    articles: typing.Optional[int] = Field(
        None,
        description='Articles number'
    )
    audio_playlists: typing.Optional[int] = Field(
        None,
        description='Audio playlists number'
    )
    audios: typing.Optional[int] = Field(
        None,
        description='Audios number'
    )
    clips: typing.Optional[int] = Field(
        None,
        description='Clips number'
    )
    clips_followers: typing.Optional[int] = Field(
        None,
        description='Clips followers number'
    )
    docs: typing.Optional[int] = Field(
        None,
        description='Docs number'
    )
    market: typing.Optional[int] = Field(
        None,
        description='Market items number'
    )
    market_services: typing.Optional[int] = Field(
        None,
        description='Market services number'
    )
    narratives: typing.Optional[int] = Field(
        None,
        description='Narratives number'
    )
    photos: typing.Optional[int] = Field(
        None,
        description='Photos number'
    )
    podcasts: typing.Optional[int] = Field(
        None,
        description='Podcasts number'
    )
    topics: typing.Optional[int] = Field(
        None,
        description='Topics number'
    )
    videos: typing.Optional[int] = Field(
        None,
        description='Videos number'
    )


class GroupsCover(BaseModel):
    enabled: "BaseBoolInt" = Field(
        None,
        description='Information whether cover is enabled'
    )
    images: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description=''
    )


class GroupsFields(enum.Enum):
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    REQUESTS_COUNT = "requests_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SUGGEST = "can_suggest"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_UPLOAD_CLIP = "can_upload_clip"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_CREATE_TOPIC = "can_create_topic"
    CROP_PHOTO = "crop_photo"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    WALL = "wall"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    HAS_GROUP_CHANNEL = "has_group_channel"
    GROUP_CHANNEL = "group_channel"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    IS_BUSINESS = "is_business"
    TEXTLIVES_COUNT = "textlives_count"
    MEMBERS_COUNT_TEXT = "members_count_text"


class GroupsFilter(enum.Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
    admin_level: typing.Optional["GroupsGroupAdminLevel"] = Field(
        None,
        description=''
    )
    deactivated: typing.Optional[str] = Field(
        None,
        description='Information whether community is banned'
    )
    est_date: typing.Optional[str] = Field(
        None,
        description='Established date'
    )
    finish_date: typing.Optional[int] = Field(
        None,
        description='Finish date in Unixtime format'
    )
    id: int = Field(
        None,
        description='Community ID'
    )
    is_admin: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user is administrator'
    )
    is_advertiser: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user is advertiser'
    )
    is_closed: typing.Optional["GroupsGroupIsClosed"] = Field(
        None,
        description=''
    )
    is_member: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user is member'
    )
    is_video_live_notifications_blocked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    name: typing.Optional[str] = Field(
        None,
        description='Community name'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 100 pixels in width'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 200 pixels in width'
    )
    photo_200_orig: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 200 pixels in width original'
    )
    photo_400: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 400 pixels in width'
    )
    photo_400_orig: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 400 pixels in width original'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with 50 pixels in width'
    )
    photo_max: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with max pixels in width'
    )
    photo_max_orig: typing.Optional[str] = Field(
        None,
        description='URL of square photo of the community with max pixels in width original'
    )
    photo_max_size: typing.Optional["GroupsPhotoSize"] = Field(
        None,
        description=''
    )
    public_date_label: typing.Optional[str] = Field(
        None,
        description='Public date label'
    )
    screen_name: typing.Optional[str] = Field(
        None,
        description='Domain of the community page'
    )
    start_date: typing.Optional[int] = Field(
        None,
        description='Start date in Unixtime format'
    )
    type: typing.Optional["GroupsGroupType"] = Field(
        None,
        description=''
    )
    video_live: typing.Optional["VideoLiveInfo"] = Field(
        None,
        description=''
    )


class GroupsGroupAccess(enum.IntEnum):
    open = 0
    closed = 1
    private = 2


class GroupsGroupAdminLevel(enum.IntEnum):
    moderator = 1
    editor = 2
    administrator = 3


class GroupsGroupAgeLimits(enum.IntEnum):
    unlimited = 1
    _16_plus = 2
    _18_plus = 3


class GroupsGroupAttach(BaseModel):
    id: int = Field(
        None,
        description='group ID'
    )
    is_favorite: bool = Field(
        None,
        description='is favorite'
    )
    size: int = Field(
        None,
        description='size of group'
    )
    status: str = Field(
        None,
        description='activity or category of group'
    )
    text: str = Field(
        None,
        description='text of attach'
    )


class GroupsGroupAudio(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupBanInfo(BaseModel):
    comment: typing.Optional[str] = Field(
        None,
        description='Ban comment'
    )
    end_date: typing.Optional[int] = Field(
        None,
        description='End date of ban in Unixtime'
    )
    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        None,
        description=''
    )


class GroupsGroupCategory(BaseModel):
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = Field(
        None,
        description=''
    )


class GroupsGroupCategoryFull(BaseModel):
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )
    page_count: int = Field(
        None,
        description='Pages number'
    )
    page_previews: typing.List["GroupsGroup"] = Field(
        None,
        description=''
    )
    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = Field(
        None,
        description=''
    )


class GroupsGroupCategoryType(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    name: str = Field(
        None,
        description=''
    )


class GroupsGroupDocs(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupFull(GroupsGroup):
    activity: typing.Optional[str] = Field(
        None,
        description='Type of group, start date of event or category of public page'
    )
    addresses: typing.Optional["GroupsAddressesInfo"] = Field(
        None,
        description='Info about addresses in groups'
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        None,
        description='Information whether age limit'
    )
    ban_info: typing.Optional["GroupsGroupBanInfo"] = Field(
        None,
        description='User ban info'
    )
    can_create_topic: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can create topic'
    )
    can_message: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can send a message to community'
    )
    can_post: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can post on communitys wall'
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can see all posts on communitys wall'
    )
    can_send_notify: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community can send notifications by phone number to current user'
    )
    can_subscribe_podcasts: typing.Optional[bool] = Field(
        None,
        description='Owner in whitelist or not'
    )
    can_subscribe_posts: typing.Optional[bool] = Field(
        None,
        description='Can subscribe to wall'
    )
    can_suggest: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    can_upload_doc: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can upload doc'
    )
    can_upload_story: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can upload story'
    )
    can_upload_video: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can upload video'
    )
    city: typing.Optional["BaseObject"] = Field(
        None,
        description=''
    )
    clips_count: typing.Optional[int] = Field(
        None,
        description='Number of communitys clips'
    )
    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = Field(
        None,
        description=''
    )
    counters: typing.Optional["GroupsCountersGroup"] = Field(
        None,
        description=''
    )
    country: typing.Optional["BaseCountry"] = Field(
        None,
        description=''
    )
    cover: typing.Optional["GroupsCover"] = Field(
        None,
        description=''
    )
    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        None,
        description='Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Community description'
    )
    fixed_post: typing.Optional[int] = Field(
        None,
        description='Fixed post ID'
    )
    has_group_channel: typing.Optional[bool] = Field(
        None,
        description=''
    )
    has_market_app: typing.Optional[bool] = Field(
        None,
        description='Information whether community has installed market app'
    )
    has_photo: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community has photo'
    )
    has_unseen_stories: typing.Optional[bool] = Field(
        None,
        description=''
    )
    invited_by: typing.Optional[int] = Field(
        None,
        description='Inviter ID'
    )
    is_adult: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community is adult'
    )
    is_favorite: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community is in faves'
    )
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community is hidden from current users newsfeed'
    )
    is_messages_blocked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community can send a message to current user'
    )
    is_subscribed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user is subscribed'
    )
    is_subscribed_podcasts: typing.Optional[bool] = Field(
        None,
        description='Information whether current user is subscribed to podcasts'
    )
    links: typing.Optional[typing.List["GroupsLinksItem"]] = Field(
        None,
        description=''
    )
    live_covers: typing.Optional["GroupsLiveCovers"] = Field(
        None,
        description='Live covers state'
    )
    main_album_id: typing.Optional[int] = Field(
        None,
        description='Communitys main photo album ID'
    )
    main_section: typing.Optional["GroupsGroupFullSection"] = Field(
        None,
        description=''
    )
    market: typing.Optional["GroupsMarketInfo"] = Field(
        None,
        description=''
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        None,
        description='Current users member status'
    )
    members_count: typing.Optional[int] = Field(
        None,
        description='Community members number'
    )
    members_count_text: typing.Optional[str] = Field(
        None,
        description='Info about number of users in group'
    )
    online_status: typing.Optional["GroupsOnlineStatus"] = Field(
        None,
        description='Status of replies in community messages'
    )
    requests_count: typing.Optional[int] = Field(
        None,
        description='The number of incoming requests to the community'
    )
    secondary_section: typing.Optional["GroupsGroupFullSection"] = Field(
        None,
        description=''
    )
    site: typing.Optional[str] = Field(
        None,
        description='Communitys website'
    )
    status: typing.Optional[str] = Field(
        None,
        description='Community status'
    )
    status_audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    stories_archive_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    trending: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the community has a "fire" pictogram.'
    )
    using_vkpay_market_app: typing.Optional[bool] = Field(
        None,
        description=''
    )
    verified: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether community is verified'
    )
    video_live_count: typing.Optional[int] = Field(
        None,
        description='Number of communitys live streams'
    )
    video_live_level: typing.Optional[int] = Field(
        None,
        description='Community level live streams achievements'
    )
    wall: typing.Optional[int] = Field(
        None,
        description='Information about wall status in community'
    )
    wiki_page: typing.Optional[str] = Field(
        None,
        description='Communitys main wiki page title'
    )


class GroupsGroupFullAgeLimits(enum.IntEnum):
    no = 1
    over_16 = 2
    over_18 = 3


class GroupsGroupFullMemberStatus(enum.IntEnum):
    not_a_member = 0
    member = 1
    not_sure = 2
    declined = 3
    has_sent_a_request = 4
    invited = 5


class GroupsGroupFullSection(enum.IntEnum):
    none = 0
    photos = 1
    topics = 2
    audios = 3
    videos = 4
    market = 5
    stories = 6
    apps = 7
    followers = 8
    links = 9
    events = 10
    places = 11
    contacts = 12
    app_btns = 13
    docs = 14
    event_counters = 15
    group_messages = 16
    albums = 24
    categories = 26
    admin_help = 27
    app_widget = 31
    public_help = 32
    hs_donation_app = 33
    hs_market_app = 34
    addresses = 35
    artist_page = 36
    podcast = 37
    articles = 39
    admin_tips = 40
    menu = 41
    fixed_post = 42
    chats = 43
    evergreen_notice = 44
    musicians = 45
    narratives = 46
    donut_donate = 47
    clips = 48
    market_cart = 49
    curators = 50
    market_services = 51
    classifieds = 53
    textlives = 54
    donut_for_dons = 55
    badges = 57
    chats_creation = 58


class GroupsGroupIsClosed(enum.IntEnum):
    open = 0
    closed = 1
    private = 2


class GroupsGroupMarketCurrency(enum.IntEnum):
    russian_rubles = 643
    ukrainian_hryvnia = 980
    kazakh_tenge = 398
    euro = 978
    us_dollars = 840


class GroupsGroupPhotos(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupPublicCategoryList(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description=''
    )
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    subcategories: typing.Optional[typing.List["GroupsGroupCategoryType"]] = Field(
        None,
        description=''
    )


class GroupsGroupRole(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.IntEnum):
    auto = 1
    activity_holidays = 2
    business = 3
    pets = 4
    health = 5
    dating_and_communication = 6
    games = 7
    it = 8
    cinema = 9
    beauty_and_fashion = 10
    cooking = 11
    art_and_culture = 12
    literature = 13
    mobile_services_and_internet = 14
    music = 15
    science_and_technology = 16
    real_estate = 17
    news_and_media = 18
    security = 19
    education = 20
    home_and_renovations = 21
    politics = 22
    food = 23
    industry = 24
    travel = 25
    work = 26
    entertainment = 27
    religion = 28
    family = 29
    sports = 30
    insurance = 31
    television = 32
    goods_and_services = 33
    hobbies = 34
    finance = 35
    photo = 36
    esoterics = 37
    electronics_and_appliances = 38
    erotic = 39
    humor = 40
    society_humanities = 41
    design_and_graphics = 42


class GroupsGroupSuggestedPrivacy(enum.IntEnum):
    none = 0
    all = 1
    subscribers = 2


class GroupsGroupTagColor(enum.Enum):
    _454647 = "454647"
    _45678F = "45678f"
    _4BB34B = "4bb34b"
    _5181B8 = "5181b8"
    _539B9C = "539b9c"
    _5C9CE6 = "5c9ce6"
    _63B9BA = "63b9ba"
    _6BC76B = "6bc76b"
    _76787A = "76787a"
    _792EC0 = "792ec0"
    _7A6C4F = "7a6c4f"
    _7ECECF = "7ececf"
    _9E8D6B = "9e8d6b"
    A162DE = "a162de"
    AAAEB3 = "aaaeb3"
    BBAA84 = "bbaa84"
    E64646 = "e64646"
    FF5C5C = "ff5c5c"
    FFA000 = "ffa000"
    FFC107 = "ffc107"


class GroupsGroupTag(BaseModel):
    color: typing.Optional["GroupsGroupTagColor"] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    name: str = Field(
        None,
        description=''
    )
    uses: typing.Optional[int] = Field(
        None,
        description=''
    )


class GroupsGroupTopics(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupType(enum.Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupWall(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2
    closed = 3


class GroupsGroupWiki(enum.IntEnum):
    disabled = 0
    open = 1
    limited = 2


class GroupsGroupsArray(BaseModel):
    count: int = Field(
        None,
        description='Communities number'
    )
    items: typing.List[int] = Field(
        None,
        description=''
    )


class GroupsLinksItem(BaseModel):
    desc: typing.Optional[str] = Field(
        None,
        description='Link description'
    )
    edit_title: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the link title can be edited'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Link ID'
    )
    image_processing: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the image on processing'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Link title'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of square image of the link with 100 pixels in width'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of square image of the link with 50 pixels in width'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Link URL'
    )


class GroupsLiveCovers(BaseModel):
    is_enabled: bool = Field(
        None,
        description='Information whether live covers is enabled'
    )
    is_scalable: typing.Optional[bool] = Field(
        None,
        description='Information whether live covers photo scaling is enabled'
    )
    story_ids: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )


class GroupsLongPollEvents(BaseModel):
    audio_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    board_post_delete: "BaseBoolInt" = Field(
        None,
        description=''
    )
    board_post_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    board_post_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    board_post_restore: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_money_withdraw: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_money_withdraw_error: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_subscription_cancelled: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_subscription_create: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_subscription_expired: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_subscription_price_changed: "BaseBoolInt" = Field(
        None,
        description=''
    )
    donut_subscription_prolonged: "BaseBoolInt" = Field(
        None,
        description=''
    )
    group_change_photo: "BaseBoolInt" = Field(
        None,
        description=''
    )
    group_change_settings: "BaseBoolInt" = Field(
        None,
        description=''
    )
    group_join: "BaseBoolInt" = Field(
        None,
        description=''
    )
    group_leave: "BaseBoolInt" = Field(
        None,
        description=''
    )
    group_officers_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    lead_forms_new: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    market_comment_delete: "BaseBoolInt" = Field(
        None,
        description=''
    )
    market_comment_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    market_comment_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    market_comment_restore: "BaseBoolInt" = Field(
        None,
        description=''
    )
    market_order_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    market_order_new: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    message_allow: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_deny: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_read: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_reply: "BaseBoolInt" = Field(
        None,
        description=''
    )
    message_typing_state: "BaseBoolInt" = Field(
        None,
        description=''
    )
    photo_comment_delete: "BaseBoolInt" = Field(
        None,
        description=''
    )
    photo_comment_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    photo_comment_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    photo_comment_restore: "BaseBoolInt" = Field(
        None,
        description=''
    )
    photo_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    poll_vote_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    user_block: "BaseBoolInt" = Field(
        None,
        description=''
    )
    user_unblock: "BaseBoolInt" = Field(
        None,
        description=''
    )
    video_comment_delete: "BaseBoolInt" = Field(
        None,
        description=''
    )
    video_comment_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    video_comment_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    video_comment_restore: "BaseBoolInt" = Field(
        None,
        description=''
    )
    video_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_post_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_reply_delete: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_reply_edit: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_reply_new: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_reply_restore: "BaseBoolInt" = Field(
        None,
        description=''
    )
    wall_repost: "BaseBoolInt" = Field(
        None,
        description=''
    )


class GroupsLongPollServer(BaseModel):
    key: str = Field(
        None,
        description='Long Poll key'
    )
    server: str = Field(
        None,
        description='Long Poll server address'
    )
    ts: str = Field(
        None,
        description='Number of the last event'
    )


class GroupsLongPollSettings(BaseModel):
    api_version: typing.Optional[str] = Field(
        None,
        description='API version used for the events'
    )
    events: "GroupsLongPollEvents" = Field(
        None,
        description=''
    )
    is_enabled: bool = Field(
        None,
        description='Shows whether Long Poll is enabled'
    )


class GroupsMarketInfo(BaseModel):
    contact_id: typing.Optional[int] = Field(
        None,
        description='Contact person ID'
    )
    currency: typing.Optional["MarketCurrency"] = Field(
        None,
        description=''
    )
    currency_text: typing.Optional[str] = Field(
        None,
        description='Currency name'
    )
    enabled: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the market is enabled'
    )
    main_album_id: typing.Optional[int] = Field(
        None,
        description='Main market album ID'
    )
    min_order_price: typing.Optional["MarketPrice"] = Field(
        None,
        description=''
    )
    price_max: typing.Optional[str] = Field(
        None,
        description='Maximum price'
    )
    price_min: typing.Optional[str] = Field(
        None,
        description='Minimum price'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Market type'
    )


class GroupsMarketState(enum.Enum):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
    id: int = Field(
        None,
        description='User ID'
    )
    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = Field(
        None,
        description=''
    )
    role: typing.Optional["GroupsMemberRoleStatus"] = Field(
        None,
        description=''
    )


class GroupsMemberRolePermission(enum.Enum):
    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


class GroupsMemberStatus(BaseModel):
    member: "BaseBoolInt" = Field(
        None,
        description='Information whether user is a member of the group'
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class GroupsMemberStatusFull(BaseModel):
    can_invite: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether user can be invited'
    )
    can_recall: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether users invite to the group can be recalled'
    )
    invitation: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether user has been invited to the group'
    )
    member: "BaseBoolInt" = Field(
        None,
        description='Information whether user is a member of the group'
    )
    request: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether user has send request to the group'
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class GroupsOnlineStatus(BaseModel):
    minutes: typing.Optional[int] = Field(
        None,
        description='Estimated time of answer (for status = answer_mark)'
    )
    status: "GroupsOnlineStatusType" = Field(
        None,
        description=''
    )


class GroupsOnlineStatusType(enum.Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfoType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"


class GroupsPhotoSize(BaseModel):
    height: int = Field(
        None,
        description='Image height'
    )
    width: int = Field(
        None,
        description='Image width'
    )


class GroupsRoleOptions(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


GroupsSectionsListItem = typing.List[typing.Union[int, str]]  # (index, title) tuples


class GroupsSettingsTwitterStatus(enum.Enum):
    LOADING = "loading"
    SYNC = "sync"


class GroupsSettingsTwitter(BaseModel):
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    status: typing.Optional["GroupsSettingsTwitterStatus"] = Field(
        None,
        description=''
    )


class GroupsSubjectItem(BaseModel):
    id: int = Field(
        None,
        description='Subject ID'
    )
    name: str = Field(
        None,
        description='Subject title'
    )


class GroupsTokenPermissionSetting(BaseModel):
    name: str = Field(
        None,
        description=''
    )
    setting: int = Field(
        None,
        description=''
    )


class GroupsUserXtrRole(UsersUserFull):
    role: typing.Optional["GroupsRoleOptions"] = Field(
        None,
        description=''
    )


class LeadFormsAnswer(BaseModel):
    answer: typing.Union["LeadFormsAnswerItem", typing.List["LeadFormsAnswerItem"]] = Field(
        None,
        description=''
    )
    key: str = Field(
        None,
        description=''
    )


class LeadFormsAnswerItem(BaseModel):
    key: typing.Optional[str] = Field(
        None,
        description=''
    )
    value: str = Field(
        None,
        description=''
    )


class LeadFormsForm(BaseModel):
    active: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    confirmation: typing.Optional[str] = Field(
        None,
        description=''
    )
    description: typing.Optional[str] = Field(
        None,
        description=''
    )
    form_id: int = Field(
        None,
        description=''
    )
    group_id: int = Field(
        None,
        description=''
    )
    leads_count: int = Field(
        None,
        description=''
    )
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    notify_admins: typing.Optional[str] = Field(
        None,
        description=''
    )
    notify_emails: typing.Optional[str] = Field(
        None,
        description=''
    )
    once_per_user: typing.Optional[int] = Field(
        None,
        description=''
    )
    photo: typing.Optional[str] = Field(
        None,
        description=''
    )
    pixel_code: typing.Optional[str] = Field(
        None,
        description=''
    )
    policy_link_url: typing.Optional[str] = Field(
        None,
        description=''
    )
    questions: typing.Optional[typing.List["LeadFormsQuestionItem"]] = Field(
        None,
        description=''
    )
    site_link_url: typing.Optional[str] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )
    url: str = Field(
        None,
        description=''
    )


class LeadFormsLead(BaseModel):
    ad_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    answers: typing.List["LeadFormsAnswer"] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description=''
    )
    lead_id: int = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )


class LeadFormsQuestionItemType(enum.Enum):
    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class LeadFormsQuestionItem(BaseModel):
    key: str = Field(
        None,
        description=''
    )
    label: typing.Optional[str] = Field(
        None,
        description=''
    )
    options: typing.Optional[typing.List["LeadFormsQuestionItemOption"]] = Field(
        None,
        description='Опции выбора для типов radio, checkbox, select'
    )
    type: typing.Optional["LeadFormsQuestionItemType"] = Field(
        None,
        description=''
    )


class LeadFormsQuestionItemOption(BaseModel):
    key: typing.Optional[str] = Field(
        None,
        description=''
    )
    label: str = Field(
        None,
        description=''
    )


class LikesType(enum.Enum):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"
    TEXTPOST = "textpost"


class LinkTargetObject(BaseModel):
    item_id: typing.Optional[int] = Field(
        None,
        description='Item ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Owner ID'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Object type'
    )


class MarketCurrency(BaseModel):
    id: int = Field(
        None,
        description='Currency ID'
    )
    name: str = Field(
        None,
        description='Currency sign'
    )
    title: str = Field(
        None,
        description='Currency title'
    )


class MarketMarketAlbum(BaseModel):
    count: int = Field(
        None,
        description='Items number'
    )
    id: int = Field(
        None,
        description='Market album ID'
    )
    is_hidden: typing.Optional[bool] = Field(
        None,
        description='Is album hidden'
    )
    is_main: typing.Optional[bool] = Field(
        None,
        description='Is album main for owner'
    )
    owner_id: int = Field(
        None,
        description='Market album owners ID'
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description='Market album title'
    )
    updated_time: int = Field(
        None,
        description='Date when album has been updated last time in Unixtime'
    )


class MarketMarketCategoryOld(BaseModel):
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )
    section: "MarketSection" = Field(
        None,
        description=''
    )


class MarketMarketCategory(MarketMarketCategoryOld):
    pass


class MarketMarketCategoryNested(BaseModel):
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )
    parent: typing.Optional["MarketMarketCategoryNested"] = Field(
        None,
        description=''
    )


class MarketMarketCategoryTree(BaseModel):
    children: typing.Optional[typing.List["MarketMarketCategoryTree"]] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Category ID'
    )
    name: str = Field(
        None,
        description='Category name'
    )


class MarketMarketItem(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the market item'
    )
    availability: "MarketMarketItemAvailability" = Field(
        None,
        description=''
    )
    button_title: typing.Optional[str] = Field(
        None,
        description='Title for button for url'
    )
    category: "MarketMarketCategory" = Field(
        None,
        description=''
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when the item has been created in Unixtime'
    )
    description: str = Field(
        None,
        description='Item description'
    )
    external_id: typing.Optional[str] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Item ID'
    )
    is_favorite: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_main_variant: typing.Optional[bool] = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description='Item owners ID'
    )
    price: "MarketPrice" = Field(
        None,
        description=''
    )
    sku: typing.Optional[str] = Field(
        None,
        description=''
    )
    thumb_photo: typing.Optional[str] = Field(
        None,
        description='URL of the preview image'
    )
    title: str = Field(
        None,
        description='Item title'
    )
    url: typing.Optional[str] = Field(
        None,
        description='URL to item'
    )
    variants_grouping_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class MarketMarketItemAvailability(enum.IntEnum):
    available = 0
    removed = 1
    unavailable = 2


class MarketMarketItemFull(MarketMarketItem):
    ad_id: typing.Optional[int] = Field(
        None,
        description='Contains ad ID if it has'
    )
    albums_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current use can comment the item'
    )
    can_repost: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current use can repost the item'
    )
    cancel_info: typing.Optional["BaseLink"] = Field(
        None,
        description='Information for cancel and revert order'
    )
    likes: typing.Optional["BaseLikes"] = Field(
        None,
        description=''
    )
    photos: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        None,
        description=''
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=''
    )
    user_agreement_info: typing.Optional[str] = Field(
        None,
        description='User agreement info'
    )
    views_count: typing.Optional[int] = Field(
        None,
        description='Views number'
    )
    wishlist_item_id: typing.Optional[int] = Field(
        None,
        description='Object identifier in wishlist of viewer'
    )


class MarketOrder(BaseModel):
    address: typing.Optional[str] = Field(
        None,
        description=''
    )
    cancel_info: typing.Optional["BaseLink"] = Field(
        None,
        description='Information for cancel and revert order'
    )
    comment: typing.Optional[str] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description=''
    )
    display_order_id: typing.Optional[str] = Field(
        None,
        description=''
    )
    group_id: int = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description=''
    )
    items_count: int = Field(
        None,
        description=''
    )
    merchant_comment: typing.Optional[str] = Field(
        None,
        description=''
    )
    preview_order_items: typing.Optional[typing.List["MarketOrderItem"]] = Field(
        None,
        description='Several order items for preview'
    )
    status: int = Field(
        None,
        description=''
    )
    total_price: "MarketPrice" = Field(
        None,
        description=''
    )
    track_link: typing.Optional[str] = Field(
        None,
        description=''
    )
    track_number: typing.Optional[str] = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description=''
    )
    weight: typing.Optional[int] = Field(
        None,
        description=''
    )


class MarketOrderItem(BaseModel):
    item: "MarketMarketItem" = Field(
        None,
        description=''
    )
    item_id: int = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    price: "MarketPrice" = Field(
        None,
        description=''
    )
    quantity: int = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )
    variants: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )


class MarketPrice(BaseModel):
    amount: str = Field(
        None,
        description='Amount'
    )
    currency: "MarketCurrency" = Field(
        None,
        description=''
    )
    discount_rate: typing.Optional[int] = Field(
        None,
        description=''
    )
    old_amount: typing.Optional[str] = Field(
        None,
        description=''
    )
    old_amount_text: typing.Optional[str] = Field(
        None,
        description='Textual representation of old price'
    )
    text: str = Field(
        None,
        description='Text'
    )


class MarketSection(BaseModel):
    id: int = Field(
        None,
        description='Section ID'
    )
    name: str = Field(
        None,
        description='Section name'
    )


class MarketServicesViewType(enum.IntEnum):
    cards = 1
    rows = 2


class MessagesAudioMessage(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for audio message'
    )
    duration: int = Field(
        None,
        description='Audio message duration in seconds'
    )
    id: int = Field(
        None,
        description='Audio message ID'
    )
    link_mp3: str = Field(
        None,
        description='MP3 file URL'
    )
    link_ogg: str = Field(
        None,
        description='OGG file URL'
    )
    owner_id: int = Field(
        None,
        description='Audio message owner ID'
    )
    transcript_error: typing.Optional[int] = Field(
        None,
        description=''
    )
    waveform: typing.List[int] = Field(
        None,
        description=''
    )


class MessagesChat(BaseModel):
    admin_id: int = Field(
        None,
        description='Chat creator ID'
    )
    id: int = Field(
        None,
        description='Chat ID'
    )
    is_default_photo: typing.Optional[bool] = Field(
        None,
        description='If provided photo is default'
    )
    is_group_channel: typing.Optional[bool] = Field(
        None,
        description='If chat is group channel'
    )
    kicked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Shows that user has been kicked from the chat'
    )
    left: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Shows that user has been left the chat'
    )
    members_count: int = Field(
        None,
        description='Count members in a chat'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 100 px in width'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 200 px in width'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 50 px in width'
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description='Chat title'
    )
    type: str = Field(
        None,
        description='Chat type'
    )
    users: typing.List[int] = Field(
        None,
        description=''
    )


class MessagesChatFull(BaseModel):
    admin_id: int = Field(
        None,
        description='Chat creator ID'
    )
    id: int = Field(
        None,
        description='Chat ID'
    )
    kicked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Shows that user has been kicked from the chat'
    )
    left: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Shows that user has been left the chat'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 100 px in width'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 200 px in width'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 50 px in width'
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description='Chat title'
    )
    type: str = Field(
        None,
        description='Chat type'
    )
    users: typing.List["MessagesUserXtrInvitedBy"] = Field(
        None,
        description=''
    )


class MessagesChatPreview(BaseModel):
    admin_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    button: typing.Optional["BaseLinkButton"] = Field(
        None,
        description=''
    )
    is_don: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_group_channel: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_member: typing.Optional[bool] = Field(
        None,
        description=''
    )
    joined: typing.Optional[bool] = Field(
        None,
        description=''
    )
    local_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    members: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    members_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )


class MessagesChatPushSettings(BaseModel):
    disabled_until: typing.Optional[int] = Field(
        None,
        description='Time until that notifications are disabled'
    )
    sound: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the sound is on'
    )


class MessagesChatRestrictions(BaseModel):
    admins_promote_users: typing.Optional[bool] = Field(
        None,
        description='Only admins can promote users to admins'
    )
    only_admins_edit_info: typing.Optional[bool] = Field(
        None,
        description='Only admins can change chat info'
    )
    only_admins_edit_pin: typing.Optional[bool] = Field(
        None,
        description='Only admins can edit pinned message'
    )
    only_admins_invite: typing.Optional[bool] = Field(
        None,
        description='Only admins can invite users to this chat'
    )
    only_admins_kick: typing.Optional[bool] = Field(
        None,
        description='Only admins can kick users from this chat'
    )


class MessagesChatSettings(BaseModel):
    acl: "MessagesChatSettingsAcl" = Field(
        None,
        description=''
    )
    active_ids: typing.List[int] = Field(
        None,
        description=''
    )
    admin_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description='Ids of chat admins'
    )
    disappearing_chat_link: typing.Optional[str] = Field(
        None,
        description=''
    )
    friends_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    is_disappearing: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_group_channel: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_service: typing.Optional[bool] = Field(
        None,
        description=''
    )
    members_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description=''
    )
    permissions: typing.Optional["MessagesChatSettingsPermissions"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        None,
        description=''
    )
    pinned_message: typing.Optional["MessagesPinnedMessage"] = Field(
        None,
        description=''
    )
    state: "MessagesChatSettingsState" = Field(
        None,
        description=''
    )
    theme: typing.Optional[str] = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description='Chat title'
    )


class MessagesChatSettingsAcl(BaseModel):
    can_call: bool = Field(
        None,
        description='Can you init group call in the chat'
    )
    can_change_info: bool = Field(
        None,
        description='Can you change photo, description and name'
    )
    can_change_invite_link: bool = Field(
        None,
        description='Can you change invite link for this chat'
    )
    can_change_pin: bool = Field(
        None,
        description='Can you pin/unpin message for this chat'
    )
    can_change_service_type: typing.Optional[bool] = Field(
        None,
        description='Can you change chat service type'
    )
    can_copy_chat: bool = Field(
        None,
        description='Can you copy chat'
    )
    can_invite: bool = Field(
        None,
        description='Can you invite other peers in chat'
    )
    can_moderate: bool = Field(
        None,
        description='Can you moderate (delete) other users messages'
    )
    can_promote_users: bool = Field(
        None,
        description='Can you promote simple users to chat admins'
    )
    can_see_invite_link: bool = Field(
        None,
        description='Can you see invite link for this chat'
    )
    can_use_mass_mentions: bool = Field(
        None,
        description='Can you use mass mentions'
    )


class MessagesChatSettingsPermissionsInvite(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeInfo(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangePin(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsUseMassMentions(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsSeeInviteLink(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class WhoCanMakeCalls(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class WhoCanChangeAdmins(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class MessagesChatSettingsPermissions(BaseModel):
    call: typing.Optional["WhoCanMakeCalls"] = Field(
        None,
        description='Who can make calls'
    )
    change_admins: typing.Optional["WhoCanChangeAdmins"] = Field(
        None,
        description='Who can change admins'
    )
    change_info: typing.Optional["MessagesChatSettingsPermissionsChangeInfo"] = Field(
        None,
        description='Who can change chat info'
    )
    change_pin: typing.Optional["MessagesChatSettingsPermissionsChangePin"] = Field(
        None,
        description='Who can change pinned message'
    )
    invite: typing.Optional["MessagesChatSettingsPermissionsInvite"] = Field(
        None,
        description='Who can invite users to chat'
    )
    see_invite_link: typing.Optional["MessagesChatSettingsPermissionsSeeInviteLink"] = Field(
        None,
        description='Who can see invite link'
    )
    use_mass_mentions: typing.Optional["MessagesChatSettingsPermissionsUseMassMentions"] = Field(
        None,
        description='Who can use mass mentions'
    )


class MessagesChatSettingsPhoto(BaseModel):
    is_default_call_photo: typing.Optional[bool] = Field(
        None,
        description='If provided photo is default call photo'
    )
    is_default_photo: typing.Optional[bool] = Field(
        None,
        description='If provided photo is default'
    )
    photo_100: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 100px in width'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 200px in width'
    )
    photo_50: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 50px in width'
    )


class MessagesChatSettingsState(enum.Enum):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"


class MessagesConversationSpecialServiceType(enum.Enum):
    BUSINESS_NOTIFY = "business_notify"


class MessagesConversation(BaseModel):
    can_write: typing.Optional["MessagesConversationCanWrite"] = Field(
        None,
        description=''
    )
    chat_settings: typing.Optional["MessagesChatSettings"] = Field(
        None,
        description=''
    )
    current_keyboard: typing.Optional["MessagesKeyboard"] = Field(
        None,
        description=''
    )
    important: typing.Optional[bool] = Field(
        None,
        description=''
    )
    in_read: int = Field(
        None,
        description='Last message user have read'
    )
    is_marked_unread: typing.Optional[bool] = Field(
        None,
        description='Is this conversation uread'
    )
    last_conversation_message_id: typing.Optional[int] = Field(
        None,
        description='Conversation message ID of the last message in conversation'
    )
    last_message_id: int = Field(
        None,
        description='ID of the last message in conversation'
    )
    mentions: typing.Optional[typing.List[int]] = Field(
        None,
        description='Ids of messages with mentions'
    )
    message_request_data: typing.Optional["MessagesMessageRequestData"] = Field(
        None,
        description=''
    )
    out_read: int = Field(
        None,
        description='Last outcoming message have been read by the opponent'
    )
    out_read_by: typing.Optional["MessagesOutReadBy"] = Field(
        None,
        description=''
    )
    peer: "MessagesConversationPeer" = Field(
        None,
        description=''
    )
    push_settings: typing.Optional["MessagesPushSettings"] = Field(
        None,
        description=''
    )
    sort_id: typing.Optional["MessagesConversationSortId"] = Field(
        None,
        description=''
    )
    special_service_type: typing.Optional["MessagesConversationSpecialServiceType"] = Field(
        None,
        description=''
    )
    unanswered: typing.Optional[bool] = Field(
        None,
        description=''
    )
    unread_count: typing.Optional[int] = Field(
        None,
        description='Unread messages number'
    )


class MessagesConversationCanWrite(BaseModel):
    allowed: bool = Field(
        None,
        description=''
    )
    reason: typing.Optional[int] = Field(
        None,
        description=''
    )


class MessagesConversationMember(BaseModel):
    can_kick: typing.Optional[bool] = Field(
        None,
        description='Is it possible for user to kick this member'
    )
    invited_by: typing.Optional[int] = Field(
        None,
        description=''
    )
    is_admin: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_message_request: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_owner: typing.Optional[bool] = Field(
        None,
        description=''
    )
    join_date: typing.Optional[int] = Field(
        None,
        description=''
    )
    member_id: int = Field(
        None,
        description=''
    )
    request_date: typing.Optional[int] = Field(
        None,
        description='Message request date'
    )


class MessagesConversationPeer(BaseModel):
    id: int = Field(
        None,
        description=''
    )
    local_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    type: "MessagesConversationPeerType" = Field(
        None,
        description=''
    )


class MessagesConversationPeerType(enum.Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(BaseModel):
    major_id: int = Field(
        None,
        description='Major id for sorting conversations'
    )
    minor_id: int = Field(
        None,
        description='Minor id for sorting conversations'
    )


class MessagesConversationWithMessage(BaseModel):
    conversation: "MessagesConversation" = Field(
        None,
        description=''
    )
    last_message: typing.Optional["MessagesMessage"] = Field(
        None,
        description=''
    )


class MessagesForeignMessage(BaseModel):
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        None,
        description=''
    )
    conversation_message_id: typing.Optional[int] = Field(
        None,
        description='Conversation message ID'
    )
    date: int = Field(
        None,
        description='Date when the message was created'
    )
    from_id: int = Field(
        None,
        description='Message authors ID'
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        None,
        description=''
    )
    geo: typing.Optional["BaseGeo"] = Field(
        None,
        description=''
    )
    id: typing.Optional[int] = Field(
        None,
        description='Message ID'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    peer_id: typing.Optional[int] = Field(
        None,
        description='Peer ID'
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='Message text'
    )
    update_time: typing.Optional[int] = Field(
        None,
        description='Date when the message has been updated in Unixtime'
    )
    was_listened: typing.Optional[bool] = Field(
        None,
        description='Was the audio message inside already listened by you'
    )


class MessagesForward(BaseModel):
    conversation_message_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    is_reply: typing.Optional[bool] = Field(
        None,
        description='If you need to reply to a message'
    )
    message_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Messages owner_id'
    )
    peer_id: typing.Optional[int] = Field(
        None,
        description='Messages peer_id'
    )


class MessagesGetConversationById(BaseModel):
    count: int = Field(
        None,
        description='Total number'
    )
    items: typing.List["MessagesConversation"] = Field(
        None,
        description=''
    )


class MessagesGetConversationByIdExtended(MessagesGetConversationById):
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        None,
        description=''
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        None,
        description=''
    )


class MessagesGetConversationMembers(BaseModel):
    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = Field(
        None,
        description=''
    )
    count: int = Field(
        None,
        description='Chat members count'
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        None,
        description=''
    )
    items: typing.List["MessagesConversationMember"] = Field(
        None,
        description=''
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        None,
        description=''
    )


class MessagesGraffiti(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for graffiti'
    )
    height: int = Field(
        None,
        description='Graffiti height'
    )
    id: int = Field(
        None,
        description='Graffiti ID'
    )
    owner_id: int = Field(
        None,
        description='Graffiti owner ID'
    )
    url: str = Field(
        None,
        description='Graffiti URL'
    )
    width: int = Field(
        None,
        description='Graffiti width'
    )


class MessagesHistoryAttachment(BaseModel):
    attachment: "MessagesHistoryMessageAttachment" = Field(
        None,
        description=''
    )
    forward_level: typing.Optional[int] = Field(
        None,
        description='Forward level (optional)'
    )
    from_id: int = Field(
        None,
        description='Message authors ID'
    )
    message_id: int = Field(
        None,
        description='Message ID'
    )
    was_listened: typing.Optional[bool] = Field(
        None,
        description=''
    )


class MessagesHistoryMessageAttachment(BaseModel):
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        None,
        description=''
    )
    doc: typing.Optional["DocsDoc"] = Field(
        None,
        description=''
    )
    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        None,
        description=''
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    market: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    type: "MessagesHistoryMessageAttachmentType" = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideo"] = Field(
        None,
        description=''
    )
    wall: typing.Optional["WallWallpostFull"] = Field(
        None,
        description=''
    )


class MessagesHistoryMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
    author_id: typing.Optional[int] = Field(
        None,
        description='Community or bot, which set this keyboard'
    )
    buttons: typing.List["list"] = Field(
        None,
        description=''
    )
    inline: typing.Optional[bool] = Field(
        None,
        description=''
    )
    one_time: bool = Field(
        None,
        description='Should this keyboard disappear on first use'
    )


class ButtonColor(enum.Enum):
    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class MessagesKeyboardButton(BaseModel):
    action: "MessagesKeyboardButtonPropertyAction" = Field(
        None,
        description=''
    )
    color: typing.Optional["ButtonColor"] = Field(
        None,
        description='Button color'
    )


class MessagesKeyboardButtonActionCallbackType(enum.Enum):
    CALLBACK = "callback"


class MessagesKeyboardButtonActionCallback(BaseModel):
    label: str = Field(
        None,
        description='Label for button'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionCallbackType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionLocationType(enum.Enum):
    LOCATION = "location"


class MessagesKeyboardButtonActionLocation(BaseModel):
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionLocationType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionOpenAppType(enum.Enum):
    OPEN_APP = "open_app"


class MessagesKeyboardButtonActionOpenApp(BaseModel):
    app_id: int = Field(
        None,
        description='Fragment value in app link like vk.com/app{app_id}_-654321#hash'
    )
    hash: typing.Optional[str] = Field(
        None,
        description='Fragment value in app link like vk.com/app123456_-654321#{hash}'
    )
    label: str = Field(
        None,
        description='Label for button'
    )
    owner_id: int = Field(
        None,
        description='Fragment value in app link like vk.com/app123456_{owner_id}#hash'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionOpenAppType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionOpenLinkType(enum.Enum):
    OPEN_LINK = "open_link"


class MessagesKeyboardButtonActionOpenLink(BaseModel):
    label: str = Field(
        None,
        description='Label for button'
    )
    link: str = Field(
        None,
        description='link for button'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionOpenLinkType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionOpenPhotoType(enum.Enum):
    OPEN_PHOTO = "open_photo"


class MessagesKeyboardButtonActionOpenPhoto(BaseModel):
    type: typing.Optional["MessagesKeyboardButtonActionOpenPhotoType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionTextType(enum.Enum):
    TEXT = "text"


class MessagesKeyboardButtonActionText(BaseModel):
    label: str = Field(
        None,
        description='Label for button'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionTextType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonActionVkpayType(enum.Enum):
    VKPAY = "vkpay"


class MessagesKeyboardButtonActionVkpay(BaseModel):
    hash: str = Field(
        None,
        description='Fragment value in app link like vk.com/app123456_-654321#{hash}'
    )
    payload: typing.Optional[str] = Field(
        None,
        description='Additional data sent along with message for developer convenience'
    )
    type: typing.Optional["MessagesKeyboardButtonActionVkpayType"] = Field(
        None,
        description=''
    )


class MessagesKeyboardButtonPropertyAction(
    MessagesKeyboardButtonActionLocation,
    MessagesKeyboardButtonActionOpenApp,
    MessagesKeyboardButtonActionOpenLink,
    MessagesKeyboardButtonActionOpenPhoto,
    MessagesKeyboardButtonActionText,
    MessagesKeyboardButtonActionCallback,
    MessagesKeyboardButtonActionVkpay
):
    pass


class MessagesLastActivity(BaseModel):
    online: "BaseBoolInt" = Field(
        None,
        description='Information whether user is online'
    )
    time: int = Field(
        None,
        description='Time when user was online in Unixtime'
    )


class MessagesLongpollMessages(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Total number'
    )
    items: typing.Optional[typing.List["MessagesMessage"]] = Field(
        None,
        description=''
    )


class MessagesLongpollParams(BaseModel):
    key: str = Field(
        None,
        description='Key'
    )
    pts: typing.Optional[int] = Field(
        None,
        description='Persistent timestamp'
    )
    server: str = Field(
        None,
        description='Server URL'
    )
    ts: int = Field(
        None,
        description='Timestamp'
    )


class MessagesMessage(BaseModel):
    action: typing.Optional["MessagesMessageAction"] = Field(
        None,
        description=''
    )
    admin_author_id: typing.Optional[int] = Field(
        None,
        description='Only for messages from community. Contains user ID of community admin, who sent this message.'
    )
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        None,
        description=''
    )
    conversation_message_id: typing.Optional[int] = Field(
        None,
        description='Unique auto-incremented number for all messages with this peer'
    )
    date: int = Field(
        None,
        description='Date when the message has been sent in Unixtime'
    )
    deleted: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Is it an deleted message'
    )
    from_id: int = Field(
        None,
        description='Message authors ID'
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        None,
        description='Forwarded messages'
    )
    geo: typing.Optional["BaseGeo"] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Message ID'
    )
    important: typing.Optional[bool] = Field(
        None,
        description='Is it an important message'
    )
    is_cropped: typing.Optional[bool] = Field(
        None,
        description='this message is cropped for bot'
    )
    is_hidden: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_silent: typing.Optional[bool] = Field(
        None,
        description='Is silent message, push without sound'
    )
    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        None,
        description=''
    )
    members_count: typing.Optional[int] = Field(
        None,
        description='Members number'
    )
    out: "BaseBoolInt" = Field(
        None,
        description='Information whether the message is outcoming'
    )
    payload: typing.Optional[str] = Field(
        None,
        description=''
    )
    peer_id: int = Field(
        None,
        description='Peer ID'
    )
    pinned_at: typing.Optional[int] = Field(
        None,
        description='Date when the message has been pinned in Unixtime'
    )
    random_id: typing.Optional[int] = Field(
        None,
        description='ID used for sending messages. It returned only for outgoing messages'
    )
    ref: typing.Optional[str] = Field(
        None,
        description=''
    )
    ref_source: typing.Optional[str] = Field(
        None,
        description=''
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='Message text'
    )
    update_time: typing.Optional[int] = Field(
        None,
        description='Date when the message has been updated in Unixtime'
    )
    was_listened: typing.Optional[bool] = Field(
        None,
        description='Was the audio message inside already listened by you'
    )


class MessagesMessageAction(BaseModel):
    conversation_message_id: typing.Optional[int] = Field(
        None,
        description='Message ID'
    )
    email: typing.Optional[str] = Field(
        None,
        description='Email address for chat_invite_user or chat_kick_user actions'
    )
    member_id: typing.Optional[int] = Field(
        None,
        description='User or email peer ID'
    )
    message: typing.Optional[str] = Field(
        None,
        description='Message body of related message'
    )
    photo: typing.Optional["MessagesMessageActionPhoto"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='New chat title for chat_create and chat_title_update actions'
    )
    type: "MessagesMessageActionStatus" = Field(
        None,
        description=''
    )


class MessagesMessageActionPhoto(BaseModel):
    photo_100: str = Field(
        None,
        description='URL of the preview image with 100px in width'
    )
    photo_200: str = Field(
        None,
        description='URL of the preview image with 200px in width'
    )
    photo_50: str = Field(
        None,
        description='URL of the preview image with 50px in width'
    )


class MessagesMessageActionStatus(enum.Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
    CHAT_SCREENSHOT = "chat_screenshot"


class MessagesMessageAttachment(BaseModel):
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        None,
        description=''
    )
    call: typing.Optional["CallsCall"] = Field(
        None,
        description=''
    )
    doc: typing.Optional["DocsDoc"] = Field(
        None,
        description=''
    )
    gift: typing.Optional["GiftsLayout"] = Field(
        None,
        description=''
    )
    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        None,
        description=''
    )
    market: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    poll: typing.Optional["PollsPoll"] = Field(
        None,
        description=''
    )
    sticker: typing.Optional["BaseSticker"] = Field(
        None,
        description=''
    )
    story: typing.Optional["StoriesStory"] = Field(
        None,
        description=''
    )
    type: "MessagesMessageAttachmentType" = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideoFull"] = Field(
        None,
        description=''
    )
    wall_reply: typing.Optional["WallWallComment"] = Field(
        None,
        description=''
    )


class MessagesMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseModel):
    inviter_id: typing.Optional[int] = Field(
        None,
        description='Message request sender id'
    )
    request_date: typing.Optional[int] = Field(
        None,
        description='Message request date'
    )
    status: typing.Optional[str] = Field(
        None,
        description='Status of message request'
    )


class MessagesMessagesArray(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description=''
    )
    items: typing.Optional[typing.List["MessagesMessage"]] = Field(
        None,
        description=''
    )


class MessagesOutReadBy(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description=''
    )
    member_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )


class MessagesPinnedMessage(BaseModel):
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        None,
        description=''
    )
    conversation_message_id: typing.Optional[int] = Field(
        None,
        description='Unique auto-incremented number for all messages with this peer'
    )
    date: int = Field(
        None,
        description='Date when the message has been sent in Unixtime'
    )
    from_id: int = Field(
        None,
        description='Message authors ID'
    )
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        None,
        description='Forwarded messages'
    )
    geo: typing.Optional["BaseGeo"] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Message ID'
    )
    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        None,
        description=''
    )
    peer_id: int = Field(
        None,
        description='Peer ID'
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='Message text'
    )


class MessagesPushSettings(BaseModel):
    disabled_forever: bool = Field(
        None,
        description='Information whether push notifications are disabled forever'
    )
    disabled_mass_mentions: typing.Optional[bool] = Field(
        None,
        description='Information whether the mass mentions (like @all, @online) are disabled'
    )
    disabled_mentions: typing.Optional[bool] = Field(
        None,
        description='Information whether the mentions are disabled'
    )
    disabled_until: typing.Optional[int] = Field(
        None,
        description='Time until what notifications are disabled'
    )
    no_sound: bool = Field(
        None,
        description='Information whether the sound is on'
    )


class MessagesSendUserIdsResponseItem(BaseModel):
    conversation_message_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    error: typing.Optional["BaseMessageError"] = Field(
        None,
        description=''
    )
    message_id: int = Field(
        None,
        description=''
    )
    peer_id: int = Field(
        None,
        description=''
    )


class MessagesTemplateActionTypeNames(enum.Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"
    INTENT_SUBSCRIBE = "intent_subscribe"
    INTENT_UNSUBSCRIBE = "intent_unsubscribe"


class UsersUserXtrType(UsersUser):
    type: typing.Optional["UsersUserType"] = Field(
        None,
        description=''
    )


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    invited_by: typing.Optional[int] = Field(
        None,
        description='ID of the inviter'
    )


class NewsfeedCommentsFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedIgnoreItemType(enum.Enum):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemBase(BaseModel):
    date: int = Field(
        None,
        description='Date when item has been added in Unixtime'
    )
    source_id: int = Field(
        None,
        description='Item source ID'
    )
    type: "NewsfeedNewsfeedItemType" = Field(
        None,
        description=''
    )


class NewsfeedItemAudio(NewsfeedItemBase):
    audio: typing.Optional["NewsfeedItemAudioAudio"] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )


class NewsfeedItemAudioAudio(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Audios number'
    )
    items: typing.Optional[typing.List["AudioAudio"]] = Field(
        None,
        description=''
    )


class NewsfeedItemDigest(NewsfeedItemBase):
    feed_id: typing.Optional[str] = Field(
        None,
        description='id of feed in digest'
    )
    footer: typing.Optional["NewsfeedItemDigestFooter"] = Field(
        None,
        description=''
    )
    header: typing.Optional["NewsfeedItemDigestHeader"] = Field(
        None,
        description=''
    )
    items: typing.Optional[typing.List["NewsfeedItemDigestItem"]] = Field(
        None,
        description=''
    )
    main_post_ids: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    template: typing.Optional[str] = Field(
        None,
        description='type of digest'
    )
    track_code: typing.Optional[str] = Field(
        None,
        description=''
    )


class NewsfeedItemDigestButtonStyle(enum.Enum):
    PRIMARY = "primary"


class NewsfeedItemDigestButton(BaseModel):
    style: typing.Optional["NewsfeedItemDigestButtonStyle"] = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description=''
    )


class NewsfeedItemDigestFooterStyle(enum.Enum):
    TEXT = "text"
    BUTTON = "button"


class NewsfeedItemDigestFooter(BaseModel):
    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        None,
        description=''
    )
    style: typing.Optional["NewsfeedItemDigestFooterStyle"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='text for invite to enable smart feed'
    )


class NewsfeedItemDigestFullItemStyle(enum.Enum):
    DEFAULT = "default"
    INVERSED = "inversed"
    SPOTLIGHT = "spotlight"


class NewsfeedItemDigestFullItem(BaseModel):
    attachment: typing.Optional["WallWallpostAttachment"] = Field(
        None,
        description=''
    )
    attachment_index: typing.Optional[int] = Field(
        None,
        description=''
    )
    post: "WallWallpost" = Field(
        None,
        description=''
    )
    source_name: typing.Optional[str] = Field(
        None,
        description=''
    )
    style: typing.Optional["NewsfeedItemDigestFullItemStyle"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description=''
    )


class NewsfeedItemDigestHeaderStyle(enum.Enum):
    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class NewsfeedItemDigestHeader(BaseModel):
    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        None,
        description=''
    )
    style: typing.Optional["NewsfeedItemDigestHeaderStyle"] = Field(
        None,
        description=''
    )
    subtitle: typing.Optional[str] = Field(
        None,
        description='Subtitle of the header, when title have two strings'
    )
    title: str = Field(
        None,
        description='Title of the header'
    )


class WallWallpost(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key to private object'
    )
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        None,
        description=''
    )
    copyright: typing.Optional["WallPostCopyright"] = Field(
        None,
        description='Information about the source of the post'
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date of publishing in Unixtime'
    )
    edited: typing.Optional[int] = Field(
        None,
        description='Date of editing in Unixtime'
    )
    from_id: typing.Optional[int] = Field(
        None,
        description='Post author ID'
    )
    geo: typing.Optional["WallGeo"] = Field(
        None,
        description=''
    )
    id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    is_archived: typing.Optional[bool] = Field(
        None,
        description='Is post archived, only for post owners'
    )
    is_deleted: typing.Optional[bool] = Field(
        None,
        description=''
    )
    is_favorite: typing.Optional[bool] = Field(
        None,
        description='Information whether the post in favorites list'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description='Count of likes'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Wall owners ID'
    )
    parents_stack: typing.Optional[typing.List[int]] = Field(
        None,
        description='If post type reply, contains original parent IDs stack'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='If post type reply, contains original post ID'
    )
    post_source: typing.Optional["WallPostSource"] = Field(
        None,
        description=''
    )
    post_type: typing.Optional["WallPostType"] = Field(
        None,
        description=''
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=''
    )
    signer_id: typing.Optional[int] = Field(
        None,
        description='Post signer ID'
    )
    text: typing.Optional[str] = Field(
        None,
        description='Post text'
    )
    views: typing.Optional["WallViews"] = Field(
        None,
        description='Count of views'
    )


class NewsfeedItemDigestItem(WallWallpost):
    pass


class NewsfeedItemFriend(NewsfeedItemBase):
    friends: typing.Optional["NewsfeedItemFriendFriends"] = Field(
        None,
        description=''
    )


class NewsfeedItemFriendFriends(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Number of friends has been added'
    )
    items: typing.Optional[typing.List["BaseUserId"]] = Field(
        None,
        description=''
    )


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    action: typing.Optional["BaseLinkButtonAction"] = Field(
        None,
        description=''
    )
    image: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description=''
    )
    subtitle: typing.Optional[str] = Field(
        None,
        description='Subtitle of the header'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Title of the header'
    )


class WallCarouselBase(BaseModel):
    carousel_offset: typing.Optional[int] = Field(
        None,
        description='Index of current carousel element'
    )


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )


class NewsfeedItemPhotoPhotos(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Photos number'
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = Field(
        None,
        description=''
    )


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Tags number'
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = Field(
        None,
        description=''
    )


class NewsfeedItemPromoButton(NewsfeedItemBase):
    action: typing.Optional["NewsfeedItemPromoButtonAction"] = Field(
        None,
        description=''
    )
    images: typing.Optional[typing.List["NewsfeedItemPromoButtonImage"]] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )
    track_code: typing.Optional[str] = Field(
        None,
        description=''
    )


class NewsfeedItemPromoButtonAction(BaseModel):
    target: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional[str] = Field(
        None,
        description=''
    )
    url: typing.Optional[str] = Field(
        None,
        description=''
    )


class NewsfeedItemPromoButtonImage(BaseModel):
    height: typing.Optional[int] = Field(
        None,
        description=''
    )
    url: typing.Optional[str] = Field(
        None,
        description=''
    )
    width: typing.Optional[int] = Field(
        None,
        description=''
    )


class NewsfeedItemTopic(NewsfeedItemBase):
    comments: typing.Optional["BaseCommentsInfo"] = Field(
        None,
        description=''
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    post_id: int = Field(
        None,
        description='Topic post ID'
    )
    text: str = Field(
        None,
        description='Post text'
    )


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    video: typing.Optional["NewsfeedItemVideoVideo"] = Field(
        None,
        description=''
    )


class NewsfeedItemVideoVideo(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Tags number'
    )
    items: typing.Optional[typing.List["VideoVideo"]] = Field(
        None,
        description=''
    )


class WallWallpostFull(WallWallpost):
    can_delete: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can delete the post'
    )
    can_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can edit the post'
    )
    can_pin: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can pin the post'
    )
    comments: typing.Optional["BaseCommentsInfo"] = Field(
        None,
        description=''
    )
    copy_history: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        None,
        description=''
    )
    created_by: typing.Optional[int] = Field(
        None,
        description='Post creator ID (if post still can be edited)'
    )
    donut: typing.Optional["WallWallpostDonut"] = Field(
        None,
        description=''
    )
    hash: typing.Optional[str] = Field(
        None,
        description='Hash for sharing'
    )
    is_pinned: typing.Optional[int] = Field(
        None,
        description='Information whether the post is pinned'
    )
    marked_as_ads: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the post is marked as ads'
    )
    short_text_rate: typing.Optional[float] = Field(
        None,
        description='Preview length control parameter'
    )
    topic_id: typing.Optional[int] = Field(
        None,
        description='Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method'
    )


class NewsfeedItemWallpost(WallCarouselBase, NewsfeedItemBase, WallWallpostFull):
    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        None,
        description=''
    )


class NewsfeedItemWallpostFeedback(BaseModel):
    answers: typing.Optional[typing.List["NewsfeedItemWallpostFeedbackAnswer"]] = Field(
        None,
        description=''
    )
    gratitude: typing.Optional[str] = Field(
        None,
        description=''
    )
    question: str = Field(
        None,
        description=''
    )
    stars_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    type: "NewsfeedItemWallpostFeedbackType" = Field(
        None,
        description=''
    )


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    id: str = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description=''
    )


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedList(BaseModel):
    id: int = Field(
        None,
        description='List ID'
    )
    title: str = Field(
        None,
        description='List title'
    )


class NewsfeedListFull(NewsfeedList):
    no_reposts: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether reposts hiding is enabled'
    )
    source_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )


class NewsfeedNewsfeedItem(
    NewsfeedItemWallpost,
    NewsfeedItemPhoto,
    NewsfeedItemPhotoTag,
    NewsfeedItemFriend,
    NewsfeedItemAudio,
    NewsfeedItemVideo,
    NewsfeedItemTopic,
    NewsfeedItemDigest,
    NewsfeedItemPromoButton
):
    pass


class NewsfeedNewsfeedItemType(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    NOTE = "note"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"


class PhotosPhoto(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the photo'
    )
    album_id: int = Field(
        None,
        description='Album ID'
    )
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment the photo'
    )
    comments: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description='Date when uploaded'
    )
    has_tags: bool = Field(
        None,
        description='Whether photo has attached tag links'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Original photo height'
    )
    id: int = Field(
        None,
        description='Photo ID'
    )
    images: typing.Optional[typing.List["PhotosImage"]] = Field(
        None,
        description=''
    )
    lat: typing.Optional[float] = Field(
        None,
        description='Latitude'
    )
    likes: typing.Optional["BaseLikes"] = Field(
        None,
        description=''
    )
    long: typing.Optional[float] = Field(
        None,
        description='Longitude'
    )
    owner_id: int = Field(
        None,
        description='Photo owners ID'
    )
    photo_256: typing.Optional[str] = Field(
        None,
        description='URL of image with 2560 px width'
    )
    place: typing.Optional[str] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=''
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )
    tags: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Photo caption'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='ID of the user who have uploaded the photo'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Original photo width'
    )


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    can_repost: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can repost the photo'
    )
    comments: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    likes: typing.Optional["BaseLikes"] = Field(
        None,
        description=''
    )


class NotesNote(BaseModel):
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment the note'
    )
    comments: int = Field(
        None,
        description='Comments number'
    )
    date: int = Field(
        None,
        description='Date when the note has been created in Unixtime'
    )
    id: int = Field(
        None,
        description='Note ID'
    )
    owner_id: int = Field(
        None,
        description='Note owners ID'
    )
    privacy_comment: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    privacy_view: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    read_comments: typing.Optional[int] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Note text'
    )
    text_wiki: typing.Optional[str] = Field(
        None,
        description='Note text in wiki format'
    )
    title: str = Field(
        None,
        description='Note title'
    )
    view_url: str = Field(
        None,
        description='URL of the page with note preview'
    )


class NotesNoteComment(BaseModel):
    date: int = Field(
        None,
        description='Date when the comment has beed added in Unixtime'
    )
    id: int = Field(
        None,
        description='Comment ID'
    )
    message: str = Field(
        None,
        description='Comment text'
    )
    nid: int = Field(
        None,
        description='Note ID'
    )
    oid: int = Field(
        None,
        description='Note ID'
    )
    reply_to: typing.Optional[int] = Field(
        None,
        description='ID of replied comment '
    )
    uid: int = Field(
        None,
        description='Comment authors ID'
    )


class NotificationsFeedback(BaseModel):
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        None,
        description=''
    )
    from_id: typing.Optional[int] = Field(
        None,
        description='Reply authors ID'
    )
    geo: typing.Optional["BaseGeo"] = Field(
        None,
        description=''
    )
    id: typing.Optional[int] = Field(
        None,
        description='Item ID'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Reply text'
    )
    to_id: typing.Optional[int] = Field(
        None,
        description='Wall owners ID'
    )


class NotificationsNotification(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Date when the event has been occurred'
    )
    feedback: typing.Optional["NotificationsFeedback"] = Field(
        None,
        description=''
    )
    parent: typing.Optional["NotificationsNotification"] = Field(
        None,
        description=''
    )
    reply: typing.Optional["NotificationsReply"] = Field(
        None,
        description=''
    )
    type: typing.Optional[str] = Field(
        None,
        description='Notification type'
    )


class NotificationsNotificationItem(NotificationsNotification):
    pass


class WallWallpostToId(BaseModel):
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        None,
        description=''
    )
    comments: typing.Optional["BaseCommentsInfo"] = Field(
        None,
        description=''
    )
    copy_owner_id: typing.Optional[int] = Field(
        None,
        description='ID of the source post owner'
    )
    copy_post_id: typing.Optional[int] = Field(
        None,
        description='ID of the source post'
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date of publishing in Unixtime'
    )
    from_id: typing.Optional[int] = Field(
        None,
        description='Post author ID'
    )
    geo: typing.Optional["WallGeo"] = Field(
        None,
        description=''
    )
    id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    is_favorite: typing.Optional[bool] = Field(
        None,
        description='Information whether the post in favorites list'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='wall post ID (if comment)'
    )
    post_source: typing.Optional["WallPostSource"] = Field(
        None,
        description=''
    )
    post_type: typing.Optional["WallPostType"] = Field(
        None,
        description=''
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=''
    )
    signer_id: typing.Optional[int] = Field(
        None,
        description='Post signer ID'
    )
    text: typing.Optional[str] = Field(
        None,
        description='Post text'
    )
    to_id: typing.Optional[int] = Field(
        None,
        description='Wall owners ID'
    )


class VideoVideoType(enum.Enum):
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    LIVE = "live"
    SHORT_VIDEO = "short_video"


class LiveStreamStatus(enum.Enum):
    WAITING = "waiting"
    STARTED = "started"
    FINISHED = "finished"
    FAILED = "failed"
    UPCOMING = "upcoming"


class VideoVideo(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description="Video access key"
    )
    added: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="1 if video is added to user's albums"
    )
    adding_date: typing.Optional[int] = Field(
        None,
        description="Date when the video has been added in Unixtime"
    )
    balance: typing.Optional[int] = Field(
        None,
        description="Live donations balance"
    )
    can_add: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can add the video"
    )
    can_add_to_faves: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can add the video to favourites"
    )
    can_attach_link: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can attach action button to the video"
    )
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can comment the video"
    )
    can_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can edit the video"
    )
    can_like: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can like the video"
    )
    can_repost: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can repost the video"
    )
    can_subscribe: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Information whether current user can subscribe to author of the video"
    )
    comments: typing.Optional[int] = Field(
        None,
        description="Number of comments"
    )
    content_restricted: typing.Optional[int] = Field(
        None,
        description="Restriction code"
    )
    content_restricted_message: typing.Optional[str] = Field(
        None,
        description="Restriction text"
    )
    converting: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="1 if  video is being converted"
    )
    date: typing.Optional[int] = Field(
        None,
        description="Date when video has been uploaded in Unixtime"
    )
    description: typing.Optional[str] = Field(
        None,
        description="Video description"
    )
    duration: typing.Optional[int] = Field(
        None,
        description="Video duration in seconds"
    )
    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        None,
        description=""
    )
    height: typing.Optional[int] = Field(
        None,
        description="Video height"
    )
    id: typing.Optional[int] = Field(
        None,
        description="Video ID"
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        None,
        description=""
    )
    is_favorite: typing.Optional[bool] = Field(
        None,
        description="Whether video is added to bookmarks"
    )
    is_private: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="1 if video is private"
    )
    is_subscribed: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="1 if user is subscribed to author of the video"
    )
    likes: typing.Optional["BaseLikes"] = Field(
        None,
        description=""
    )
    live: typing.Optional["BasePropertyExists"] = Field(
        None,
        description="1 if the video is a live stream"
    )
    live_notify: typing.Optional["BaseBoolInt"] = Field(
        None,
        description="Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)"
    )
    live_start_time: typing.Optional[int] = Field(
        None,
        description="Date in Unixtime when the live stream is scheduled to start by the author"
    )
    live_status: typing.Optional["LiveStreamStatus"] = Field(
        None,
        description="Live stream status"
    )
    local_views: typing.Optional[int] = Field(
        None,
        description="If video is external, number of views on vk"
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description="Video owner ID"
    )
    platform: typing.Optional[str] = Field(
        None,
        description="External platform"
    )
    player: typing.Optional[str] = Field(
        None,
        description="Video embed URL"
    )
    processing: typing.Optional["BasePropertyExists"] = Field(
        None,
        description="Returns if the video is processing"
    )
    repeat: typing.Optional["BasePropertyExists"] = Field(
        None,
        description="Information whether the video is repeated"
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=""
    )
    spectators: typing.Optional[int] = Field(
        None,
        description="Number of spectators of the stream"
    )
    title: typing.Optional[str] = Field(
        None,
        description="Video title"
    )
    track_code: typing.Optional[str] = Field(
        None,
        description=""
    )
    type: typing.Optional["VideoVideoType"] = Field(
        None,
        description=""
    )
    upcoming: typing.Optional["BasePropertyExists"] = Field(
        None,
        description="1 if the video is an upcoming stream"
    )
    user_id: typing.Optional[int] = Field(
        None,
        description="ID of the user who uploaded the video if it was uploaded to a group by member"
    )
    views: typing.Optional[int] = Field(
        None,
        description="Number of views"
    )
    width: typing.Optional[int] = Field(
        None,
        description="Video width"
    )


class NotificationsNotificationsComment(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Date when the comment has been added in Unixtime'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Comment ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Author ID'
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    post: typing.Optional["WallWallpost"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Comment text'
    )
    topic: typing.Optional["BoardTopic"] = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideo"] = Field(
        None,
        description=''
    )


class NotificationsNotificationParent(
    WallWallpostToId,
    PhotosPhoto,
    BoardTopic,
    VideoVideo,
    NotificationsNotificationsComment
):
    pass


class NotificationsReply(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Date when the reply has been created in Unixtime'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Reply ID'
    )
    text: typing.Optional[int] = Field(
        None,
        description='Reply text'
    )


class ErrorCode(enum.IntEnum):
    notifications_disabled = 1
    flood_control_per_hour = 2
    flood_control_per_day = 3
    app_is_not_installed = 4


class NotificationsSendMessageError(BaseModel):
    code: typing.Optional["ErrorCode"] = Field(
        None,
        description='Error code'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Error description'
    )


class NotificationsSendMessageItem(BaseModel):
    error: typing.Optional["NotificationsSendMessageError"] = Field(
        None,
        description=''
    )
    status: typing.Optional[bool] = Field(
        None,
        description='Notification status'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class OauthError(BaseModel):
    error: str = Field(
        None,
        description='Error type'
    )
    error_description: str = Field(
        None,
        description='Error description'
    )
    redirect_uri: typing.Optional[str] = Field(
        None,
        description='URI for validation'
    )


class OrdersAmount(BaseModel):
    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = Field(
        None,
        description=''
    )
    currency: typing.Optional[str] = Field(
        None,
        description='Currency name'
    )


class OrdersAmountItem(BaseModel):
    amount: typing.Optional[float] = Field(
        None,
        description='Votes amount in users currency'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Amount description'
    )
    votes: typing.Optional[str] = Field(
        None,
        description='Votes number'
    )


class OrderStatus(enum.Enum):
    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    amount: str = Field(
        None,
        description='Amount'
    )
    app_order_id: str = Field(
        None,
        description='App order ID'
    )
    cancel_transaction_id: typing.Optional[str] = Field(
        None,
        description='Cancel transaction ID'
    )
    date: str = Field(
        None,
        description='Date of creation in Unixtime'
    )
    id: str = Field(
        None,
        description='Order ID'
    )
    item: str = Field(
        None,
        description='Order item'
    )
    receiver_id: str = Field(
        None,
        description='Receiver ID'
    )
    status: typing.Optional["OrderStatus"] = Field(
        None,
        description='Order status'
    )
    transaction_id: typing.Optional[str] = Field(
        None,
        description='Transaction ID'
    )
    user_id: str = Field(
        None,
        description='User ID'
    )


class OrdersSubscription(BaseModel):
    app_id: typing.Optional[int] = Field(
        None,
        description='Subscriptions application id'
    )
    application_name: typing.Optional[str] = Field(
        None,
        description='Subscriptions application name'
    )
    cancel_reason: typing.Optional[str] = Field(
        None,
        description='Cancel reason'
    )
    create_time: int = Field(
        None,
        description='Date of creation in Unixtime'
    )
    expire_time: typing.Optional[int] = Field(
        None,
        description='Subscription expiration time in Unixtime'
    )
    id: int = Field(
        None,
        description='Subscription ID'
    )
    item_id: str = Field(
        None,
        description='Subscription order item'
    )
    next_bill_time: typing.Optional[int] = Field(
        None,
        description='Date of next bill in Unixtime'
    )
    pending_cancel: typing.Optional[bool] = Field(
        None,
        description='Pending cancel state'
    )
    period: int = Field(
        None,
        description='Subscription period'
    )
    period_start_time: int = Field(
        None,
        description='Date of last period start in Unixtime'
    )
    photo_url: typing.Optional[str] = Field(
        None,
        description='Item photo image url'
    )
    price: int = Field(
        None,
        description='Subscription price'
    )
    status: str = Field(
        None,
        description='Subscription status'
    )
    test_mode: typing.Optional[bool] = Field(
        None,
        description='Is test subscription'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Subscription name'
    )
    trial_expire_time: typing.Optional[int] = Field(
        None,
        description='Date of trial expire in Unixtime'
    )
    update_time: int = Field(
        None,
        description='Date of last change in Unixtime'
    )


class OwnerStateState(enum.IntEnum):
    banned = 1
    adult = 2
    hidden = 3
    deleted = 4
    blacklisted = 5


class OwnerState(BaseModel):
    description: typing.Optional[str] = Field(
        None,
        description='wiki text to describe user state'
    )
    state: typing.Optional["OwnerStateState"] = Field(
        None,
        description=''
    )


class PagesPrivacySettings(enum.IntEnum):
    community_managers_only = 0
    community_members_only = 1
    everyone = 2


class PagesWikipage(BaseModel):
    creator_id: typing.Optional[int] = Field(
        None,
        description='Page creator ID'
    )
    creator_name: typing.Optional[str] = Field(
        None,
        description='Page creator name'
    )
    editor_id: typing.Optional[int] = Field(
        None,
        description='Last editor ID'
    )
    editor_name: typing.Optional[str] = Field(
        None,
        description='Last editor name'
    )
    group_id: int = Field(
        None,
        description='Community ID'
    )
    id: int = Field(
        None,
        description='Page ID'
    )
    title: str = Field(
        None,
        description='Page title'
    )
    views: int = Field(
        None,
        description='Views number'
    )
    who_can_edit: "PagesPrivacySettings" = Field(
        None,
        description='Edit settings of the page'
    )
    who_can_view: "PagesPrivacySettings" = Field(
        None,
        description='View settings of the page'
    )


class PagesWikipageFull(BaseModel):
    created: int = Field(
        None,
        description='Date when the page has been created in Unixtime'
    )
    creator_id: typing.Optional[int] = Field(
        None,
        description='Page creator ID'
    )
    current_user_can_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can edit the page'
    )
    current_user_can_edit_access: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can edit the page access settings'
    )
    edited: int = Field(
        None,
        description='Date when the page has been edited in Unixtime'
    )
    editor_id: typing.Optional[int] = Field(
        None,
        description='Last editor ID'
    )
    group_id: int = Field(
        None,
        description='Community ID'
    )
    html: typing.Optional[str] = Field(
        None,
        description='Page content, HTML'
    )
    id: int = Field(
        None,
        description='Page ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Owner ID'
    )
    parent: typing.Optional[str] = Field(
        None,
        description='Parent'
    )
    parent2: typing.Optional[str] = Field(
        None,
        description='Parent2'
    )
    source: typing.Optional[str] = Field(
        None,
        description='Page content, wiki'
    )
    title: str = Field(
        None,
        description='Page title'
    )
    url: typing.Optional[str] = Field(
        None,
        description='URL'
    )
    view_url: str = Field(
        None,
        description='URL of the page preview'
    )
    views: int = Field(
        None,
        description='Views number'
    )
    who_can_edit: "PagesPrivacySettings" = Field(
        None,
        description='Edit settings of the page'
    )
    who_can_view: "PagesPrivacySettings" = Field(
        None,
        description='View settings of the page'
    )


class PagesWikipageHistory(BaseModel):
    date: int = Field(
        None,
        description='Date when the page has been edited in Unixtime'
    )
    editor_id: int = Field(
        None,
        description='Last editor ID'
    )
    editor_name: str = Field(
        None,
        description='Last editor name'
    )
    id: int = Field(
        None,
        description='Version ID'
    )
    length: int = Field(
        None,
        description='Page size in bytes'
    )


class PhotosImage(BaseModel):
    height: typing.Optional[int] = Field(
        None,
        description='Height of the photo in px.'
    )
    type: typing.Optional["PhotosImageType"] = Field(
        None,
        description=''
    )
    url: typing.Optional[str] = Field(
        None,
        description='Photo URL.'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Width of the photo in px.'
    )


class PhotosImageType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


class PhotosPhotoAlbum(BaseModel):
    created: int = Field(
        None,
        description='Date when the album has been created in Unixtime'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Photo album description'
    )
    id: int = Field(
        None,
        description='Photo album ID'
    )
    owner_id: int = Field(
        None,
        description='Album owners ID'
    )
    size: int = Field(
        None,
        description='Photos number'
    )
    thumb: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    title: str = Field(
        None,
        description='Photo album title'
    )
    updated: int = Field(
        None,
        description='Date when the album has been updated last time in Unixtime'
    )


class PhotosPhotoAlbumFull(BaseModel):
    can_delete: typing.Optional[bool] = Field(
        None,
        description='album can delete'
    )
    can_upload: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can upload photo to the album'
    )
    comments_disabled: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether album comments are disabled'
    )
    created: int = Field(
        None,
        description='Date when the album has been created in Unixtime'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Photo album description'
    )
    id: int = Field(
        None,
        description='Photo album ID'
    )
    owner_id: int = Field(
        None,
        description='Album owners ID'
    )
    size: int = Field(
        None,
        description='Photos number'
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )
    thumb_id: typing.Optional[int] = Field(
        None,
        description='Thumb photo ID'
    )
    thumb_is_last: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the album thumb is last photo'
    )
    thumb_src: typing.Optional[str] = Field(
        None,
        description='URL of the thumb image'
    )
    title: str = Field(
        None,
        description='Photo album title'
    )
    updated: int = Field(
        None,
        description='Date when the album has been updated last time in Unixtime'
    )
    upload_by_admins_only: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether only community administrators can upload photos'
    )


PhotosPhotoFalseable = typing.Union[bool, str]


class PhotosPhotoFullXtrRealOffset(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the photo'
    )
    album_id: int = Field(
        None,
        description='Album ID'
    )
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    comments: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description='Date when uploaded'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Original photo height'
    )
    hidden: typing.Optional["BasePropertyExists"] = Field(
        None,
        description='Returns if the photo is hidden above the wall'
    )
    id: int = Field(
        None,
        description='Photo ID'
    )
    lat: typing.Optional[float] = Field(
        None,
        description='Latitude'
    )
    likes: typing.Optional["BaseLikes"] = Field(
        None,
        description=''
    )
    long: typing.Optional[float] = Field(
        None,
        description='Longitude'
    )
    owner_id: int = Field(
        None,
        description='Photo owners ID'
    )
    photo_1280: typing.Optional[str] = Field(
        None,
        description='URL of image with 1280 px width'
    )
    photo_130: typing.Optional[str] = Field(
        None,
        description='URL of image with 130 px width'
    )
    photo_2560: typing.Optional[str] = Field(
        None,
        description='URL of image with 2560 px width'
    )
    photo_604: typing.Optional[str] = Field(
        None,
        description='URL of image with 604 px width'
    )
    photo_75: typing.Optional[str] = Field(
        None,
        description='URL of image with 75 px width'
    )
    photo_807: typing.Optional[str] = Field(
        None,
        description='URL of image with 807 px width'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    real_offset: typing.Optional[int] = Field(
        None,
        description='Real position of the photo'
    )
    reposts: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )
    tags: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Photo caption'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='ID of the user who have uploaded the photo'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Original photo width'
    )


class PhotosPhotoSizes(BaseModel):
    height: int = Field(
        None,
        description='Height in px'
    )
    src: typing.Optional[str] = Field(
        None,
        description='URL of the image'
    )
    type: "PhotosPhotoSizesType" = Field(
        None,
        description=''
    )
    url: str = Field(
        None,
        description='URL of the image'
    )
    width: int = Field(
        None,
        description='Width in px'
    )


class PhotosPhotoSizesType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"


class PhotosPhotoTag(BaseModel):
    date: int = Field(
        None,
        description='Date when tag has been added in Unixtime'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Tagged description.'
    )
    id: int = Field(
        None,
        description='Tag ID'
    )
    placer_id: int = Field(
        None,
        description='ID of the tag creator'
    )
    tagged_name: str = Field(
        None,
        description='Tag description'
    )
    user_id: int = Field(
        None,
        description='Tagged user ID'
    )
    viewed: "BaseBoolInt" = Field(
        None,
        description='Information whether the tag is reviewed'
    )
    x: float = Field(
        None,
        description='Coordinate X of the left upper corner'
    )
    x2: float = Field(
        None,
        description='Coordinate X of the right lower corner'
    )
    y: float = Field(
        None,
        description='Coordinate Y of the left upper corner'
    )
    y2: float = Field(
        None,
        description='Coordinate Y of the right lower corner'
    )


class PhotosPhotoUpload(BaseModel):
    album_id: int = Field(
        None,
        description='Album ID'
    )
    fallback_upload_url: typing.Optional[str] = Field(
        None,
        description='Fallback URL if upload_url returned error'
    )
    group_id: typing.Optional[int] = Field(
        None,
        description='Group ID'
    )
    upload_url: str = Field(
        None,
        description='URL to upload photo'
    )
    user_id: int = Field(
        None,
        description='User ID'
    )


class PhotosPhotoXtrRealOffset(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the photo'
    )
    album_id: int = Field(
        None,
        description='Album ID'
    )
    date: int = Field(
        None,
        description='Date when uploaded'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Original photo height'
    )
    hidden: typing.Optional["BasePropertyExists"] = Field(
        None,
        description='Returns if the photo is hidden above the wall'
    )
    id: int = Field(
        None,
        description='Photo ID'
    )
    lat: typing.Optional[float] = Field(
        None,
        description='Latitude'
    )
    long: typing.Optional[float] = Field(
        None,
        description='Longitude'
    )
    owner_id: int = Field(
        None,
        description='Photo owners ID'
    )
    photo_1280: typing.Optional[str] = Field(
        None,
        description='URL of image with 1280 px width'
    )
    photo_130: typing.Optional[str] = Field(
        None,
        description='URL of image with 130 px width'
    )
    photo_2560: typing.Optional[str] = Field(
        None,
        description='URL of image with 2560 px width'
    )
    photo_604: typing.Optional[str] = Field(
        None,
        description='URL of image with 604 px width'
    )
    photo_75: typing.Optional[str] = Field(
        None,
        description='URL of image with 75 px width'
    )
    photo_807: typing.Optional[str] = Field(
        None,
        description='URL of image with 807 px width'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    real_offset: typing.Optional[int] = Field(
        None,
        description='Real position of the photo'
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Photo caption'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='ID of the user who have uploaded the photo'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Original photo width'
    )


class PhotosPhotoXtrTagInfo(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the photo'
    )
    album_id: int = Field(
        None,
        description='Album ID'
    )
    date: int = Field(
        None,
        description='Date when uploaded'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Original photo height'
    )
    id: int = Field(
        None,
        description='Photo ID'
    )
    lat: typing.Optional[float] = Field(
        None,
        description='Latitude'
    )
    long: typing.Optional[float] = Field(
        None,
        description='Longitude'
    )
    owner_id: int = Field(
        None,
        description='Photo owners ID'
    )
    photo_1280: typing.Optional[str] = Field(
        None,
        description='URL of image with 1280 px width'
    )
    photo_130: typing.Optional[str] = Field(
        None,
        description='URL of image with 130 px width'
    )
    photo_2560: typing.Optional[str] = Field(
        None,
        description='URL of image with 2560 px width'
    )
    photo_604: typing.Optional[str] = Field(
        None,
        description='URL of image with 604 px width'
    )
    photo_75: typing.Optional[str] = Field(
        None,
        description='URL of image with 75 px width'
    )
    photo_807: typing.Optional[str] = Field(
        None,
        description='URL of image with 807 px width'
    )
    placer_id: typing.Optional[int] = Field(
        None,
        description='ID of the tag creator'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description='Post ID'
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )
    tag_created: typing.Optional[int] = Field(
        None,
        description='Date when tag has been added in Unixtime'
    )
    tag_id: typing.Optional[int] = Field(
        None,
        description='Tag ID'
    )
    text: typing.Optional[str] = Field(
        None,
        description='Photo caption'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='ID of the user who have uploaded the photo'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Original photo width'
    )


class PhotosTagsSuggestionItem(BaseModel):
    buttons: typing.Optional[typing.List["PhotosTagsSuggestionItemButton"]] = Field(
        None,
        description=''
    )
    caption: typing.Optional[str] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    tags: typing.Optional[typing.List["PhotosPhotoTag"]] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )
    track_code: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional[str] = Field(
        None,
        description=''
    )


class PhotosTagsSuggestionItemButtonAction(enum.Enum):
    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class PhotosTagsSuggestionItemButtonStyle(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class PhotosTagsSuggestionItemButton(BaseModel):
    action: typing.Optional["PhotosTagsSuggestionItemButtonAction"] = Field(
        None,
        description=''
    )
    style: typing.Optional["PhotosTagsSuggestionItemButtonStyle"] = Field(
        None,
        description=''
    )
    title: typing.Optional[str] = Field(
        None,
        description=''
    )


class PodcastCover(BaseModel):
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        None,
        description=''
    )


class PodcastExternalData(BaseModel):
    cover: typing.Optional["PodcastCover"] = Field(
        None,
        description='Podcast cover'
    )
    owner_name: typing.Optional[str] = Field(
        None,
        description='Name of the podcasts owner community'
    )
    owner_url: typing.Optional[str] = Field(
        None,
        description='Url of the podcasts owner community'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Podcast title'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Url of the podcast page'
    )


class PollsAnswer(BaseModel):
    id: int = Field(
        None,
        description='Answer ID'
    )
    rate: float = Field(
        None,
        description='Answer rate in percents'
    )
    text: str = Field(
        None,
        description='Answer text'
    )
    votes: int = Field(
        None,
        description='Votes number'
    )


class PollsBackgroundType(enum.Enum):
    GRADIENT = "gradient"
    TILE = "tile"


class PollsBackground(BaseModel):
    angle: typing.Optional[int] = Field(
        None,
        description='Gradient angle with 0 on positive X axis'
    )
    color: typing.Optional[str] = Field(
        None,
        description='Hex color code without #'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Original height of pattern tile'
    )
    id: typing.Optional[int] = Field(
        None,
        description=''
    )
    images: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description='Pattern tiles'
    )
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    points: typing.Optional[typing.List["BaseGradientPoint"]] = Field(
        None,
        description='Gradient points'
    )
    type: typing.Optional["PollsBackgroundType"] = Field(
        None,
        description=''
    )
    width: typing.Optional[int] = Field(
        None,
        description='Original with of pattern tile'
    )


class PollsFriend(BaseModel):
    id: int = Field(
        None,
        description=''
    )


class PollsPoll(BaseModel):
    anonymous: typing.Optional["PollsPollAnonymous"] = Field(
        None,
        description=''
    )
    answer_id: typing.Optional[int] = Field(
        None,
        description='Current users answer ID'
    )
    answer_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description='Current users answer IDs'
    )
    answers: typing.List["PollsAnswer"] = Field(
        None,
        description=''
    )
    author_id: typing.Optional[int] = Field(
        None,
        description='Poll authors ID'
    )
    background: typing.Optional["PollsBackground"] = Field(
        None,
        description=''
    )
    can_edit: bool = Field(
        None,
        description=''
    )
    can_report: bool = Field(
        None,
        description=''
    )
    can_share: bool = Field(
        None,
        description=''
    )
    can_vote: bool = Field(
        None,
        description=''
    )
    closed: bool = Field(
        None,
        description=''
    )
    created: int = Field(
        None,
        description='Date when poll has been created in Unixtime'
    )
    disable_unvote: bool = Field(
        None,
        description=''
    )
    embed_hash: typing.Optional[str] = Field(
        None,
        description=''
    )
    end_date: int = Field(
        None,
        description=''
    )
    friends: typing.Optional[typing.List["PollsFriend"]] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Poll ID'
    )
    is_board: bool = Field(
        None,
        description=''
    )
    multiple: bool = Field(
        None,
        description='Information whether the poll with multiple choices'
    )
    owner_id: int = Field(
        None,
        description='Poll owners ID'
    )
    photo: typing.Optional["PollsBackground"] = Field(
        None,
        description=''
    )
    question: str = Field(
        None,
        description='Poll question'
    )
    votes: int = Field(
        None,
        description='Votes number'
    )


PollsPollAnonymous = typing.Optional[bool]  # Information whether the field is anonymous


class PollsVoters(BaseModel):
    answer_id: typing.Optional[int] = Field(
        None,
        description='Answer ID'
    )
    users: typing.Optional["PollsVotersUsers"] = Field(
        None,
        description=''
    )


class PollsVotersUsers(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Votes number'
    )
    items: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )


class PrettyCardsPrettyCard(BaseModel):
    button: typing.Optional[typing.Union["BaseLinkButton", str]] = Field(
        None,
        description='Button key'
    )
    button_text: typing.Optional[str] = Field(
        None,
        description='Button text in current language'
    )
    card_id: str = Field(
        None,
        description='Card ID (long int returned as string)'
    )
    images: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description=''
    )
    link_url: str = Field(
        None,
        description='Link URL'
    )
    photo: str = Field(
        None,
        description='Photo ID (format "<owner_id>_<media_id>")'
    )
    price: typing.Optional[str] = Field(
        None,
        description='Price if set (decimal number returned as string)'
    )
    price_old: typing.Optional[str] = Field(
        None,
        description='Old price if set (decimal number returned as string)'
    )
    title: str = Field(
        None,
        description='Title'
    )


class PrettyCardsPrettyCardOrError(PrettyCardsPrettyCard, BaseError):
    pass


class SearchHint(BaseModel):
    app: typing.Optional["AppsApp"] = Field(
        None,
        description=''
    )
    description: str = Field(
        None,
        description='Object description'
    )
    _global: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the object has been found globally'
    )
    group: typing.Optional["GroupsGroup"] = Field(
        None,
        description=''
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    profile: typing.Optional["UsersUserMin"] = Field(
        None,
        description=''
    )
    section: typing.Optional["SearchHintSection"] = Field(
        None,
        description=''
    )
    type: "SearchHintType" = Field(
        None,
        description=''
    )


class SearchHintSection(enum.Enum):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class SearchHintType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"


class SecureGiveEventStickerItem(BaseModel):
    status: typing.Optional[str] = Field(
        None,
        description=''
    )
    user_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class SecureLevel(BaseModel):
    level: typing.Optional[int] = Field(
        None,
        description='Level'
    )
    uid: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class SecureSetCounterItem(BaseModel):
    id: int = Field(
        None,
        description='User ID'
    )
    result: "BaseBoolInt" = Field(
        None,
        description=''
    )


class SecureSmsNotification(BaseModel):
    app_id: typing.Optional[str] = Field(
        None,
        description='Application ID'
    )
    date: typing.Optional[str] = Field(
        None,
        description='Date when message has been sent in Unixtime'
    )
    id: typing.Optional[str] = Field(
        None,
        description='Notification ID'
    )
    message: typing.Optional[str] = Field(
        None,
        description='Messsage text'
    )
    user_id: typing.Optional[str] = Field(
        None,
        description='User ID'
    )


class SecureTokenChecked(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Date when access_token has been generated in Unixtime'
    )
    expire: typing.Optional[int] = Field(
        None,
        description='Date when access_token will expire in Unixtime'
    )
    success: typing.Optional[int] = Field(
        None,
        description='Returns if successfully processed'
    )
    user_id: typing.Optional[int] = Field(
        None,
        description='User ID'
    )


class SecureTransaction(BaseModel):
    date: typing.Optional[int] = Field(
        None,
        description='Transaction date in Unixtime'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Transaction ID'
    )
    uid_from: typing.Optional[int] = Field(
        None,
        description='From ID'
    )
    uid_to: typing.Optional[int] = Field(
        None,
        description='To ID'
    )
    votes: typing.Optional[int] = Field(
        None,
        description='Votes number'
    )


class StatsActivity(BaseModel):
    comments: typing.Optional[int] = Field(
        None,
        description='Comments number'
    )
    copies: typing.Optional[int] = Field(
        None,
        description='Reposts number'
    )
    hidden: typing.Optional[int] = Field(
        None,
        description='Hidden from news count'
    )
    likes: typing.Optional[int] = Field(
        None,
        description='Likes number'
    )
    subscribed: typing.Optional[int] = Field(
        None,
        description='New subscribers count'
    )
    unsubscribed: typing.Optional[int] = Field(
        None,
        description='Unsubscribed count'
    )


class StatsCity(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Visitors number'
    )
    name: typing.Optional[str] = Field(
        None,
        description='City name'
    )
    value: typing.Optional[int] = Field(
        None,
        description='City ID'
    )


class StatsCountry(BaseModel):
    code: typing.Optional[str] = Field(
        None,
        description='Country code'
    )
    count: typing.Optional[int] = Field(
        None,
        description='Visitors number'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Country name'
    )
    value: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )


class StatsPeriod(BaseModel):
    activity: typing.Optional["StatsActivity"] = Field(
        None,
        description=''
    )
    period_from: typing.Optional[int] = Field(
        None,
        description='Unix timestamp'
    )
    period_to: typing.Optional[int] = Field(
        None,
        description='Unix timestamp'
    )
    reach: typing.Optional["StatsReach"] = Field(
        None,
        description=''
    )
    visitors: typing.Optional["StatsViews"] = Field(
        None,
        description=''
    )


class StatsReach(BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        None,
        description=''
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        None,
        description=''
    )
    mobile_reach: typing.Optional[int] = Field(
        None,
        description='Reach count from mobile devices'
    )
    reach: typing.Optional[int] = Field(
        None,
        description='Reach count'
    )
    reach_subscribers: typing.Optional[int] = Field(
        None,
        description='Subscribers reach count'
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )


class StatsSexAge(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Visitors number'
    )
    count_subscribers: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach_subscribers: typing.Optional[int] = Field(
        None,
        description=''
    )
    value: str = Field(
        None,
        description='Sex/age value'
    )


class StatsViews(BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        None,
        description=''
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        None,
        description=''
    )
    mobile_views: typing.Optional[int] = Field(
        None,
        description='Number of views from mobile devices'
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    views: typing.Optional[int] = Field(
        None,
        description='Views number'
    )
    visitors: typing.Optional[int] = Field(
        None,
        description='Visitors number'
    )


class StatsWallpostStat(BaseModel):
    hide: typing.Optional[int] = Field(
        None,
        description='Hidings number'
    )
    join_group: typing.Optional[int] = Field(
        None,
        description='People have joined the group'
    )
    links: typing.Optional[int] = Field(
        None,
        description='Link clickthrough'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach_ads: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach_subscribers: typing.Optional[int] = Field(
        None,
        description='Subscribers reach'
    )
    reach_subscribers_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach_total: typing.Optional[int] = Field(
        None,
        description='Total reach'
    )
    reach_total_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    reach_viral: typing.Optional[int] = Field(
        None,
        description=''
    )
    report: typing.Optional[int] = Field(
        None,
        description='Reports number'
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        None,
        description=''
    )
    to_group: typing.Optional[int] = Field(
        None,
        description='Clickthrough to community'
    )
    unsubscribe: typing.Optional[int] = Field(
        None,
        description='Unsubscribed members'
    )


class StatusStatus(BaseModel):
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='Status text'
    )


class StickersImageSet(BaseModel):
    base_url: str = Field(
        None,
        description='Base URL for images in set'
    )
    version: typing.Optional[int] = Field(
        None,
        description='Version number to be appended to the image URL'
    )


class StorageValue(BaseModel):
    key: str = Field(
        None,
        description=''
    )
    value: str = Field(
        None,
        description=''
    )


class ProductType(enum.Enum):
    STICKERS = "stickers"


class StoreProduct(BaseModel):
    active: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the product is active (1 - yes, 0 - no)'
    )
    has_animation: typing.Optional[bool] = Field(
        None,
        description='Information whether the product is an animated sticker pack (for stickers product type)'
    )
    icon: typing.Optional["StoreProductIcon"] = Field(
        None,
        description='Array of icon images or icon set object of the product (for stickers product type)'
    )
    id: int = Field(
        None,
        description='Id of the product'
    )
    is_new: typing.Optional[bool] = Field(
        None,
        description='Information whether sticker product wasnt used after being purchased'
    )
    payment_region: typing.Optional[str] = Field(
        None,
        description=''
    )
    previews: typing.Optional[typing.List["BaseImage"]] = Field(
        None,
        description='Array of preview images of the product (for stickers product type)'
    )
    promoted: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the product is promoted (1 - yes, 0 - no)'
    )
    purchase_date: typing.Optional[int] = Field(
        None,
        description='Date (Unix time) when the product was purchased'
    )
    purchased: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether the product is purchased (1 - yes, 0 - no)'
    )
    stickers: typing.Optional["BaseStickersList"] = Field(
        None,
        description=''
    )
    style_sticker_ids: typing.Optional[typing.List[int]] = Field(
        None,
        description='Array of style sticker ids (for sticker pack styles)'
    )
    subtitle: typing.Optional[str] = Field(
        None,
        description='Subtitle of the product'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Title of the product'
    )
    type: typing.Optional["ProductType"] = Field(
        None,
        description='Product type'
    )


StoreProductIcon = typing.List["BaseImage"]


class StoreStickersKeyword(BaseModel):
    promoted_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        None,
        description=''
    )
    stickers: typing.Optional[typing.List["StoreStickersKeywordSticker"]] = Field(
        None,
        description=''
    )
    user_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        None,
        description=''
    )
    words: typing.List[str] = Field(
        None,
        description=''
    )


class StoreStickersKeywordSticker(BaseModel):
    pack_id: int = Field(
        None,
        description='Pack id'
    )
    sticker_id: int = Field(
        None,
        description='Sticker id'
    )


StoreStickersKeywordStickers = BaseStickersList


class StoriesClickableArea(BaseModel):
    x: int = Field(
        None,
        description=''
    )
    y: int = Field(
        None,
        description=''
    )


class StoriesClickableStickerStyle(enum.Enum):
    TRANSPARENT = "transparent"
    BLUE_GRADIENT = "blue_gradient"
    RED_GRADIENT = "red_gradient"
    UNDERLINE = "underline"
    BLUE = "blue"
    GREEN = "green"
    WHITE = "white"
    QUESTION_REPLY = "question_reply"
    LIGHT = "light"
    IMPRESSIVE = "impressive"


class StoriesClickableStickerType(enum.Enum):
    HASHTAG = "hashtag"
    MENTION = "mention"
    LINK = "link"
    QUESTION = "question"
    PLACE = "place"
    MARKET_ITEM = "market_item"
    MUSIC = "music"
    STORY_REPLY = "story_reply"
    OWNER = "owner"
    POST = "post"
    POLL = "poll"
    STICKER = "sticker"
    APP = "app"
    SITUATIONAL_THEME = "situational_theme"


class StoriesClickableStickerSubtype(enum.Enum):
    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class StoriesClickableSticker(BaseModel):
    app: typing.Optional["AppsAppMin"] = Field(
        None,
        description=''
    )
    app_context: typing.Optional[str] = Field(
        None,
        description='Additional context for app sticker'
    )
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    audio_start_time: typing.Optional[int] = Field(
        None,
        description=''
    )
    clickable_area: typing.List["StoriesClickableArea"] = Field(
        None,
        description=''
    )
    color: typing.Optional[str] = Field(
        None,
        description='Color, hex format'
    )
    has_new_interactions: typing.Optional[bool] = Field(
        None,
        description='Whether current user has unread interaction with this app'
    )
    hashtag: typing.Optional[str] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Clickable sticker ID'
    )
    is_broadcast_notify_allowed: typing.Optional[bool] = Field(
        None,
        description='Whether current user allowed broadcast notify from this app'
    )
    link_object: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    market_item: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    mention: typing.Optional[str] = Field(
        None,
        description=''
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    place_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    poll: typing.Optional["PollsPoll"] = Field(
        None,
        description=''
    )
    post_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    post_owner_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    question: typing.Optional[str] = Field(
        None,
        description=''
    )
    question_button: typing.Optional[str] = Field(
        None,
        description=''
    )
    situational_app_url: typing.Optional[str] = Field(
        None,
        description=''
    )
    situational_theme_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    sticker_id: typing.Optional[int] = Field(
        None,
        description='Sticker ID'
    )
    sticker_pack_id: typing.Optional[int] = Field(
        None,
        description='Sticker pack ID'
    )
    story_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    style: typing.Optional["StoriesClickableStickerStyle"] = Field(
        None,
        description=''
    )
    subtype: typing.Optional["StoriesClickableStickerSubtype"] = Field(
        None,
        description=''
    )
    tooltip_text: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional["StoriesClickableStickerType"] = Field(
        None,
        description=''
    )


class StoriesClickableStickers(BaseModel):
    clickable_stickers: typing.List["StoriesClickableSticker"] = Field(
        None,
        description=''
    )
    original_height: int = Field(
        None,
        description=''
    )
    original_width: int = Field(
        None,
        description=''
    )


class FeedItemType(enum.Enum):
    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    COMMUNITY_GROUPED_STORIES = "community_grouped_stories"
    APP_GROUPED_STORIES = "app_grouped_stories"
    BIRTHDAY = "birthday"
    DISCOVER = "discover"
    ADVICES = "advices"


class StoriesFeedItem(BaseModel):
    app: typing.Optional["AppsAppMin"] = Field(
        None,
        description='App, which stories has been grouped (for type app_grouped_stories)'
    )
    birthday_user_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    grouped: typing.Optional[typing.List["StoriesFeedItem"]] = Field(
        None,
        description='Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)'
    )
    has_unseen: typing.Optional[bool] = Field(
        None,
        description=''
    )
    id: typing.Optional[str] = Field(
        None,
        description=''
    )
    name: typing.Optional[str] = Field(
        None,
        description=''
    )
    promo_data: typing.Optional["StoriesPromoBlock"] = Field(
        None,
        description='Additional data for promo stories (for type promo_stories)'
    )
    stories: typing.Optional[typing.List["StoriesStory"]] = Field(
        None,
        description='Author stories'
    )
    track_code: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional["FeedItemType"] = Field(
        None,
        description='Type of Feed Item'
    )


class StoriesPromoBlock(BaseModel):
    name: str = Field(
        None,
        description='Promo story title'
    )
    not_animated: bool = Field(
        None,
        description='Hide animation for promo story'
    )
    photo_100: str = Field(
        None,
        description='RL of square photo of the story with 100 pixels in width'
    )
    photo_50: str = Field(
        None,
        description='RL of square photo of the story with 50 pixels in width'
    )


class StoriesReplies(BaseModel):
    count: int = Field(
        None,
        description='Replies number.'
    )
    new: typing.Optional[int] = Field(
        None,
        description='New replies number.'
    )


class StoriesStatLine(BaseModel):
    counter: typing.Optional[int] = Field(
        None,
        description=''
    )
    is_unavailable: typing.Optional[bool] = Field(
        None,
        description=''
    )
    name: str = Field(
        None,
        description=''
    )


class StoriesStory(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for private object.'
    )
    birthday_wish_user_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    can_ask: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether story has question sticker and current user can send question to the author'
    )
    can_ask_anonymous: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether story has question sticker and current user can send anonymous question to the author'
    )
    can_comment: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment the story (0 - no, 1 - yes).'
    )
    can_hide: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can hide the story (0 - no, 1 - yes).'
    )
    can_like: typing.Optional[bool] = Field(
        None,
        description='Information whether current user can like the story.'
    )
    can_reply: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can reply to the story (0 - no, 1 - yes).'
    )
    can_see: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can see the story (0 - no, 1 - yes).'
    )
    can_share: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can share the story (0 - no, 1 - yes).'
    )
    can_use_in_narrative: typing.Optional[bool] = Field(
        None,
        description=''
    )
    clickable_stickers: typing.Optional["StoriesClickableStickers"] = Field(
        None,
        description=''
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when story has been added in Unixtime.'
    )
    expires_at: typing.Optional[int] = Field(
        None,
        description='Story expiration time. Unixtime.'
    )
    first_narrative_title: typing.Optional[str] = Field(
        None,
        description=''
    )
    id: int = Field(
        None,
        description='Story ID.'
    )
    is_deleted: typing.Optional[bool] = Field(
        None,
        description='Information whether the story is deleted (false - no, true - yes).'
    )
    is_expired: typing.Optional[bool] = Field(
        None,
        description='Information whether the story is expired (false - no, true - yes).'
    )
    link: typing.Optional["StoriesStoryLink"] = Field(
        None,
        description=''
    )
    narratives_count: typing.Optional[int] = Field(
        None,
        description=''
    )
    owner_id: int = Field(
        None,
        description='Story owners ID.'
    )
    parent_story: typing.Optional["StoriesStory"] = Field(
        None,
        description=''
    )
    parent_story_access_key: typing.Optional[str] = Field(
        None,
        description='Access key for private object.'
    )
    parent_story_id: typing.Optional[int] = Field(
        None,
        description='Parent story ID.'
    )
    parent_story_owner_id: typing.Optional[int] = Field(
        None,
        description='Parent story owners ID.'
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    replies: typing.Optional["StoriesReplies"] = Field(
        None,
        description='Replies counters to current story.'
    )
    seen: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user has seen the story or not (0 - no, 1 - yes).'
    )
    type: typing.Optional["StoriesStoryType"] = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideoFull"] = Field(
        None,
        description=''
    )
    views: typing.Optional[int] = Field(
        None,
        description='Views number.'
    )


class StoriesStoryLink(BaseModel):
    link_url_target: typing.Optional[str] = Field(
        None,
        description='How to open url'
    )
    text: str = Field(
        None,
        description='Link text'
    )
    url: str = Field(
        None,
        description='Link URL'
    )


class StoriesStoryStats(BaseModel):
    answer: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    bans: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    likes: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    open_link: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    replies: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    shares: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    subscribers: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )
    views: "StoriesStoryStatsStat" = Field(
        None,
        description=''
    )


class StoriesStoryStatsStat(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Stat value'
    )
    state: "StoriesStoryStatsState" = Field(
        None,
        description=''
    )


class StoriesStoryStatsState(enum.Enum):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"


class StoriesUploadLinkText(enum.Enum):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"


class StoriesViewersItem(BaseModel):
    is_liked: bool = Field(
        None,
        description='user has like for this object'
    )
    user: typing.Optional["UsersUserFull"] = Field(
        None,
        description=''
    )
    user_id: int = Field(
        None,
        description='user id'
    )


class UsersCareer(BaseModel):
    city_id: typing.Optional[int] = Field(
        None,
        description='City ID'
    )
    city_name: typing.Optional[str] = Field(
        None,
        description='City name'
    )
    company: typing.Optional[str] = Field(
        None,
        description='Company name'
    )
    country_id: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )
    _from: typing.Optional[int] = Field(
        None,
        description='From year'
    )
    group_id: typing.Optional[int] = Field(
        None,
        description='Community ID'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Career ID'
    )
    position: typing.Optional[str] = Field(
        None,
        description='Position'
    )
    until: typing.Optional[int] = Field(
        None,
        description='Till year'
    )


class UsersExports(BaseModel):
    facebook: typing.Optional[int] = Field(
        None,
        description=''
    )
    livejournal: typing.Optional[int] = Field(
        None,
        description=''
    )
    twitter: typing.Optional[int] = Field(
        None,
        description=''
    )


class UsersFields(enum.Enum):
    FIRST_NAME_NOM = "first_name_nom"
    FIRST_NAME_GEN = "first_name_gen"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_INS = "first_name_ins"
    FIRST_NAME_ABL = "first_name_abl"
    LAST_NAME_NOM = "last_name_nom"
    LAST_NAME_GEN = "last_name_gen"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_INS = "last_name_ins"
    LAST_NAME_ABL = "last_name_abl"
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    BDATE_VISIBILITY = "bdate_visibility"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO = "photo"
    PHOTO_REC = "photo_rec"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_BIG = "photo_big"
    PHOTO_MEDIUM = "photo_medium"
    PHOTO_MEDIUM_REC = "photo_medium_rec"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    THIRD_PARTY_BUTTONS = "third_party_buttons"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    LANGUAGE = "language"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    ONLINE_INFO = "online_info"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    WALL_DEFAULT = "wall_default"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    IS_NO_INDEX = "is_no_index"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEE_GIFTS = "can_see_gifts"
    WORK = "work"
    PLACES = "places"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_DOC = "can_upload_doc"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    VIDEO_LIVE = "video_live"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    CAN_SEE_WISHES = "can_see_wishes"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"


class UsersLastSeen(BaseModel):
    platform: typing.Optional[int] = Field(
        None,
        description='Type of the platform that used for the last authorization'
    )
    time: typing.Optional[int] = Field(
        None,
        description='Last visit date (in Unix time)'
    )


class UsersMilitary(BaseModel):
    country_id: int = Field(
        None,
        description='Country ID'
    )
    _from: typing.Optional[int] = Field(
        None,
        description='From year'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Military ID'
    )
    unit: str = Field(
        None,
        description='Unit name'
    )
    unit_id: int = Field(
        None,
        description='Unit ID'
    )
    until: typing.Optional[int] = Field(
        None,
        description='Till year'
    )


class UsersOccupation(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='ID of school, university, company group'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Name of occupation'
    )
    type: typing.Optional[str] = Field(
        None,
        description='Type of occupation'
    )


class UsersOnlineInfoStatus(enum.Enum):
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class UsersOnlineInfo(BaseModel):
    app_id: typing.Optional[int] = Field(
        None,
        description='Application id from which user is currently online or was last seen online'
    )
    is_mobile: typing.Optional[bool] = Field(
        None,
        description='Is user online from desktop app or mobile app'
    )
    is_online: typing.Optional[bool] = Field(
        None,
        description='Whether user is currently online or not'
    )
    last_seen: typing.Optional[int] = Field(
        None,
        description='Last time we saw user being active'
    )
    status: typing.Optional["UsersOnlineInfoStatus"] = Field(
        None,
        description='In case user online is not visible, it indicates approximate timeframe of user online'
    )
    visible: bool = Field(
        None,
        description='Whether you can see real online status of user or not'
    )


class UsersPersonal(BaseModel):
    alcohol: typing.Optional[int] = Field(
        None,
        description='Users views on alcohol'
    )
    inspired_by: typing.Optional[str] = Field(
        None,
        description='Users inspired by'
    )
    langs: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    life_main: typing.Optional[int] = Field(
        None,
        description='Users personal priority in life'
    )
    people_main: typing.Optional[int] = Field(
        None,
        description='Users personal priority in people'
    )
    political: typing.Optional[int] = Field(
        None,
        description='Users political views'
    )
    religion: typing.Optional[str] = Field(
        None,
        description='Users religion'
    )
    religion_id: typing.Optional[int] = Field(
        None,
        description='Users religion id'
    )
    smoking: typing.Optional[int] = Field(
        None,
        description='Users views on smoking'
    )


class RelativeType(enum.Enum):
    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class UsersRelative(BaseModel):
    birth_date: typing.Optional[str] = Field(
        None,
        description='Date of child birthday (format dd.mm.yyyy)'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Relative ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Name of relative'
    )
    type: typing.Optional["RelativeType"] = Field(
        None,
        description='Relative type'
    )


class UsersSchool(BaseModel):
    city: typing.Optional[int] = Field(
        None,
        description='City ID'
    )
    _class: typing.Optional[str] = Field(
        None,
        description='School class letter'
    )
    country: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )
    id: typing.Optional[str] = Field(
        None,
        description='School ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='School name'
    )
    speciality: typing.Optional[str] = Field(
        None,
        description=''
    )
    type: typing.Optional[int] = Field(
        None,
        description='School type ID'
    )
    type_str: typing.Optional[str] = Field(
        None,
        description='School type name'
    )
    year_from: typing.Optional[int] = Field(
        None,
        description='Year the user started to study'
    )
    year_graduated: typing.Optional[int] = Field(
        None,
        description='Graduation year'
    )
    year_to: typing.Optional[int] = Field(
        None,
        description='Year the user finished to study'
    )


class UsersSubscriptionsItem(UsersUserXtrType, GroupsGroupFull):
    pass


class UsersUniversity(BaseModel):
    chair: typing.Optional[int] = Field(
        None,
        description='Chair ID'
    )
    chair_name: typing.Optional[str] = Field(
        None,
        description='Chair name'
    )
    city: typing.Optional[int] = Field(
        None,
        description='City ID'
    )
    country: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )
    education_form: typing.Optional[str] = Field(
        None,
        description='Education form'
    )
    education_status: typing.Optional[str] = Field(
        None,
        description='Education status'
    )
    faculty: typing.Optional[int] = Field(
        None,
        description='Faculty ID'
    )
    faculty_name: typing.Optional[str] = Field(
        None,
        description='Faculty name'
    )
    graduation: typing.Optional[int] = Field(
        None,
        description='Graduation year'
    )
    id: typing.Optional[int] = Field(
        None,
        description='University ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='University name'
    )
    university_group_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class UsersUserConnections(BaseModel):
    facebook: str = Field(
        None,
        description='Users Facebook account'
    )
    facebook_name: typing.Optional[str] = Field(
        None,
        description='Users Facebook name'
    )
    instagram: str = Field(
        None,
        description='Users Instagram account'
    )
    livejournal: typing.Optional[str] = Field(
        None,
        description='Users Livejournal account'
    )
    skype: str = Field(
        None,
        description='Users Skype nickname'
    )
    twitter: str = Field(
        None,
        description='Users Twitter account'
    )


class UsersUserCounters(BaseModel):
    albums: typing.Optional[int] = Field(
        None,
        description='Albums number'
    )
    articles: typing.Optional[int] = Field(
        None,
        description=''
    )
    audios: typing.Optional[int] = Field(
        None,
        description='Audios number'
    )
    badges: typing.Optional[int] = Field(
        None,
        description='Badges number'
    )
    clips: typing.Optional[int] = Field(
        None,
        description=''
    )
    clips_followers: typing.Optional[int] = Field(
        None,
        description=''
    )
    followers: typing.Optional[int] = Field(
        None,
        description='Followers number'
    )
    friends: typing.Optional[int] = Field(
        None,
        description='Friends number'
    )
    gifts: typing.Optional[int] = Field(
        None,
        description='Gifts number'
    )
    groups: typing.Optional[int] = Field(
        None,
        description='Communities number'
    )
    mutual_friends: typing.Optional[int] = Field(
        None,
        description=''
    )
    new_photo_tags: typing.Optional[int] = Field(
        None,
        description=''
    )
    new_recognition_tags: typing.Optional[int] = Field(
        None,
        description=''
    )
    notes: typing.Optional[int] = Field(
        None,
        description='Notes number'
    )
    online_friends: typing.Optional[int] = Field(
        None,
        description='Online friends number'
    )
    pages: typing.Optional[int] = Field(
        None,
        description='Public pages number'
    )
    photos: typing.Optional[int] = Field(
        None,
        description='Photos number'
    )
    podcasts: typing.Optional[int] = Field(
        None,
        description=''
    )
    posts: typing.Optional[int] = Field(
        None,
        description=''
    )
    subscriptions: typing.Optional[int] = Field(
        None,
        description='Subscriptions number'
    )
    user_photos: typing.Optional[int] = Field(
        None,
        description='Number of photos with user'
    )
    user_videos: typing.Optional[int] = Field(
        None,
        description='Number of videos with user'
    )
    videos: typing.Optional[int] = Field(
        None,
        description='Videos number'
    )
    wishes: typing.Optional[int] = Field(
        None,
        description=''
    )


class UsersUserRelation(enum.IntEnum):
    not_specified = 0
    single = 1
    in_a_relationship = 2
    engaged = 3
    married = 4
    complicated = 5
    actively_searching = 6
    in_love = 7
    in_a_civil_union = 8


class UsersUserType(enum.Enum):
    PROFILE = "profile"


class UsersUsersArray(BaseModel):
    count: int = Field(
        None,
        description='Users number'
    )
    items: typing.List[int] = Field(
        None,
        description=''
    )


class UtilsDomainResolved(BaseModel):
    group_id: typing.Optional[int] = Field(
        None,
        description='Group ID'
    )
    object_id: typing.Optional[int] = Field(
        None,
        description='Object ID'
    )
    type: typing.Optional["UtilsDomainResolvedType"] = Field(
        None,
        description=''
    )


class UtilsDomainResolvedType(enum.Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for private stats'
    )
    key: typing.Optional[str] = Field(
        None,
        description='Link key (characters after vk.cc/)'
    )
    short_url: typing.Optional[str] = Field(
        None,
        description='Short link URL'
    )
    timestamp: typing.Optional[int] = Field(
        None,
        description='Creation time in Unixtime'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Full URL'
    )
    views: typing.Optional[int] = Field(
        None,
        description='Total views number'
    )


class UtilsLinkChecked(BaseModel):
    link: typing.Optional[str] = Field(
        None,
        description='Link URL'
    )
    status: typing.Optional["UtilsLinkCheckedStatus"] = Field(
        None,
        description=''
    )


class UtilsLinkCheckedStatus(enum.Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
    key: typing.Optional[str] = Field(
        None,
        description='Link key (characters after vk.cc/)'
    )
    stats: typing.Optional[typing.List["UtilsStats"]] = Field(
        None,
        description=''
    )


class UtilsLinkStatsExtended(BaseModel):
    key: typing.Optional[str] = Field(
        None,
        description='Link key (characters after vk.cc/)'
    )
    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = Field(
        None,
        description=''
    )


class UtilsShortLink(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for private stats'
    )
    key: typing.Optional[str] = Field(
        None,
        description='Link key (characters after vk.cc/)'
    )
    short_url: typing.Optional[str] = Field(
        None,
        description='Short link URL'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Full URL'
    )


class UtilsStats(BaseModel):
    timestamp: typing.Optional[int] = Field(
        None,
        description='Start time'
    )
    views: typing.Optional[int] = Field(
        None,
        description='Total views number'
    )


class UtilsStatsCity(BaseModel):
    city_id: typing.Optional[int] = Field(
        None,
        description='City ID'
    )
    views: typing.Optional[int] = Field(
        None,
        description='Views number'
    )


class UtilsStatsCountry(BaseModel):
    country_id: typing.Optional[int] = Field(
        None,
        description='Country ID'
    )
    views: typing.Optional[int] = Field(
        None,
        description='Views number'
    )


class UtilsStatsExtended(BaseModel):
    cities: typing.Optional[typing.List["UtilsStatsCity"]] = Field(
        None,
        description=''
    )
    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = Field(
        None,
        description=''
    )
    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = Field(
        None,
        description=''
    )
    timestamp: typing.Optional[int] = Field(
        None,
        description='Start time'
    )
    views: typing.Optional[int] = Field(
        None,
        description='Total views number'
    )


class UtilsStatsSexAge(BaseModel):
    age_range: typing.Optional[str] = Field(
        None,
        description='Age denotation'
    )
    female: typing.Optional[int] = Field(
        None,
        description=' Views by female users'
    )
    male: typing.Optional[int] = Field(
        None,
        description=' Views by male users'
    )


class VideoLiveInfo(BaseModel):
    enabled: "BaseBoolInt" = Field(
        None,
        description=''
    )
    is_notifications_blocked: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )


class VideoLiveSettings(BaseModel):
    can_rewind: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='If user car rewind live or not'
    )
    is_endless: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='If live is endless or not'
    )
    max_duration: typing.Optional[int] = Field(
        None,
        description='Max possible time for rewind'
    )


class VideoSaveResult(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Video access key'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Video description'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Video owner ID'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Video title'
    )
    upload_url: typing.Optional[str] = Field(
        None,
        description='URL for the video uploading'
    )
    video_id: typing.Optional[int] = Field(
        None,
        description='Video ID'
    )


class VideoVideoAlbum(BaseModel):
    id: int = Field(
        None,
        description='Album ID'
    )
    owner_id: int = Field(
        None,
        description='Album owners ID'
    )
    title: str = Field(
        None,
        description='Album title'
    )


class VideoVideoAlbumFull(VideoVideoAlbum):
    count: int = Field(
        None,
        description='Total number of videos in album'
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        None,
        description='Album cover image in different sizes'
    )
    image_blur: typing.Optional["BasePropertyExists"] = Field(
        None,
        description='Need blur album thumb or not'
    )
    is_system: typing.Optional["BasePropertyExists"] = Field(
        None,
        description='Information whether album is system'
    )
    updated_time: int = Field(
        None,
        description='Date when the album has been updated last time in Unixtime'
    )


class VideoVideoFiles(BaseModel):
    external: typing.Optional[str] = Field(
        None,
        description='URL of the external player'
    )
    flv_320: typing.Optional[str] = Field(
        None,
        description='URL of the flv file with 320p quality'
    )
    mp4_1080: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 1080p quality'
    )
    mp4_144: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 144p quality'
    )
    mp4_1440: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 2K quality'
    )
    mp4_2160: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 4K quality'
    )
    mp4_240: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 240p quality'
    )
    mp4_360: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 360p quality'
    )
    mp4_480: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 480p quality'
    )
    mp4_720: typing.Optional[str] = Field(
        None,
        description='URL of the mpeg4 file with 720p quality'
    )


class VideoVideoFull(VideoVideo):
    files: typing.Optional["VideoVideoFiles"] = Field(
        None,
        description=''
    )
    live_settings: typing.Optional["VideoLiveSettings"] = Field(
        None,
        description='Settings for live stream'
    )
    trailer: typing.Optional["VideoVideoFiles"] = Field(
        None,
        description=''
    )


class VideoVideoImage(BaseImage):
    with_padding: typing.Optional["BasePropertyExists"] = Field(
        None,
        description=''
    )


class WallAppPost(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Application ID'
    )
    name: typing.Optional[str] = Field(
        None,
        description='Application name'
    )
    photo_130: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 130 px in width'
    )
    photo_604: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 604 px in width'
    )


class WallAttachedNote(BaseModel):
    can_comment: typing.Optional[int] = Field(
        None,
        description=''
    )
    comments: int = Field(
        None,
        description='Comments number'
    )
    date: int = Field(
        None,
        description='Date when the note has been created in Unixtime'
    )
    id: int = Field(
        None,
        description='Note ID'
    )
    owner_id: int = Field(
        None,
        description='Note owners ID'
    )
    privacy_comment: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    privacy_view: typing.Optional[typing.List[str]] = Field(
        None,
        description=''
    )
    read_comments: int = Field(
        None,
        description='Read comments number'
    )
    text: typing.Optional[str] = Field(
        None,
        description='Note text'
    )
    text_wiki: typing.Optional[str] = Field(
        None,
        description='Note wiki text'
    )
    title: str = Field(
        None,
        description='Note title'
    )
    view_url: str = Field(
        None,
        description='URL of the page with note preview'
    )


class WallCommentAttachment(BaseModel):
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    doc: typing.Optional["DocsDoc"] = Field(
        None,
        description=''
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    market: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        None,
        description=''
    )
    note: typing.Optional["WallAttachedNote"] = Field(
        None,
        description=''
    )
    page: typing.Optional["PagesWikipageFull"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    sticker: typing.Optional["BaseSticker"] = Field(
        None,
        description=''
    )
    type: "WallCommentAttachmentType" = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideo"] = Field(
        None,
        description=''
    )


class WallCommentAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


class PlaceType(enum.Enum):
    PLACE = "place"
    POINT = "point"


class WallGeo(BaseModel):
    coordinates: typing.Optional[str] = Field(
        None,
        description='Coordinates as string. <latitude> <longtitude>'
    )
    place: typing.Optional["BasePlace"] = Field(
        None,
        description=''
    )
    showmap: typing.Optional[int] = Field(
        None,
        description='Information whether a map is showed'
    )
    type: typing.Optional["PlaceType"] = Field(
        None,
        description='Place type'
    )


class WallGetFilter(enum.Enum):
    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


class WallGraffiti(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for graffiti'
    )
    height: typing.Optional[int] = Field(
        None,
        description='Graffiti height'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Graffiti ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Graffiti owners ID'
    )
    photo_200: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 200 px in width'
    )
    photo_586: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 586 px in width'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Graffiti URL'
    )
    width: typing.Optional[int] = Field(
        None,
        description='Graffiti width'
    )


class WallPostCopyright(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description=''
    )
    link: str = Field(
        None,
        description=''
    )
    name: str = Field(
        None,
        description=''
    )
    type: str = Field(
        None,
        description=''
    )


class WallPostSource(BaseModel):
    data: typing.Optional[str] = Field(
        None,
        description='Additional data'
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    platform: typing.Optional[str] = Field(
        None,
        description='Platform name'
    )
    type: typing.Optional["WallPostSourceType"] = Field(
        None,
        description=''
    )
    url: typing.Optional[str] = Field(
        None,
        description='URL to an external site used to publish the post'
    )


class WallPostSourceType(enum.Enum):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class WallPostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    POST_ADS = "post_ads"
    PHOTO = "photo"
    VIDEO = "video"


class WallPostedPhoto(BaseModel):
    id: typing.Optional[int] = Field(
        None,
        description='Photo ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Photo owners ID'
    )
    photo_130: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 130 px in width'
    )
    photo_604: typing.Optional[str] = Field(
        None,
        description='URL of the preview image with 604 px in width'
    )


class WallViews(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Count'
    )


class WallWallComment(BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        None,
        description=''
    )
    can_edit: typing.Optional["BaseBoolInt"] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description='Date when the comment has been added in Unixtime'
    )
    deleted: typing.Optional[bool] = Field(
        None,
        description=''
    )
    donut: typing.Optional["WallWallCommentDonut"] = Field(
        None,
        description=''
    )
    from_id: int = Field(
        None,
        description='Author ID'
    )
    id: int = Field(
        None,
        description='Comment ID'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    parents_stack: typing.Optional[typing.List[int]] = Field(
        None,
        description=''
    )
    photo_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    pid: typing.Optional[int] = Field(
        None,
        description='Photo ID'
    )
    post_id: typing.Optional[int] = Field(
        None,
        description=''
    )
    real_offset: typing.Optional[int] = Field(
        None,
        description='Real position of the comment'
    )
    reply_to_comment: typing.Optional[int] = Field(
        None,
        description='Replied comment ID'
    )
    reply_to_user: typing.Optional[int] = Field(
        None,
        description='Replied user ID'
    )
    text: str = Field(
        None,
        description='Comment text'
    )
    thread: typing.Optional["CommentThread"] = Field(
        None,
        description=''
    )
    video_id: typing.Optional[int] = Field(
        None,
        description=''
    )


class WallWallCommentDonut(BaseModel):
    is_don: typing.Optional[bool] = Field(
        None,
        description='Means commentator is donator'
    )
    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = Field(
        None,
        description=''
    )


class WallWallCommentDonutPlaceholder(BaseModel):
    text: str = Field(
        None,
        description=''
    )


class WallWallpostAttachment(BaseModel):
    access_key: typing.Optional[str] = Field(
        None,
        description='Access key for the audio'
    )
    album: typing.Optional["PhotosPhotoAlbum"] = Field(
        None,
        description=''
    )
    app: typing.Optional["WallAppPost"] = Field(
        None,
        description=''
    )
    audio: typing.Optional["AudioAudio"] = Field(
        None,
        description=''
    )
    doc: typing.Optional["DocsDoc"] = Field(
        None,
        description=''
    )
    event: typing.Optional["EventsEventAttach"] = Field(
        None,
        description=''
    )
    graffiti: typing.Optional["WallGraffiti"] = Field(
        None,
        description=''
    )
    group: typing.Optional["GroupsGroupAttach"] = Field(
        None,
        description=''
    )
    link: typing.Optional["BaseLink"] = Field(
        None,
        description=''
    )
    market: typing.Optional["MarketMarketItem"] = Field(
        None,
        description=''
    )
    market_album: typing.Optional["MarketMarketAlbum"] = Field(
        None,
        description=''
    )
    note: typing.Optional["NotesNote"] = Field(
        None,
        description=''
    )
    page: typing.Optional["PagesWikipageFull"] = Field(
        None,
        description=''
    )
    photo: typing.Optional["PhotosPhoto"] = Field(
        None,
        description=''
    )
    poll: typing.Optional["PollsPoll"] = Field(
        None,
        description=''
    )
    posted_photo: typing.Optional["WallPostedPhoto"] = Field(
        None,
        description=''
    )
    type: "WallWallpostAttachmentType" = Field(
        None,
        description=''
    )
    video: typing.Optional["VideoVideoFull"] = Field(
        None,
        description=''
    )


class WallWallpostAttachmentType(enum.Enum):
    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    MARKET_ALBUM = "market_album"
    MARKET = "market"
    EVENT = "event"
    DONUT_LINK = "donut_link"
    ARTICLE = "article"
    TEXTLIVE = "textlive"
    TEXTPOST = "textpost"
    TEXTPOST_PUBLISH = "textpost_publish"
    SITUATIONAL_THEME = "situational_theme"
    GROUP = "group"
    STICKER = "sticker"
    PODCAST = "podcast"


class WallWallpostCommentsDonut(BaseModel):
    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = Field(
        None,
        description=''
    )


class WallWallpostCommentsDonutPlaceholder(BaseModel):
    text: str = Field(
        None,
        description=''
    )


class WallWallpostDonutEditMode(enum.Enum):
    ALL = "all"
    DURATION = "duration"


class WallWallpostDonut(BaseModel):
    can_publish_free_copy: typing.Optional[bool] = Field(
        None,
        description='Says whether group admin can post free copy of this donut post'
    )
    edit_mode: typing.Optional["WallWallpostDonutEditMode"] = Field(
        None,
        description='Says what user can edit in post about donut properties'
    )
    is_donut: bool = Field(
        None,
        description='Post only for dons'
    )
    paid_duration: typing.Optional[int] = Field(
        None,
        description='Value of this field need to pass in wall.post/edit in donut_paid_duration'
    )
    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = Field(
        None,
        description='If placeholder was respond, text and all attachments will be hidden'
    )


class WallWallpostDonutPlaceholder(BaseModel):
    text: str = Field(
        None,
        description=''
    )


class WidgetsCommentMedia(BaseModel):
    item_id: typing.Optional[int] = Field(
        None,
        description='Media item ID'
    )
    owner_id: typing.Optional[int] = Field(
        None,
        description='Media owners ID'
    )
    thumb_src: typing.Optional[str] = Field(
        None,
        description='URL of the preview image (type=photo only)'
    )
    type: typing.Optional["WidgetsCommentMediaType"] = Field(
        None,
        description=''
    )


class WidgetsCommentMediaType(enum.Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
    can_post: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can comment the post'
    )
    count: typing.Optional[int] = Field(
        None,
        description='Comments number'
    )
    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = Field(
        None,
        description=''
    )


class WidgetsCommentRepliesItem(BaseModel):
    cid: typing.Optional[int] = Field(
        None,
        description='Comment ID'
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when the comment has been added in Unixtime'
    )
    likes: typing.Optional["WidgetsWidgetLikes"] = Field(
        None,
        description=''
    )
    text: typing.Optional[str] = Field(
        None,
        description='Comment text'
    )
    uid: typing.Optional[int] = Field(
        None,
        description='User ID'
    )
    user: typing.Optional["UsersUserFull"] = Field(
        None,
        description=''
    )


class WidgetsWidgetComment(BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        None,
        description=''
    )
    can_delete: typing.Optional["BaseBoolInt"] = Field(
        None,
        description='Information whether current user can delete the comment'
    )
    comments: typing.Optional["WidgetsCommentReplies"] = Field(
        None,
        description=''
    )
    date: int = Field(
        None,
        description='Date when the comment has been added in Unixtime'
    )
    from_id: int = Field(
        None,
        description='Comment author ID'
    )
    id: int = Field(
        None,
        description='Comment ID'
    )
    likes: typing.Optional["BaseLikesInfo"] = Field(
        None,
        description=''
    )
    media: typing.Optional["WidgetsCommentMedia"] = Field(
        None,
        description=''
    )
    post_source: typing.Optional["WallPostSource"] = Field(
        None,
        description=''
    )
    post_type: int = Field(
        None,
        description='Post type'
    )
    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        None,
        description=''
    )
    text: str = Field(
        None,
        description='Comment text'
    )
    to_id: int = Field(
        None,
        description='Wall owner'
    )
    user: typing.Optional["UsersUserFull"] = Field(
        None,
        description=''
    )


class WidgetsWidgetLikes(BaseModel):
    count: typing.Optional[int] = Field(
        None,
        description='Likes number'
    )


class WidgetsWidgetPage(BaseModel):
    comments: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    date: typing.Optional[int] = Field(
        None,
        description='Date when widgets on the page has been initialized firstly in Unixtime'
    )
    description: typing.Optional[str] = Field(
        None,
        description='Page description'
    )
    id: typing.Optional[int] = Field(
        None,
        description='Page ID'
    )
    likes: typing.Optional["BaseObjectCount"] = Field(
        None,
        description=''
    )
    page_id: typing.Optional[str] = Field(
        None,
        description='page_id parameter value'
    )
    photo: typing.Optional[str] = Field(
        None,
        description='URL of the preview image'
    )
    title: typing.Optional[str] = Field(
        None,
        description='Page title'
    )
    url: typing.Optional[str] = Field(
        None,
        description='Page absolute URL'
    )


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseModel):
        item.update_forward_refs()
