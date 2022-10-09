import pydantic

from .objects import *


class AccountChangePasswordResponse(pydantic.BaseModel):
    response: "AccountChangePasswordResponseModel" = pydantic.Field(..., description="")


class AccountGetActiveOffersResponse(pydantic.BaseModel):
    response: "AccountGetActiveOffersResponseModel" = pydantic.Field(
        ..., description=""
    )


class AccountGetAppPermissionsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Permissions mask")


class AccountGetBannedResponse(pydantic.BaseModel):
    response: "AccountGetBannedResponseModel" = pydantic.Field(..., description="")


class AccountGetCountersResponse(pydantic.BaseModel):
    response: AccountAccountCounters = pydantic.Field(..., description="")


class AccountGetInfoResponse(pydantic.BaseModel):
    response: AccountInfo = pydantic.Field(..., description="")


class AccountGetProfileInfoResponse(pydantic.BaseModel):
    response: AccountUserSettings = pydantic.Field(..., description="")


class AccountGetPushSettingsResponse(pydantic.BaseModel):
    response: AccountPushSettings = pydantic.Field(..., description="")


class AccountSaveProfileInfoResponse(pydantic.BaseModel):
    response: "AccountSaveProfileInfoResponseModel" = pydantic.Field(
        ..., description=""
    )


class AccountChangePasswordResponseModel(pydantic.BaseModel):
    token: typing.Optional[str]
    secret: typing.Optional[str]


class AccountGetActiveOffersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AccountOffer"]]


class AccountGetBannedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]


class AccountSaveProfileInfoResponseModel(pydantic.BaseModel):
    changed: typing.Optional["BaseBoolInt"]
    name_request: typing.Optional["AccountNameRequest"]


class AdsAddOfficeUsersResponse(pydantic.BaseModel):
    response: bool = pydantic.Field(..., description="true if success")


class AdsCheckLinkResponse(pydantic.BaseModel):
    response: AdsLinkStatus = pydantic.Field(..., description="")


class AdsCreateAdsResponse(pydantic.BaseModel):
    response: typing.List["AdsCreateAdStatus"] = pydantic.Field(..., description="")


class AdsCreateCampaignsResponse(pydantic.BaseModel):
    response: typing.List["AdsCreateCampaignStatus"] = pydantic.Field(
        ..., description=""
    )


class AdsCreateClientsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class AdsCreateTargetGroupResponse(pydantic.BaseModel):
    response: "AdsCreateTargetGroupResponseModel" = pydantic.Field(..., description="")


class AdsDeleteAdsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class AdsDeleteCampaignsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class AdsDeleteClientsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class AdsGetAccountsResponse(pydantic.BaseModel):
    response: typing.List["AdsAccount"] = pydantic.Field(..., description="")


class AdsGetAdsLayoutResponse(pydantic.BaseModel):
    response: typing.List["AdsAdLayout"] = pydantic.Field(..., description="")


class AdsGetAdsTargetingResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSettings"] = pydantic.Field(..., description="")


class AdsGetAdsResponse(pydantic.BaseModel):
    response: typing.List["AdsAd"] = pydantic.Field(..., description="")


class AdsGetBudgetResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Budget")


class AdsGetCampaignsResponse(pydantic.BaseModel):
    response: typing.List["AdsCampaign"] = pydantic.Field(..., description="")


class AdsGetCategoriesResponse(pydantic.BaseModel):
    response: "AdsGetCategoriesResponseModel" = pydantic.Field(..., description="")


class AdsGetClientsResponse(pydantic.BaseModel):
    response: typing.List["AdsClient"] = pydantic.Field(..., description="")


class AdsGetDemographicsResponse(pydantic.BaseModel):
    response: typing.List["AdsDemoStats"] = pydantic.Field(..., description="")


class AdsGetFloodStatsResponse(pydantic.BaseModel):
    response: AdsFloodStats = pydantic.Field(..., description="")


class AdsGetLookalikeRequestsResponse(pydantic.BaseModel):
    response: "AdsGetLookalikeRequestsResponseModel" = pydantic.Field(
        ..., description=""
    )


class AdsGetMusiciansResponse(pydantic.BaseModel):
    response: "AdsGetMusiciansResponseModel" = pydantic.Field(..., description="")


class AdsGetOfficeUsersResponse(pydantic.BaseModel):
    response: typing.List["AdsUsers"] = pydantic.Field(..., description="")


class AdsGetPostsReachResponse(pydantic.BaseModel):
    response: typing.List["AdsPromotedPostReach"] = pydantic.Field(..., description="")


class AdsGetRejectionReasonResponse(pydantic.BaseModel):
    response: AdsRejectReason = pydantic.Field(..., description="")


class AdsGetStatisticsResponse(pydantic.BaseModel):
    response: typing.List["AdsStats"] = pydantic.Field(..., description="")


class AdsGetSuggestionsCitiesResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsCities"] = pydantic.Field(
        ..., description=""
    )


class AdsGetSuggestionsRegionsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsRegions"] = pydantic.Field(
        ..., description=""
    )


class AdsGetSuggestionsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestions"] = pydantic.Field(..., description="")


class AdsGetSuggestionsSchoolsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsSchools"] = pydantic.Field(
        ..., description=""
    )


class AdsGetTargetGroupsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargetGroup"] = pydantic.Field(..., description="")


class AdsGetTargetingStatsResponse(pydantic.BaseModel):
    response: AdsTargStats = pydantic.Field(..., description="")


class AdsGetUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="Photo upload URL")


class AdsGetVideoUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="Video upload URL")


class AdsImportTargetContactsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Imported contacts number")


class AdsRemoveOfficeUsersResponse(pydantic.BaseModel):
    response: bool = pydantic.Field(..., description="true if success")


class AdsUpdateAdsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class AdsUpdateCampaignsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Campaign ID")


class AdsUpdateClientsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Client ID")


class AdsUpdateOfficeUsersResponse(pydantic.BaseModel):
    response: typing.List["AdsUpdateOfficeUsersResult"] = pydantic.Field(
        ..., description=""
    )


class AdsCreateTargetGroupResponseModel(pydantic.BaseModel):
    id: typing.Optional[int]
    pixel: typing.Optional[str]


class AdsGetCategoriesResponseModel(pydantic.BaseModel):
    v1: typing.Optional[typing.List["AdsCategory"]]
    v2: typing.Optional[typing.List["AdsCategory"]]


class AdsGetLookalikeRequestsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AdsLookalikeRequest"]]


class AdsGetMusiciansResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["AdsMusician"]]


class AdswebGetAdCategoriesResponse(pydantic.BaseModel):
    response: "AdswebGetAdCategoriesResponseModel" = pydantic.Field(..., description="")


class AdswebGetAdUnitCodeResponse(pydantic.BaseModel):
    response: "AdswebGetAdUnitCodeResponseModel" = pydantic.Field(..., description="")


class AdswebGetAdUnitsResponse(pydantic.BaseModel):
    response: "AdswebGetAdUnitsResponseModel" = pydantic.Field(..., description="")


class AdswebGetFraudHistoryResponse(pydantic.BaseModel):
    response: "AdswebGetFraudHistoryResponseModel" = pydantic.Field(..., description="")


class AdswebGetSitesResponse(pydantic.BaseModel):
    response: "AdswebGetSitesResponseModel" = pydantic.Field(..., description="")


class AdswebGetStatisticsResponse(pydantic.BaseModel):
    response: "AdswebGetStatisticsResponseModel" = pydantic.Field(..., description="")


class AdswebGetAdCategoriesResponseModel(pydantic.BaseModel):
    categories: typing.Optional[
        typing.List["AdswebGetAdCategoriesResponseCategoriesCategory"]
    ]


class AdswebGetAdUnitCodeResponseModel(pydantic.BaseModel):
    html: typing.Optional[str]


class AdswebGetAdUnitsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    ad_units: typing.Optional[typing.List["AdswebGetAdUnitsResponseAdUnitsAdUnit"]]


class AdswebGetFraudHistoryResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    entries: typing.Optional[typing.List["AdswebGetFraudHistoryResponseEntriesEntry"]]


class AdswebGetSitesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    sites: typing.Optional[typing.List["AdswebGetSitesResponseSitesSite"]]


class AdswebGetStatisticsResponseModel(pydantic.BaseModel):
    next_page_id: typing.Optional[str]
    items: typing.Optional[typing.List["AdswebGetStatisticsResponseItemsItem"]]


class AppWidgetsGetAppImageUploadServerResponse(pydantic.BaseModel):
    response: "AppWidgetsGetAppImageUploadServerResponseModel" = pydantic.Field(
        ..., description=""
    )


class AppWidgetsGetAppImagesResponse(pydantic.BaseModel):
    response: AppWidgetsPhotos = pydantic.Field(..., description="")


class AppWidgetsGetGroupImageUploadServerResponse(pydantic.BaseModel):
    response: "AppWidgetsGetGroupImageUploadServerResponseModel" = pydantic.Field(
        ..., description=""
    )


class AppWidgetsGetGroupImagesResponse(pydantic.BaseModel):
    response: AppWidgetsPhotos = pydantic.Field(..., description="")


class AppWidgetsGetImagesByIdResponse(pydantic.BaseModel):
    response: typing.List["AppWidgetsPhoto"] = pydantic.Field(..., description="")


class AppWidgetsSaveAppImageResponse(pydantic.BaseModel):
    response: AppWidgetsPhoto = pydantic.Field(..., description="")


class AppWidgetsSaveGroupImageResponse(pydantic.BaseModel):
    response: AppWidgetsPhoto = pydantic.Field(..., description="")


class AppWidgetsGetAppImageUploadServerResponseModel(pydantic.BaseModel):
    upload_url: typing.Optional[str]


class AppWidgetsGetGroupImageUploadServerResponseModel(pydantic.BaseModel):
    upload_url: typing.Optional[str]


class AppsGetCatalogResponse(pydantic.BaseModel):
    response: AppsCatalogList = pydantic.Field(..., description="")


class AppsGetFriendsListExtendedResponse(pydantic.BaseModel):
    response: "AppsGetFriendsListExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class AppsGetFriendsListResponse(pydantic.BaseModel):
    response: "AppsGetFriendsListResponseModel" = pydantic.Field(..., description="")


class AppsGetLeaderboardExtendedResponse(pydantic.BaseModel):
    response: "AppsGetLeaderboardExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class AppsGetLeaderboardResponse(pydantic.BaseModel):
    response: "AppsGetLeaderboardResponseModel" = pydantic.Field(..., description="")


class AppsGetMiniAppPoliciesResponse(pydantic.BaseModel):
    response: "AppsGetMiniAppPoliciesResponseModel" = pydantic.Field(
        ..., description=""
    )


class AppsGetScopesResponse(pydantic.BaseModel):
    response: "AppsGetScopesResponseModel" = pydantic.Field(..., description="")


class AppsGetScoreResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Score number")


class AppsGetResponse(pydantic.BaseModel):
    response: "AppsGetResponseModel" = pydantic.Field(..., description="")


class AppsImageUploadResponse(pydantic.BaseModel):
    response: "AppsImageUploadResponseModel" = pydantic.Field(..., description="")


class AppsSendRequestResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Request ID")


class AppsGetFriendsListExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class AppsGetFriendsListResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class AppsGetLeaderboardExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AppsLeaderboard"]]
    profiles: typing.Optional[typing.List["UsersUser"]]


class AppsGetLeaderboardResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AppsLeaderboard"]]


class AppsGetMiniAppPoliciesResponseModel(pydantic.BaseModel):
    privacy_policy: typing.Optional[str]
    terms: typing.Optional[str]


class AppsGetScopesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AppsScope"]]


class AppsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["AppsApp"]]


class AppsImageUploadResponseModel(pydantic.BaseModel):
    hash: typing.Optional[str]
    image: typing.Optional[str]


class AuthRestoreResponse(pydantic.BaseModel):
    response: "AuthRestoreResponseModel" = pydantic.Field(..., description="")


class AuthRestoreResponseModel(pydantic.BaseModel):
    success: typing.Optional[int]
    sid: typing.Optional[str]


class BaseBoolResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="")


class BaseGetUploadServerResponse(pydantic.BaseModel):
    response: BaseUploadServer = pydantic.Field(..., description="")


class BaseOkResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="")


class BoardAddTopicResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Topic ID")


class BoardCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Comment ID")


class BoardGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class BoardGetCommentsResponse(pydantic.BaseModel):
    response: "BoardGetCommentsResponseModel" = pydantic.Field(..., description="")


class BoardGetTopicsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetTopicsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class BoardGetTopicsResponse(pydantic.BaseModel):
    response: "BoardGetTopicsResponseModel" = pydantic.Field(..., description="")


class BoardGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BoardTopicComment"]]
    poll: typing.Optional[typing.Any]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    real_offset: typing.Optional[int]


class BoardGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BoardTopicComment"]]
    poll: typing.Optional[typing.Any]
    real_offset: typing.Optional[int]


class BoardGetTopicsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BoardTopic"]]
    default_order: typing.Optional["BoardDefaultOrder"]
    can_add_topics: typing.Optional["BaseBoolInt"]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class BoardGetTopicsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BoardTopic"]]
    default_order: typing.Optional["BoardDefaultOrder"]
    can_add_topics: typing.Optional["BaseBoolInt"]


class DatabaseGetChairsResponse(pydantic.BaseModel):
    response: "DatabaseGetChairsResponseModel" = pydantic.Field(..., description="")


class DatabaseGetCitiesByIdResponse(pydantic.BaseModel):
    response: typing.List["DatabaseCityById"] = pydantic.Field(..., description="")


class DatabaseGetCitiesResponse(pydantic.BaseModel):
    response: "DatabaseGetCitiesResponseModel" = pydantic.Field(..., description="")


class DatabaseGetCountriesByIdResponse(pydantic.BaseModel):
    response: typing.List["BaseCountry"] = pydantic.Field(..., description="")


class DatabaseGetCountriesResponse(pydantic.BaseModel):
    response: "DatabaseGetCountriesResponseModel" = pydantic.Field(..., description="")


class DatabaseGetFacultiesResponse(pydantic.BaseModel):
    response: "DatabaseGetFacultiesResponseModel" = pydantic.Field(..., description="")


class DatabaseGetMetroStationsByIdResponse(pydantic.BaseModel):
    response: typing.List["DatabaseStation"] = pydantic.Field(..., description="")


class DatabaseGetMetroStationsResponse(pydantic.BaseModel):
    response: "DatabaseGetMetroStationsResponseModel" = pydantic.Field(
        ..., description=""
    )


class DatabaseGetRegionsResponse(pydantic.BaseModel):
    response: "DatabaseGetRegionsResponseModel" = pydantic.Field(..., description="")


class DatabaseGetSchoolClassesResponse(pydantic.BaseModel):
    response: typing.List[list] = pydantic.Field(..., description="")


class DatabaseGetSchoolsResponse(pydantic.BaseModel):
    response: "DatabaseGetSchoolsResponseModel" = pydantic.Field(..., description="")


class DatabaseGetUniversitiesResponse(pydantic.BaseModel):
    response: "DatabaseGetUniversitiesResponseModel" = pydantic.Field(
        ..., description=""
    )


class DatabaseGetChairsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BaseObject"]]


class DatabaseGetCitiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseCity"]]


class DatabaseGetCountriesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["BaseCountry"]]


class DatabaseGetFacultiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseFaculty"]]


class DatabaseGetMetroStationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseStation"]]


class DatabaseGetRegionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseRegion"]]


class DatabaseGetSchoolsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseSchool"]]


class DatabaseGetUniversitiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DatabaseUniversity"]]


class DocsAddResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Document ID")


class DocsDocUploadResponse(pydantic.BaseModel):
    response: "DocsDocUploadResponseModel" = pydantic.Field(..., description="")


class DocsGetByIdResponse(pydantic.BaseModel):
    response: typing.List["DocsDoc"] = pydantic.Field(..., description="")


class DocsGetTypesResponse(pydantic.BaseModel):
    response: "DocsGetTypesResponseModel" = pydantic.Field(..., description="")


class DocsGetUploadServerResponse(pydantic.BaseModel):
    response: BaseUploadServer = pydantic.Field(..., description="")


class DocsGetResponse(pydantic.BaseModel):
    response: "DocsGetResponseModel" = pydantic.Field(..., description="")


class DocsSaveResponse(pydantic.BaseModel):
    response: "DocsSaveResponseModel" = pydantic.Field(..., description="")


class DocsSearchResponse(pydantic.BaseModel):
    response: "DocsSearchResponseModel" = pydantic.Field(..., description="")


class DocsDocUploadResponseModel(pydantic.BaseModel):
    file: typing.Optional[str]


class DocsGetTypesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DocsDocTypes"]]


class DocsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DocsDoc"]]


class DocsSaveResponseModel(pydantic.BaseModel):
    type: typing.Optional["DocsDocAttachmentType"]
    audio_message: typing.Optional["MessagesAudioMessage"]
    doc: typing.Optional["DocsDoc"]
    graffiti: typing.Optional["MessagesGraffiti"]


class DocsSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["DocsDoc"]]


class DonutGetSubscriptionResponse(pydantic.BaseModel):
    response: DonutDonatorSubscriptionInfo = pydantic.Field(..., description="")


class DonutGetSubscriptionsResponse(pydantic.BaseModel):
    response: "DonutGetSubscriptionsResponseModel" = pydantic.Field(..., description="")


class DonutGetSubscriptionsResponseModel(pydantic.BaseModel):
    subscriptions: typing.Optional[typing.List["DonutDonatorSubscriptionInfo"]]
    count: typing.Optional[int]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class Downloaded_gamesPaidStatusResponse(pydantic.BaseModel):
    response: "Downloaded_gamesPaidStatusResponseModel" = pydantic.Field(
        ..., description=""
    )


class Downloaded_gamesPaidStatusResponseModel(pydantic.BaseModel):
    is_paid: typing.Optional[bool]


class FaveAddTagResponse(pydantic.BaseModel):
    response: FaveTag = pydantic.Field(..., description="")


class FaveGetPagesResponse(pydantic.BaseModel):
    response: "FaveGetPagesResponseModel" = pydantic.Field(..., description="")


class FaveGetPostsResponse(pydantic.BaseModel):
    response: "FaveGetPostsResponseModel" = pydantic.Field(..., description="")


class FaveGetPhotosResponse(pydantic.BaseModel):
    response: "FaveGetPhotosResponseModel" = pydantic.Field(..., description="")


class FaveGetVideosResponse(pydantic.BaseModel):
    response: "FaveGetVideosResponseModel" = pydantic.Field(..., description="")


class FaveGetTagsResponse(pydantic.BaseModel):
    response: "FaveGetTagsResponseModel" = pydantic.Field(..., description="")


class FaveGetExtendedResponse(pydantic.BaseModel):
    response: "FaveGetExtendedResponseModel" = pydantic.Field(..., description="")


class FaveGetResponse(pydantic.BaseModel):
    response: "FaveGetResponseModel" = pydantic.Field(..., description="")


class FaveGetPagesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FavePage"]]


class FaveGetPostsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostFull"]]


class FaveGetVideosResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoFull"]]


class FaveGetPhotosResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhoto"]]


class FaveGetTagsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FaveTag"]]


class FaveGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FaveBookmark"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]


class FaveGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FaveBookmark"]]


class FriendsAddListResponse(pydantic.BaseModel):
    response: "FriendsAddListResponseModel" = pydantic.Field(..., description="")


class FriendsAddResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Friend request status")


class FriendsAreFriendsExtendedResponse(pydantic.BaseModel):
    response: typing.List["FriendsFriendExtendedStatus"] = pydantic.Field(
        ..., description=""
    )


class FriendsAreFriendsResponse(pydantic.BaseModel):
    response: typing.List["FriendsFriendStatus"] = pydantic.Field(..., description="")


class FriendsDeleteResponse(pydantic.BaseModel):
    response: "FriendsDeleteResponseModel" = pydantic.Field(..., description="")


class FriendsGetAppUsersResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class FriendsGetByPhonesResponse(pydantic.BaseModel):
    response: typing.List["FriendsUserXtrPhone"] = pydantic.Field(..., description="")


class FriendsGetListsResponse(pydantic.BaseModel):
    response: "FriendsGetListsResponseModel" = pydantic.Field(..., description="")


class FriendsGetMutualResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class FriendsGetMutualTargetUidsResponse(pydantic.BaseModel):
    response: typing.List["FriendsMutualFriend"] = pydantic.Field(..., description="")


class FriendsGetOnlineOnlineMobileResponse(pydantic.BaseModel):
    response: "FriendsGetOnlineOnlineMobileResponseModel" = pydantic.Field(
        ..., description=""
    )


class FriendsGetOnlineResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class FriendsGetRecentResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class FriendsGetRequestsExtendedResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class FriendsGetRequestsNeedMutualResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsNeedMutualResponseModel" = pydantic.Field(
        ..., description=""
    )


class FriendsGetRequestsResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsResponseModel" = pydantic.Field(..., description="")


class FriendsGetSuggestionsResponse(pydantic.BaseModel):
    response: "FriendsGetSuggestionsResponseModel" = pydantic.Field(..., description="")


class FriendsGetFieldsResponse(pydantic.BaseModel):
    response: "FriendsGetFieldsResponseModel" = pydantic.Field(..., description="")


class FriendsGetResponse(pydantic.BaseModel):
    response: "FriendsGetResponseModel" = pydantic.Field(..., description="")


class FriendsSearchResponse(pydantic.BaseModel):
    response: "FriendsSearchResponseModel" = pydantic.Field(..., description="")


class FriendsAddListResponseModel(pydantic.BaseModel):
    list_id: typing.Optional[int]


class FriendsDeleteResponseModel(pydantic.BaseModel):
    success: typing.Optional[int]
    friend_deleted: typing.Optional[int]
    out_request_deleted: typing.Optional[int]
    in_request_deleted: typing.Optional[int]
    suggestion_deleted: typing.Optional[int]


class FriendsGetListsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FriendsFriendsList"]]


class FriendsGetOnlineOnlineMobileResponseModel(pydantic.BaseModel):
    online: typing.Optional[typing.List[int]]
    online_mobile: typing.Optional[typing.List[int]]


class FriendsGetRequestsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FriendsRequestsXtrMessage"]]


class FriendsGetRequestsNeedMutualResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["FriendsRequests"]]


class FriendsGetRequestsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]
    count_unread: typing.Optional[int]


class FriendsGetSuggestionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class FriendsGetFieldsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class FriendsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class FriendsSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class GiftsGetResponse(pydantic.BaseModel):
    response: "GiftsGetResponseModel" = pydantic.Field(..., description="")


class GiftsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GiftsGift"]]


class GroupsAddAddressResponse(pydantic.BaseModel):
    response: GroupsAddress = pydantic.Field(..., description="")


class GroupsAddCallbackServerResponse(pydantic.BaseModel):
    response: "GroupsAddCallbackServerResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsAddLinkResponse(pydantic.BaseModel):
    response: GroupsLinksItem = pydantic.Field(..., description="")


class GroupsCreateResponse(pydantic.BaseModel):
    response: GroupsGroup = pydantic.Field(..., description="")


class GroupsEditAddressResponse(pydantic.BaseModel):
    response: GroupsAddress = pydantic.Field(..., description="Result")


class GroupsGetAddressesResponse(pydantic.BaseModel):
    response: "GroupsGetAddressesResponseModel" = pydantic.Field(..., description="")


class GroupsGetBannedResponse(pydantic.BaseModel):
    response: "GroupsGetBannedResponseModel" = pydantic.Field(..., description="")


class GroupsGetByIdLegacyResponse(pydantic.BaseModel):
    response: typing.List["GroupsGroupFull"] = pydantic.Field(..., description="")


class GroupsGetCallbackConfirmationCodeResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackConfirmationCodeResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetCallbackServersResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackServersResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetCallbackSettingsResponse(pydantic.BaseModel):
    response: GroupsCallbackSettings = pydantic.Field(..., description="")


class GroupsGetCatalogInfoExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetCatalogInfoResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoResponseModel" = pydantic.Field(..., description="")


class GroupsGetCatalogResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogResponseModel" = pydantic.Field(..., description="")


class GroupsGetInvitedUsersResponse(pydantic.BaseModel):
    response: "GroupsGetInvitedUsersResponseModel" = pydantic.Field(..., description="")


class GroupsGetInvitesExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetInvitesResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesResponseModel" = pydantic.Field(..., description="")


class GroupsGetLongPollServerResponse(pydantic.BaseModel):
    response: GroupsLongPollServer = pydantic.Field(..., description="")


class GroupsGetLongPollSettingsResponse(pydantic.BaseModel):
    response: GroupsLongPollSettings = pydantic.Field(..., description="")


class GroupsGetMembersFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFieldsResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetMembersFilterResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFilterResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetMembersResponse(pydantic.BaseModel):
    response: "GroupsGetMembersResponseModel" = pydantic.Field(..., description="")


class GroupsGetRequestsFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsFieldsResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetRequestsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsResponseModel" = pydantic.Field(..., description="")


class GroupsGetSettingsResponse(pydantic.BaseModel):
    response: "GroupsGetSettingsResponseModel" = pydantic.Field(..., description="")


class GroupsGetTagListResponse(pydantic.BaseModel):
    response: typing.List["GroupsGroupTag"] = pydantic.Field(..., description="")


class GroupsGetTokenPermissionsResponse(pydantic.BaseModel):
    response: "GroupsGetTokenPermissionsResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsGetResponse(pydantic.BaseModel):
    response: "GroupsGetResponseModel" = pydantic.Field(..., description="")


class GroupsIsMemberExtendedResponse(pydantic.BaseModel):
    response: "GroupsIsMemberExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class GroupsIsMemberResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ..., description="Information whether user is a member of the group"
    )


class GroupsIsMemberUserIdsExtendedResponse(pydantic.BaseModel):
    response: typing.List["GroupsMemberStatusFull"] = pydantic.Field(
        ..., description=""
    )


class GroupsIsMemberUserIdsResponse(pydantic.BaseModel):
    response: typing.List["GroupsMemberStatus"] = pydantic.Field(..., description="")


class GroupsSearchResponse(pydantic.BaseModel):
    response: "GroupsSearchResponseModel" = pydantic.Field(..., description="")


class GroupsAddCallbackServerResponseModel(pydantic.BaseModel):
    server_id: typing.Optional[int]


class GroupsGetAddressesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsAddress"]]


class GroupsGetBannedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsBannedItem"]]


class GroupsGetCallbackConfirmationCodeResponseModel(pydantic.BaseModel):
    code: typing.Optional[str]


class GroupsGetCallbackServersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsCallbackServer"]]


class GroupsGetCatalogInfoExtendedResponseModel(pydantic.BaseModel):
    enabled: typing.Optional["BaseBoolInt"]
    categories: typing.Optional[typing.List["GroupsGroupCategoryFull"]]


class GroupsGetCatalogInfoResponseModel(pydantic.BaseModel):
    enabled: typing.Optional["BaseBoolInt"]
    categories: typing.Optional[typing.List["GroupsGroupCategory"]]


class GroupsGetCatalogResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsGroup"]]


class GroupsGetInvitedUsersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class GroupsGetInvitesExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsGroupFull"]]
    profiles: typing.Optional[typing.List["UsersUserMin"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class GroupsGetInvitesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsGroupFull"]]


class GroupsGetMembersFieldsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsUserXtrRole"]]


class GroupsGetMembersFilterResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsMemberRole"]]


class GroupsGetMembersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class GroupsGetRequestsFieldsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class GroupsGetRequestsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class GroupsGetSettingsResponseModel(pydantic.BaseModel):
    access: typing.Optional["GroupsGroupAccess"]
    address: typing.Optional[str]
    audio: typing.Optional["GroupsGroupAudio"]
    articles: typing.Optional[int]
    recognize_photo: typing.Optional[int]
    city_id: typing.Optional[int]
    city_name: typing.Optional[str]
    contacts: typing.Optional["BaseBoolInt"]
    links: typing.Optional["BaseBoolInt"]
    sections_list: typing.Optional[typing.List["GroupsSectionsListItem"]]
    main_section: typing.Optional["GroupsGroupFullSection"]
    secondary_section: typing.Optional["GroupsGroupFullSection"]
    age_limits: typing.Optional["GroupsGroupAgeLimits"]
    country_id: typing.Optional[int]
    country_name: typing.Optional[str]
    description: typing.Optional[str]
    docs: typing.Optional["GroupsGroupDocs"]
    events: typing.Optional["BaseBoolInt"]
    obscene_filter: typing.Optional["BaseBoolInt"]
    obscene_stopwords: typing.Optional["BaseBoolInt"]
    obscene_words: typing.Optional[typing.List[str]]
    event_group_id: typing.Optional[int]
    photos: typing.Optional["GroupsGroupPhotos"]
    public_category: typing.Optional[int]
    public_category_list: typing.Optional[typing.List["GroupsGroupPublicCategoryList"]]
    public_date: typing.Optional[str]
    public_date_label: typing.Optional[str]
    public_subcategory: typing.Optional[int]
    rss: typing.Optional[str]
    start_date: typing.Optional[int]
    finish_date: typing.Optional[int]
    subject: typing.Optional[int]
    subject_list: typing.Optional[typing.List["GroupsSubjectItem"]]
    suggested_privacy: typing.Optional["GroupsGroupSuggestedPrivacy"]
    title: typing.Optional[str]
    topics: typing.Optional["GroupsGroupTopics"]
    twitter: typing.Optional["GroupsSettingsTwitter"]
    video: typing.Optional["GroupsGroupVideo"]
    wall: typing.Optional["GroupsGroupWall"]
    website: typing.Optional[str]
    phone: typing.Optional[str]
    email: typing.Optional[str]
    wiki: typing.Optional["GroupsGroupWiki"]


class GroupsGetTokenPermissionsResponseModel(pydantic.BaseModel):
    mask: typing.Optional[int]
    permissions: typing.Optional[typing.List["GroupsTokenPermissionSetting"]]


class GroupsGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsGroupFull"]]


class GroupsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class GroupsIsMemberExtendedResponseModel(pydantic.BaseModel):
    member: typing.Optional["BaseBoolInt"]
    invitation: typing.Optional["BaseBoolInt"]
    can_invite: typing.Optional["BaseBoolInt"]
    can_recall: typing.Optional["BaseBoolInt"]
    request: typing.Optional["BaseBoolInt"]


class GroupsSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["GroupsGroup"]]


class LeadFormsCreateResponse(pydantic.BaseModel):
    response: "LeadFormsCreateResponseModel" = pydantic.Field(..., description="")


class LeadFormsDeleteResponse(pydantic.BaseModel):
    response: "LeadFormsDeleteResponseModel" = pydantic.Field(..., description="")


class LeadFormsGetLeadsResponse(pydantic.BaseModel):
    response: "LeadFormsGetLeadsResponseModel" = pydantic.Field(..., description="")


class LeadFormsGetResponse(pydantic.BaseModel):
    response: LeadFormsForm = pydantic.Field(..., description="")


class LeadFormsListResponse(pydantic.BaseModel):
    response: typing.List["LeadFormsForm"] = pydantic.Field(..., description="")


class LeadFormsUploadUrlResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="")


class LeadFormsCreateResponseModel(pydantic.BaseModel):
    form_id: typing.Optional[int]
    url: typing.Optional[str]


class LeadFormsDeleteResponseModel(pydantic.BaseModel):
    form_id: typing.Optional[int]


class LeadFormsGetLeadsResponseModel(pydantic.BaseModel):
    leads: typing.Optional[typing.List["LeadFormsLead"]]
    next_page_token: typing.Optional[str]


class LikesAddResponse(pydantic.BaseModel):
    response: "LikesAddResponseModel" = pydantic.Field(..., description="")


class LikesDeleteResponse(pydantic.BaseModel):
    response: "LikesDeleteResponseModel" = pydantic.Field(..., description="")


class LikesGetListExtendedResponse(pydantic.BaseModel):
    response: "LikesGetListExtendedResponseModel" = pydantic.Field(..., description="")


class LikesGetListResponse(pydantic.BaseModel):
    response: "LikesGetListResponseModel" = pydantic.Field(..., description="")


class LikesIsLikedResponse(pydantic.BaseModel):
    response: "LikesIsLikedResponseModel" = pydantic.Field(..., description="")


class LikesAddResponseModel(pydantic.BaseModel):
    likes: typing.Optional[int]


class LikesDeleteResponseModel(pydantic.BaseModel):
    likes: typing.Optional[int]


class LikesGetListExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserMin"]]


class LikesGetListResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class LikesIsLikedResponseModel(pydantic.BaseModel):
    liked: typing.Optional["BaseBoolInt"]
    copied: typing.Optional["BaseBoolInt"]


class MarketAddAlbumResponse(pydantic.BaseModel):
    response: "MarketAddAlbumResponseModel" = pydantic.Field(..., description="")


class MarketAddResponse(pydantic.BaseModel):
    response: "MarketAddResponseModel" = pydantic.Field(..., description="")


class MarketCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Comment ID")


class MarketDeleteCommentResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully (0 if the comment is not found)",
    )


class MarketGetAlbumByIdResponse(pydantic.BaseModel):
    response: "MarketGetAlbumByIdResponseModel" = pydantic.Field(..., description="")


class MarketGetAlbumsResponse(pydantic.BaseModel):
    response: "MarketGetAlbumsResponseModel" = pydantic.Field(..., description="")


class MarketGetByIdExtendedResponse(pydantic.BaseModel):
    response: "MarketGetByIdExtendedResponseModel" = pydantic.Field(..., description="")


class MarketGetByIdResponse(pydantic.BaseModel):
    response: "MarketGetByIdResponseModel" = pydantic.Field(..., description="")


class MarketGetCategoriesNewResponse(pydantic.BaseModel):
    response: "MarketGetCategoriesNewResponseModel" = pydantic.Field(
        ..., description=""
    )


class MarketGetCategoriesResponse(pydantic.BaseModel):
    response: "MarketGetCategoriesResponseModel" = pydantic.Field(..., description="")


class MarketGetCommentsResponse(pydantic.BaseModel):
    response: "MarketGetCommentsResponseModel" = pydantic.Field(..., description="")


class MarketGetGroupOrdersResponse(pydantic.BaseModel):
    response: "MarketGetGroupOrdersResponseModel" = pydantic.Field(..., description="")


class MarketGetOrderByIdResponse(pydantic.BaseModel):
    response: "MarketGetOrderByIdResponseModel" = pydantic.Field(..., description="")


class MarketGetOrderItemsResponse(pydantic.BaseModel):
    response: "MarketGetOrderItemsResponseModel" = pydantic.Field(..., description="")


class MarketGetOrdersExtendedResponse(pydantic.BaseModel):
    response: "MarketGetOrdersExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MarketGetOrdersResponse(pydantic.BaseModel):
    response: "MarketGetOrdersResponseModel" = pydantic.Field(..., description="")


class MarketGetExtendedResponse(pydantic.BaseModel):
    response: "MarketGetExtendedResponseModel" = pydantic.Field(..., description="")


class MarketGetResponse(pydantic.BaseModel):
    response: "MarketGetResponseModel" = pydantic.Field(..., description="")


class MarketRestoreCommentResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully (0 if the comment is not found)",
    )


class MarketSearchExtendedResponse(pydantic.BaseModel):
    response: "MarketSearchExtendedResponseModel" = pydantic.Field(..., description="")


class MarketSearchResponse(pydantic.BaseModel):
    response: "MarketSearchResponseModel" = pydantic.Field(..., description="")


class MarketAddAlbumResponseModel(pydantic.BaseModel):
    market_album_id: typing.Optional[int]
    albums_count: typing.Optional[int]


class MarketAddResponseModel(pydantic.BaseModel):
    market_item_id: typing.Optional[int]


class MarketGetAlbumByIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketAlbum"]]


class MarketGetAlbumsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketAlbum"]]


class MarketGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketItemFull"]]


class MarketGetByIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketItem"]]


class MarketGetCategoriesNewResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["MarketMarketCategoryTree"]]


class MarketGetCategoriesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketCategory"]]


class MarketGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]


class MarketGetGroupOrdersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketOrder"]]


class MarketGetOrderByIdResponseModel(pydantic.BaseModel):
    order: typing.Optional["MarketOrder"]


class MarketGetOrderItemsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketOrderItem"]]


class MarketGetOrdersExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketOrder"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MarketGetOrdersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketOrder"]]


class MarketGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketItemFull"]]
    variants: typing.Optional[typing.List["MarketMarketItemFull"]]


class MarketGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MarketMarketItem"]]
    variants: typing.Optional[typing.List["MarketMarketItem"]]


class MarketSearchExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    view_type: typing.Optional["MarketServicesViewType"]
    items: typing.Optional[typing.List["MarketMarketItemFull"]]
    variants: typing.Optional[typing.List["MarketMarketItemFull"]]


class MarketSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    view_type: typing.Optional["MarketServicesViewType"]
    items: typing.Optional[typing.List["MarketMarketItem"]]
    variants: typing.Optional[typing.List["MarketMarketItem"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesCreateChatResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Chat ID")


class MessagesDeleteChatPhotoResponse(pydantic.BaseModel):
    response: "MessagesDeleteChatPhotoResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesDeleteConversationResponse(pydantic.BaseModel):
    response: "MessagesDeleteConversationResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesDeleteResponse(pydantic.BaseModel):
    response: typing.Dict[str, int] = pydantic.Field(..., description="")


class MessagesEditResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class MessagesGetByConversationMessageIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetByConversationMessageIdExtendedResponseModel" = (
        pydantic.Field(..., description="")
    )


class MessagesGetByConversationMessageIdResponse(pydantic.BaseModel):
    response: "MessagesGetByConversationMessageIdResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetByIdResponse(pydantic.BaseModel):
    response: "MessagesGetByIdResponseModel" = pydantic.Field(..., description="")


class MessagesGetChatPreviewResponse(pydantic.BaseModel):
    response: "MessagesGetChatPreviewResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetChatChatIdsFieldsResponse(pydantic.BaseModel):
    response: typing.List["MessagesChatFull"] = pydantic.Field(..., description="")


class MessagesGetChatChatIdsResponse(pydantic.BaseModel):
    response: typing.List["MessagesChat"] = pydantic.Field(..., description="")


class MessagesGetChatFieldsResponse(pydantic.BaseModel):
    response: MessagesChatFull = pydantic.Field(..., description="")


class MessagesGetChatResponse(pydantic.BaseModel):
    response: MessagesChat = pydantic.Field(..., description="")


class MessagesGetConversationMembersResponse(pydantic.BaseModel):
    response: MessagesGetConversationMembers = pydantic.Field(..., description="")


class MessagesGetConversationsByIdExtendedResponse(pydantic.BaseModel):
    response: MessagesGetConversationByIdExtended = pydantic.Field(..., description="")


class MessagesGetConversationsByIdResponse(pydantic.BaseModel):
    response: MessagesGetConversationById = pydantic.Field(..., description="")


class MessagesGetConversationsResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetHistoryAttachmentsResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryAttachmentsResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetHistoryExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetHistoryResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryResponseModel" = pydantic.Field(..., description="")


class MessagesGetImportantMessagesExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetImportantMessagesExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetImportantMessagesResponse(pydantic.BaseModel):
    response: "MessagesGetImportantMessagesResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetIntentUsersResponse(pydantic.BaseModel):
    response: "MessagesGetIntentUsersResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesGetInviteLinkResponseModel" = pydantic.Field(..., description="")


class MessagesGetLastActivityResponse(pydantic.BaseModel):
    response: MessagesLastActivity = pydantic.Field(..., description="")


class MessagesGetLongPollHistoryResponse(pydantic.BaseModel):
    response: "MessagesGetLongPollHistoryResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesGetLongPollServerResponse(pydantic.BaseModel):
    response: MessagesLongpollParams = pydantic.Field(..., description="")


class MessagesIsMessagesFromGroupAllowedResponse(pydantic.BaseModel):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesJoinChatByInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesJoinChatByInviteLinkResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesMarkAsImportantResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class MessagesPinResponse(pydantic.BaseModel):
    response: MessagesPinnedMessage = pydantic.Field(..., description="")


class MessagesSearchConversationsExtendedResponse(pydantic.BaseModel):
    response: "MessagesSearchConversationsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesSearchConversationsResponse(pydantic.BaseModel):
    response: "MessagesSearchConversationsResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesSearchExtendedResponse(pydantic.BaseModel):
    response: "MessagesSearchExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class MessagesSearchResponse(pydantic.BaseModel):
    response: "MessagesSearchResponseModel" = pydantic.Field(..., description="")


class MessagesSendResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Message ID")


class MessagesSendUserIdsResponse(pydantic.BaseModel):
    response: typing.List["MessagesSendUserIdsResponseItem"] = pydantic.Field(
        ..., description=""
    )


class MessagesSetChatPhotoResponse(pydantic.BaseModel):
    response: "MessagesSetChatPhotoResponseModel" = pydantic.Field(..., description="")


class MessagesDeleteChatPhotoResponseModel(pydantic.BaseModel):
    message_id: typing.Optional[int]
    chat: typing.Optional["MessagesChat"]


class MessagesDeleteConversationResponseModel(pydantic.BaseModel):
    last_deleted_id: typing.Optional[int]


class MessagesGetByConversationMessageIdExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesGetByConversationMessageIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]


class MessagesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesGetByIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]


class MessagesGetChatPreviewResponseModel(pydantic.BaseModel):
    preview: typing.Optional["MessagesChatPreview"]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesGetConversationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    unread_count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesConversationWithMessage"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesGetHistoryAttachmentsResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["MessagesHistoryAttachment"]]
    next_from: typing.Optional[str]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesGetHistoryExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    conversations: typing.Optional[typing.List["MessagesConversation"]]


class MessagesGetHistoryResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]


class MessagesGetImportantMessagesExtendedResponseModel(pydantic.BaseModel):
    messages: typing.Optional["MessagesMessagesArray"]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    conversations: typing.Optional[typing.List["MessagesConversation"]]


class MessagesGetImportantMessagesResponseModel(pydantic.BaseModel):
    messages: typing.Optional["MessagesMessagesArray"]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    conversations: typing.Optional[typing.List["MessagesConversation"]]


class MessagesGetIntentUsersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]


class MessagesGetInviteLinkResponseModel(pydantic.BaseModel):
    link: typing.Optional[str]


class MessagesGetLongPollHistoryResponseModel(pydantic.BaseModel):
    history: typing.Optional[typing.List["list"]]
    messages: typing.Optional["MessagesLongpollMessages"]
    credentials: typing.Optional["MessagesLongpollParams"]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    chats: typing.Optional[typing.List["MessagesChat"]]
    new_pts: typing.Optional[int]
    from_pts: typing.Optional[int]
    more: typing.Optional[bool]
    conversations: typing.Optional[typing.List["MessagesConversation"]]


class MessagesIsMessagesFromGroupAllowedResponseModel(pydantic.BaseModel):
    is_allowed: typing.Optional["BaseBoolInt"]


class MessagesJoinChatByInviteLinkResponseModel(pydantic.BaseModel):
    chat_id: typing.Optional[int]


class MessagesSearchConversationsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesConversation"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class MessagesSearchConversationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesConversation"]]


class MessagesSearchExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    conversations: typing.Optional[typing.List["MessagesConversation"]]


class MessagesSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["MessagesMessage"]]


class MessagesSetChatPhotoResponseModel(pydantic.BaseModel):
    message_id: typing.Optional[int]
    chat: typing.Optional["MessagesChat"]


class NewsfeedGenericResponse(pydantic.BaseModel):
    response: "NewsfeedGenericResponseModel" = pydantic.Field(..., description="")


class NewsfeedGetBannedExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class NewsfeedGetBannedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedResponseModel" = pydantic.Field(..., description="")


class NewsfeedGetCommentsResponse(pydantic.BaseModel):
    response: "NewsfeedGetCommentsResponseModel" = pydantic.Field(..., description="")


class NewsfeedGetListsExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class NewsfeedGetListsResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsResponseModel" = pydantic.Field(..., description="")


class NewsfeedGetMentionsResponse(pydantic.BaseModel):
    response: "NewsfeedGetMentionsResponseModel" = pydantic.Field(..., description="")


class NewsfeedGetSuggestedSourcesResponse(pydantic.BaseModel):
    response: "NewsfeedGetSuggestedSourcesResponseModel" = pydantic.Field(
        ..., description=""
    )


class NewsfeedIgnoreItemResponse(pydantic.BaseModel):
    response: "NewsfeedIgnoreItemResponseModel" = pydantic.Field(..., description="")


class NewsfeedSaveListResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="List ID")


class NewsfeedSearchExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedSearchExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class NewsfeedSearchResponse(pydantic.BaseModel):
    response: "NewsfeedSearchResponseModel" = pydantic.Field(..., description="")


class NewsfeedGenericResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    new_returned_news_items_count: typing.Optional[int]


class NewsfeedGetBannedExtendedResponseModel(pydantic.BaseModel):
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class NewsfeedGetBannedResponseModel(pydantic.BaseModel):
    groups: typing.Optional[typing.List[int]]
    members: typing.Optional[typing.List[int]]


class NewsfeedGetCommentsResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    next_from: typing.Optional[str]


class NewsfeedGetListsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["NewsfeedListFull"]]


class NewsfeedGetListsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["NewsfeedList"]]


class NewsfeedGetMentionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostToId"]]


class NewsfeedGetSuggestedSourcesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersSubscriptionsItem"]]


class NewsfeedIgnoreItemResponseModel(pydantic.BaseModel):
    status: typing.Optional[bool]


class NewsfeedSearchExtendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallpostFull"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]
    suggested_queries: typing.Optional[typing.List[str]]
    next_from: typing.Optional[str]
    count: typing.Optional[int]
    total_count: typing.Optional[int]


class NewsfeedSearchResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallpostFull"]]
    suggested_queries: typing.Optional[typing.List[str]]
    next_from: typing.Optional[str]
    count: typing.Optional[int]
    total_count: typing.Optional[int]


class NotesAddResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Note ID")


class NotesCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Comment ID")


class NotesGetByIdResponse(pydantic.BaseModel):
    response: NotesNote = pydantic.Field(..., description="")


class NotesGetCommentsResponse(pydantic.BaseModel):
    response: "NotesGetCommentsResponseModel" = pydantic.Field(..., description="")


class NotesGetResponse(pydantic.BaseModel):
    response: "NotesGetResponseModel" = pydantic.Field(..., description="")


class NotesGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["NotesNoteComment"]]


class NotesGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["NotesNote"]]


class NotificationsGetResponse(pydantic.BaseModel):
    response: "NotificationsGetResponseModel" = pydantic.Field(..., description="")


class NotificationsMarkAsViewedResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class NotificationsSendMessageResponse(pydantic.BaseModel):
    response: typing.List["NotificationsSendMessageItem"] = pydantic.Field(
        ..., description=""
    )


class NotificationsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["NotificationsNotificationItem"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]
    last_viewed: typing.Optional[int]
    photos: typing.Optional[typing.List["PhotosPhoto"]]
    videos: typing.Optional[typing.List["VideoVideo"]]
    apps: typing.Optional[typing.List["AppsApp"]]
    next_from: typing.Optional[str]
    ttl: typing.Optional[int]


class OrdersCancelSubscriptionResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class OrdersChangeStateResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="New state")


class OrdersGetAmountResponse(pydantic.BaseModel):
    response: typing.List["OrdersAmount"] = pydantic.Field(..., description="")


class OrdersGetByIdResponse(pydantic.BaseModel):
    response: typing.List["OrdersOrder"] = pydantic.Field(..., description="")


class OrdersGetUserSubscriptionByIdResponse(pydantic.BaseModel):
    response: OrdersSubscription = pydantic.Field(..., description="")


class OrdersGetUserSubscriptionsResponse(pydantic.BaseModel):
    response: "OrdersGetUserSubscriptionsResponseModel" = pydantic.Field(
        ..., description=""
    )


class OrdersGetResponse(pydantic.BaseModel):
    response: typing.List["OrdersOrder"] = pydantic.Field(..., description="")


class OrdersUpdateSubscriptionResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class OrdersGetUserSubscriptionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["OrdersSubscription"]]


class PagesGetHistoryResponse(pydantic.BaseModel):
    response: typing.List["PagesWikipageHistory"] = pydantic.Field(..., description="")


class PagesGetTitlesResponse(pydantic.BaseModel):
    response: typing.List["PagesWikipage"] = pydantic.Field(..., description="")


class PagesGetVersionResponse(pydantic.BaseModel):
    response: PagesWikipageFull = pydantic.Field(..., description="")


class PagesGetResponse(pydantic.BaseModel):
    response: PagesWikipageFull = pydantic.Field(..., description="")


class PagesParseWikiResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="HTML source")


class PagesSaveAccessResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Page ID")


class PagesSaveResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Page ID")


class PhotosCopyResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Photo ID")


class PhotosCreateAlbumResponse(pydantic.BaseModel):
    response: PhotosPhotoAlbumFull = pydantic.Field(..., description="")


class PhotosCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Created comment ID")


class PhotosDeleteCommentResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosGetAlbumsCountResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Albums number")


class PhotosGetAlbumsResponse(pydantic.BaseModel):
    response: "PhotosGetAlbumsResponseModel" = pydantic.Field(..., description="")


class PhotosGetAllCommentsResponse(pydantic.BaseModel):
    response: "PhotosGetAllCommentsResponseModel" = pydantic.Field(..., description="")


class PhotosGetAllExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetAllExtendedResponseModel" = pydantic.Field(..., description="")


class PhotosGetAllResponse(pydantic.BaseModel):
    response: "PhotosGetAllResponseModel" = pydantic.Field(..., description="")


class PhotosGetByIdResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class PhotosGetCommentsResponse(pydantic.BaseModel):
    response: "PhotosGetCommentsResponseModel" = pydantic.Field(..., description="")


class PhotosGetMarketUploadServerResponse(pydantic.BaseModel):
    response: BaseUploadServer = pydantic.Field(..., description="")


class PhotosGetMessagesUploadServerResponse(pydantic.BaseModel):
    response: PhotosPhotoUpload = pydantic.Field(..., description="")


class PhotosGetNewTagsResponse(pydantic.BaseModel):
    response: "PhotosGetNewTagsResponseModel" = pydantic.Field(..., description="")


class PhotosGetTagsResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhotoTag"] = pydantic.Field(..., description="")


class PhotosGetUploadServerResponse(pydantic.BaseModel):
    response: PhotosPhotoUpload = pydantic.Field(..., description="")


class PhotosGetUserPhotosResponse(pydantic.BaseModel):
    response: "PhotosGetUserPhotosResponseModel" = pydantic.Field(..., description="")


class PhotosGetWallUploadServerResponse(pydantic.BaseModel):
    response: PhotosPhotoUpload = pydantic.Field(..., description="")


class PhotosGetResponse(pydantic.BaseModel):
    response: "PhotosGetResponseModel" = pydantic.Field(..., description="")


class PhotosMarketAlbumUploadResponse(pydantic.BaseModel):
    response: "PhotosMarketAlbumUploadResponseModel" = pydantic.Field(
        ..., description=""
    )


class PhotosMarketUploadResponse(pydantic.BaseModel):
    response: "PhotosMarketUploadResponseModel" = pydantic.Field(..., description="")


class PhotosMessageUploadResponse(pydantic.BaseModel):
    response: "PhotosMessageUploadResponseModel" = pydantic.Field(..., description="")


class PhotosOwnerCoverUploadResponse(pydantic.BaseModel):
    response: "PhotosOwnerCoverUploadResponseModel" = pydantic.Field(
        ..., description=""
    )


class PhotosOwnerUploadResponse(pydantic.BaseModel):
    response: "PhotosOwnerUploadResponseModel" = pydantic.Field(..., description="")


class PhotosPhotoUploadResponse(pydantic.BaseModel):
    response: "PhotosPhotoUploadResponseModel" = pydantic.Field(..., description="")


class PhotosPutTagResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Created tag ID")


class PhotosRestoreCommentResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosSaveMarketAlbumPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosSaveMarketPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosSaveMessagesPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosSaveOwnerCoverPhotoResponse(pydantic.BaseModel):
    response: "PhotosSaveOwnerCoverPhotoResponseModel" = pydantic.Field(
        ..., description=""
    )


class PhotosSaveOwnerPhotoResponse(pydantic.BaseModel):
    response: "PhotosSaveOwnerPhotoResponseModel" = pydantic.Field(..., description="")


class PhotosSaveWallPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosSaveResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(..., description="")


class PhotosSearchResponse(pydantic.BaseModel):
    response: "PhotosSearchResponseModel" = pydantic.Field(..., description="")


class PhotosWallUploadResponse(pydantic.BaseModel):
    response: "PhotosWallUploadResponseModel" = pydantic.Field(..., description="")


class PhotosGetAlbumsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhotoAlbumFull"]]


class PhotosGetAllCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]


class PhotosGetAllExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhotoFullXtrRealOffset"]]
    more: typing.Optional["BaseBoolInt"]


class PhotosGetAllResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhotoXtrRealOffset"]]
    more: typing.Optional["BaseBoolInt"]


class PhotosGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    real_offset: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class PhotosGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    real_offset: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]


class PhotosGetNewTagsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhotoXtrTagInfo"]]


class PhotosGetUserPhotosResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhoto"]]


class PhotosGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhoto"]]


class PhotosMarketAlbumUploadResponseModel(pydantic.BaseModel):
    gid: typing.Optional[int]
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    server: typing.Optional[int]


class PhotosMarketUploadResponseModel(pydantic.BaseModel):
    crop_data: typing.Optional[str]
    crop_hash: typing.Optional[str]
    group_id: typing.Optional[int]
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    server: typing.Optional[int]


class PhotosMessageUploadResponseModel(pydantic.BaseModel):
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    server: typing.Optional[int]


class PhotosOwnerCoverUploadResponseModel(pydantic.BaseModel):
    hash: typing.Optional[str]
    photo: typing.Optional[str]


class PhotosOwnerUploadResponseModel(pydantic.BaseModel):
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    server: typing.Optional[int]


class PhotosPhotoUploadResponseModel(pydantic.BaseModel):
    aid: typing.Optional[int]
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    photos_list: typing.Optional[str]
    server: typing.Optional[int]


class PhotosSaveOwnerCoverPhotoResponseModel(pydantic.BaseModel):
    images: typing.Optional[typing.List["BaseImage"]]


class PhotosSaveOwnerPhotoResponseModel(pydantic.BaseModel):
    photo_hash: typing.Optional[str]
    photo_src: typing.Optional[str]
    photo_src_big: typing.Optional[str]
    photo_src_small: typing.Optional[str]
    saved: typing.Optional[int]
    post_id: typing.Optional[int]


class PhotosSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PhotosPhoto"]]


class PhotosWallUploadResponseModel(pydantic.BaseModel):
    hash: typing.Optional[str]
    photo: typing.Optional[str]
    server: typing.Optional[int]


class PodcastsSearchPodcastResponse(pydantic.BaseModel):
    response: "PodcastsSearchPodcastResponseModel" = pydantic.Field(..., description="")


class PodcastsSearchPodcastResponseModel(pydantic.BaseModel):
    podcasts: typing.Optional[typing.List["PodcastExternalData"]]
    results_total: typing.Optional[int]


class PollsAddVoteResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class PollsCreateResponse(pydantic.BaseModel):
    response: PollsPoll = pydantic.Field(..., description="")


class PollsDeleteVoteResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(..., description="Result")


class PollsGetBackgroundsResponse(pydantic.BaseModel):
    response: typing.List["PollsBackground"] = pydantic.Field(..., description="")


class PollsGetByIdResponse(pydantic.BaseModel):
    response: PollsPoll = pydantic.Field(..., description="")


class PollsGetVotersResponse(pydantic.BaseModel):
    response: typing.List["PollsVoters"] = pydantic.Field(..., description="")


class PollsSavePhotoResponse(pydantic.BaseModel):
    response: PollsBackground = pydantic.Field(..., description="")


class PrettyCardsCreateResponse(pydantic.BaseModel):
    response: "PrettyCardsCreateResponseModel" = pydantic.Field(..., description="")


class PrettyCardsDeleteResponse(pydantic.BaseModel):
    response: "PrettyCardsDeleteResponseModel" = pydantic.Field(..., description="")


class PrettyCardsEditResponse(pydantic.BaseModel):
    response: "PrettyCardsEditResponseModel" = pydantic.Field(..., description="")


class PrettyCardsGetByIdResponse(pydantic.BaseModel):
    response: typing.List["PrettyCardsPrettyCardOrError"] = pydantic.Field(
        ..., description=""
    )


class PrettyCardsGetUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(..., description="Upload URL")


class PrettyCardsGetResponse(pydantic.BaseModel):
    response: "PrettyCardsGetResponseModel" = pydantic.Field(..., description="")


class PrettyCardsCreateResponseModel(pydantic.BaseModel):
    owner_id: typing.Optional[int]
    card_id: typing.Optional[str]


class PrettyCardsDeleteResponseModel(pydantic.BaseModel):
    owner_id: typing.Optional[int]
    card_id: typing.Optional[str]
    error: typing.Optional[str]


class PrettyCardsEditResponseModel(pydantic.BaseModel):
    owner_id: typing.Optional[int]
    card_id: typing.Optional[str]


class PrettyCardsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["PrettyCardsPrettyCard"]]


class SearchGetHintsResponse(pydantic.BaseModel):
    response: "SearchGetHintsResponseModel" = pydantic.Field(..., description="")


class SearchGetHintsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["SearchHint"]]
    suggested_queries: typing.Optional[typing.List[str]]


class SecureCheckTokenResponse(pydantic.BaseModel):
    response: SecureTokenChecked = pydantic.Field(..., description="")


class SecureGetAppBalanceResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="App balance")


class SecureGetSMSHistoryResponse(pydantic.BaseModel):
    response: typing.List["SecureSmsNotification"] = pydantic.Field(..., description="")


class SecureGetTransactionsHistoryResponse(pydantic.BaseModel):
    response: typing.List["SecureTransaction"] = pydantic.Field(..., description="")


class SecureGetUserLevelResponse(pydantic.BaseModel):
    response: typing.List["SecureLevel"] = pydantic.Field(..., description="")


class SecureGiveEventStickerResponse(pydantic.BaseModel):
    response: typing.List["SecureGiveEventStickerItem"] = pydantic.Field(
        ..., description=""
    )


class SecureSendNotificationResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class SecureSetCounterArrayResponse(pydantic.BaseModel):
    response: typing.List["SecureSetCounterItem"] = pydantic.Field(..., description="")


class StatsGetPostReachResponse(pydantic.BaseModel):
    response: typing.List["StatsWallpostStat"] = pydantic.Field(..., description="")


class StatsGetResponse(pydantic.BaseModel):
    response: typing.List["StatsPeriod"] = pydantic.Field(..., description="")


class StatusGetResponse(pydantic.BaseModel):
    response: StatusStatus = pydantic.Field(..., description="")


class StorageGetKeysResponse(pydantic.BaseModel):
    response: typing.List[str] = pydantic.Field(..., description="")


class StorageGetResponse(pydantic.BaseModel):
    response: typing.List["StorageValue"] = pydantic.Field(..., description="")


class StoreGetFavoriteStickersResponse(pydantic.BaseModel):
    response: typing.List["BaseSticker"] = pydantic.Field(..., description="")


class StoreGetProductsResponse(pydantic.BaseModel):
    response: typing.List["StoreProduct"] = pydantic.Field(..., description="")


class StoreGetStickersKeywordsResponse(pydantic.BaseModel):
    response: "StoreGetStickersKeywordsResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoreGetStickersKeywordsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    dictionary: typing.Optional[typing.List["StoreStickersKeyword"]]
    chunks_count: typing.Optional[int]
    chunks_hash: typing.Optional[str]


class StoriesGetBannedExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetBannedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedResponseModel" = pydantic.Field(..., description="")


class StoriesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetPhotoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetPhotoUploadServerResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetStatsResponse(pydantic.BaseModel):
    response: StoriesStoryStats = pydantic.Field(..., description="")


class StoriesGetVideoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetVideoUploadServerResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetViewersExtendedV5115Response(pydantic.BaseModel):
    response: "StoriesGetViewersExtendedV5115ResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetViewersExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetViewersExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class StoriesGetV5113Response(pydantic.BaseModel):
    response: "StoriesGetV5113ResponseModel" = pydantic.Field(..., description="")


class StoriesGetResponse(pydantic.BaseModel):
    response: "StoriesGetResponseModel" = pydantic.Field(..., description="")


class StoriesSaveResponse(pydantic.BaseModel):
    response: "StoriesSaveResponseModel" = pydantic.Field(..., description="")


class StoriesUploadResponse(pydantic.BaseModel):
    response: "StoriesUploadResponseModel" = pydantic.Field(..., description="")


class StoriesGetBannedExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class StoriesGetBannedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class StoriesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["StoriesStory"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class StoriesGetPhotoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: typing.Optional[str]
    user_ids: typing.Optional[typing.List[int]]


class StoriesGetVideoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: typing.Optional[str]
    user_ids: typing.Optional[typing.List[int]]


class StoriesGetViewersExtendedV5115ResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["StoriesViewersItem"]]
    hidden_reason: typing.Optional[str]
    next_from: typing.Optional[str]


class StoriesGetViewersExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class StoriesGetV5113ResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["StoriesFeedItem"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]
    need_upload_screen: typing.Optional[bool]
    next_from: typing.Optional[str]


class StoriesGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["list"]]
    promo_data: typing.Optional["StoriesPromoBlock"]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]
    need_upload_screen: typing.Optional[bool]


class StoriesSaveResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["StoriesStory"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]


class StoriesUploadResponseModel(pydantic.BaseModel):
    upload_result: typing.Optional[str]


class StreamingGetServerUrlResponse(pydantic.BaseModel):
    response: "StreamingGetServerUrlResponseModel" = pydantic.Field(..., description="")


class StreamingGetServerUrlResponseModel(pydantic.BaseModel):
    endpoint: typing.Optional[str]
    key: typing.Optional[str]


class UsersGetFollowersFieldsResponse(pydantic.BaseModel):
    response: "UsersGetFollowersFieldsResponseModel" = pydantic.Field(
        ..., description=""
    )


class UsersGetFollowersResponse(pydantic.BaseModel):
    response: "UsersGetFollowersResponseModel" = pydantic.Field(..., description="")


class UsersGetSubscriptionsExtendedResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class UsersGetSubscriptionsResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsResponseModel" = pydantic.Field(..., description="")


class UsersGetResponse(pydantic.BaseModel):
    response: typing.List["UsersUserFull"] = pydantic.Field(..., description="")


class UsersSearchResponse(pydantic.BaseModel):
    response: "UsersSearchResponseModel" = pydantic.Field(..., description="")


class UsersGetFollowersFieldsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class UsersGetFollowersResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List[int]]


class UsersGetSubscriptionsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersSubscriptionsItem"]]


class UsersGetSubscriptionsResponseModel(pydantic.BaseModel):
    users: typing.Optional["UsersUsersArray"]
    groups: typing.Optional["GroupsGroupsArray"]


class UsersSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UsersUserFull"]]


class UtilsCheckLinkResponse(pydantic.BaseModel):
    response: UtilsLinkChecked = pydantic.Field(..., description="")


class UtilsGetLastShortenedLinksResponse(pydantic.BaseModel):
    response: "UtilsGetLastShortenedLinksResponseModel" = pydantic.Field(
        ..., description=""
    )


class UtilsGetLinkStatsExtendedResponse(pydantic.BaseModel):
    response: UtilsLinkStatsExtended = pydantic.Field(..., description="")


class UtilsGetLinkStatsResponse(pydantic.BaseModel):
    response: UtilsLinkStats = pydantic.Field(..., description="")


class UtilsGetServerTimeResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Time as Unixtime")


class UtilsGetShortLinkResponse(pydantic.BaseModel):
    response: UtilsShortLink = pydantic.Field(..., description="")


class UtilsResolveScreenNameResponse(pydantic.BaseModel):
    response: UtilsDomainResolved = pydantic.Field(..., description="")


class UtilsGetLastShortenedLinksResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["UtilsLastShortenedLink"]]


class VideoAddAlbumResponse(pydantic.BaseModel):
    response: "VideoAddAlbumResponseModel" = pydantic.Field(..., description="")


class VideoChangeVideoAlbumsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class VideoCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(..., description="Created comment ID")


class VideoGetAlbumByIdResponse(pydantic.BaseModel):
    response: VideoVideoAlbumFull = pydantic.Field(..., description="")


class VideoGetAlbumsByVideoExtendedResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsByVideoExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class VideoGetAlbumsByVideoResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(..., description="")


class VideoGetAlbumsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class VideoGetAlbumsResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsResponseModel" = pydantic.Field(..., description="")


class VideoGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class VideoGetCommentsResponse(pydantic.BaseModel):
    response: "VideoGetCommentsResponseModel" = pydantic.Field(..., description="")


class VideoGetResponse(pydantic.BaseModel):
    response: "VideoGetResponseModel" = pydantic.Field(..., description="")


class VideoRestoreCommentResponse(pydantic.BaseModel):
    response: BaseBoolInt = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class VideoSaveResponse(pydantic.BaseModel):
    response: VideoSaveResult = pydantic.Field(..., description="")


class VideoSearchExtendedResponse(pydantic.BaseModel):
    response: "VideoSearchExtendedResponseModel" = pydantic.Field(..., description="")


class VideoSearchResponse(pydantic.BaseModel):
    response: "VideoSearchResponseModel" = pydantic.Field(..., description="")


class VideoUploadResponse(pydantic.BaseModel):
    response: "VideoUploadResponseModel" = pydantic.Field(..., description="")


class VideoAddAlbumResponseModel(pydantic.BaseModel):
    album_id: typing.Optional[int]


class VideoGetAlbumsByVideoExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]]


class VideoGetAlbumsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]]


class VideoGetAlbumsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoAlbum"]]


class VideoGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]
    current_level_count: typing.Optional[int]
    can_post: typing.Optional[bool]
    show_reply_button: typing.Optional[bool]
    groups_can_post: typing.Optional[bool]
    real_offset: typing.Optional[int]


class VideoGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]
    current_level_count: typing.Optional[int]
    can_post: typing.Optional[bool]
    show_reply_button: typing.Optional[bool]
    groups_can_post: typing.Optional[bool]
    real_offset: typing.Optional[int]


class VideoGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoFull"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class VideoSearchExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoFull"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class VideoSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["VideoVideoFull"]]


class VideoUploadResponseModel(pydantic.BaseModel):
    size: typing.Optional[int]
    video_id: typing.Optional[int]


class WallCreateCommentResponse(pydantic.BaseModel):
    response: "WallCreateCommentResponseModel" = pydantic.Field(..., description="")


class WallEditResponse(pydantic.BaseModel):
    response: "WallEditResponseModel" = pydantic.Field(..., description="")


class WallGetByIdExtendedResponse(pydantic.BaseModel):
    response: "WallGetByIdExtendedResponseModel" = pydantic.Field(..., description="")


class WallGetByIdLegacyResponse(pydantic.BaseModel):
    response: typing.List["WallWallpostFull"] = pydantic.Field(..., description="")


class WallGetByIdResponse(pydantic.BaseModel):
    response: "WallGetByIdResponseModel" = pydantic.Field(..., description="")


class WallGetCommentExtendedResponse(pydantic.BaseModel):
    response: "WallGetCommentExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class WallGetCommentResponse(pydantic.BaseModel):
    response: "WallGetCommentResponseModel" = pydantic.Field(..., description="")


class WallGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "WallGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description=""
    )


class WallGetCommentsResponse(pydantic.BaseModel):
    response: "WallGetCommentsResponseModel" = pydantic.Field(..., description="")


class WallGetRepostsResponse(pydantic.BaseModel):
    response: "WallGetRepostsResponseModel" = pydantic.Field(..., description="")


class WallGetExtendedResponse(pydantic.BaseModel):
    response: "WallGetExtendedResponseModel" = pydantic.Field(..., description="")


class WallGetResponse(pydantic.BaseModel):
    response: "WallGetResponseModel" = pydantic.Field(..., description="")


class WallPostAdsStealthResponse(pydantic.BaseModel):
    response: "WallPostAdsStealthResponseModel" = pydantic.Field(..., description="")


class WallPostResponse(pydantic.BaseModel):
    response: "WallPostResponseModel" = pydantic.Field(..., description="")


class WallRepostResponse(pydantic.BaseModel):
    response: "WallRepostResponseModel" = pydantic.Field(..., description="")


class WallSearchExtendedResponse(pydantic.BaseModel):
    response: "WallSearchExtendedResponseModel" = pydantic.Field(..., description="")


class WallSearchResponse(pydantic.BaseModel):
    response: "WallSearchResponseModel" = pydantic.Field(..., description="")


class WallCreateCommentResponseModel(pydantic.BaseModel):
    comment_id: typing.Optional[int]


class WallEditResponseModel(pydantic.BaseModel):
    post_id: typing.Optional[int]


class WallGetByIdExtendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallpostFull"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class WallGetByIdResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallpostFull"]]


class WallGetCommentExtendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallComment"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]


class WallGetCommentResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallComment"]]


class WallGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]
    current_level_count: typing.Optional[int]
    can_post: typing.Optional[bool]
    show_reply_button: typing.Optional[bool]
    groups_can_post: typing.Optional[bool]


class WallGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallComment"]]
    current_level_count: typing.Optional[int]
    can_post: typing.Optional[bool]
    show_reply_button: typing.Optional[bool]
    groups_can_post: typing.Optional[bool]


class WallGetRepostsResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List["WallWallpostFull"]]
    profiles: typing.Optional[typing.List["UsersUser"]]
    groups: typing.Optional[typing.List["GroupsGroup"]]


class WallGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostFull"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class WallGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostFull"]]


class WallPostAdsStealthResponseModel(pydantic.BaseModel):
    post_id: typing.Optional[int]


class WallPostResponseModel(pydantic.BaseModel):
    post_id: typing.Optional[int]


class WallRepostResponseModel(pydantic.BaseModel):
    success: typing.Optional[int]
    post_id: typing.Optional[int]
    reposts_count: typing.Optional[int]
    wall_repost_count: typing.Optional[int]
    mail_repost_count: typing.Optional[int]
    likes_count: typing.Optional[int]


class WallSearchExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostFull"]]
    profiles: typing.Optional[typing.List["UsersUserFull"]]
    groups: typing.Optional[typing.List["GroupsGroupFull"]]


class WallSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    items: typing.Optional[typing.List["WallWallpostFull"]]


class WidgetsGetCommentsResponse(pydantic.BaseModel):
    response: "WidgetsGetCommentsResponseModel" = pydantic.Field(..., description="")


class WidgetsGetPagesResponse(pydantic.BaseModel):
    response: "WidgetsGetPagesResponseModel" = pydantic.Field(..., description="")


class WidgetsGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    posts: typing.Optional[typing.List["WidgetsWidgetComment"]]


class WidgetsGetPagesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int]
    pages: typing.Optional[typing.List["WidgetsWidgetPage"]]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseModel):
        item.update_forward_refs()
