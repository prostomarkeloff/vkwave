import typing
import pydantic
from enum import Enum


class AccountNameRequest(pydantic.BaseModel):
    first_name: typing.Optional[str] = pydantic.Field(
        None, description="First name in request",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Request ID needed to cancel the request",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None, description="Last name in request",
    )
    status: typing.Optional["AccountNameRequestStatus"] = pydantic.Field(
        None, description="",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class AccountNameRequestStatusEnum(str, Enum):
    success = "success"
    processing = "processing"
    declined = "declined"
    was_accepted = "was_accepted"
    was_declined = "was_declined"


class AccountNameRequestStatus(pydantic.BaseModel):
    enum: typing.Optional[AccountNameRequestStatusEnum] = pydantic.Field(
        None, description="Request status",
    )


class AccountPushConversations(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Items count",
    )
    items: typing.Optional[
        typing.List["AccountPushConversationsItem"]
    ] = pydantic.Field(
        None, description="",
    )


class AccountPushParams(pydantic.BaseModel):
    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = pydantic.Field(
        None, description="",
    )
    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = pydantic.Field(
        None, description="",
    )
    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None, description="",
    )
    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None, description="",
    )
    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None, description="",
    )
    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = pydantic.Field(
        None, description="",
    )
    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    wall_publish: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    friend_found: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    friend_accepted: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    group_invite: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    group_accepted: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )
    app_request: typing.Optional[
        typing.List["AccountPushParamsOnoff"]
    ] = pydantic.Field(
        None, description="",
    )
    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = pydantic.Field(
        None, description="",
    )


class AccountUserSettingsInterest(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class AccountUserSettingsInterests(pydantic.BaseModel):
    activities: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    interests: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    music: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    tv: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    movies: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    books: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    games: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    quotes: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )
    about: typing.Optional["AccountUserSettingsInterest"] = pydantic.Field(
        None, description="",
    )


class AdsAccessRoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    reports = "reports"


class AdsAccessRole(pydantic.BaseModel):
    enum: typing.Optional[AdsAccessRoleEnum] = pydantic.Field(
        None, description="Current user's role",
    )


class AdsAccountTypeEnum(str, Enum):
    general = "general"
    agency = "agency"


class AdsAccountType(pydantic.BaseModel):
    enum: typing.Optional[AdsAccountTypeEnum] = pydantic.Field(
        None, description="Account type",
    )


class AdsAdApprovedEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class AdsAdApproved(pydantic.BaseModel):
    enum: typing.Optional[AdsAdApprovedEnum] = pydantic.Field(
        None, description="Review status",
    )


class AdsAdCostTypeEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class AdsAdCostType(pydantic.BaseModel):
    enum: typing.Optional[AdsAdCostTypeEnum] = pydantic.Field(
        None, description="Cost type",
    )


class AdsAdStatusEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class AdsAdStatus(pydantic.BaseModel):
    enum: typing.Optional[AdsAdStatusEnum] = pydantic.Field(
        None, description="Ad atatus",
    )


class AdsCampaignStatusEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class AdsCampaignStatus(pydantic.BaseModel):
    enum: typing.Optional[AdsCampaignStatusEnum] = pydantic.Field(
        None, description="Campaign status",
    )


class AdsCampaignTypeEnum(str, Enum):
    normal = "normal"
    vk_apps_managed = "vk_apps_managed"
    mobile_apps = "mobile_apps"
    promoted_posts = "promoted_posts"


class AdsCampaignType(pydantic.BaseModel):
    enum: typing.Optional[AdsCampaignTypeEnum] = pydantic.Field(
        None, description="Campaign type",
    )


class AdsCriteriaSexEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class AdsCriteriaSex(pydantic.BaseModel):
    enum: typing.Optional[AdsCriteriaSexEnum] = pydantic.Field(
        None, description="Sex",
    )


class AdsDemostatsFormat(pydantic.BaseModel):
    age: typing.Optional[typing.List["AdsStatsAge"]] = pydantic.Field(
        None, description="",
    )
    cities: typing.Optional[typing.List["AdsStatsCities"]] = pydantic.Field(
        None, description="",
    )
    day: typing.Optional[str] = pydantic.Field(
        None, description="Day as YYYY-MM-DD",
    )
    month: typing.Optional[str] = pydantic.Field(
        None, description="Month as YYYY-MM",
    )
    overall: typing.Optional[int] = pydantic.Field(
        None, description="1 if period=overall",
    )
    sex: typing.Optional[typing.List["AdsStatsSex"]] = pydantic.Field(
        None, description="",
    )
    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = pydantic.Field(
        None, description="",
    )


class AdsObjectTypeEnum(str, Enum):
    ad = "ad"
    campaign = "campaign"
    client = "client"
    office = "office"


class AdsObjectType(pydantic.BaseModel):
    enum: typing.Optional[AdsObjectTypeEnum] = pydantic.Field(
        None, description="Object type",
    )


class AdsStatsFormat(pydantic.BaseModel):
    clicks: typing.Optional[int] = pydantic.Field(
        None, description="Clicks number",
    )
    day: typing.Optional[str] = pydantic.Field(
        None, description="Day as YYYY-MM-DD",
    )
    impressions: typing.Optional[int] = pydantic.Field(
        None, description="Impressions number",
    )
    join_rate: typing.Optional[int] = pydantic.Field(
        None, description="Events number",
    )
    month: typing.Optional[str] = pydantic.Field(
        None, description="Month as YYYY-MM",
    )
    overall: typing.Optional[int] = pydantic.Field(
        None, description="1 if period=overall",
    )
    reach: typing.Optional[int] = pydantic.Field(
        None, description="Reach ",
    )
    spent: typing.Optional[int] = pydantic.Field(
        None, description="Spent funds",
    )
    video_clicks_site: typing.Optional[int] = pydantic.Field(
        None, description="Clickthoughs to the advertised site",
    )
    video_views: typing.Optional[int] = pydantic.Field(
        None, description="Video views number",
    )
    video_views_full: typing.Optional[int] = pydantic.Field(
        None, description="Video views (full video)",
    )
    video_views_half: typing.Optional[int] = pydantic.Field(
        None, description="Video views (half of video)",
    )


class AdsStatsSexValueEnum(str, Enum):
    f = "f"
    m = "m"


class AdsStatsSexValue(pydantic.BaseModel):
    enum: typing.Optional[AdsStatsSexValueEnum] = pydantic.Field(
        None, description="Sex",
    )


class AdsTargSuggestionsSchoolsTypeEnum(str, Enum):
    school = "school"
    university = "university"
    faculty = "faculty"
    chair = "chair"


class AdsTargSuggestionsSchoolsType(pydantic.BaseModel):
    enum: typing.Optional[AdsTargSuggestionsSchoolsTypeEnum] = pydantic.Field(
        None, description="School type",
    )


class AppsApp(pydantic.BaseModel):
    apps_app_min: typing.Optional["AppsAppMin"] = pydantic.Field(
        None, description="",
    )
    author_group: typing.Optional[int] = pydantic.Field(
        None, description="Official community's ID",
    )
    author_url: typing.Optional[str] = pydantic.Field(
        None, description="Application author's URL",
    )
    banner_1120: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app banner with 1120 px in width",
    )
    banner_560: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app banner with 560 px in width",
    )
    friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    catalog_position: typing.Optional[int] = pydantic.Field(
        None, description="Catalog position",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Application description",
    )
    genre: typing.Optional[str] = pydantic.Field(
        None, description="Genre name",
    )
    genre_id: typing.Optional[int] = pydantic.Field(
        None, description="Genre ID",
    )
    international: typing.Optional[int] = pydantic.Field(
        None, description="Information whether the application is multilanguage",
    )
    is_in_catalog: typing.Optional[int] = pydantic.Field(
        None, description="Information whether application is in mobile catalog",
    )
    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = pydantic.Field(
        None, description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None, description="Members number",
    )
    platform_id: typing.Optional[int] = pydantic.Field(
        None, description="Application ID in store",
    )
    published_date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the application has been published in Unixtime",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="Screen name",
    )
    screenshots: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )
    section: typing.Optional[str] = pydantic.Field(
        None, description="Application section name",
    )


class AppsAppTypeEnum(str, Enum):
    app = "app"
    game = "game"
    site = "site"
    standalone = "standalone"
    vk_app = "vk_app"
    community_app = "community_app"
    html5_game = "html5_game"


class AppsAppType(pydantic.BaseModel):
    enum: typing.Optional[AppsAppTypeEnum] = pydantic.Field(
        None, description="Application type",
    )


class AudioAudio(pydantic.BaseModel):
    artist: typing.Optional[str] = pydantic.Field(
        None, description="Artist name",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Audio ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="URL of mp3 file",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None, description="Duration in seconds",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    genre_id: typing.Optional[int] = pydantic.Field(
        None, description="Genre ID",
    )
    performer: typing.Optional[str] = pydantic.Field(
        None, description="Performer name",
    )


class BaseBoolIntEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1


class BaseBoolInt(pydantic.BaseModel):
    enum: typing.Optional[BaseBoolIntEnum] = pydantic.Field(
        None, description="",
    )


class BaseCity(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="City title",
    )


class BaseCommentsInfo(pydantic.BaseModel):
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the post",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether groups can comment the post",
    )


class BaseCountry(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Country title",
    )


class BaseGeo(pydantic.BaseModel):
    coordinates: typing.Optional["BaseGeoCoordinates"] = pydantic.Field(
        None, description="",
    )
    place: typing.Optional["BasePlace"] = pydantic.Field(
        None, description="",
    )
    showmap: typing.Optional[int] = pydantic.Field(
        None, description="Information whether a map is showed",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Place type",
    )


class BaseGeoCoordinates(pydantic.BaseModel):
    latitude: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    longitude: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class BaseLikes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Likes number",
    )
    user_likes: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user likes the photo",
    )


class BaseLikesInfo(pydantic.BaseModel):
    can_like: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can like the post",
    )
    can_publish: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can repost",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Likes number",
    )
    user_likes: typing.Optional[int] = pydantic.Field(
        None, description="Information whether current uer has liked the post",
    )


class BaseLink(pydantic.BaseModel):
    application: typing.Optional["BaseLinkApplication"] = pydantic.Field(
        None, description="",
    )
    button: typing.Optional["BaseLinkButton"] = pydantic.Field(
        None, description="",
    )
    caption: typing.Optional[str] = pydantic.Field(
        None, description="Link caption",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Link description",
    )
    id: typing.Optional[str] = pydantic.Field(
        None, description="Link ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    preview_page: typing.Optional[str] = pydantic.Field(
        None, description="String ID of the page with article preview",
    )
    preview_url: typing.Optional[str] = pydantic.Field(
        None, description="URL of the page with article preview",
    )
    product: typing.Optional["BaseLinkProduct"] = pydantic.Field(
        None, description="",
    )
    rating: typing.Optional["BaseLinkRating"] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Link title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )


class BaseLinkApplication(pydantic.BaseModel):
    app_id: typing.Optional[int] = pydantic.Field(
        None, description="Application Id",
    )
    store: typing.Optional["BaseLinkApplicationStore"] = pydantic.Field(
        None, description="",
    )


class BaseLinkApplicationStore(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Store Id",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Store name",
    )


class BaseLinkButton(pydantic.BaseModel):
    action: typing.Optional["BaseLinkButtonAction"] = pydantic.Field(
        None, description="Button action",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Button title",
    )


class BaseLinkButtonAction(pydantic.BaseModel):
    type: typing.Optional["BaseLinkButtonActionType"] = pydantic.Field(
        None, description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Action URL",
    )


class BaseLinkButtonActionTypeEnum(str, Enum):
    open_url = "open_url"


class BaseLinkButtonActionType(pydantic.BaseModel):
    enum: typing.Optional[BaseLinkButtonActionTypeEnum] = pydantic.Field(
        None, description="Action type",
    )


class BaseLinkProduct(pydantic.BaseModel):
    price: typing.Optional["MarketPrice"] = pydantic.Field(
        None, description="",
    )
    merchant: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    orders_count: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class BaseLinkRating(pydantic.BaseModel):
    reviews_count: typing.Optional[int] = pydantic.Field(
        None, description="Count of reviews",
    )
    stars: typing.Optional[int] = pydantic.Field(
        None, description="Count of stars",
    )


class BaseObjectCount(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Items count",
    )


class BaseOkResponseEnum(int, Enum):
    enum_1 = 1


class BaseOkResponse(pydantic.BaseModel):
    enum: typing.Optional[BaseOkResponseEnum] = pydantic.Field(
        None, description="Returns 1 if request has been processed successfully",
    )


class BasePlace(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None, description="Place address",
    )
    checkins: typing.Optional[int] = pydantic.Field(
        None, description="Checkins number",
    )
    city: typing.Optional[str] = pydantic.Field(
        None, description="City name",
    )
    country: typing.Optional[str] = pydantic.Field(
        None, description="Country name",
    )
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date of the place creation in Unixtime",
    )
    icon: typing.Optional[str] = pydantic.Field(
        None, description="URL of the place's icon",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Place ID",
    )
    latitude: typing.Optional[int] = pydantic.Field(
        None, description="Place latitude",
    )
    longitude: typing.Optional[int] = pydantic.Field(
        None, description="Place longitude",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Place title",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Place type",
    )


class BasePropertyExistsEnum(int, Enum):
    enum_1 = 1


class BasePropertyExists(pydantic.BaseModel):
    enum: typing.Optional[BasePropertyExistsEnum] = pydantic.Field(
        None, description="",
    )


class BaseRepostsInfo(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Reposts number",
    )
    user_reposted: typing.Optional[int] = pydantic.Field(
        None, description="Information whether current user has reposted the post",
    )


class BaseSexEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class BaseSex(pydantic.BaseModel):
    enum: typing.Optional[BaseSexEnum] = pydantic.Field(
        None, description="",
    )


class BaseSticker(pydantic.BaseModel):
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None, description="",
    )
    images_with_background: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None, description="",
    )
    product_id: typing.Optional[int] = pydantic.Field(
        None, description="Collection ID",
    )
    sticker_id: typing.Optional[int] = pydantic.Field(
        None, description="Sticker ID",
    )


class BoardTopic(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when the topic has been created in Unixtime",
    )
    created_by: typing.Optional[int] = pydantic.Field(
        None, description="Creator ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Topic ID",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the topic is closed",
    )
    is_fixed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the topic is fixed",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Topic title",
    )
    updated: typing.Optional[int] = pydantic.Field(
        None, description="Date when the topic has been updated in Unixtime",
    )
    updated_by: typing.Optional[int] = pydantic.Field(
        None, description="ID of user who updated the topic",
    )


class CallbackGroupJoinTypeEnum(str, Enum):
    join = "join"
    unsure = "unsure"
    accepted = "accepted"
    approved = "approved"
    request = "request"


class CallbackGroupJoinType(pydantic.BaseModel):
    enum: typing.Optional[CallbackGroupJoinTypeEnum] = pydantic.Field(
        None, description="",
    )


class CallbackGroupMarketEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1


class CallbackGroupMarket(pydantic.BaseModel):
    enum: typing.Optional[CallbackGroupMarketEnum] = pydantic.Field(
        None, description="",
    )


class CallbackGroupOfficerRoleEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class CallbackGroupOfficerRole(pydantic.BaseModel):
    enum: typing.Optional[CallbackGroupOfficerRoleEnum] = pydantic.Field(
        None, description="",
    )


class CallbackMessageTypeEnum(str, Enum):
    confirmation = "confirmation"
    group_change_photo = "group_change_photo"
    group_change_settings = "group_change_settings"
    group_officers_edit = "group_officers_edit"
    lead_forms_new = "lead_forms_new"
    market_comment_delete = "market_comment_delete"
    market_comment_edit = "market_comment_edit"
    market_comment_restore = "market_comment_restore"
    message_allow = "message_allow"
    message_deny = "message_deny"
    message_read = "message_read"
    message_reply = "message_reply"
    message_typing_state = "message_typing_state"
    messages_edit = "messages_edit"
    photo_comment_delete = "photo_comment_delete"
    photo_comment_edit = "photo_comment_edit"
    photo_comment_restore = "photo_comment_restore"
    poll_vote_new = "poll_vote_new"
    user_block = "user_block"
    user_unblock = "user_unblock"
    video_comment_delete = "video_comment_delete"
    video_comment_edit = "video_comment_edit"
    video_comment_restore = "video_comment_restore"
    wall_reply_delete = "wall_reply_delete"
    wall_reply_restore = "wall_reply_restore"
    wall_repost = "wall_repost"


class CallbackMessageType(pydantic.BaseModel):
    enum: typing.Optional[CallbackMessageTypeEnum] = pydantic.Field(
        None, description="",
    )


class CommentThread(pydantic.BaseModel):
    can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether current user can comment the post",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether groups can comment the post",
    )
    items: typing.Optional[typing.List["WallWallComment"]] = pydantic.Field(
        None, description="",
    )
    show_reply_button: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether recommended to display reply button",
    )


class DocsDoc(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the document",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when file has been uploaded in Unixtime",
    )
    ext: typing.Optional[str] = pydantic.Field(
        None, description="File extension",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Document ID",
    )
    is_licensed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Document owner ID",
    )
    preview: typing.Optional["DocsDocPreview"] = pydantic.Field(
        None, description="",
    )
    size: typing.Optional[int] = pydantic.Field(
        None, description="File size in bites",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Document title",
    )
    type: typing.Optional[int] = pydantic.Field(
        None, description="Document type",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="File URL",
    )


class DocsDocPreview(pydantic.BaseModel):
    photo: typing.Optional["DocsDocPreviewPhoto"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["DocsDocPreviewVideo"] = pydantic.Field(
        None, description="",
    )


class DocsDocPreviewPhoto(pydantic.BaseModel):
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )


class DocsDocPreviewVideo(pydantic.BaseModel):
    filesize: typing.Optional[int] = pydantic.Field(
        None, description="Video file size in bites",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Video's height in pixels",
    )
    src: typing.Optional[str] = pydantic.Field(
        None, description="Video URL",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Video's width in pixels",
    )


class EventsEventAttach(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None, description="address of event",
    )
    button_text: typing.Optional[str] = pydantic.Field(
        None, description="text of attach",
    )
    friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="array of friends ids",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="event ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None, description="is favorite",
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = pydantic.Field(
        None, description="Current user's member status",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="text of attach",
    )
    time: typing.Optional[int] = pydantic.Field(
        None, description="event start time",
    )


class FaveBookmarkTypeEnum(str, Enum):
    post = "post"
    video = "video"
    product = "product"
    article = "article"
    link = "link"


class FaveBookmarkType(pydantic.BaseModel):
    enum: typing.Optional[FaveBookmarkTypeEnum] = pydantic.Field(
        None, description="",
    )


class FavePageTypeEnum(str, Enum):
    user = "user"
    group = "group"
    hints = "hints"


class FavePageType(pydantic.BaseModel):
    enum: typing.Optional[FavePageTypeEnum] = pydantic.Field(
        None, description="",
    )


class FriendsFriendStatusStatusEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class FriendsFriendStatusStatus(pydantic.BaseModel):
    enum: typing.Optional[FriendsFriendStatusStatusEnum] = pydantic.Field(
        None, description="Friend status with the user",
    )


class FriendsRequestsMutual(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total mutual friends number",
    )
    users: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class GiftsGiftPrivacyEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GiftsGiftPrivacy(pydantic.BaseModel):
    enum: typing.Optional[GiftsGiftPrivacyEnum] = pydantic.Field(
        None, description="Gift privacy",
    )


class GiftsLayout(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Gift ID",
    )
    thumb_256: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 256 px in width",
    )
    thumb_48: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 48 px in width",
    )
    thumb_96: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 96 px in width",
    )


class GroupsAddressTimetable(pydantic.BaseModel):
    fri: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for friday",
    )
    mon: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for monday",
    )
    sat: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for saturday",
    )
    sun: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for sunday",
    )
    thu: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for thursday",
    )
    tue: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for tuesday",
    )
    wed: typing.Optional["GroupsAddressTimetableDay"] = pydantic.Field(
        None, description="Timetable for wednesday",
    )


class GroupsAddressTimetableDay(pydantic.BaseModel):
    break_close_time: typing.Optional[int] = pydantic.Field(
        None, description="Close time of the break in minutes",
    )
    break_open_time: typing.Optional[int] = pydantic.Field(
        None, description="Start time of the break in minutes",
    )
    close_time: typing.Optional[int] = pydantic.Field(
        None, description="Close time in minutes",
    )
    open_time: typing.Optional[int] = pydantic.Field(
        None, description="Open time in minutes",
    )


class GroupsAddressWorkInfoStatusEnum(str, Enum):
    no_information = "no_information"
    temporarily_closed = "temporarily_closed"
    always_opened = "always_opened"
    timetable = "timetable"
    forever_closed = "forever_closed"


class GroupsAddressWorkInfoStatus(pydantic.BaseModel):
    enum: typing.Optional[GroupsAddressWorkInfoStatusEnum] = pydantic.Field(
        None, description="Status of information about timetable",
    )


class GroupsBanInfo(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="Administrator ID",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None, description="Comment for a ban",
    )
    comment_visible: typing.Optional[bool] = pydantic.Field(
        None, description="Show comment for user",
    )
    is_closed: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when user has been added to blacklist in Unixtime",
    )
    end_date: typing.Optional[int] = pydantic.Field(
        None, description="Date when user will be removed from blacklist in Unixtime",
    )
    reason: typing.Optional["GroupsBanInfoReason"] = pydantic.Field(
        None, description="",
    )


class GroupsBanInfoReasonEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3
    enum_4 = 4


class GroupsBanInfoReason(pydantic.BaseModel):
    enum: typing.Optional[GroupsBanInfoReasonEnum] = pydantic.Field(
        None, description="Ban reason",
    )


class GroupsGroup(pydantic.BaseModel):
    admin_level: typing.Optional["GroupsGroupAdminLevel"] = pydantic.Field(
        None, description="",
    )
    deactivated: typing.Optional[str] = pydantic.Field(
        None, description="Information whether community is banned",
    )
    finish_date: typing.Optional[int] = pydantic.Field(
        None, description="Finish date in Unixtime format",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    is_admin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is administrator",
    )
    is_advertiser: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is advertiser",
    )
    is_closed: typing.Optional["GroupsGroupIsClosed"] = pydantic.Field(
        None, description="",
    )
    is_member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is member",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Community name",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 100 pixels in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 200 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 50 pixels in width",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="Domain of the community page",
    )
    start_date: typing.Optional[int] = pydantic.Field(
        None, description="Start date in Unixtime format",
    )
    type: typing.Optional["GroupsGroupType"] = pydantic.Field(
        None, description="",
    )


class GroupsGroupAdminLevelEnum(int, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class GroupsGroupAdminLevel(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupAdminLevelEnum] = pydantic.Field(
        None, description="Level of current user's credentials as manager",
    )


class GroupsGroupAudioEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupAudio(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupAudioEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupFull(pydantic.BaseModel):
    groups_group: typing.Optional["GroupsGroup"] = pydantic.Field(
        None, description="",
    )
    market: typing.Optional["GroupsMarketInfo"] = pydantic.Field(
        None, description="",
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = pydantic.Field(
        None, description="Current user's member status",
    )
    is_favorite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether community is in faves",
    )
    is_subscribed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is subscribed",
    )
    city: typing.Optional["BaseObject"] = pydantic.Field(
        None, description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None, description="",
    )
    verified: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether community is verified",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Community description",
    )
    wiki_page: typing.Optional[str] = pydantic.Field(
        None, description="Community's main wiki page title",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None, description="Community members number",
    )
    counters: typing.Optional["GroupsCountersGroup"] = pydantic.Field(
        None, description="",
    )
    cover: typing.Optional["GroupsCover"] = pydantic.Field(
        None, description="",
    )
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can post on community's wall",
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see all posts on community's wall",
    )
    activity: typing.Optional[str] = pydantic.Field(
        None,
        description="Type of group, start date of event or category of public page",
    )
    fixed_post: typing.Optional[int] = pydantic.Field(
        None, description="Fixed post ID",
    )
    can_create_topic: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can create topic",
    )
    can_upload_video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can upload video",
    )
    has_photo: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether community has photo",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="Community status",
    )
    main_album_id: typing.Optional[int] = pydantic.Field(
        None, description="Community's main photo album ID",
    )
    links: typing.Optional[typing.List["GroupsLinksItem"]] = pydantic.Field(
        None, description="",
    )
    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = pydantic.Field(
        None, description="",
    )
    site: typing.Optional[str] = pydantic.Field(
        None, description="Community's website",
    )
    main_section: typing.Optional["GroupsGroupFullMainSection"] = pydantic.Field(
        None, description="",
    )
    trending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the community has a fire pictogram.",
    )
    can_message: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can send a message to community",
    )
    is_messages_blocked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community can send a message to current user",
    )
    can_send_notify: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether community can send notifications by phone number to current user",
    )
    online_status: typing.Optional["GroupsOnlineStatus"] = pydantic.Field(
        None, description="Status of replies in community messages",
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = pydantic.Field(
        None, description="Information whether age limit",
    )
    ban_info: typing.Optional["GroupsGroupBanInfo"] = pydantic.Field(
        None, description="User ban info",
    )
    addresses: typing.Optional["GroupsAddressesInfo"] = pydantic.Field(
        None, description="Info about addresses in groups",
    )
    is_subscribed_podcasts: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether current user is subscribed to podcasts",
    )
    can_subscribe_podcasts: typing.Optional[bool] = pydantic.Field(
        None, description="Owner in whitelist or not",
    )
    can_subscribe_posts: typing.Optional[bool] = pydantic.Field(
        None, description="Can subscribe to wall",
    )


class GroupsGroupFullAgeLimitsEnum(int, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class GroupsGroupFullAgeLimits(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupFullAgeLimitsEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupFullMemberStatusEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3
    enum_4 = 4
    enum_5 = 5


class GroupsGroupFullMemberStatus(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupFullMemberStatusEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupIsClosedEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupIsClosed(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupIsClosedEnum] = pydantic.Field(
        None, description="Information whether community is closed",
    )


class GroupsGroupPhotosEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupPhotos(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupPhotosEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupTypeEnum(str, Enum):
    group = "group"
    page = "page"
    event = "event"


class GroupsGroupType(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupTypeEnum] = pydantic.Field(
        None, description="Community type",
    )


class GroupsGroupVideoEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupVideo(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupVideoEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupWallEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class GroupsGroupWall(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupWallEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupXtrInvitedByAdminLevelEnum(int, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class GroupsGroupXtrInvitedByAdminLevel(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupXtrInvitedByAdminLevelEnum] = pydantic.Field(
        None, description="Level of current user's credentials as manager",
    )


class GroupsGroupXtrInvitedByTypeEnum(str, Enum):
    group = "group"
    page = "page"
    event = "event"


class GroupsGroupXtrInvitedByType(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupXtrInvitedByTypeEnum] = pydantic.Field(
        None, description="Community type",
    )


class GroupsLongPollEvents(pydantic.BaseModel):
    audio_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    board_post_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    board_post_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    board_post_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    board_post_restore: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    group_change_photo: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    group_change_settings: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    group_join: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    group_leave: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    group_officers_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    lead_forms_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    market_comment_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    market_comment_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    market_comment_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    market_comment_restore: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_allow: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_deny: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_read: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_reply: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    message_typing_state: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    messages_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    photo_comment_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    photo_comment_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    photo_comment_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    photo_comment_restore: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    photo_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    poll_vote_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    user_block: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    user_unblock: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    video_comment_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    video_comment_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    video_comment_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    video_comment_restore: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    video_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_post_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_reply_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_reply_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_reply_new: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_reply_restore: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    wall_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )


class GroupsMemberRoleStatusEnum(str, Enum):
    moderator = "moderator"
    editor = "editor"
    administrator = "administrator"
    creator = "creator"


class GroupsMemberRoleStatus(pydantic.BaseModel):
    enum: typing.Optional[GroupsMemberRoleStatusEnum] = pydantic.Field(
        None, description="User's credentials as community admin",
    )


class GroupsOnlineStatusTypeEnum(str, Enum):
    none = "none"
    online = "online"
    answer_mark = "answer_mark"


class GroupsOnlineStatusType(pydantic.BaseModel):
    enum: typing.Optional[GroupsOnlineStatusTypeEnum] = pydantic.Field(
        None, description="Type of online status of group",
    )


class GroupsOwnerXtrBanInfoTypeEnum(str, Enum):
    group = "group"
    profile = "profile"


class GroupsOwnerXtrBanInfoType(pydantic.BaseModel):
    enum: typing.Optional[GroupsOwnerXtrBanInfoTypeEnum] = pydantic.Field(
        None, description="Owner type",
    )


class LeadsCheckedResultEnum(str, Enum):
    true = "true"
    false = "false"


class LeadsCheckedResult(pydantic.BaseModel):
    enum: typing.Optional[LeadsCheckedResultEnum] = pydantic.Field(
        None, description="Information whether user can start the lead",
    )


class LeadsLeadDays(pydantic.BaseModel):
    completed: typing.Optional[int] = pydantic.Field(
        None, description="Completed offers number",
    )
    impressions: typing.Optional[int] = pydantic.Field(
        None, description="Impressions number",
    )
    spent: typing.Optional[int] = pydantic.Field(
        None, description="Amount of spent votes",
    )
    started: typing.Optional[int] = pydantic.Field(
        None, description="Started offers number",
    )


class MarketCurrency(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Currency ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Currency sign",
    )


class MarketMarketAlbum(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Items number",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Market album ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Market album owner's ID",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Market album title",
    )
    updated_time: typing.Optional[int] = pydantic.Field(
        None, description="Date when album has been updated last time in Unixtime",
    )


class MarketMarketCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Category ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Category name",
    )
    section: typing.Optional["MarketSection"] = pydantic.Field(
        None, description="",
    )


class MarketMarketItem(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the market item",
    )
    availability: typing.Optional["MarketMarketItemAvailability"] = pydantic.Field(
        None, description="",
    )
    button_title: typing.Optional[str] = pydantic.Field(
        None, description="Title for button for url",
    )
    category: typing.Optional["MarketMarketCategory"] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the item has been created in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Item description",
    )
    external_id: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Item ID",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Item owner's ID",
    )
    price: typing.Optional["MarketPrice"] = pydantic.Field(
        None, description="",
    )
    thumb_photo: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Item title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="URL to item",
    )


class MarketMarketItemAvailabilityEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class MarketMarketItemAvailability(pydantic.BaseModel):
    enum: typing.Optional[MarketMarketItemAvailabilityEnum] = pydantic.Field(
        None, description="Information whether the item is available",
    )


class MarketPrice(pydantic.BaseModel):
    amount: typing.Optional[str] = pydantic.Field(
        None, description="Amount",
    )
    currency: typing.Optional["MarketCurrency"] = pydantic.Field(
        None, description="",
    )
    discount_rate: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    old_amount: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Text",
    )


class MarketSection(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Section ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Section name",
    )


class MessagesAudioMessage(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for audio message",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None, description="Audio message duration in seconds",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Audio message ID",
    )
    link_mp3: typing.Optional[str] = pydantic.Field(
        None, description="MP3 file URL",
    )
    link_ogg: typing.Optional[str] = pydantic.Field(
        None, description="OGG file URL",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Audio message owner ID",
    )
    waveform: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class MessagesChatPushSettings(pydantic.BaseModel):
    disabled_until: typing.Optional[int] = pydantic.Field(
        None, description="Time until that notifications are disabled",
    )
    sound: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the sound is on",
    )


class MessagesConversation(pydantic.BaseModel):
    peer: typing.Optional["MessagesConversationPeer"] = pydantic.Field(
        None, description="",
    )
    last_message_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the last message in conversation",
    )
    in_read: typing.Optional[int] = pydantic.Field(
        None, description="Last message user have read",
    )
    out_read: typing.Optional[int] = pydantic.Field(
        None, description="Last outcoming message have been read by the opponent",
    )
    unread_count: typing.Optional[int] = pydantic.Field(
        None, description="Unread messages number",
    )
    important: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    unanswered: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    special_service_type: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    message_request: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    mentions: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="Ids of messages with mentions",
    )
    current_keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None, description="",
    )


class MessagesConversationPeer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    local_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["MessagesConversationPeerType"] = pydantic.Field(
        None, description="",
    )


class MessagesConversationPeerTypeEnum(str, Enum):
    chat = "chat"
    email = "email"
    user = "user"
    group = "group"


class MessagesConversationPeerType(pydantic.BaseModel):
    enum: typing.Optional[MessagesConversationPeerTypeEnum] = pydantic.Field(
        None, description="Peer type",
    )


class MessagesForeignMessage(pydantic.BaseModel):
    attachments: typing.Optional[
        typing.List["MessagesMessageAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None, description="Conversation message ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the message was created",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Message author's ID",
    )
    fwd_messages: typing.Optional[
        typing.List["MessagesForeignMessage"]
    ] = pydantic.Field(
        None, description="",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None, description="Peer ID",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Message text",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None, description="Date when the message has been updated in Unixtime",
    )


class MessagesGraffiti(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for graffiti",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti owner ID",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Graffiti URL",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti width",
    )


class MessagesHistoryMessageAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = pydantic.Field(
        None, description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None, description="",
    )
    graffiti: typing.Optional["MessagesGraffiti"] = pydantic.Field(
        None, description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    market: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    share: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["MessagesHistoryMessageAttachmentType"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )
    wall: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )


class MessagesHistoryMessageAttachmentTypeEnum(str, Enum):
    photo = "photo"
    video = "video"
    audio = "audio"
    doc = "doc"
    link = "link"
    market = "market"
    wall = "wall"
    share = "share"
    graffiti = "graffiti"
    audio_message = "audio_message"


class MessagesHistoryMessageAttachmentType(pydantic.BaseModel):
    enum: typing.Optional[MessagesHistoryMessageAttachmentTypeEnum] = pydantic.Field(
        None, description="Attachments type",
    )


class MessagesKeyboard(pydantic.BaseModel):
    author_id: typing.Optional[int] = pydantic.Field(
        None, description="Community or bot, which set this keyboard",
    )
    buttons: typing.Optional[
        typing.List[typing.List["MessagesKeyboardButton"]]
    ] = pydantic.Field(
        None, description="",
    )
    one_time: typing.Optional[bool] = pydantic.Field(
        None, description="Should this keyboard disappear on first use",
    )
    inline: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )


class MessagesKeyboardButtonAction(pydantic.BaseModel):
    app_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app{app_id}_-654321#hash",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )
    label: typing.Optional[str] = pydantic.Field(
        None, description="Label for button",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Fragment value in app link like vk.com/app123456_{owner_id}#hash",
    )
    payload: typing.Optional[str] = pydantic.Field(
        None,
        description="Additional data sent along with message for developer convenience",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Button type",
    )


class MessagesMessage(pydantic.BaseModel):
    action: typing.Optional["MessagesMessageAction"] = pydantic.Field(
        None, description="",
    )
    admin_author_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Only for messages from community. Contains user ID of community admin, who sent this message.",
    )
    attachments: typing.Optional[
        typing.List["MessagesMessageAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Unique auto-incremented number for all messages with this peer",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the message has been sent in Unixtime",
    )
    deleted: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Is it an deleted message",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Message author's ID",
    )
    fwd_messages: typing.Optional[
        typing.List["MessagesForeignMessage"]
    ] = pydantic.Field(
        None, description="Forwarded messages",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )
    important: typing.Optional[bool] = pydantic.Field(
        None, description="Is it an important message",
    )
    is_hidden: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None, description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None, description="Members number",
    )
    out: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the message is outcoming",
    )
    payload: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None, description="Peer ID",
    )
    random_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID used for sending messages. It returned only for outgoing messages",
    )
    ref: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    ref_source: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Message text",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None, description="Date when the message has been updated in Unixtime",
    )


class MessagesMessageAction(pydantic.BaseModel):
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )
    email: typing.Optional[str] = pydantic.Field(
        None,
        description="Email address for chat_invite_user or chat_kick_user actions",
    )
    member_id: typing.Optional[int] = pydantic.Field(
        None, description="User or email peer ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None, description="Message body of related message",
    )
    photo: typing.Optional["MessagesMessageActionPhoto"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="New chat title for chat_create and chat_title_update actions",
    )
    type: typing.Optional["MessagesMessageActionStatus"] = pydantic.Field(
        None, description="",
    )


class MessagesMessageActionPhoto(pydantic.BaseModel):
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 100px in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 200px in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 50px in width",
    )


class MessagesMessageActionStatusEnum(str, Enum):
    chat_photo_update = "chat_photo_update"
    chat_photo_remove = "chat_photo_remove"
    chat_create = "chat_create"
    chat_title_update = "chat_title_update"
    chat_invite_user = "chat_invite_user"
    chat_kick_user = "chat_kick_user"
    chat_pin_message = "chat_pin_message"
    chat_unpin_message = "chat_unpin_message"
    chat_invite_user_by_link = "chat_invite_user_by_link"


class MessagesMessageActionStatus(pydantic.BaseModel):
    enum: typing.Optional[MessagesMessageActionStatusEnum] = pydantic.Field(
        None, description="Action status",
    )


class MessagesMessageAttachmentTypeEnum(str, Enum):
    photo = "photo"
    audio = "audio"
    video = "video"
    doc = "doc"
    link = "link"
    market = "market"
    market_album = "market_album"
    gift = "gift"
    sticker = "sticker"
    wall = "wall"
    wall_reply = "wall_reply"
    article = "article"
    graffiti = "graffiti"
    audio_message = "audio_message"


class MessagesMessageAttachmentType(pydantic.BaseModel):
    enum: typing.Optional[MessagesMessageAttachmentTypeEnum] = pydantic.Field(
        None, description="Attachment type",
    )


class NewsfeedNewsfeedItemTypeEnum(str, Enum):
    post = "post"
    photo = "photo"
    photo_tag = "photo_tag"
    wall_photo = "wall_photo"
    friend = "friend"
    note = "note"
    audio = "audio"
    video = "video"
    topic = "topic"
    digest = "digest"
    stories = "stories"


class NewsfeedNewsfeedItemType(pydantic.BaseModel):
    enum: typing.Optional[NewsfeedNewsfeedItemTypeEnum] = pydantic.Field(
        None, description="Item type",
    )


class NotificationsFeedback(pydantic.BaseModel):
    attachments: typing.Optional[
        typing.List["WallWallpostAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Reply author's ID",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Item ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Reply text",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None, description="Wall owner's ID",
    )


class NotificationsNotificationParent(pydantic.BaseModel):
    wall_wallpost_to_id: typing.Optional["WallWallpostToId"] = pydantic.Field(
        None, description="",
    )
    photos_photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    board_topic: typing.Optional["BoardTopic"] = pydantic.Field(
        None, description="",
    )
    video_video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )
    notifications_notifications_comment: typing.Optional[
        "NotificationsNotificationsComment"
    ] = pydantic.Field(
        None, description="",
    )


class NotificationsReply(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the reply has been created in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Reply ID",
    )
    text: typing.Optional[int] = pydantic.Field(
        None, description="Reply text",
    )


class NotificationsSendMessageError(pydantic.BaseModel):
    code: typing.Optional[int] = pydantic.Field(
        None, description="Error code",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Error description",
    )


class PagesPrivacySettingsEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class PagesPrivacySettings(pydantic.BaseModel):
    enum: typing.Optional[PagesPrivacySettingsEnum] = pydantic.Field(
        None, description="",
    )


class PagesWikipageFull(pydantic.BaseModel):
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when the page has been created in Unixtime",
    )
    creator_id: typing.Optional[int] = pydantic.Field(
        None, description="Page creator ID",
    )
    current_user_can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can edit the page",
    )
    current_user_can_edit_access: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can edit the page access settings",
    )
    edited: typing.Optional[int] = pydantic.Field(
        None, description="Date when the page has been edited in Unixtime",
    )
    editor_id: typing.Optional[int] = pydantic.Field(
        None, description="Last editor ID",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    html: typing.Optional[str] = pydantic.Field(
        None, description="Page content, HTML",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Page ID",
    )
    source: typing.Optional[str] = pydantic.Field(
        None, description="Page content, wiki",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Page title",
    )
    view_url: typing.Optional[str] = pydantic.Field(
        None, description="URL of the page preview",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )
    who_can_edit: typing.Optional["PagesPrivacySettings"] = pydantic.Field(
        None, description="Edit settings of the page",
    )
    who_can_view: typing.Optional["PagesPrivacySettings"] = pydantic.Field(
        None, description="View settings of the page",
    )


class PhotosImageTypeEnum(str, Enum):
    s = "s"
    m = "m"
    x = "x"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    y = "y"
    z = "z"
    w = "w"


class PhotosImageType(pydantic.BaseModel):
    enum: typing.Optional[PhotosImageTypeEnum] = pydantic.Field(
        None, description="Photo's type.",
    )


class PhotosPhoto(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the photo",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Original photo height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    images: typing.Optional[typing.List["PhotosImage"]] = pydantic.Field(
        None, description="",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None, description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None, description="Longitude",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Original photo width",
    )


class PhotosPhotoAlbum(pydantic.BaseModel):
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when the album has been created in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Photo album description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo album ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Album owner's ID",
    )
    size: typing.Optional[int] = pydantic.Field(
        None, description="Photos number",
    )
    thumb: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Photo album title",
    )
    updated: typing.Optional[int] = pydantic.Field(
        None, description="Date when the album has been updated last time in Unixtime",
    )


class PhotosPhotoSizesTypeEnum(str, Enum):
    s = "s"
    m = "m"
    x = "x"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    y = "y"
    z = "z"
    w = "w"


class PhotosPhotoSizesType(pydantic.BaseModel):
    enum: typing.Optional[PhotosPhotoSizesTypeEnum] = pydantic.Field(
        None, description="Size type",
    )


class PollsPoll(pydantic.BaseModel):
    anonymous: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether the field is anonymous",
    )
    answer_id: typing.Optional[int] = pydantic.Field(
        None, description="Current user's answer ID",
    )
    answers: typing.Optional[typing.List["PollsAnswer"]] = pydantic.Field(
        None, description="",
    )
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when poll has been created in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Poll ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Poll owner's ID",
    )
    question: typing.Optional[str] = pydantic.Field(
        None, description="Poll question",
    )
    votes: typing.Optional[str] = pydantic.Field(
        None, description="Votes number",
    )


class PollsVotersUsers(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Votes number",
    )
    items: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class SearchHintSectionEnum(str, Enum):
    groups = "groups"
    events = "events"
    publics = "publics"
    correspondents = "correspondents"
    people = "people"
    friends = "friends"
    mutual_friends = "mutual_friends"


class SearchHintSection(pydantic.BaseModel):
    enum: typing.Optional[SearchHintSectionEnum] = pydantic.Field(
        None, description="Section title",
    )


class SearchHintTypeEnum(str, Enum):
    group = "group"
    profile = "profile"
    vk_app = "vk_app"


class SearchHintType(pydantic.BaseModel):
    enum: typing.Optional[SearchHintTypeEnum] = pydantic.Field(
        None, description="Object type",
    )


class StatsActivity(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    copies: typing.Optional[int] = pydantic.Field(
        None, description="Reposts number",
    )
    hidden: typing.Optional[int] = pydantic.Field(
        None, description="Hidden from news count",
    )
    likes: typing.Optional[int] = pydantic.Field(
        None, description="Likes number",
    )
    subscribed: typing.Optional[int] = pydantic.Field(
        None, description="New subscribers count",
    )
    unsubscribed: typing.Optional[int] = pydantic.Field(
        None, description="Unsubscribed count",
    )


class StatsReach(pydantic.BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    cities: typing.Optional[typing.List["StatsCity"]] = pydantic.Field(
        None, description="",
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = pydantic.Field(
        None, description="",
    )
    mobile_reach: typing.Optional[int] = pydantic.Field(
        None, description="Reach count from mobile devices",
    )
    reach: typing.Optional[int] = pydantic.Field(
        None, description="Reach count",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None, description="Subscribers reach count",
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )


class StatsViews(pydantic.BaseModel):
    age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    cities: typing.Optional[typing.List["StatsCity"]] = pydantic.Field(
        None, description="",
    )
    countries: typing.Optional[typing.List["StatsCountry"]] = pydantic.Field(
        None, description="",
    )
    mobile_views: typing.Optional[int] = pydantic.Field(
        None, description="Number of views from mobile devices",
    )
    sex: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )
    visitors: typing.Optional[int] = pydantic.Field(
        None, description="Visitors number",
    )


class StoriesReplies(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Replies number.",
    )
    new: typing.Optional[int] = pydantic.Field(
        None, description="New replies number.",
    )


class StoriesStory(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for private object.",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can comment the story (0 - no, 1 - yes).",
    )
    can_reply: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can reply to the story (0 - no, 1 - yes).",
    )
    can_see: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see the story (0 - no, 1 - yes).",
    )
    can_share: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can share the story (0 - no, 1 - yes).",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when story has been added in Unixtime.",
    )
    expires_at: typing.Optional[int] = pydantic.Field(
        None, description="Story expiration time. Unixtime.",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Story ID.",
    )
    is_deleted: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the story is deleted (false - no, true - yes).",
    )
    is_expired: typing.Optional[bool] = pydantic.Field(
        None,
        description="Information whether the story is expired (false - no, true - yes).",
    )
    link: typing.Optional["StoriesStoryLink"] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Story owner's ID.",
    )
    parent_story: typing.Optional["StoriesStory"] = pydantic.Field(
        None, description="",
    )
    parent_story_access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for private object.",
    )
    parent_story_id: typing.Optional[int] = pydantic.Field(
        None, description="Parent story ID.",
    )
    parent_story_owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Parent story owner's ID.",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    replies: typing.Optional["StoriesReplies"] = pydantic.Field(
        None, description="Replies to current story.",
    )
    seen: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user has seen the story or not (0 - no, 1 - yes).",
    )
    type: typing.Optional["StoriesStoryType"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["StoriesStoryVideo"] = pydantic.Field(
        None, description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number.",
    )
    is_restricted: typing.Optional[bool] = pydantic.Field(
        None, description="Does author have stories privacy restrictions",
    )
    no_sound: typing.Optional[bool] = pydantic.Field(
        None, description="Is video without sound",
    )
    need_mute: typing.Optional[bool] = pydantic.Field(
        None, description="Does video need to be muted",
    )
    can_ask: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether story has question sticker and current user can send question to the author",
    )
    can_ask_anonymous: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether story has question sticker and current user can send anonymous question to the author",
    )


class StoriesStoryLink(pydantic.BaseModel):
    text: typing.Optional[str] = pydantic.Field(
        None, description="Link text",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )


class StoriesStoryStatsStat(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Stat value",
    )
    state: typing.Optional["StoriesStoryStatsState"] = pydantic.Field(
        None, description="",
    )


class StoriesStoryStatsStateEnum(str, Enum):
    on = "on"
    off = "off"
    hidden = "hidden"


class StoriesStoryStatsState(pydantic.BaseModel):
    enum: typing.Optional[StoriesStoryStatsStateEnum] = pydantic.Field(
        None, description="Statistic state",
    )


class StoriesStoryTypeEnum(str, Enum):
    photo = "photo"
    video = "video"


class StoriesStoryType(pydantic.BaseModel):
    enum: typing.Optional[StoriesStoryTypeEnum] = pydantic.Field(
        None, description="Story type.",
    )


class StoriesStoryVideo(pydantic.BaseModel):
    video_video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )
    is_private: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether story is private (0 - no, 1 - yes).",
    )


class UsersCropPhotoCrop(pydantic.BaseModel):
    x: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the left upper corner",
    )
    x2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the right lower corner",
    )
    y: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the left upper corner",
    )
    y2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the right lower corner",
    )


class UsersCropPhotoRect(pydantic.BaseModel):
    x: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the left upper corner",
    )
    x2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the right lower corner",
    )
    y: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the left upper corner",
    )
    y2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the right lower corner",
    )


class UsersPersonal(pydantic.BaseModel):
    alcohol: typing.Optional[int] = pydantic.Field(
        None, description="User's views on alcohol",
    )
    inspired_by: typing.Optional[str] = pydantic.Field(
        None, description="User's inspired by",
    )
    langs: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )
    life_main: typing.Optional[int] = pydantic.Field(
        None, description="User's personal priority in life",
    )
    people_main: typing.Optional[int] = pydantic.Field(
        None, description="User's personal priority in people",
    )
    political: typing.Optional[int] = pydantic.Field(
        None, description="User's political views",
    )
    religion: typing.Optional[str] = pydantic.Field(
        None, description="User's religion",
    )
    religion_id: typing.Optional[int] = pydantic.Field(
        None, description="User's religion id",
    )
    smoking: typing.Optional[int] = pydantic.Field(
        None, description="User's views on smoking",
    )


class UsersUser(pydantic.BaseModel):
    users_user_min: typing.Optional["UsersUserMin"] = pydantic.Field(
        None, description="",
    )
    sex: typing.Optional["BaseSex"] = pydantic.Field(
        None, description="User sex",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="Domain name of the user's page",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="URL of square photo of the user with 50 pixels in width",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="URL of square photo of the user with 100 pixels in width",
    )
    online: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user is online",
    )
    online_mobile: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user is online in mobile site or application",
    )
    online_app: typing.Optional[int] = pydantic.Field(
        None, description="Application ID",
    )
    verified: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user is verified",
    )
    trending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user has a fire pictogram.",
    )
    friend_status: typing.Optional["FriendsFriendStatusStatus"] = pydantic.Field(
        None, description="",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None, description="",
    )


class UsersUserConnections(pydantic.BaseModel):
    skype: typing.Optional[str] = pydantic.Field(
        None, description="User's Skype nickname",
    )
    facebook: typing.Optional[str] = pydantic.Field(
        None, description="User's Facebook account",
    )
    facebook_name: typing.Optional[str] = pydantic.Field(
        None, description="User's Facebook name",
    )
    twitter: typing.Optional[str] = pydantic.Field(
        None, description="User's Twitter account",
    )
    livejournal: typing.Optional[str] = pydantic.Field(
        None, description="User's Livejournal account",
    )
    instagram: typing.Optional[str] = pydantic.Field(
        None, description="User's Instagram account",
    )


class UsersUserFull(pydantic.BaseModel):
    users_user: typing.Optional["UsersUser"] = pydantic.Field(
        None, description="",
    )
    nickname: typing.Optional[str] = pydantic.Field(
        None, description="User nickname",
    )
    maiden_name: typing.Optional[str] = pydantic.Field(
        None, description="User maiden name",
    )
    domain: typing.Optional[str] = pydantic.Field(
        None, description="Domain name of the user's page",
    )
    bdate: typing.Optional[str] = pydantic.Field(
        None, description="User's date of birth",
    )
    city: typing.Optional["BaseObject"] = pydantic.Field(
        None, description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None, description="",
    )
    timezone: typing.Optional[int] = pydantic.Field(
        None, description="User's timezone",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None, description="URL of square photo of the user with 200 pixels in width",
    )
    photo_max: typing.Optional[str] = pydantic.Field(
        None, description="URL of square photo of the user with maximum width",
    )
    photo_200_orig: typing.Optional[str] = pydantic.Field(
        None, description="URL of user's photo with 200 pixels in width",
    )
    photo_400_orig: typing.Optional[str] = pydantic.Field(
        None, description="URL of user's photo with 400 pixels in width",
    )
    photo_max_orig: typing.Optional[str] = pydantic.Field(
        None, description="URL of user's photo of maximum size",
    )
    photo_id: typing.Optional[str] = pydantic.Field(
        None, description="ID of the user's main photo",
    )
    has_photo: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user has main photo",
    )
    has_mobile: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user specified his phone number",
    )
    is_friend: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user is a friend of current user",
    )
    wall_comments: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment wall posts",
    )
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can post on the user's wall",
    )
    can_see_all_posts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can see other users' audio on the wall",
    )
    can_see_audio: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can see the user's audio",
    )
    can_write_private_message: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can write private message",
    )
    can_send_friend_request: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can send a friend request",
    )
    mobile_phone: typing.Optional[str] = pydantic.Field(
        None, description="Information whether current user can see",
    )
    home_phone: typing.Optional[str] = pydantic.Field(
        None, description="User's mobile phone number",
    )
    site: typing.Optional[str] = pydantic.Field(
        None, description="User's website",
    )
    status_audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="User's status",
    )
    activity: typing.Optional[str] = pydantic.Field(
        None, description="User's status",
    )
    last_seen: typing.Optional["UsersLastSeen"] = pydantic.Field(
        None, description="",
    )
    exports: typing.Optional["UsersExports"] = pydantic.Field(
        None, description="",
    )
    crop_photo: typing.Optional["UsersCropPhoto"] = pydantic.Field(
        None, description="",
    )
    followers_count: typing.Optional[int] = pydantic.Field(
        None, description="Number of user's followers",
    )
    blacklisted: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user is in the requested user's blacklist.",
    )
    blacklisted_by_me: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is in current user's blacklist",
    )
    is_favorite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is in faves of current user",
    )
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the requested user is hidden from current user's newsfeed",
    )
    common_count: typing.Optional[int] = pydantic.Field(
        None, description="Number of common friends with current user",
    )
    occupation: typing.Optional["UsersOccupation"] = pydantic.Field(
        None, description="",
    )
    career: typing.Optional[typing.List["UsersCareer"]] = pydantic.Field(
        None, description="",
    )
    military: typing.Optional[typing.List["UsersMilitary"]] = pydantic.Field(
        None, description="",
    )
    university: typing.Optional[int] = pydantic.Field(
        None, description="University ID",
    )
    university_name: typing.Optional[str] = pydantic.Field(
        None, description="University name",
    )
    faculty: typing.Optional[int] = pydantic.Field(
        None, description="Faculty ID",
    )
    faculty_name: typing.Optional[str] = pydantic.Field(
        None, description="Faculty name",
    )
    graduation: typing.Optional[int] = pydantic.Field(
        None, description="Graduation year",
    )
    education_form: typing.Optional[str] = pydantic.Field(
        None, description="Education form",
    )
    education_status: typing.Optional[str] = pydantic.Field(
        None, description="User's education status",
    )
    home_town: typing.Optional[str] = pydantic.Field(
        None, description="User hometown",
    )
    relation: typing.Optional["UsersUserRelation"] = pydantic.Field(
        None, description="User relationship status",
    )
    relation_partner: typing.Optional["UsersUserMin"] = pydantic.Field(
        None, description="",
    )
    personal: typing.Optional["UsersPersonal"] = pydantic.Field(
        None, description="",
    )
    universities: typing.Optional[typing.List["UsersUniversity"]] = pydantic.Field(
        None, description="",
    )
    schools: typing.Optional[typing.List["UsersSchool"]] = pydantic.Field(
        None, description="",
    )
    relatives: typing.Optional[typing.List["UsersRelative"]] = pydantic.Field(
        None, description="",
    )
    is_subscribed_podcasts: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether current user is subscribed to podcasts",
    )
    can_subscribe_podcasts: typing.Optional[bool] = pydantic.Field(
        None, description="Owner in whitelist or not",
    )
    can_subscribe_posts: typing.Optional[bool] = pydantic.Field(
        None, description="Can subscribe to wall",
    )


class UsersUserMin(pydantic.BaseModel):
    deactivated: typing.Optional[str] = pydantic.Field(
        None, description="Returns if a profile is deleted or blocked",
    )
    first_name: typing.Optional[str] = pydantic.Field(
        None, description="User first name",
    )
    hidden: typing.Optional[int] = pydantic.Field(
        None, description="Returns if a profile is hidden.",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None, description="User last name",
    )
    can_access_closed: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    is_closed: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )


class UsersUserRelationEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3
    enum_4 = 4
    enum_5 = 5
    enum_6 = 6
    enum_7 = 7
    enum_8 = 8


class UsersUserRelation(pydantic.BaseModel):
    enum: typing.Optional[UsersUserRelationEnum] = pydantic.Field(
        None, description="",
    )


class UtilsDomainResolvedTypeEnum(str, Enum):
    user = "user"
    group = "group"
    application = "application"
    page = "page"


class UtilsDomainResolvedType(pydantic.BaseModel):
    enum: typing.Optional[UtilsDomainResolvedTypeEnum] = pydantic.Field(
        None, description="Object type",
    )


class UtilsLinkCheckedStatusEnum(str, Enum):
    not_banned = "not_banned"
    banned = "banned"
    processing = "processing"


class UtilsLinkCheckedStatus(pydantic.BaseModel):
    enum: typing.Optional[UtilsLinkCheckedStatusEnum] = pydantic.Field(
        None, description="Link status",
    )


class VideoVideo(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Video access key",
    )
    adding_date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the video has been added in Unixtime",
    )
    can_add: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can add the video",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the video",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can edit the video",
    )
    can_like: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can like the video",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can repost this video",
    )
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Number of comments",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when video has been uploaded in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Video description",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None, description="Video duration in seconds",
    )
    files: typing.Optional["VideoVideoFiles"] = pydantic.Field(
        None, description="",
    )
    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None, description="",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Video height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Video ID",
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None, description="",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    live: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the video is a live stream",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Video owner ID",
    )
    player: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the page with a player that can be used to play the video in the browser.",
    )
    processing: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the video is processing",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Video title",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Number of views",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Video width",
    )


class VideoVideoFiles(pydantic.BaseModel):
    external: typing.Optional[str] = pydantic.Field(
        None, description="URL of the external player",
    )
    mp4_1080: typing.Optional[str] = pydantic.Field(
        None, description="URL of the mpeg4 file with 1080p quality",
    )
    mp4_240: typing.Optional[str] = pydantic.Field(
        None, description="URL of the mpeg4 file with 240p quality",
    )
    mp4_360: typing.Optional[str] = pydantic.Field(
        None, description="URL of the mpeg4 file with 360p quality",
    )
    mp4_480: typing.Optional[str] = pydantic.Field(
        None, description="URL of the mpeg4 file with 480p quality",
    )
    mp4_720: typing.Optional[str] = pydantic.Field(
        None, description="URL of the mpeg4 file with 720p quality",
    )


class WallAppPost(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Application ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Application name",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 130 px in width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 604 px in width",
    )


class WallAttachedNote(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the note has been created in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Note owner's ID",
    )
    read_comments: typing.Optional[int] = pydantic.Field(
        None, description="Read comments number",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Note title",
    )
    view_url: typing.Optional[str] = pydantic.Field(
        None, description="URL of the page with note preview",
    )


class WallCommentAttachmentTypeEnum(str, Enum):
    photo = "photo"
    audio = "audio"
    video = "video"
    doc = "doc"
    link = "link"
    note = "note"
    page = "page"
    market_market_album = "market_market_album"
    market = "market"
    sticker = "sticker"


class WallCommentAttachmentType(pydantic.BaseModel):
    enum: typing.Optional[WallCommentAttachmentTypeEnum] = pydantic.Field(
        None, description="Attachment type",
    )


class WallGeo(pydantic.BaseModel):
    coordinates: typing.Optional[str] = pydantic.Field(
        None, description="Coordinates as string. <latitude> <longtitude>",
    )
    place: typing.Optional["BasePlace"] = pydantic.Field(
        None, description="",
    )
    showmap: typing.Optional[int] = pydantic.Field(
        None, description="Information whether a map is showed",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Place type",
    )


class WallGraffiti(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Graffiti owner's ID",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 200 px in width",
    )
    photo_586: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 586 px in width",
    )


class WallPostSource(pydantic.BaseModel):
    data: typing.Optional[str] = pydantic.Field(
        None, description="Additional data",
    )
    platform: typing.Optional[str] = pydantic.Field(
        None, description="Platform name",
    )
    type: typing.Optional["WallPostSourceType"] = pydantic.Field(
        None, description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="URL to an external site used to publish the post",
    )


class WallPostSourceTypeEnum(str, Enum):
    vk = "vk"
    widget = "widget"
    api = "api"
    rss = "rss"
    sms = "sms"


class WallPostSourceType(pydantic.BaseModel):
    enum: typing.Optional[WallPostSourceTypeEnum] = pydantic.Field(
        None, description="Type of post source",
    )


class WallPostTypeEnum(str, Enum):
    post = "post"
    copy = "copy"
    reply = "reply"
    postpone = "postpone"
    suggest = "suggest"


class WallPostType(pydantic.BaseModel):
    enum: typing.Optional[WallPostTypeEnum] = pydantic.Field(
        None, description="Post type",
    )


class WallPostedPhoto(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 130 px in width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 604 px in width",
    )


class WallViews(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Count",
    )


class WallWallComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Author ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real position of the comment",
    )
    reply_to_comment: typing.Optional[int] = pydantic.Field(
        None, description="Replied comment ID",
    )
    reply_to_user: typing.Optional[int] = pydantic.Field(
        None, description="Replied user ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    thread: typing.Optional["CommentThread"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    parents_stack: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    deleted: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )


class WallWallpost(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key to private object",
    )
    attachments: typing.Optional[
        typing.List["WallWallpostAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date of publishing in Unixtime",
    )
    edited: typing.Optional[int] = pydantic.Field(
        None, description="Date of editing in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Post author ID",
    )
    geo: typing.Optional["WallGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    is_archived: typing.Optional[bool] = pydantic.Field(
        None, description="Is post archived, only for post owners",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether the post in favorites list",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="Count of likes",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Wall owner's ID",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None, description="",
    )
    post_type: typing.Optional["WallPostType"] = pydantic.Field(
        None, description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None, description="Count of views",
    )
    signer_id: typing.Optional[int] = pydantic.Field(
        None, description="Post signer ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Post text",
    )
    views: typing.Optional["WallViews"] = pydantic.Field(
        None, description="Count of views",
    )


class WallWallpostAttachmentTypeEnum(str, Enum):
    photo = "photo"
    posted_photo = "posted_photo"
    audio = "audio"
    video = "video"
    doc = "doc"
    link = "link"
    graffiti = "graffiti"
    note = "note"
    app = "app"
    poll = "poll"
    page = "page"
    album = "album"
    photos_list = "photos_list"
    market_market_album = "market_market_album"
    market = "market"
    event = "event"


class WallWallpostAttachmentType(pydantic.BaseModel):
    enum: typing.Optional[WallWallpostAttachmentTypeEnum] = pydantic.Field(
        None, description="Attachment type",
    )


class WallWallpostFull(pydantic.BaseModel):
    wall_wallpost: typing.Optional["WallWallpost"] = pydantic.Field(
        None, description="",
    )
    copy_history: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None, description="",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can edit the post",
    )
    created_by: typing.Optional[int] = pydantic.Field(
        None, description="Post creator ID (if post still can be edited)",
    )
    can_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can delete the post",
    )
    can_pin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can pin the post",
    )
    is_pinned: typing.Optional[int] = pydantic.Field(
        None, description="Information whether the post is pinned",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None, description="",
    )
    marked_as_ads: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the post is marked as ads",
    )


class WidgetsCommentMedia(pydantic.BaseModel):
    item_id: typing.Optional[int] = pydantic.Field(
        None, description="Media item ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Media owner's ID",
    )
    thumb_src: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image (type=photo only)",
    )
    type: typing.Optional["WidgetsCommentMediaType"] = pydantic.Field(
        None, description="",
    )


class WidgetsCommentMediaTypeEnum(str, Enum):
    audio = "audio"
    photo = "photo"
    video = "video"


class WidgetsCommentMediaType(pydantic.BaseModel):
    enum: typing.Optional[WidgetsCommentMediaTypeEnum] = pydantic.Field(
        None, description="Media type",
    )


class WidgetsCommentReplies(pydantic.BaseModel):
    can_post: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the post",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = pydantic.Field(
        None, description="",
    )


class WidgetsWidgetLikes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Likes number",
    )


class AccountAccountCounters(pydantic.BaseModel):
    app_requests: typing.Optional[int] = pydantic.Field(
        None, description="New app requests number",
    )
    events: typing.Optional[int] = pydantic.Field(
        None, description="New events number",
    )
    friends: typing.Optional[int] = pydantic.Field(
        None, description="New friends requests number",
    )
    friends_suggestions: typing.Optional[int] = pydantic.Field(
        None, description="New friends suggestions number",
    )
    gifts: typing.Optional[int] = pydantic.Field(
        None, description="New gifts number",
    )
    groups: typing.Optional[int] = pydantic.Field(
        None, description="New groups number",
    )
    messages: typing.Optional[int] = pydantic.Field(
        None, description="New messages number",
    )
    notifications: typing.Optional[int] = pydantic.Field(
        None, description="New notifications number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None, description="New photo tags number",
    )
    videos: typing.Optional[int] = pydantic.Field(
        None, description="New video tags number",
    )


class AccountInfo(pydantic.BaseModel):
    twofa_required: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Two factor authentication is enabled", alias="2fa_required"
    )
    country: typing.Optional[str] = pydantic.Field(
        None, description="Country code",
    )
    https_required: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether HTTPS-only is enabled",
    )
    intro: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user has been processed intro",
    )
    lang: typing.Optional[int] = pydantic.Field(
        None, description="Language ID",
    )
    no_wall_replies: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether wall comments should be hidden",
    )
    own_posts_default: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether only owners posts should be shown",
    )


class AccountOffer(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        None, description="Offer description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Offer ID",
    )
    img: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image",
    )
    instruction: typing.Optional[str] = pydantic.Field(
        None, description="Instruction how to process the offer",
    )
    instruction_html: typing.Optional[str] = pydantic.Field(
        None, description="Instruction how to process the offer (HTML format)",
    )
    price: typing.Optional[int] = pydantic.Field(
        None, description="Offer price",
    )
    short_description: typing.Optional[str] = pydantic.Field(
        None, description="Offer short description",
    )
    tag: typing.Optional[str] = pydantic.Field(
        None, description="Offer tag",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Offer title",
    )


class AccountPushConversationsItem(pydantic.BaseModel):
    disabled_until: typing.Optional[int] = pydantic.Field(
        None, description="Time until that notifications are disabled in seconds",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None, description="Peer ID",
    )
    sound: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the sound are enabled",
    )


class AccountPushParamsModeEnum(str, Enum):
    on = "on"
    off = "off"
    no_sound = "no_sound"
    no_text = "no_text"


class AccountPushParamsMode(pydantic.BaseModel):
    enum: typing.Optional[AccountPushParamsModeEnum] = pydantic.Field(
        None, description="Settings parameters",
    )


class AccountPushParamsOnoffEnum(str, Enum):
    on = "on"
    off = "off"


class AccountPushParamsOnoff(pydantic.BaseModel):
    enum: typing.Optional[AccountPushParamsOnoffEnum] = pydantic.Field(
        None, description="Settings parameters",
    )


class AccountPushParamsSettingsEnum(str, Enum):
    on = "on"
    off = "off"
    fr_of_fr = "fr_of_fr"


class AccountPushParamsSettings(pydantic.BaseModel):
    enum: typing.Optional[AccountPushParamsSettingsEnum] = pydantic.Field(
        None, description="Settings parameters",
    )


class AccountPushSettings(pydantic.BaseModel):
    disabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether notifications are disabled",
    )
    disabled_until: typing.Optional[int] = pydantic.Field(
        None, description="Time until that notifications are disabled in Unixtime",
    )
    settings: typing.Optional["AccountPushParams"] = pydantic.Field(
        None, description="",
    )
    conversations: typing.Optional["AccountPushConversations"] = pydantic.Field(
        None, description="",
    )


class AccountUserSettings(pydantic.BaseModel):
    users_user_min: typing.Optional["UsersUserMin"] = pydantic.Field(
        None, description="",
    )
    users_user_settings_xtr: typing.Optional["UsersUserSettingsXtr"] = pydantic.Field(
        None, description="",
    )


class AddressesFieldsEnum(str, Enum):
    id = "id"
    title = "title"
    address = "address"
    additional_address = "additional_address"
    country_id = "country_id"
    city_id = "city_id"
    metro_station_id = "metro_station_id"
    latitude = "latitude"
    longitude = "longitude"
    distance = "distance"
    work_info_status = "work_info_status"
    timetable = "timetable"
    phone = "phone"
    time_offset = "time_offset"


class AddressesFields(pydantic.BaseModel):
    enum: typing.Optional[AddressesFieldsEnum] = pydantic.Field(
        None, description="",
    )


class AdsAccesses(pydantic.BaseModel):
    client_id: typing.Optional[str] = pydantic.Field(
        None, description="Client ID",
    )
    role: typing.Optional["AdsAccessRole"] = pydantic.Field(
        None, description="",
    )


class AdsAccount(pydantic.BaseModel):
    access_role: typing.Optional["AdsAccessRole"] = pydantic.Field(
        None, description="",
    )
    account_id: typing.Optional[int] = pydantic.Field(
        None, description="Account ID",
    )
    account_status: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether account is active",
    )
    account_type: typing.Optional["AdsAccountType"] = pydantic.Field(
        None, description="",
    )


class AdsAd(pydantic.BaseModel):
    ad_format: typing.Optional[int] = pydantic.Field(
        None, description="Ad format",
    )
    ad_platform: typing.Optional[("typing.Union[int, str]",)] = pydantic.Field(
        None, description="Ad platform",
    )
    all_limit: typing.Optional[int] = pydantic.Field(
        None, description="Total limit",
    )
    approved: typing.Optional["AdsAdApproved"] = pydantic.Field(
        None, description="",
    )
    campaign_id: typing.Optional[int] = pydantic.Field(
        None, description="Campaign ID",
    )
    category1_id: typing.Optional[int] = pydantic.Field(
        None, description="Category ID",
    )
    category2_id: typing.Optional[int] = pydantic.Field(
        None, description="Additional category ID",
    )
    cost_type: typing.Optional["AdsAdCostType"] = pydantic.Field(
        None, description="",
    )
    cpc: typing.Optional[int] = pydantic.Field(
        None, description="Cost of a click, kopecks",
    )
    cpm: typing.Optional[int] = pydantic.Field(
        None, description="Cost of 1000 impressions, kopecks",
    )
    cpa: typing.Optional[int] = pydantic.Field(
        None, description="Cost of an action, kopecks",
    )
    disclaimer_medical: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether disclaimer is enabled",
    )
    disclaimer_specialist: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether disclaimer is enabled",
    )
    disclaimer_supplements: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether disclaimer is enabled",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Ad ID",
    )
    impressions_limit: typing.Optional[int] = pydantic.Field(
        None, description="Impressions limit",
    )
    impressions_limited: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether impressions are limited",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Ad title",
    )
    status: typing.Optional["AdsAdStatus"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the ad is a video",
    )


class AdsAdLayout(pydantic.BaseModel):
    ad_format: typing.Optional[int] = pydantic.Field(
        None, description="Ad format",
    )
    campaign_id: typing.Optional[int] = pydantic.Field(
        None, description="Campaign ID",
    )
    cost_type: typing.Optional["AdsAdCostType"] = pydantic.Field(
        None, description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Ad description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Ad ID",
    )
    image_src: typing.Optional[str] = pydantic.Field(
        None, description="Image URL",
    )
    image_src_2x: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image in double size",
    )
    link_domain: typing.Optional[str] = pydantic.Field(
        None, description="Domain of advertised object",
    )
    link_url: typing.Optional[str] = pydantic.Field(
        None, description="URL of advertised object",
    )
    preview_link: typing.Optional[("typing.Union[int, str]",)] = pydantic.Field(
        None, description="link to preview an ad as it is shown on the website",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Ad title",
    )
    video: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the ad is a video",
    )


class AdsCampaign(pydantic.BaseModel):
    all_limit: typing.Optional[str] = pydantic.Field(
        None, description="Campaign's total limit, rubles",
    )
    day_limit: typing.Optional[str] = pydantic.Field(
        None, description="Campaign's day limit, rubles",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Campaign ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Campaign title",
    )
    start_time: typing.Optional[int] = pydantic.Field(
        None, description="Campaign start time, as Unixtime",
    )
    status: typing.Optional["AdsCampaignStatus"] = pydantic.Field(
        None, description="",
    )
    stop_time: typing.Optional[int] = pydantic.Field(
        None, description="Campaign stop time, as Unixtime",
    )
    type: typing.Optional["AdsCampaignType"] = pydantic.Field(
        None, description="",
    )


class AdsCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Category ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Category name",
    )
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = pydantic.Field(
        None, description="",
    )


class AdsClient(pydantic.BaseModel):
    all_limit: typing.Optional[str] = pydantic.Field(
        None, description="Client's total limit, rubles",
    )
    day_limit: typing.Optional[str] = pydantic.Field(
        None, description="Client's day limit, rubles",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Client ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Client name",
    )


class AdsCriteria(pydantic.BaseModel):
    age_from: typing.Optional[int] = pydantic.Field(
        None, description="Age from",
    )
    age_to: typing.Optional[int] = pydantic.Field(
        None, description="Age to",
    )
    apps: typing.Optional[str] = pydantic.Field(
        None, description="Apps IDs",
    )
    apps_not: typing.Optional[str] = pydantic.Field(
        None, description="Apps IDs to except",
    )
    birthday: typing.Optional[int] = pydantic.Field(
        None, description="Days to birthday",
    )
    cities: typing.Optional[str] = pydantic.Field(
        None, description="Cities IDs",
    )
    cities_not: typing.Optional[str] = pydantic.Field(
        None, description="Cities IDs to except",
    )
    country: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    districts: typing.Optional[str] = pydantic.Field(
        None, description="Districts IDs",
    )
    groups: typing.Optional[str] = pydantic.Field(
        None, description="Communities IDs",
    )
    interest_categories: typing.Optional[str] = pydantic.Field(
        None, description="Interests categories IDs",
    )
    interests: typing.Optional[str] = pydantic.Field(
        None, description="Interests",
    )
    paying: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the user has proceeded VK payments before",
    )
    positions: typing.Optional[str] = pydantic.Field(
        None, description="Positions IDs",
    )
    religions: typing.Optional[str] = pydantic.Field(
        None, description="Religions IDs",
    )
    retargeting_groups: typing.Optional[str] = pydantic.Field(
        None, description="Retargeting groups IDs",
    )
    retargeting_groups_not: typing.Optional[str] = pydantic.Field(
        None, description="Retargeting groups IDs to except",
    )
    school_from: typing.Optional[int] = pydantic.Field(
        None, description="School graduation year from",
    )
    school_to: typing.Optional[int] = pydantic.Field(
        None, description="School graduation year to",
    )
    schools: typing.Optional[str] = pydantic.Field(
        None, description="Schools IDs",
    )
    sex: typing.Optional["AdsCriteriaSex"] = pydantic.Field(
        None, description="",
    )
    stations: typing.Optional[str] = pydantic.Field(
        None, description="Stations IDs",
    )
    statuses: typing.Optional[str] = pydantic.Field(
        None, description="Relationship statuses",
    )
    streets: typing.Optional[str] = pydantic.Field(
        None, description="Streets IDs",
    )
    travellers: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Travellers only",
    )
    uni_from: typing.Optional[int] = pydantic.Field(
        None, description="University graduation year from",
    )
    uni_to: typing.Optional[int] = pydantic.Field(
        None, description="University graduation year to",
    )
    user_browsers: typing.Optional[str] = pydantic.Field(
        None, description="Browsers",
    )
    user_devices: typing.Optional[str] = pydantic.Field(
        None, description="Devices",
    )
    user_os: typing.Optional[str] = pydantic.Field(
        None, description="Operating systems",
    )


class AdsDemoStats(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    stats: typing.Optional["AdsDemostatsFormat"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["AdsObjectType"] = pydantic.Field(
        None, description="",
    )


class AdsFloodStats(pydantic.BaseModel):
    left: typing.Optional[int] = pydantic.Field(
        None, description="Requests left",
    )
    refresh: typing.Optional[int] = pydantic.Field(
        None, description="Time to refresh in seconds",
    )


class AdsLinkStatus(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        None, description="Reject reason",
    )
    redirect_url: typing.Optional[str] = pydantic.Field(
        None, description="URL",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="Link status",
    )


class AdsParagraphs(pydantic.BaseModel):
    paragraph: typing.Optional[str] = pydantic.Field(
        None, description="Rules paragraph",
    )


class AdsPromotedPostReach(pydantic.BaseModel):
    hide: typing.Optional[int] = pydantic.Field(
        None, description="Hides amount",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID from 'ids' parameter",
    )
    join_group: typing.Optional[int] = pydantic.Field(
        None, description="Community joins",
    )
    links: typing.Optional[int] = pydantic.Field(
        None, description="Link clicks",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None, description="Subscribers reach",
    )
    reach_total: typing.Optional[int] = pydantic.Field(
        None, description="Total reach",
    )
    report: typing.Optional[int] = pydantic.Field(
        None, description="Reports amount",
    )
    to_group: typing.Optional[int] = pydantic.Field(
        None, description="Community clicks",
    )
    unsubscribe: typing.Optional[int] = pydantic.Field(
        None, description="'Unsubscribe' events amount",
    )
    video_views_100p: typing.Optional[int] = pydantic.Field(
        None, description="Video views for 100 percent",
    )
    video_views_25p: typing.Optional[int] = pydantic.Field(
        None, description="Video views for 25 percent",
    )
    video_views_3s: typing.Optional[int] = pydantic.Field(
        None, description="Video views for 3 seconds",
    )
    video_views_50p: typing.Optional[int] = pydantic.Field(
        None, description="Video views for 50 percent",
    )
    video_views_75p: typing.Optional[int] = pydantic.Field(
        None, description="Video views for 75 percent",
    )
    video_views_start: typing.Optional[int] = pydantic.Field(
        None, description="Video starts",
    )


class AdsRejectReason(pydantic.BaseModel):
    comment: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    rules: typing.Optional[typing.List["AdsRules"]] = pydantic.Field(
        None, description="",
    )


class AdsRules(pydantic.BaseModel):
    paragraphs: typing.Optional[typing.List["AdsParagraphs"]] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Comment",
    )


class AdsStats(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    stats: typing.Optional["AdsStatsFormat"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["AdsObjectType"] = pydantic.Field(
        None, description="",
    )


class AdsStatsAge(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None, description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None, description="Impressions rate",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="Age interval",
    )


class AdsStatsCities(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None, description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None, description="Impressions rate",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="City name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )


class AdsStatsSex(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None, description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None, description="Impressions rate",
    )
    value: typing.Optional["AdsStatsSexValue"] = pydantic.Field(
        None, description="",
    )


class AdsStatsSexAge(pydantic.BaseModel):
    clicks_rate: typing.Optional[int] = pydantic.Field(
        None, description="Clicks rate",
    )
    impressions_rate: typing.Optional[int] = pydantic.Field(
        None, description="Impressions rate",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="Sex and age interval",
    )


class AdsTargSettings(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Ad ID",
    )
    campaign_id: typing.Optional[int] = pydantic.Field(
        None, description="Campaign ID",
    )
    ads_criteria: typing.Optional["AdsCriteria"] = pydantic.Field(
        None, description="",
    )


class AdsTargStats(pydantic.BaseModel):
    audience_count: typing.Optional[int] = pydantic.Field(
        None, description="Audience",
    )
    recommended_cpc: typing.Optional[int] = pydantic.Field(
        None, description="Recommended CPC value",
    )
    recommended_cpm: typing.Optional[int] = pydantic.Field(
        None, description="Recommended CPM value",
    )


class AdsTargSuggestions(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Object name",
    )


class AdsTargSuggestionsCities(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Object name",
    )
    parent: typing.Optional[str] = pydantic.Field(
        None, description="Parent object",
    )


class AdsTargSuggestionsRegions(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Object name",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Object type",
    )


class AdsTargSuggestionsSchools(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None, description="Full school title",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="School ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="School title",
    )
    parent: typing.Optional[str] = pydantic.Field(
        None, description="City name",
    )
    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = pydantic.Field(
        None, description="",
    )


class AdsTargetGroup(pydantic.BaseModel):
    audience_count: typing.Optional[int] = pydantic.Field(
        None, description="Audience",
    )
    domain: typing.Optional[str] = pydantic.Field(
        None, description="Site domain",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Group ID",
    )
    lifetime: typing.Optional[int] = pydantic.Field(
        None, description="Number of days for user to be in group",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Group name",
    )
    pixel: typing.Optional[str] = pydantic.Field(
        None, description="Pixel code",
    )


class AdsUsers(pydantic.BaseModel):
    accesses: typing.Optional[typing.List["AdsAccesses"]] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class AppsAppLeaderboardTypeEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class AppsAppLeaderboardType(pydantic.BaseModel):
    enum: typing.Optional[AppsAppLeaderboardTypeEnum] = pydantic.Field(
        None, description="Leaderboard type",
    )


class AppsAppMin(pydantic.BaseModel):
    type: typing.Optional["AppsAppType"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Application ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Application title",
    )
    author_id: typing.Optional[int] = pydantic.Field(
        None, description="Application author's ID",
    )
    icon_139: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app icon with 139 px in width",
    )
    icon_150: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app icon with 150 px in width",
    )
    icon_278: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app icon with 278 px in width",
    )
    icon_75: typing.Optional[str] = pydantic.Field(
        None, description="URL of the app icon with 75 px in width",
    )


class AppsLeaderboard(pydantic.BaseModel):
    level: typing.Optional[int] = pydantic.Field(
        None, description="Level",
    )
    points: typing.Optional[int] = pydantic.Field(
        None, description="Points number",
    )
    score: typing.Optional[int] = pydantic.Field(
        None, description="Score number",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class AppsScope(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Scope name",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Scope title",
    )


class BaseError(pydantic.BaseModel):
    error_code: typing.Optional[int] = pydantic.Field(
        None, description="Error code",
    )
    error_msg: typing.Optional[str] = pydantic.Field(
        None, description="Error message",
    )
    request_params: typing.Optional[typing.List["BaseRequestParam"]] = pydantic.Field(
        None, description="",
    )


class BaseImage(pydantic.BaseModel):
    height: typing.Optional[int] = pydantic.Field(
        None, description="Image height",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Image url",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Image width",
    )


class BaseMessageError(pydantic.BaseModel):
    code: typing.Optional[int] = pydantic.Field(
        None, description="Error code",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Error message",
    )


class BaseObject(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Object title",
    )


class BaseObjectWithName(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Object name",
    )


class BaseRequestParam(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="Parameter name",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="Parameter value",
    )


class BaseUploadServer(pydantic.BaseModel):
    upload_url: typing.Optional[str] = pydantic.Field(
        None, description="Upload URL",
    )


class BaseUserGroupFieldsEnum(str, Enum):
    about = "about"
    action_button = "action_button"
    activities = "activities"
    activity = "activity"
    addresses = "addresses"
    admin_level = "admin_level"
    age_limits = "age_limits"
    author_id = "author_id"
    ban_info = "ban_info"
    bdate = "bdate"
    blacklisted = "blacklisted"
    blacklisted_by_me = "blacklisted_by_me"
    books = "books"
    can_create_topic = "can_create_topic"
    can_message = "can_message"
    can_post = "can_post"
    can_see_all_posts = "can_see_all_posts"
    can_see_audio = "can_see_audio"
    can_send_friend_request = "can_send_friend_request"
    can_upload_video = "can_upload_video"
    can_write_private_message = "can_write_private_message"
    career = "career"
    city = "city"
    common_count = "common_count"
    connections = "connections"
    contacts = "contacts"
    counters = "counters"
    country = "country"
    cover = "cover"
    crop_photo = "crop_photo"
    deactivated = "deactivated"
    description = "description"
    domain = "domain"
    education = "education"
    exports = "exports"
    finish_date = "finish_date"
    fixed_post = "fixed_post"
    followers_count = "followers_count"
    friend_status = "friend_status"
    games = "games"
    has_market_app = "has_market_app"
    has_mobile = "has_mobile"
    has_photo = "has_photo"
    home_town = "home_town"
    id = "id"
    interests = "interests"
    is_admin = "is_admin"
    is_closed = "is_closed"
    is_favorite = "is_favorite"
    is_friend = "is_friend"
    is_hidden_from_feed = "is_hidden_from_feed"
    is_member = "is_member"
    is_messages_blocked = "is_messages_blocked"
    can_send_notify = "can_send_notify"
    is_subscribed = "is_subscribed"
    last_seen = "last_seen"
    links = "links"
    lists = "lists"
    maiden_name = "maiden_name"
    main_album_id = "main_album_id"
    main_section = "main_section"
    market = "market"
    member_status = "member_status"
    members_count = "members_count"
    military = "military"
    movies = "movies"
    music = "music"
    name = "name"
    nickname = "nickname"
    occupation = "occupation"
    online = "online"
    online_status = "online_status"
    personal = "personal"
    phone = "phone"
    photo_100 = "photo_100"
    photo_200 = "photo_200"
    photo_200_orig = "photo_200_orig"
    photo_400_orig = "photo_400_orig"
    photo_50 = "photo_50"
    photo_id = "photo_id"
    photo_max = "photo_max"
    photo_max_orig = "photo_max_orig"
    quotes = "quotes"
    relation = "relation"
    relatives = "relatives"
    schools = "schools"
    screen_name = "screen_name"
    sex = "sex"
    site = "site"
    start_date = "start_date"
    status = "status"
    timezone = "timezone"
    trending = "trending"
    tv = "tv"
    type = "type"
    universities = "universities"
    verified = "verified"
    wall_comments = "wall_comments"
    wiki_page = "wiki_page"
    vk_admin_status = "vk_admin_status"


class BaseUserGroupFields(pydantic.BaseModel):
    enum: typing.Optional[BaseUserGroupFieldsEnum] = pydantic.Field(
        None, description="",
    )


class BaseUserId(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class BoardDefaultOrderEnum(int, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_minus_1 = -1
    enum_minus_2 = -2


class BoardDefaultOrder(pydantic.BaseModel):
    enum: typing.Optional[BoardDefaultOrderEnum] = pydantic.Field(
        None, description="Sort type",
    )


class BoardTopicComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Author ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real position of the comment",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )


class BoardTopicPoll(pydantic.BaseModel):
    answer_id: typing.Optional[int] = pydantic.Field(
        None, description="Current user's answer ID",
    )
    answers: typing.Optional[typing.List["PollsAnswer"]] = pydantic.Field(
        None, description="",
    )
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when poll has been created in Unixtime",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the poll is closed",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Poll owner's ID",
    )
    poll_id: typing.Optional[int] = pydantic.Field(
        None, description="Poll ID",
    )
    question: typing.Optional[str] = pydantic.Field(
        None, description="Poll question",
    )
    votes: typing.Optional[str] = pydantic.Field(
        None, description="Votes number",
    )


class CallbackBoardPostDelete(pydantic.BaseModel):
    topic_owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    topic_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackConfirmationMessage(pydantic.BaseModel):
    type: typing.Optional["CallbackMessageType"] = pydantic.Field(
        None, description="",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    secret: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class CallbackGroupChangePhoto(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )


class CallbackGroupChangeSettings(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    self: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )


class CallbackGroupJoin(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    join_type: typing.Optional["CallbackGroupJoinType"] = pydantic.Field(
        None, description="",
    )


class CallbackGroupLeave(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    self: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )


class CallbackGroupOfficersEdit(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    level_old: typing.Optional["CallbackGroupOfficerRole"] = pydantic.Field(
        None, description="",
    )
    level_new: typing.Optional["CallbackGroupOfficerRole"] = pydantic.Field(
        None, description="",
    )


class CallbackGroupSettingsChanges(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    access: typing.Optional["GroupsGroupIsClosed"] = pydantic.Field(
        None, description="",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    public_category: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    public_subcategory: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = pydantic.Field(
        None, description="",
    )
    website: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    enable_status_default: typing.Optional["GroupsGroupWall"] = pydantic.Field(
        None, description="",
    )
    enable_audio: typing.Optional["GroupsGroupAudio"] = pydantic.Field(
        None, description="",
    )
    enable_video: typing.Optional["GroupsGroupVideo"] = pydantic.Field(
        None, description="",
    )
    enable_photo: typing.Optional["GroupsGroupPhotos"] = pydantic.Field(
        None, description="",
    )
    enable_market: typing.Optional["CallbackGroupMarket"] = pydantic.Field(
        None, description="",
    )


class CallbackMarketComment(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    market_owner_od: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    photo_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackMarketCommentDelete(pydantic.BaseModel):
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    item_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackMessageAllow(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    key: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class CallbackMessageBase(pydantic.BaseModel):
    type: typing.Optional["CallbackMessageType"] = pydantic.Field(
        None, description="",
    )
    object: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackMessageDeny(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackPhotoComment(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    photo_owner_od: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackPhotoCommentDelete(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    photo_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackPollVoteNew(pydantic.BaseModel):
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    poll_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    option_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackUserBlock(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    unblock_date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    reason: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class CallbackUserUnblock(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    by_end_date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackVideoComment(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    video_owner_od: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackVideoCommentDelete(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    video_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class CallbackWallCommentDelete(pydantic.BaseModel):
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class DatabaseCity(pydantic.BaseModel):
    base_object: typing.Optional["BaseObject"] = pydantic.Field(
        None, description="",
    )
    area: typing.Optional[str] = pydantic.Field(
        None, description="Area title",
    )
    region: typing.Optional[str] = pydantic.Field(
        None, description="Region title",
    )
    important: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the city is included in important cities list",
    )


class DatabaseFaculty(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Faculty ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Faculty title",
    )


class DatabaseRegion(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Region ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Region title",
    )


class DatabaseSchool(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="School ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="School title",
    )


class DatabaseStation(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    color: typing.Optional[str] = pydantic.Field(
        None, description="Hex color code without #",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Station ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Station name",
    )


class DatabaseUniversity(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="University ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="University title",
    )


class DocsDocAttachmentTypeEnum(str, Enum):
    doc = "doc"
    graffiti = "graffiti"
    audio_message = "audio_message"


class DocsDocAttachmentType(pydantic.BaseModel):
    enum: typing.Optional[DocsDocAttachmentTypeEnum] = pydantic.Field(
        None, description="Doc attachment type",
    )


class DocsDocTypes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Number of docs",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Doc type ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Doc type title",
    )


class DocsDocUploadResponse(pydantic.BaseModel):
    file: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded file data",
    )


class FaveBookmark(pydantic.BaseModel):
    added_date: typing.Optional[int] = pydantic.Field(
        None, description="Timestamp, when this item was bookmarked",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    post: typing.Optional["WallWallpostFull"] = pydantic.Field(
        None, description="",
    )
    product: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None, description="",
    )
    seen: typing.Optional[bool] = pydantic.Field(
        None, description="Has user seen this item",
    )
    tags: typing.Optional[typing.List["FaveTag"]] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["FaveBookmarkType"] = pydantic.Field(
        None, description="Item type",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )


class FavePage(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        None, description="Some info about user or group",
    )
    group: typing.Optional["GroupsGroupFull"] = pydantic.Field(
        None, description="",
    )
    tags: typing.Optional[typing.List["FaveTag"]] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["FavePageType"] = pydantic.Field(
        None, description="Item type",
    )
    updated_date: typing.Optional[int] = pydantic.Field(
        None, description="Timestamp, when this page was bookmarked",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )


class FaveTag(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Tag id",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Tag name",
    )


class FriendsFriendStatus(pydantic.BaseModel):
    friend_status: typing.Optional["FriendsFriendStatusStatus"] = pydantic.Field(
        None, description="",
    )
    read_state: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether request is unviewed",
    )
    request_message: typing.Optional[str] = pydantic.Field(
        None, description="Message sent with request",
    )
    sign: typing.Optional[str] = pydantic.Field(
        None, description="MD5 hash for the result validation",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class FriendsFriendsList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="List ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="List title",
    )


class FriendsMutualFriend(pydantic.BaseModel):
    common_count: typing.Optional[int] = pydantic.Field(
        None, description="Total mutual friends number",
    )
    common_friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class FriendsRequests(pydantic.BaseModel):
    from_: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class FriendsRequestsXtrMessage(pydantic.BaseModel):
    from_: typing.Optional[str] = pydantic.Field(
        None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )
    message: typing.Optional[str] = pydantic.Field(
        None, description="Message sent with a request",
    )
    mutual: typing.Optional["FriendsRequestsMutual"] = pydantic.Field(
        None, description="",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class FriendsUserXtrLists(pydantic.BaseModel):
    users_user_full: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )
    lists: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class FriendsUserXtrPhone(pydantic.BaseModel):
    users_user_full: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None, description="User phone",
    )


class GiftsGift(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when gist has been sent in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Gift sender ID",
    )
    gift: typing.Optional["GiftsLayout"] = pydantic.Field(
        None, description="",
    )
    gift_hash: typing.Optional[str] = pydantic.Field(
        None, description="Hash",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Gift ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    privacy: typing.Optional["GiftsGiftPrivacy"] = pydantic.Field(
        None, description="",
    )


class GroupsAddress(pydantic.BaseModel):
    additional_address: typing.Optional[str] = pydantic.Field(
        None, description="Additional address to the place (6 floor, left door)",
    )
    address: typing.Optional[str] = pydantic.Field(
        None, description="String address to the place (Nevsky, 28)",
    )
    city_id: typing.Optional[int] = pydantic.Field(
        None, description="City id of address",
    )
    country_id: typing.Optional[int] = pydantic.Field(
        None, description="Country id of address",
    )
    distance: typing.Optional[int] = pydantic.Field(
        None, description="Distance from the point",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Address id",
    )
    latitude: typing.Optional[int] = pydantic.Field(
        None, description="Address latitude",
    )
    longitude: typing.Optional[int] = pydantic.Field(
        None, description="Address longitude",
    )
    metro_station_id: typing.Optional[int] = pydantic.Field(
        None, description="Metro id of address",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None, description="Address phone",
    )
    time_offset: typing.Optional[int] = pydantic.Field(
        None, description="Time offset int minutes from utc time",
    )
    timetable: typing.Optional["GroupsAddressTimetable"] = pydantic.Field(
        None, description="Week timetable for the address",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Title of the place (Zinger, etc)",
    )
    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = pydantic.Field(
        None, description="Status of information about timetable",
    )


class GroupsAddressesInfo(pydantic.BaseModel):
    is_enabled: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether addresses is enabled",
    )
    main_address_id: typing.Optional[int] = pydantic.Field(
        None, description="Main address id for group",
    )


class GroupsBannedItem(pydantic.BaseModel):
    owner_xtr_ban: typing.Optional[
        typing.Union["GroupsOwnerXtrBanInfo"]
    ] = pydantic.Field(
        None, description="",
    )


class GroupsCallbackServer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    creator_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    secret_key: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class GroupsCallbackSettings(pydantic.BaseModel):
    api_version: typing.Optional[str] = pydantic.Field(
        None, description="API version used for the events",
    )
    events: typing.Optional["GroupsLongPollEvents"] = pydantic.Field(
        None, description="",
    )


class GroupsContactsItem(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None, description="Contact description",
    )
    email: typing.Optional[str] = pydantic.Field(
        None, description="Contact email",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None, description="Contact phone",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class GroupsCountersGroup(pydantic.BaseModel):
    addresses: typing.Optional[int] = pydantic.Field(
        None, description="Addresses number",
    )
    albums: typing.Optional[int] = pydantic.Field(
        None, description="Photo albums number",
    )
    audios: typing.Optional[int] = pydantic.Field(
        None, description="Audios number",
    )
    docs: typing.Optional[int] = pydantic.Field(
        None, description="Docs number",
    )
    market: typing.Optional[int] = pydantic.Field(
        None, description="Market items number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None, description="Photos number",
    )
    topics: typing.Optional[int] = pydantic.Field(
        None, description="Topics number",
    )
    videos: typing.Optional[int] = pydantic.Field(
        None, description="Videos number",
    )


class GroupsCover(pydantic.BaseModel):
    enabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether cover is enabled",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None, description="",
    )


class GroupsFieldsEnum(str, Enum):
    market = "market"
    member_status = "member_status"
    is_favorite = "is_favorite"
    is_subscribed = "is_subscribed"
    city = "city"
    country = "country"
    verified = "verified"
    description = "description"
    wiki_page = "wiki_page"
    members_count = "members_count"
    counters = "counters"
    cover = "cover"
    can_post = "can_post"
    can_see_all_posts = "can_see_all_posts"
    activity = "activity"
    fixed_post = "fixed_post"
    can_create_topic = "can_create_topic"
    can_upload_video = "can_upload_video"
    has_photo = "has_photo"
    status = "status"
    main_album_id = "main_album_id"
    links = "links"
    contacts = "contacts"
    site = "site"
    main_section = "main_section"
    trending = "trending"
    can_message = "can_message"
    is_market_cart_enabled = "is_market_cart_enabled"
    is_messages_blocked = "is_messages_blocked"
    can_send_notify = "can_send_notify"
    online_status = "online_status"
    start_date = "start_date"
    finish_date = "finish_date"
    age_limits = "age_limits"
    ban_info = "ban_info"
    action_button = "action_button"
    author_id = "author_id"
    phone = "phone"
    has_market_app = "has_market_app"
    addresses = "addresses"
    live_covers = "live_covers"
    is_adult = "is_adult"
    can_subscribe_posts = "can_subscribe_posts"
    warning_notification = "warning_notification"


class GroupsFields(pydantic.BaseModel):
    enum: typing.Optional[GroupsFieldsEnum] = pydantic.Field(
        None, description="",
    )


class GroupsFilterEnum(str, Enum):
    admin = "admin"
    editor = "editor"
    moder = "moder"
    groups = "groups"
    publics = "publics"
    events = "events"
    has_addresses = "has_addresses"


class GroupsFilter(pydantic.BaseModel):
    enum: typing.Optional[GroupsFilterEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupAccessEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupAccess(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupAccessEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupAgeLimitsEnum(int, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3


class GroupsGroupAgeLimits(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupAgeLimitsEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupBanInfo(pydantic.BaseModel):
    comment: typing.Optional[str] = pydantic.Field(
        None, description="Ban comment",
    )
    end_date: typing.Optional[int] = pydantic.Field(
        None, description="End date of ban in Unixtime",
    )


class GroupsGroupCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Category ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Category name",
    )
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = pydantic.Field(
        None, description="",
    )


class GroupsGroupCategoryFull(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Category ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Category name",
    )
    page_count: typing.Optional[int] = pydantic.Field(
        None, description="Pages number",
    )
    page_previews: typing.Optional[typing.List["GroupsGroup"]] = pydantic.Field(
        None, description="",
    )
    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = pydantic.Field(
        None, description="",
    )


class GroupsGroupCategoryType(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class GroupsGroupDocsEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupDocs(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupDocsEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupFullMainSectionEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3
    enum_4 = 4
    enum_5 = 5


class GroupsGroupFullMainSection(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupFullMainSectionEnum] = pydantic.Field(
        None, description="Main section of community",
    )


class GroupsGroupLink(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Link label",
    )
    desc: typing.Optional[str] = pydantic.Field(
        None, description="Link description",
    )
    edit_title: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the title can be edited",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Link ID",
    )
    image_processing: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the image on processing",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )


class GroupsGroupMarketCurrencyEnum(int, Enum):
    enum_643 = 643
    enum_980 = 980
    enum_398 = 398
    enum_978 = 978
    enum_840 = 840


class GroupsGroupMarketCurrency(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupMarketCurrencyEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupPublicCategoryList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    subtypes_list: typing.Optional[
        typing.List["GroupsGroupCategoryType"]
    ] = pydantic.Field(
        None, description="",
    )


class GroupsGroupRoleEnum(str, Enum):
    moderator = "moderator"
    editor = "editor"
    administrator = "administrator"


class GroupsGroupRole(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupRoleEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupSettings(pydantic.BaseModel):
    access: typing.Optional[int] = pydantic.Field(
        None, description="Community access settings",
    )
    address: typing.Optional[str] = pydantic.Field(
        None, description="Community's page domain",
    )
    audio: typing.Optional[int] = pydantic.Field(
        None, description="Audio settings",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Community description",
    )
    docs: typing.Optional[int] = pydantic.Field(
        None, description="Docs settings",
    )
    obscene_filter: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the obscene filter is enabled",
    )
    obscene_stopwords: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the stopwords filter is enabled",
    )
    obscene_words: typing.Optional[str] = pydantic.Field(
        None, description="The list of stop words",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None, description="Photos settings",
    )
    public_category: typing.Optional[int] = pydantic.Field(
        None, description="Information about the group category",
    )
    public_category_list: typing.Optional[
        typing.List["GroupsGroupPublicCategoryList"]
    ] = pydantic.Field(
        None, description="",
    )
    public_subcategory: typing.Optional[int] = pydantic.Field(
        None, description="Information about the group subcategory",
    )
    rss: typing.Optional[str] = pydantic.Field(
        None, description="URL of the RSS feed",
    )
    subject: typing.Optional[int] = pydantic.Field(
        None, description="Community subject ID",
    )
    subject_list: typing.Optional[typing.List["GroupsSubjectItem"]] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Community title",
    )
    topics: typing.Optional[int] = pydantic.Field(
        None, description="Topics settings",
    )
    video: typing.Optional[int] = pydantic.Field(
        None, description="Video settings",
    )
    wall: typing.Optional[int] = pydantic.Field(
        None, description="Wall settings",
    )
    website: typing.Optional[str] = pydantic.Field(
        None, description="Community website",
    )
    wiki: typing.Optional[int] = pydantic.Field(
        None, description="Wiki settings",
    )


class GroupsGroupSubjectEnum(str, Enum):
    enum_1 = 1
    enum_2 = 2
    enum_3 = 3
    enum_4 = 4
    enum_5 = 5
    enum_6 = 6
    enum_7 = 7
    enum_8 = 8
    enum_9 = 9
    enum_10 = 10
    enum_11 = 11
    enum_12 = 12
    enum_13 = 13
    enum_14 = 14
    enum_15 = 15
    enum_16 = 16
    enum_17 = 17
    enum_18 = 18
    enum_19 = 19
    enum_20 = 20
    enum_21 = 21
    enum_22 = 22
    enum_23 = 23
    enum_24 = 24
    enum_25 = 25
    enum_26 = 26
    enum_27 = 27
    enum_28 = 28
    enum_29 = 29
    enum_30 = 30
    enum_31 = 31
    enum_32 = 32
    enum_33 = 33
    enum_34 = 34
    enum_35 = 35
    enum_36 = 36
    enum_37 = 37
    enum_38 = 38
    enum_39 = 39
    enum_40 = 40
    enum_41 = 41
    enum_42 = 42


class GroupsGroupSubject(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupSubjectEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupTopicsEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupTopics(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupTopicsEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupWikiEnum(int, Enum):
    enum_0 = 0
    enum_1 = 1
    enum_2 = 2


class GroupsGroupWiki(pydantic.BaseModel):
    enum: typing.Optional[GroupsGroupWikiEnum] = pydantic.Field(
        None, description="",
    )


class GroupsGroupXtrInvitedBy(pydantic.BaseModel):
    admin_level: typing.Optional["GroupsGroupXtrInvitedByAdminLevel"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[str] = pydantic.Field(
        None, description="Community ID",
    )
    invited_by: typing.Optional[int] = pydantic.Field(
        None, description="Inviter ID",
    )
    is_admin: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is manager",
    )
    is_advertiser: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is advertiser",
    )
    is_closed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether community is closed",
    )
    is_member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user is member",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Community name",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 100 pixels in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 200 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of square photo of the community with 50 pixels in width",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="Domain of the community page",
    )
    type: typing.Optional["GroupsGroupXtrInvitedByType"] = pydantic.Field(
        None, description="",
    )


class GroupsGroupsArray(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Communities number",
    )
    items: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class GroupsLinksItem(pydantic.BaseModel):
    desc: typing.Optional[str] = pydantic.Field(
        None, description="Link description",
    )
    edit_title: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the link title can be edited",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Link ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Link title",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="URL of square image of the link with 100 pixels in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="URL of square image of the link with 50 pixels in width",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )


class GroupsLongPollServer(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="Long Poll key",
    )
    server: typing.Optional[str] = pydantic.Field(
        None, description="Long Poll server address",
    )
    ts: typing.Optional[str] = pydantic.Field(
        None, description="Number of the last event",
    )


class GroupsLongPollSettings(pydantic.BaseModel):
    api_version: typing.Optional[str] = pydantic.Field(
        None, description="API version used for the events",
    )
    events: typing.Optional["GroupsLongPollEvents"] = pydantic.Field(
        None, description="",
    )
    is_enabled: typing.Optional[bool] = pydantic.Field(
        None, description="Shows whether Long Poll is enabled",
    )


class GroupsMarketInfo(pydantic.BaseModel):
    contact_id: typing.Optional[int] = pydantic.Field(
        None, description="Contact person ID",
    )
    currency: typing.Optional["MarketCurrency"] = pydantic.Field(
        None, description="",
    )
    currency_text: typing.Optional[str] = pydantic.Field(
        None, description="Currency name",
    )
    enabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the market is enabled",
    )
    main_album_id: typing.Optional[int] = pydantic.Field(
        None, description="Main market album ID",
    )
    price_max: typing.Optional[int] = pydantic.Field(
        None, description="Maximum price",
    )
    price_min: typing.Optional[int] = pydantic.Field(
        None, description="Minimum price",
    )


class GroupsMemberRole(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )
    permissions: typing.Optional[
        typing.List["GroupsMemberRolePermission"]
    ] = pydantic.Field(
        None, description="",
    )
    role: typing.Optional["GroupsMemberRoleStatus"] = pydantic.Field(
        None, description="",
    )


class GroupsMemberRolePermissionEnum(str, Enum):
    ads = "ads"


class GroupsMemberRolePermission(pydantic.BaseModel):
    enum: typing.Optional[GroupsMemberRolePermissionEnum] = pydantic.Field(
        None, description="",
    )


class GroupsMemberStatus(pydantic.BaseModel):
    member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user is a member of the group",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class GroupsMemberStatusFull(pydantic.BaseModel):
    can_invite: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user can be invited",
    )
    can_recall: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether user's invite to the group can be recalled",
    )
    invitation: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user has been invited to the group",
    )
    member: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user is a member of the group",
    )
    request: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user has send request to the group",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class GroupsOnlineStatus(pydantic.BaseModel):
    minutes: typing.Optional[int] = pydantic.Field(
        None, description="Estimated time of answer (for status = answer_mark)",
    )
    status: typing.Optional["GroupsOnlineStatusType"] = pydantic.Field(
        None, description="",
    )


class GroupsOwnerXtrBanInfo(pydantic.BaseModel):
    ban_info: typing.Optional["GroupsBanInfo"] = pydantic.Field(
        None, description="",
    )
    group: typing.Optional["GroupsGroup"] = pydantic.Field(
        None, description="Information about group if type = group",
    )
    profile: typing.Optional["UsersUser"] = pydantic.Field(
        None, description="Information about group if type = profile",
    )
    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = pydantic.Field(
        None, description="",
    )


class GroupsRoleOptionsEnum(str, Enum):
    moderator = "moderator"
    editor = "editor"
    administrator = "administrator"
    creator = "creator"


class GroupsRoleOptions(pydantic.BaseModel):
    enum: typing.Optional[GroupsRoleOptionsEnum] = pydantic.Field(
        None, description="User's credentials as community admin",
    )


class GroupsSubjectItem(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Subject ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Subject title",
    )


class GroupsTokenPermissionSetting(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    setting: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class GroupsUserXtrRole(pydantic.BaseModel):
    users_user_full: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )
    role: typing.Optional["GroupsRoleOptions"] = pydantic.Field(
        None, description="",
    )


class LeadsChecked(pydantic.BaseModel):
    reason: typing.Optional[str] = pydantic.Field(
        None, description="Reason why user can't start the lead",
    )
    result: typing.Optional["LeadsCheckedResult"] = pydantic.Field(
        None, description="",
    )
    sid: typing.Optional[str] = pydantic.Field(
        None, description="Session ID",
    )
    start_link: typing.Optional[str] = pydantic.Field(
        None, description="URL user should open to start the lead",
    )


class LeadsComplete(pydantic.BaseModel):
    cost: typing.Optional[int] = pydantic.Field(
        None, description="Offer cost",
    )
    limit: typing.Optional[int] = pydantic.Field(
        None, description="Offer limit",
    )
    spent: typing.Optional[int] = pydantic.Field(
        None, description="Amount of spent votes",
    )
    success: typing.Optional["BaseOkResponse"] = pydantic.Field(
        None, description="",
    )
    test_mode: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether test mode is enabled",
    )


class LeadsEntry(pydantic.BaseModel):
    aid: typing.Optional[int] = pydantic.Field(
        None, description="Application ID",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the action has been started in Unixtime",
    )
    sid: typing.Optional[str] = pydantic.Field(
        None, description="Session string ID",
    )
    start_date: typing.Optional[int] = pydantic.Field(
        None, description="Start date in Unixtime (for status=2)",
    )
    status: typing.Optional[int] = pydantic.Field(
        None, description="Action type",
    )
    test_mode: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether test mode is enabled",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class LeadsLead(pydantic.BaseModel):
    completed: typing.Optional[int] = pydantic.Field(
        None, description="Completed offers number",
    )
    cost: typing.Optional[int] = pydantic.Field(
        None, description="Offer cost",
    )
    days: typing.Optional["LeadsLeadDays"] = pydantic.Field(
        None, description="",
    )
    impressions: typing.Optional[int] = pydantic.Field(
        None, description="Impressions number",
    )
    limit: typing.Optional[int] = pydantic.Field(
        None, description="Lead limit",
    )
    spent: typing.Optional[int] = pydantic.Field(
        None, description="Amount of spent votes",
    )
    started: typing.Optional[int] = pydantic.Field(
        None, description="Started offers number",
    )


class LeadsStart(pydantic.BaseModel):
    test_mode: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether test mode is enabled",
    )
    vk_sid: typing.Optional[str] = pydantic.Field(
        None, description="Session data",
    )


class LikesTypeEnum(str, Enum):
    post = "post"
    comment = "comment"
    photo = "photo"
    audio = "audio"
    video = "video"
    note = "note"
    market = "market"
    photo_comment = "photo_comment"
    video_comment = "video_comment"
    topic_comment = "topic_comment"
    market_comment = "market_comment"
    sitepage = "sitepage"


class LikesType(pydantic.BaseModel):
    enum: typing.Optional[LikesTypeEnum] = pydantic.Field(
        None, description="",
    )


class MarketMarketItemFull(pydantic.BaseModel):
    market_market_item: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None, description="",
    )
    albums_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    photos: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current use can comment the item",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current use can repost the item",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None, description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None, description="",
    )
    views_count: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )


class MessageChatPreview(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    joined: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    local_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    members: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    members_count: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class MessagesChat(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="Chat creator ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Chat ID",
    )
    kicked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Shows that user has been kicked from the chat",
    )
    left: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Shows that user has been left the chat",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 100 px in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 200 px in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 50 px in width",
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Chat title",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Chat type",
    )
    users: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class MessagesChatFull(pydantic.BaseModel):
    admin_id: typing.Optional[int] = pydantic.Field(
        None, description="Chat creator ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Chat ID",
    )
    kicked: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Shows that user has been kicked from the chat",
    )
    left: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Shows that user has been left the chat",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 100 px in width",
    )
    photo_200: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 200 px in width",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image with 50 px in width",
    )
    push_settings: typing.Optional["MessagesChatPushSettings"] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Chat title",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Chat type",
    )
    users: typing.Optional[typing.List["MessagesUserXtrInvitedBy"]] = pydantic.Field(
        None, description="",
    )


class MessagesChatRestrictions(pydantic.BaseModel):
    admins_promote_users: typing.Optional[bool] = pydantic.Field(
        None, description="Only admins can promote users to admins",
    )
    only_admins_edit_info: typing.Optional[bool] = pydantic.Field(
        None, description="Only admins can change chat info",
    )
    only_admins_edit_pin: typing.Optional[bool] = pydantic.Field(
        None, description="Only admins can edit pinned message",
    )
    only_admins_invite: typing.Optional[bool] = pydantic.Field(
        None, description="Only admins can invite users to this chat",
    )
    only_admins_kick: typing.Optional[bool] = pydantic.Field(
        None, description="Only admins can kick users from this chat",
    )


class MessagesConversationMember(pydantic.BaseModel):
    can_kick: typing.Optional[bool] = pydantic.Field(
        None, description="Is it possible for user to kick this member",
    )
    invited_by: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    is_admin: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    is_owner: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    is_message_request: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    join_date: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    request_date: typing.Optional[int] = pydantic.Field(
        None, description="Message request date",
    )
    member_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class MessagesConversationWithMessage(pydantic.BaseModel):
    conversation: typing.Optional["MessagesConversation"] = pydantic.Field(
        None, description="",
    )
    last_message: typing.Optional["MessagesMessage"] = pydantic.Field(
        None, description="",
    )


class MessagesHistoryAttachment(pydantic.BaseModel):
    attachment: typing.Optional["MessagesHistoryMessageAttachment"] = pydantic.Field(
        None, description="",
    )
    message_id: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Message author's ID",
    )


class MessagesKeyboardButton(pydantic.BaseModel):
    action: typing.Optional["MessagesKeyboardButtonAction"] = pydantic.Field(
        None, description="",
    )
    color: typing.Optional[str] = pydantic.Field(
        None, description="Button color",
    )


class MessagesLastActivity(pydantic.BaseModel):
    online: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user is online",
    )
    time: typing.Optional[int] = pydantic.Field(
        None, description="Time when user was online in Unixtime",
    )


class MessagesLongpollMessages(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List["MessagesMessage"]] = pydantic.Field(
        None, description="",
    )


class MessagesLongpollParams(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="Key",
    )
    pts: typing.Optional[int] = pydantic.Field(
        None, description="Persistent timestamp",
    )
    server: typing.Optional[str] = pydantic.Field(
        None, description="Server URL",
    )
    ts: typing.Optional[int] = pydantic.Field(
        None, description="Timestamp",
    )


class MessagesMessageAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = pydantic.Field(
        None, description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None, description="",
    )
    gift: typing.Optional["GiftsLayout"] = pydantic.Field(
        None, description="",
    )
    graffiti: typing.Optional["MessagesGraffiti"] = pydantic.Field(
        None, description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None, description="",
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    sticker: typing.Optional["BaseSticker"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["MessagesMessageAttachmentType"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )
    wall: typing.Optional["WallWallpostFull"] = pydantic.Field(
        None, description="",
    )
    wall_reply: typing.Optional["WallWallComment"] = pydantic.Field(
        None, description="",
    )


class MessagesPinnedMessage(pydantic.BaseModel):
    attachments: typing.Optional[
        typing.List["MessagesMessageAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    conversation_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Unique auto-incremented number for all messages with this peer",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the message has been sent in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Message author's ID",
    )
    fwd_messages: typing.Optional[
        typing.List["MessagesForeignMessage"]
    ] = pydantic.Field(
        None, description="Forwarded messages",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )
    peer_id: typing.Optional[int] = pydantic.Field(
        None, description="Peer ID",
    )
    reply_message: typing.Optional["MessagesForeignMessage"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Message text",
    )
    keyboard: typing.Optional["MessagesKeyboard"] = pydantic.Field(
        None, description="",
    )


class MessagesUserXtrInvitedBy(pydantic.BaseModel):
    users_user_xtr_type: typing.Optional["UsersUserXtrType"] = pydantic.Field(
        None, description="",
    )
    invited_by: typing.Optional[int] = pydantic.Field(
        None, description="ID of the inviter",
    )


class NewsfeedCommentsFiltersEnum(str, Enum):
    post = "post"
    photo = "photo"
    video = "video"
    topic = "topic"
    note = "note"


class NewsfeedCommentsFilters(pydantic.BaseModel):
    enum: typing.Optional[NewsfeedCommentsFiltersEnum] = pydantic.Field(
        None, description="",
    )


class NewsfeedEventActivity(pydantic.BaseModel):
    address: typing.Optional[str] = pydantic.Field(
        None, description="address of event",
    )
    button_text: typing.Optional[str] = pydantic.Field(
        None, description="text of attach",
    )
    friends: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="array of friends ids",
    )
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = pydantic.Field(
        None, description="Current user's member status",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="text of attach",
    )
    time: typing.Optional[int] = pydantic.Field(
        None, description="event start time",
    )


class NewsfeedFiltersEnum(str, Enum):
    post = "post"
    photo = "photo"
    photo_tag = "photo_tag"
    wall_photo = "wall_photo"
    friend = "friend"
    note = "note"
    audio = "audio"
    video = "video"


class NewsfeedFilters(pydantic.BaseModel):
    enum: typing.Optional[NewsfeedFiltersEnum] = pydantic.Field(
        None, description="",
    )


class NewsfeedIgnoreItemTypeEnum(str, Enum):
    wall = "wall"
    tag = "tag"
    profilephoto = "profilephoto"
    video = "video"
    photo = "photo"
    audio = "audio"


class NewsfeedIgnoreItemType(pydantic.BaseModel):
    enum: typing.Optional[NewsfeedIgnoreItemTypeEnum] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemAudio(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    audio: typing.Optional["NewsfeedItemAudioAudio"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )


class NewsfeedItemAudioAudio(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Audios number",
    )
    items: typing.Optional[typing.List["AudioAudio"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemBase(pydantic.BaseModel):
    type: typing.Optional["NewsfeedNewsfeedItemType"] = pydantic.Field(
        None, description="",
    )
    source_id: typing.Optional[int] = pydantic.Field(
        None, description="Item source ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when item has been added in Unixtime",
    )


class NewsfeedItemDigest(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    button_text: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    feed_id: typing.Optional[str] = pydantic.Field(
        None, description="id of feed in digest",
    )
    items: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None, description="",
    )
    main_post_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )
    template: typing.Optional[str] = pydantic.Field(
        None, description="type of digest",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemFriend(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    friends: typing.Optional["NewsfeedItemFriendFriends"] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemFriendFriends(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Number of friends has been added",
    )
    items: typing.Optional[typing.List["BaseUserId"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemNote(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    notes: typing.Optional["NewsfeedItemNoteNotes"] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemNoteNotes(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Notes number",
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedNote"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemPhoto(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )


class NewsfeedItemPhotoPhotos(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Photos number",
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemPhotoTag(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )


class NewsfeedItemPhotoTagPhotoTags(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Tags number",
    )
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemStoriesBlock(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    block_type: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    stories: typing.Optional[typing.List["StoriesStory"]] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    track_code: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemTopic(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None, description="",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Topic post ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Post text",
    )


class NewsfeedItemVideo(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["NewsfeedItemVideoVideo"] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemVideoVideo(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Tags number",
    )
    items: typing.Optional[typing.List["VideoVideo"]] = pydantic.Field(
        None, description="",
    )


class NewsfeedItemWallpost(pydantic.BaseModel):
    newsfeed_item_base: typing.Optional["NewsfeedItemBase"] = pydantic.Field(
        None, description="",
    )
    activity: typing.Optional["NewsfeedEventActivity"] = pydantic.Field(
        None, description="",
    )
    attachments: typing.Optional[
        typing.List["WallWallpostAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None, description="",
    )
    copy_history: typing.Optional[typing.List["WallWallpost"]] = pydantic.Field(
        None, description="",
    )
    geo: typing.Optional["BaseGeo"] = pydantic.Field(
        None, description="",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None, description="",
    )
    post_type: typing.Optional["NewsfeedItemWallpostType"] = pydantic.Field(
        None, description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Post text",
    )


class NewsfeedItemWallpostTypeEnum(str, Enum):
    post = "post"
    copy = "copy"
    reply = "reply"


class NewsfeedItemWallpostType(pydantic.BaseModel):
    enum: typing.Optional[NewsfeedItemWallpostTypeEnum] = pydantic.Field(
        None, description="Post type",
    )


class NewsfeedList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="List ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="List title",
    )


class NewsfeedListFull(pydantic.BaseModel):
    newsfeed_list: typing.Optional["NewsfeedList"] = pydantic.Field(
        None, description="",
    )
    no_reposts: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether reposts hiding is enabled",
    )
    source_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class NewsfeedNewsfeedItem(pydantic.BaseModel):
    item_stories: typing.Optional[
        typing.Union[
            "NewsfeedItemWallpost",
            "NewsfeedItemPhoto",
            "NewsfeedItemPhotoTag",
            "NewsfeedItemFriend",
            "NewsfeedItemNote",
            "NewsfeedItemAudio",
            "NewsfeedItemVideo",
            "NewsfeedItemTopic",
            "NewsfeedItemDigest",
            "NewsfeedItemStoriesBlock",
        ]
    ] = pydantic.Field(
        None, description="",
    )


class NewsfeedNewsfeedNote(pydantic.BaseModel):
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Comments Number",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="integer",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Note title",
    )


class NewsfeedNewsfeedPhoto(pydantic.BaseModel):
    photos_photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None, description="",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the photo",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can repost the photo",
    )


class NotesNote(pydantic.BaseModel):
    read_comments: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the note",
    )
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Comments number",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the note has been created in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Note owner's ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Note text",
    )
    text_wiki: typing.Optional[str] = pydantic.Field(
        None, description="Note text in wiki format",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Note title",
    )
    view_url: typing.Optional[str] = pydantic.Field(
        None, description="URL of the page with note preview",
    )


class NotesNoteComment(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has beed added in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    nid: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )
    oid: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )
    reply_to: typing.Optional[int] = pydantic.Field(
        None, description="ID of replied comment ",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None, description="Comment author's ID",
    )


class NotificationsNotification(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the event has been occurred",
    )
    feedback: typing.Optional["NotificationsFeedback"] = pydantic.Field(
        None, description="",
    )
    parent: typing.Optional["NotificationsNotificationParent"] = pydantic.Field(
        None, description="",
    )
    reply: typing.Optional["NotificationsReply"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Notification type",
    )


class NotificationsNotificationsComment(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Author ID",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    post: typing.Optional["WallWallpost"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    topic: typing.Optional["BoardTopic"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )


class NotificationsSendMessageItem(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )
    status: typing.Optional[bool] = pydantic.Field(
        None, description="Notification status",
    )
    error: typing.Optional["NotificationsSendMessageError"] = pydantic.Field(
        None, description="",
    )


class OauthError(pydantic.BaseModel):
    error: typing.Optional[str] = pydantic.Field(
        None, description="Error type",
    )
    error_description: typing.Optional[str] = pydantic.Field(
        None, description="Error description",
    )
    redirect_uri: typing.Optional[str] = pydantic.Field(
        None, description="URI for validation",
    )


class OrdersAmount(pydantic.BaseModel):
    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = pydantic.Field(
        None, description="",
    )
    currency: typing.Optional[str] = pydantic.Field(
        None, description="Currency name",
    )


class OrdersAmountItem(pydantic.BaseModel):
    amount: typing.Optional[int] = pydantic.Field(
        None, description="Votes amount in user's currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Amount description",
    )
    votes: typing.Optional[str] = pydantic.Field(
        None, description="Votes number",
    )


class OrdersOrder(pydantic.BaseModel):
    amount: typing.Optional[int] = pydantic.Field(
        None, description="Amount",
    )
    app_order_id: typing.Optional[int] = pydantic.Field(
        None, description="App order ID",
    )
    cancel_transaction_id: typing.Optional[int] = pydantic.Field(
        None, description="Cancel transaction ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date of creation in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Order ID",
    )
    item: typing.Optional[str] = pydantic.Field(
        None, description="Order item",
    )
    receiver_id: typing.Optional[int] = pydantic.Field(
        None, description="Receiver ID",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="Order status",
    )
    transaction_id: typing.Optional[int] = pydantic.Field(
        None, description="Transaction ID",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class OrdersSubscription(pydantic.BaseModel):
    cancel_reason: typing.Optional[str] = pydantic.Field(
        None, description="Cancel reason",
    )
    create_time: typing.Optional[int] = pydantic.Field(
        None, description="Date of creation in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Subscription ID",
    )
    item_id: typing.Optional[str] = pydantic.Field(
        None, description="Subscription order item",
    )
    next_bill_time: typing.Optional[int] = pydantic.Field(
        None, description="Date of next bill in Unixtime",
    )
    pending_cancel: typing.Optional[bool] = pydantic.Field(
        None, description="Pending cancel state",
    )
    period: typing.Optional[int] = pydantic.Field(
        None, description="Subscription period",
    )
    period_start_time: typing.Optional[int] = pydantic.Field(
        None, description="Date of last period start in Unixtime",
    )
    price: typing.Optional[int] = pydantic.Field(
        None, description="Subscription price",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="Subscription status",
    )
    test_mode: typing.Optional[bool] = pydantic.Field(
        None, description="Is test subscription",
    )
    trial_expire_time: typing.Optional[int] = pydantic.Field(
        None, description="Date of trial expire in Unixtime",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None, description="Date of last change in Unixtime",
    )


class PagesWikipage(pydantic.BaseModel):
    creator_id: typing.Optional[int] = pydantic.Field(
        None, description="Page creator ID",
    )
    creator_name: typing.Optional[int] = pydantic.Field(
        None, description="Page creator name",
    )
    editor_id: typing.Optional[int] = pydantic.Field(
        None, description="Last editor ID",
    )
    editor_name: typing.Optional[str] = pydantic.Field(
        None, description="Last editor name",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Page ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Page title",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )
    who_can_edit: typing.Optional["PagesPrivacySettings"] = pydantic.Field(
        None, description="Edit settings of the page",
    )
    who_can_view: typing.Optional["PagesPrivacySettings"] = pydantic.Field(
        None, description="View settings of the page",
    )


class PagesWikipageHistory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Version ID",
    )
    length: typing.Optional[int] = pydantic.Field(
        None, description="Page size in bytes",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the page has been edited in Unixtime",
    )
    editor_id: typing.Optional[int] = pydantic.Field(
        None, description="Last editor ID",
    )
    editor_name: typing.Optional[str] = pydantic.Field(
        None, description="Last editor name",
    )


class PhotosCommentXtrPid(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Author ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    pid: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    reply_to_comment: typing.Optional[int] = pydantic.Field(
        None, description="Replied comment ID",
    )
    reply_to_user: typing.Optional[int] = pydantic.Field(
        None, description="Replied user ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    parents_stack: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    thread: typing.Optional["CommentThread"] = pydantic.Field(
        None, description="",
    )


class PhotosImage(pydantic.BaseModel):
    height: typing.Optional[int] = pydantic.Field(
        None, description="Height of the photo in px.",
    )
    type: typing.Optional["PhotosImageType"] = pydantic.Field(
        None, description="",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Photo URL.",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Width of the photo in px.",
    )


class PhotosMarketAlbumUploadResponse(pydantic.BaseModel):
    gid: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PhotosMarketUploadResponse(pydantic.BaseModel):
    crop_data: typing.Optional[str] = pydantic.Field(
        None, description="Crop data",
    )
    crop_hash: typing.Optional[str] = pydantic.Field(
        None, description="Crop hash",
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PhotosMessageUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PhotosOwnerUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PhotosPhotoAlbumFull(pydantic.BaseModel):
    can_upload: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can upload photo to the album",
    )
    comments_disabled: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether album comments are disabled",
    )
    created: typing.Optional[int] = pydantic.Field(
        None, description="Date when the album has been created in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Photo album description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo album ID",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Album owner's ID",
    )
    size: typing.Optional[int] = pydantic.Field(
        None, description="Photos number",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )
    thumb_id: typing.Optional[int] = pydantic.Field(
        None, description="Thumb photo ID",
    )
    thumb_is_last: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the album thumb is last photo",
    )
    thumb_src: typing.Optional[str] = pydantic.Field(
        None, description="URL of the thumb image",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Photo album title",
    )
    updated: typing.Optional[int] = pydantic.Field(
        None, description="Date when the album has been updated last time in Unixtime",
    )
    upload_by_admins_only: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether only community administrators can upload photos",
    )


class PhotosPhotoFull(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the photo",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the photo",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Original photo height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    images: typing.Optional[typing.List["PhotosImage"]] = pydantic.Field(
        None, description="",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None, description="Latitude",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None, description="",
    )
    long: typing.Optional[int] = pydantic.Field(
        None, description="Longitude",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    reposts: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    tags: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Original photo width",
    )


class PhotosPhotoFullXtrRealOffset(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the photo",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Original photo height",
    )
    hidden: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the photo is hidden above the wall",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None, description="Latitude",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None, description="",
    )
    long: typing.Optional[int] = pydantic.Field(
        None, description="Longitude",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 807 px width",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real position of the photo",
    )
    reposts: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )
    tags: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Original photo width",
    )


class PhotosPhotoSizes(pydantic.BaseModel):
    height: typing.Optional[int] = pydantic.Field(
        None, description="Height in px",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="URL of the image",
    )
    type: typing.Optional["PhotosPhotoSizesType"] = pydantic.Field(
        None, description="",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Width in px",
    )


class PhotosPhotoTag(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when tag has been added in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Tag ID",
    )
    placer_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the tag creator",
    )
    tagged_name: typing.Optional[str] = pydantic.Field(
        None, description="Tag description",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="Tagged user ID",
    )
    viewed: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the tag is reviewed",
    )
    x: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the left upper corner",
    )
    x2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate X of the right lower corner",
    )
    y: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the left upper corner",
    )
    y2: typing.Optional[int] = pydantic.Field(
        None, description="Coordinate Y of the right lower corner",
    )


class PhotosPhotoUpload(pydantic.BaseModel):
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    upload_url: typing.Optional[str] = pydantic.Field(
        None, description="URL to upload photo",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class PhotosPhotoUploadResponse(pydantic.BaseModel):
    aid: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photos_list: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photos data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PhotosPhotoXtrRealOffset(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the photo",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Original photo height",
    )
    hidden: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the photo is hidden above the wall",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None, description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None, description="Longitude",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 807 px width",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real position of the photo",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Original photo width",
    )


class PhotosPhotoXtrTagInfo(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the photo",
    )
    album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when uploaded",
    )
    height: typing.Optional[int] = pydantic.Field(
        None, description="Original photo height",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )
    lat: typing.Optional[int] = pydantic.Field(
        None, description="Latitude",
    )
    long: typing.Optional[int] = pydantic.Field(
        None, description="Longitude",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Photo owner's ID",
    )
    photo_1280: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 1280 px width",
    )
    photo_130: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 130 px width",
    )
    photo_2560: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 2560 px width",
    )
    photo_604: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 604 px width",
    )
    photo_75: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 75 px width",
    )
    photo_807: typing.Optional[str] = pydantic.Field(
        None, description="URL of image with 807 px width",
    )
    placer_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the tag creator",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = pydantic.Field(
        None, description="",
    )
    tag_created: typing.Optional[int] = pydantic.Field(
        None, description="Date when tag has been added in Unixtime",
    )
    tag_id: typing.Optional[int] = pydantic.Field(
        None, description="Tag ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Photo caption",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the user who have uploaded the photo",
    )
    width: typing.Optional[int] = pydantic.Field(
        None, description="Original photo width",
    )


class PhotosWallUploadResponse(pydantic.BaseModel):
    hash: typing.Optional[str] = pydantic.Field(
        None, description="Uploading hash",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded photo data",
    )
    server: typing.Optional[int] = pydantic.Field(
        None, description="Upload server number",
    )


class PollsAnswer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Answer ID",
    )
    rate: typing.Optional[int] = pydantic.Field(
        None, description="Answer rate in percents",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Answer text",
    )
    votes: typing.Optional[int] = pydantic.Field(
        None, description="Votes number",
    )


class PollsVoters(pydantic.BaseModel):
    answer_id: typing.Optional[int] = pydantic.Field(
        None, description="Answer ID",
    )
    users: typing.Optional["PollsVotersUsers"] = pydantic.Field(
        None, description="",
    )


class PrettyCardsPrettyCard(pydantic.BaseModel):
    button: typing.Optional[str] = pydantic.Field(
        None, description="Button key",
    )
    button_text: typing.Optional[str] = pydantic.Field(
        None, description="Button text in current language",
    )
    card_id: typing.Optional[str] = pydantic.Field(
        None, description="Card ID (long int returned as string)",
    )
    images: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None, description="",
    )
    link_url: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="Photo ID (format <owner_id>_<media_id>)",
    )
    price: typing.Optional[str] = pydantic.Field(
        None, description="Price if set (decimal number returned as string)",
    )
    price_old: typing.Optional[str] = pydantic.Field(
        None, description="Old price if set (decimal number returned as string)",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Title",
    )


class SearchHint(pydantic.BaseModel):
    app: typing.Optional["AppsApp"] = pydantic.Field(
        None, description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Object description",
    )
    global_: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether the object has been found globally",
        alias="global",
    )
    group: typing.Optional["GroupsGroup"] = pydantic.Field(
        None, description="",
    )
    profile: typing.Optional["UsersUserMin"] = pydantic.Field(
        None, description="",
    )
    section: typing.Optional["SearchHintSection"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["SearchHintType"] = pydantic.Field(
        None, description="",
    )


class SecureLevel(pydantic.BaseModel):
    level: typing.Optional[int] = pydantic.Field(
        None, description="Level",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class SecureSmsNotification(pydantic.BaseModel):
    app_id: typing.Optional[str] = pydantic.Field(
        None, description="Application ID",
    )
    date: typing.Optional[str] = pydantic.Field(
        None, description="Date when message has been sent in Unixtime",
    )
    id: typing.Optional[str] = pydantic.Field(
        None, description="Notification ID",
    )
    message: typing.Optional[str] = pydantic.Field(
        None, description="Messsage text",
    )
    user_id: typing.Optional[str] = pydantic.Field(
        None, description="User ID",
    )


class SecureTokenChecked(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when access_token has been generated in Unixtime",
    )
    expire: typing.Optional[int] = pydantic.Field(
        None, description="Date when access_token will expire in Unixtime",
    )
    success: typing.Optional["BaseOkResponse"] = pydantic.Field(
        None, description="Returns if successfully processed",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )


class SecureTransaction(pydantic.BaseModel):
    date: typing.Optional[int] = pydantic.Field(
        None, description="Transaction date in Unixtime",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Transaction ID",
    )
    uid_from: typing.Optional[int] = pydantic.Field(
        None, description="From ID",
    )
    uid_to: typing.Optional[int] = pydantic.Field(
        None, description="To ID",
    )
    votes: typing.Optional[int] = pydantic.Field(
        None, description="Votes number",
    )


class StatsCity(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Visitors number",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="City name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )


class StatsCountry(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(
        None, description="Country code",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Visitors number",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Country name",
    )
    value: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )


class StatsPeriod(pydantic.BaseModel):
    activity: typing.Optional["StatsActivity"] = pydantic.Field(
        None, description="",
    )
    period_from: typing.Optional[int] = pydantic.Field(
        None, description="Unix timestamp",
    )
    period_to: typing.Optional[int] = pydantic.Field(
        None, description="Unix timestamp",
    )
    reach: typing.Optional["StatsReach"] = pydantic.Field(
        None, description="",
    )
    visitors: typing.Optional["StatsViews"] = pydantic.Field(
        None, description="",
    )


class StatsSexAge(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Visitors number",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="Sex/age value",
    )


class StatsWallpostStat(pydantic.BaseModel):
    hide: typing.Optional[int] = pydantic.Field(
        None, description="Hidings number",
    )
    join_group: typing.Optional[int] = pydantic.Field(
        None, description="People have joined the group",
    )
    links: typing.Optional[int] = pydantic.Field(
        None, description="Link clickthrough",
    )
    reach_subscribers: typing.Optional[int] = pydantic.Field(
        None, description="Subscribers reach",
    )
    reach_total: typing.Optional[int] = pydantic.Field(
        None, description="Total reach",
    )
    report: typing.Optional[int] = pydantic.Field(
        None, description="Reports number",
    )
    to_group: typing.Optional[int] = pydantic.Field(
        None, description="Clickthrough to community",
    )
    unsubscribe: typing.Optional[int] = pydantic.Field(
        None, description="Unsubscribed members",
    )


class StatusStatus(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Status text",
    )


class StorageValue(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    value: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class StoriesPromoBlock(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Promo story title",
    )
    photo_50: typing.Optional[str] = pydantic.Field(
        None, description="RL of square photo of the story with 50 pixels in width",
    )
    photo_100: typing.Optional[str] = pydantic.Field(
        None, description="RL of square photo of the story with 100 pixels in width",
    )
    not_animated: typing.Optional[bool] = pydantic.Field(
        None, description="Hide animation for promo story",
    )


class StoriesStoryStats(pydantic.BaseModel):
    answer: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    bans: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    open_link: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    replies: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    shares: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    subscribers: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )
    views: typing.Optional["StoriesStoryStatsStat"] = pydantic.Field(
        None, description="",
    )


class StoriesUploadLinkTextEnum(str, Enum):
    to_store = "to_store"
    vote = "vote"
    more = "more"
    book = "book"
    order = "order"
    enroll = "enroll"
    fill = "fill"
    signup = "signup"
    buy = "buy"
    ticket = "ticket"
    write = "write"
    open = "open"
    learn_more = "learn_more"
    view = "view"
    go_to = "go_to"
    contact = "contact"
    watch = "watch"
    play = "play"
    install = "install"
    read = "read"


class StoriesUploadLinkText(pydantic.BaseModel):
    enum: typing.Optional[StoriesUploadLinkTextEnum] = pydantic.Field(
        None, description="",
    )


class UsersCareer(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    company: typing.Optional[str] = pydantic.Field(
        None, description="Company name",
    )
    country_id: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    from_: typing.Optional[int] = pydantic.Field(
        None, description="From year", alias="from"
    )
    group_id: typing.Optional[int] = pydantic.Field(
        None, description="Community ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Career ID",
    )
    position: typing.Optional[str] = pydantic.Field(
        None, description="Position",
    )
    until: typing.Optional[int] = pydantic.Field(
        None, description="Till year",
    )


class UsersCropPhoto(pydantic.BaseModel):
    crop: typing.Optional["UsersCropPhotoCrop"] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    rect: typing.Optional["UsersCropPhotoRect"] = pydantic.Field(
        None, description="",
    )


class UsersExports(pydantic.BaseModel):
    facebook: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    livejournal: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    twitter: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class UsersFieldsEnum(str, Enum):
    photo_id = "photo_id"
    verified = "verified"
    sex = "sex"
    bdate = "bdate"
    city = "city"
    country = "country"
    home_town = "home_town"
    has_photo = "has_photo"
    photo_50 = "photo_50"
    photo_100 = "photo_100"
    photo_200_orig = "photo_200_orig"
    photo_200 = "photo_200"
    photo_400_orig = "photo_400_orig"
    photo_max = "photo_max"
    photo_max_orig = "photo_max_orig"
    online = "online"
    lists = "lists"
    domain = "domain"
    has_mobile = "has_mobile"
    contacts = "contacts"
    site = "site"
    education = "education"
    universities = "universities"
    schools = "schools"
    status = "status"
    last_seen = "last_seen"
    followers_count = "followers_count"
    counters = "counters"
    common_count = "common_count"
    occupation = "occupation"
    nickname = "nickname"
    relatives = "relatives"
    relation = "relation"
    personal = "personal"
    connections = "connections"
    exports = "exports"
    wall_comments = "wall_comments"
    activities = "activities"
    interests = "interests"
    music = "music"
    movies = "movies"
    tv = "tv"
    books = "books"
    games = "games"
    about = "about"
    quotes = "quotes"
    can_post = "can_post"
    can_see_all_posts = "can_see_all_posts"
    can_see_audio = "can_see_audio"
    can_write_private_message = "can_write_private_message"
    can_send_friend_request = "can_send_friend_request"
    is_favorite = "is_favorite"
    is_hidden_from_feed = "is_hidden_from_feed"
    timezone = "timezone"
    screen_name = "screen_name"
    maiden_name = "maiden_name"
    crop_photo = "crop_photo"
    is_friend = "is_friend"
    friend_status = "friend_status"
    career = "career"
    military = "military"
    blacklisted = "blacklisted"
    blacklisted_by_me = "blacklisted_by_me"
    can_subscribe_posts = "can_subscribe_posts"
    descriptions = "descriptions"
    trending = "trending"
    mutual = "mutual"


class UsersFields(pydantic.BaseModel):
    enum: typing.Optional[UsersFieldsEnum] = pydantic.Field(
        None, description="",
    )


class UsersLastSeen(pydantic.BaseModel):
    platform: typing.Optional[int] = pydantic.Field(
        None, description="Type of the platform that used for the last authorization",
    )
    time: typing.Optional[int] = pydantic.Field(
        None, description="Last visit date (in Unix time)",
    )


class UsersMilitary(pydantic.BaseModel):
    country_id: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    from_: typing.Optional[int] = pydantic.Field(
        None, description="From year", alias="from"
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Military ID",
    )
    unit: typing.Optional[str] = pydantic.Field(
        None, description="Unit name",
    )
    unit_id: typing.Optional[int] = pydantic.Field(
        None, description="Unit ID",
    )
    until: typing.Optional[int] = pydantic.Field(
        None, description="Till year",
    )


class UsersOccupation(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="ID of school, university, company group",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Name of occupation",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Type of occupation",
    )


class UsersRelative(pydantic.BaseModel):
    birth_date: typing.Optional[str] = pydantic.Field(
        None, description="Date of child birthday (format dd.mm.yyyy)",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Relative ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="Name of relative",
    )
    type: typing.Optional[str] = pydantic.Field(
        None, description="Relative type",
    )


class UsersSchool(pydantic.BaseModel):
    city: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    class_: typing.Optional[str] = pydantic.Field(
        None, description="School class letter", alias="class"
    )
    country: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    id: typing.Optional[str] = pydantic.Field(
        None, description="School ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="School name",
    )
    type: typing.Optional[int] = pydantic.Field(
        None, description="School type ID",
    )
    type_str: typing.Optional[str] = pydantic.Field(
        None, description="School type name",
    )
    year_from: typing.Optional[int] = pydantic.Field(
        None, description="Year the user started to study",
    )
    year_graduated: typing.Optional[int] = pydantic.Field(
        None, description="Graduation year",
    )
    year_to: typing.Optional[int] = pydantic.Field(
        None, description="Year the user finished to study",
    )


class UsersSubscriptionsItem(pydantic.BaseModel):
    group: typing.Optional[
        typing.Union["UsersUserXtrType", "GroupsGroupFull"]
    ] = pydantic.Field(
        None, description="",
    )


class UsersUniversity(pydantic.BaseModel):
    chair: typing.Optional[int] = pydantic.Field(
        None, description="Chair ID",
    )
    chair_name: typing.Optional[str] = pydantic.Field(
        None, description="Chair name",
    )
    city: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    country: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    education_form: typing.Optional[str] = pydantic.Field(
        None, description="Education form",
    )
    education_status: typing.Optional[str] = pydantic.Field(
        None, description="Education status",
    )
    faculty: typing.Optional[int] = pydantic.Field(
        None, description="Faculty ID",
    )
    faculty_name: typing.Optional[str] = pydantic.Field(
        None, description="Faculty name",
    )
    graduation: typing.Optional[int] = pydantic.Field(
        None, description="Graduation year",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="University ID",
    )
    name: typing.Optional[str] = pydantic.Field(
        None, description="University name",
    )


class UsersUserCounters(pydantic.BaseModel):
    albums: typing.Optional[int] = pydantic.Field(
        None, description="Albums number",
    )
    audios: typing.Optional[int] = pydantic.Field(
        None, description="Audios number",
    )
    followers: typing.Optional[int] = pydantic.Field(
        None, description="Followers number",
    )
    friends: typing.Optional[int] = pydantic.Field(
        None, description="Friends number",
    )
    gifts: typing.Optional[int] = pydantic.Field(
        None, description="Gifts number",
    )
    groups: typing.Optional[int] = pydantic.Field(
        None, description="Communities number",
    )
    notes: typing.Optional[int] = pydantic.Field(
        None, description="Notes number",
    )
    online_friends: typing.Optional[int] = pydantic.Field(
        None, description="Online friends number",
    )
    pages: typing.Optional[int] = pydantic.Field(
        None, description="Public pages number",
    )
    photos: typing.Optional[int] = pydantic.Field(
        None, description="Photos number",
    )
    subscriptions: typing.Optional[int] = pydantic.Field(
        None, description="Subscriptions number",
    )
    user_photos: typing.Optional[int] = pydantic.Field(
        None, description="Number of photos with user",
    )
    user_videos: typing.Optional[int] = pydantic.Field(
        None, description="Number of videos with user",
    )
    videos: typing.Optional[int] = pydantic.Field(
        None, description="Videos number",
    )


class UsersUserSettingsXtr(pydantic.BaseModel):
    connections: typing.Optional["UsersUserConnections"] = pydantic.Field(
        None, description="",
    )
    bdate: typing.Optional[str] = pydantic.Field(
        None, description="User's date of birth",
    )
    bdate_visibility: typing.Optional[int] = pydantic.Field(
        None, description="Information whether user's birthdate are hidden",
    )
    city: typing.Optional["BaseCity"] = pydantic.Field(
        None, description="",
    )
    country: typing.Optional["BaseCountry"] = pydantic.Field(
        None, description="",
    )
    first_name: typing.Optional[str] = pydantic.Field(
        None, description="User first name",
    )
    home_town: typing.Optional[str] = pydantic.Field(
        None, description="User's hometown",
    )
    last_name: typing.Optional[str] = pydantic.Field(
        None, description="User last name",
    )
    maiden_name: typing.Optional[str] = pydantic.Field(
        None, description="User maiden name",
    )
    name_request: typing.Optional["AccountNameRequest"] = pydantic.Field(
        None, description="",
    )
    personal: typing.Optional["UsersPersonal"] = pydantic.Field(
        None, description="",
    )
    phone: typing.Optional[str] = pydantic.Field(
        None, description="User phone number with some hidden digits",
    )
    relation: typing.Optional["UsersUserRelation"] = pydantic.Field(
        None, description="User relationship status",
    )
    relation_partner: typing.Optional["UsersUserMin"] = pydantic.Field(
        None, description="",
    )
    relation_pending: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether relation status is pending",
    )
    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = pydantic.Field(
        None, description="",
    )
    screen_name: typing.Optional[str] = pydantic.Field(
        None, description="Domain name of the user's page",
    )
    sex: typing.Optional["BaseSex"] = pydantic.Field(
        None, description="User sex",
    )
    status: typing.Optional[str] = pydantic.Field(
        None, description="User status",
    )
    status_audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    interests: typing.Optional["AccountUserSettingsInterests"] = pydantic.Field(
        None, description="",
    )
    languages: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )


class UsersUserTypeEnum(str, Enum):
    profile = "profile"


class UsersUserType(pydantic.BaseModel):
    enum: typing.Optional[UsersUserTypeEnum] = pydantic.Field(
        None, description="Object type",
    )


class UsersUserXtrCounters(pydantic.BaseModel):
    users_user_full: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )
    counters: typing.Optional["UsersUserCounters"] = pydantic.Field(
        None, description="",
    )


class UsersUserXtrType(pydantic.BaseModel):
    users_user: typing.Optional["UsersUser"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["UsersUserType"] = pydantic.Field(
        None, description="",
    )


class UsersUsersArray(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Users number",
    )
    items: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class UtilsDomainResolved(pydantic.BaseModel):
    object_id: typing.Optional[int] = pydantic.Field(
        None, description="Object ID",
    )
    type: typing.Optional["UtilsDomainResolvedType"] = pydantic.Field(
        None, description="",
    )


class UtilsLastShortenedLink(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for private stats",
    )
    key: typing.Optional[str] = pydantic.Field(
        None, description="Link key (characters after vk.cc/)",
    )
    short_url: typing.Optional[str] = pydantic.Field(
        None, description="Short link URL",
    )
    timestamp: typing.Optional[int] = pydantic.Field(
        None, description="Creation time in Unixtime",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Full URL",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Total views number",
    )


class UtilsLinkChecked(pydantic.BaseModel):
    link: typing.Optional[str] = pydantic.Field(
        None, description="Link URL",
    )
    status: typing.Optional["UtilsLinkCheckedStatus"] = pydantic.Field(
        None, description="",
    )


class UtilsLinkStats(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="Link key (characters after vk.cc/)",
    )
    stats: typing.Optional[typing.List["UtilsStats"]] = pydantic.Field(
        None, description="",
    )


class UtilsLinkStatsExtended(pydantic.BaseModel):
    key: typing.Optional[str] = pydantic.Field(
        None, description="Link key (characters after vk.cc/)",
    )
    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = pydantic.Field(
        None, description="",
    )


class UtilsShortLink(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for private stats",
    )
    key: typing.Optional[str] = pydantic.Field(
        None, description="Link key (characters after vk.cc/)",
    )
    short_url: typing.Optional[str] = pydantic.Field(
        None, description="Short link URL",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Full URL",
    )


class UtilsStats(pydantic.BaseModel):
    timestamp: typing.Optional[int] = pydantic.Field(
        None, description="Start time",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Total views number",
    )


class UtilsStatsCity(pydantic.BaseModel):
    city_id: typing.Optional[int] = pydantic.Field(
        None, description="City ID",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )


class UtilsStatsCountry(pydantic.BaseModel):
    country_id: typing.Optional[int] = pydantic.Field(
        None, description="Country ID",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Views number",
    )


class UtilsStatsExtended(pydantic.BaseModel):
    cities: typing.Optional[typing.List["UtilsStatsCity"]] = pydantic.Field(
        None, description="",
    )
    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = pydantic.Field(
        None, description="",
    )
    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = pydantic.Field(
        None, description="",
    )
    timestamp: typing.Optional[int] = pydantic.Field(
        None, description="Start time",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Total views number",
    )


class UtilsStatsSexAge(pydantic.BaseModel):
    age_range: typing.Optional[str] = pydantic.Field(
        None, description="Age denotation",
    )
    female: typing.Optional[int] = pydantic.Field(
        None, description=" Views by female users",
    )
    male: typing.Optional[int] = pydantic.Field(
        None, description=" Views by male users",
    )


class VideoSaveResult(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Video access key",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Video description",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Video owner ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Video title",
    )
    upload_url: typing.Optional[str] = pydantic.Field(
        None, description="URL for the video uploading",
    )
    video_id: typing.Optional[int] = pydantic.Field(
        None, description="Video ID",
    )


class VideoVideoAlbumFull(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number of videos in album",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None, description="Album cover image in different sizes",
    )
    is_system: typing.Optional[int] = pydantic.Field(
        None, description="Information whether album is system",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Album owner's ID",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Album title",
    )
    updated_time: typing.Optional[int] = pydantic.Field(
        None, description="Date when the album has been updated last time in Unixtime",
    )


class VideoVideoFull(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Video access key",
    )
    adding_date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the video has been added in Unixtime",
    )
    can_add: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can add the video",
    )
    can_add_to_faves: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Information whether current user can add the video to favourites",
    )
    can_comment: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the video",
    )
    can_edit: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can edit the video",
    )
    can_repost: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can comment the video",
    )
    comments: typing.Optional[int] = pydantic.Field(
        None, description="Number of comments",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when video has been uploaded in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Video description",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None, description="Video duration in seconds",
    )
    files: typing.Optional["VideoVideoFiles"] = pydantic.Field(
        None, description="",
    )
    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None, description="",
    )
    first_frame_640: typing.Optional[str] = pydantic.Field(
        None, description="URL of the first frame for the corresponding width.",
    )
    first_frame_1280: typing.Optional[str] = pydantic.Field(
        None, description="URL of the first frame for the corresponding width.",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Video ID",
    )
    image: typing.Optional[typing.List["VideoVideoImage"]] = pydantic.Field(
        None, description="",
    )
    likes: typing.Optional["BaseLikes"] = pydantic.Field(
        None, description="",
    )
    live: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the video is live translation",
    )
    owner_id: typing.Optional[int] = pydantic.Field(
        None, description="Video owner ID",
    )
    player: typing.Optional[str] = pydantic.Field(
        None,
        description="URL of the page with a player that can be used to play the video in the browser.",
    )
    processing: typing.Optional["BasePropertyExists"] = pydantic.Field(
        None, description="Returns if the video is processing",
    )
    repeat: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the video is repeated",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Video title",
    )
    views: typing.Optional[int] = pydantic.Field(
        None, description="Number of views",
    )


class VideoVideoImage(pydantic.BaseModel):
    base_image: typing.Optional["BaseImage"] = pydantic.Field(
        None, description="",
    )
    with_padding: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )


class WallCommentAttachment(pydantic.BaseModel):
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None, description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None, description="",
    )
    market_market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None, description="",
    )
    note: typing.Optional["WallAttachedNote"] = pydantic.Field(
        None, description="",
    )
    page: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    sticker: typing.Optional["BaseSticker"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["WallCommentAttachmentType"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )


class WallWallpostAttachment(pydantic.BaseModel):
    access_key: typing.Optional[str] = pydantic.Field(
        None, description="Access key for the audio",
    )
    album: typing.Optional["PhotosPhotoAlbum"] = pydantic.Field(
        None, description="",
    )
    app: typing.Optional["WallAppPost"] = pydantic.Field(
        None, description="",
    )
    audio: typing.Optional["AudioAudio"] = pydantic.Field(
        None, description="",
    )
    doc: typing.Optional["DocsDoc"] = pydantic.Field(
        None, description="",
    )
    event: typing.Optional["EventsEventAttach"] = pydantic.Field(
        None, description="",
    )
    graffiti: typing.Optional["WallGraffiti"] = pydantic.Field(
        None, description="",
    )
    link: typing.Optional["BaseLink"] = pydantic.Field(
        None, description="",
    )
    market: typing.Optional["MarketMarketItem"] = pydantic.Field(
        None, description="",
    )
    market_album: typing.Optional["MarketMarketAlbum"] = pydantic.Field(
        None, description="",
    )
    note: typing.Optional["WallAttachedNote"] = pydantic.Field(
        None, description="",
    )
    page: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None, description="",
    )
    photo: typing.Optional["PhotosPhoto"] = pydantic.Field(
        None, description="",
    )
    photos_list: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )
    poll: typing.Optional["PollsPoll"] = pydantic.Field(
        None, description="",
    )
    posted_photo: typing.Optional["WallPostedPhoto"] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["WallWallpostAttachmentType"] = pydantic.Field(
        None, description="",
    )
    video: typing.Optional["VideoVideo"] = pydantic.Field(
        None, description="",
    )


class WallWallpostToId(pydantic.BaseModel):
    attachments: typing.Optional[
        typing.List["WallWallpostAttachment"]
    ] = pydantic.Field(
        None, description="",
    )
    comments: typing.Optional["BaseCommentsInfo"] = pydantic.Field(
        None, description="",
    )
    copy_owner_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the source post owner",
    )
    copy_post_id: typing.Optional[int] = pydantic.Field(
        None, description="ID of the source post",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date of publishing in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Post author ID",
    )
    geo: typing.Optional["WallGeo"] = pydantic.Field(
        None, description="",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Post ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="wall post ID (if comment)",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None, description="",
    )
    post_type: typing.Optional["WallPostType"] = pydantic.Field(
        None, description="",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None, description="",
    )
    signer_id: typing.Optional[int] = pydantic.Field(
        None, description="Post signer ID",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Post text",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None, description="Wall owner's ID",
    )


class WidgetsCommentRepliesItem(pydantic.BaseModel):
    cid: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    likes: typing.Optional["WidgetsWidgetLikes"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    uid: typing.Optional[int] = pydantic.Field(
        None, description="User ID",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )


class WidgetsWidgetComment(pydantic.BaseModel):
    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = pydantic.Field(
        None, description="",
    )
    can_delete: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether current user can delete the comment",
    )
    comments: typing.Optional["WidgetsCommentReplies"] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None, description="Date when the comment has been added in Unixtime",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None, description="Comment author ID",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )
    likes: typing.Optional["BaseLikesInfo"] = pydantic.Field(
        None, description="",
    )
    media: typing.Optional["WidgetsCommentMedia"] = pydantic.Field(
        None, description="",
    )
    post_source: typing.Optional["WallPostSource"] = pydantic.Field(
        None, description="",
    )
    post_type: typing.Optional[int] = pydantic.Field(
        None, description="Post type",
    )
    reposts: typing.Optional["BaseRepostsInfo"] = pydantic.Field(
        None, description="",
    )
    text: typing.Optional[str] = pydantic.Field(
        None, description="Comment text",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None, description="Wall owner",
    )
    user: typing.Optional["UsersUserFull"] = pydantic.Field(
        None, description="",
    )


class WidgetsWidgetPage(pydantic.BaseModel):
    comments: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    date: typing.Optional[int] = pydantic.Field(
        None,
        description="Date when widgets on the page has been initialized firstly in Unixtime",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Page description",
    )
    id: typing.Optional[int] = pydantic.Field(
        None, description="Page ID",
    )
    likes: typing.Optional["BaseObjectCount"] = pydantic.Field(
        None, description="",
    )
    page_id: typing.Optional[str] = pydantic.Field(
        None, description="page_id parameter value",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None, description="URL of the preview image",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="Page title",
    )
    url: typing.Optional[str] = pydantic.Field(
        None, description="Page absolute URL",
    )
