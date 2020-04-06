from .objects import *


class AccountChangePasswordResponseModel(pydantic.BaseModel):
    token: str = pydantic.Field(
        ..., description="New token",
    )
    secret: typing.Optional[str] = pydantic.Field(
        None, description="New secret",
    )


class AccountChangePasswordResponse(pydantic.BaseModel):
    response: "AccountChangePasswordResponseModel" = pydantic.Field(
        ..., description="",
    )


class AccountGetActiveOffersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[AccountOffer] = pydantic.Field(
        ..., description="",
    )


class AccountGetActiveOffersResponse(pydantic.BaseModel):
    response: "AccountGetActiveOffersResponseModel" = pydantic.Field(
        ..., description="",
    )


class AccountGetAppPermissionsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Permissions mask",
    )


class AccountGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.Optional[typing.List[UsersUserMin]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroup]] = pydantic.Field(
        None, description="",
    )


class AccountGetBannedResponse(pydantic.BaseModel):
    response: "AccountGetBannedResponseModel" = pydantic.Field(
        ..., description="",
    )


class AccountGetCountersResponse(pydantic.BaseModel):
    response: "AccountAccountCounters" = pydantic.Field(
        ..., description="",
    )


class AccountGetInfoResponse(pydantic.BaseModel):
    response: "AccountInfo" = pydantic.Field(
        ..., description="",
    )


class AccountGetProfileInfoResponse(pydantic.BaseModel):
    response: "AccountUserSettings" = pydantic.Field(
        ..., description="",
    )


class AccountGetPushSettingsResponse(pydantic.BaseModel):
    response: "AccountPushSettings" = pydantic.Field(
        ..., description="",
    )


class AccountSaveProfileInfoResponseModel(pydantic.BaseModel):
    changed: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="1 if changes has been processed",
    )
    name_request: typing.Optional[AccountNameRequest] = pydantic.Field(
        None, description="",
    )


class AccountSaveProfileInfoResponse(pydantic.BaseModel):
    response: "AccountSaveProfileInfoResponseModel" = pydantic.Field(
        ..., description="",
    )


class AdsAddOfficeUsersResponse(pydantic.BaseModel):
    response: bool = pydantic.Field(
        ..., description="true if success",
    )


class AdsCheckLinkResponse(pydantic.BaseModel):
    response: "AdsLinkStatus" = pydantic.Field(
        ..., description="",
    )


class AdsCreateAdsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class AdsCreateCampaignsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class AdsCreateClientsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class AdsCreateTargetGroupResponseModel(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Group ID",
    )
    pixel: typing.Optional[str] = pydantic.Field(
        None, description="Pixel code",
    )


class AdsCreateTargetGroupResponse(pydantic.BaseModel):
    response: "AdsCreateTargetGroupResponseModel" = pydantic.Field(
        ..., description="",
    )


class AdsDeleteAdsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class AdsDeleteCampaignsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="0 if success",
    )


class AdsDeleteClientsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="0 if sucess",
    )


class AdsGetAccountsResponse(pydantic.BaseModel):
    response: typing.List["AdsAccount"] = pydantic.Field(
        ..., description="",
    )


class AdsGetAdsLayoutResponse(pydantic.BaseModel):
    response: typing.List["AdsAdLayout"] = pydantic.Field(
        ..., description="",
    )


class AdsGetAdsTargetingResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSettings"] = pydantic.Field(
        ..., description="",
    )


class AdsGetAdsResponse(pydantic.BaseModel):
    response: typing.List["AdsAd"] = pydantic.Field(
        ..., description="",
    )


class AdsGetBudgetResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Budget",
    )


class AdsGetCampaignsResponse(pydantic.BaseModel):
    response: typing.List["AdsCampaign"] = pydantic.Field(
        ..., description="",
    )


class AdsGetCategoriesResponseModel(pydantic.BaseModel):
    v1: typing.Optional[AdsCategory] = pydantic.Field(
        None, description="Old categories",
    )
    v2: typing.Optional[AdsCategory] = pydantic.Field(
        None, description="Actual categories",
    )


class AdsGetCategoriesResponse(pydantic.BaseModel):
    response: "AdsGetCategoriesResponseModel" = pydantic.Field(
        ..., description="",
    )


class AdsGetClientsResponse(pydantic.BaseModel):
    response: typing.List["AdsClient"] = pydantic.Field(
        ..., description="",
    )


class AdsGetDemographicsResponse(pydantic.BaseModel):
    response: typing.List["AdsDemoStats"] = pydantic.Field(
        ..., description="",
    )


class AdsGetFloodStatsResponse(pydantic.BaseModel):
    response: "AdsFloodStats" = pydantic.Field(
        ..., description="",
    )


class AdsGetOfficeUsersResponse(pydantic.BaseModel):
    response: typing.List["AdsUsers"] = pydantic.Field(
        ..., description="",
    )


class AdsGetPostsReachResponse(pydantic.BaseModel):
    response: typing.List["AdsPromotedPostReach"] = pydantic.Field(
        ..., description="",
    )


class AdsGetRejectionReasonResponse(pydantic.BaseModel):
    response: "AdsRejectReason" = pydantic.Field(
        ..., description="",
    )


class AdsGetStatisticsResponse(pydantic.BaseModel):
    response: typing.List["AdsStats"] = pydantic.Field(
        ..., description="",
    )


class AdsGetSuggestionsCitiesResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsCities"] = pydantic.Field(
        ..., description="",
    )


class AdsGetSuggestionsRegionsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsRegions"] = pydantic.Field(
        ..., description="",
    )


class AdsGetSuggestionsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestions"] = pydantic.Field(
        ..., description="",
    )


class AdsGetSuggestionsSchoolsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargSuggestionsSchools"] = pydantic.Field(
        ..., description="",
    )


class AdsGetTargetGroupsResponse(pydantic.BaseModel):
    response: typing.List["AdsTargetGroup"] = pydantic.Field(
        ..., description="",
    )


class AdsGetTargetingStatsResponse(pydantic.BaseModel):
    response: "AdsTargStats" = pydantic.Field(
        ..., description="",
    )


class AdsGetUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="Photo upload URL",
    )


class AdsGetVideoUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="Video upload URL",
    )


class AdsImportTargetContactsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Imported contacts number",
    )


class AdsRemoveOfficeUsersResponse(pydantic.BaseModel):
    response: bool = pydantic.Field(
        ..., description="true if success",
    )


class AdsUpdateAdsResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class AdsUpdateCampaignsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Campaign ID",
    )


class AdsUpdateClientsResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Client ID",
    )


class AppsGetCatalogResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[AppsApp]] = pydantic.Field(
        None, description="",
    )


class AppsGetCatalogResponse(pydantic.BaseModel):
    response: "AppsGetCatalogResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsGetFriendsListResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )


class AppsGetFriendsListResponse(pydantic.BaseModel):
    response: "AppsGetFriendsListResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsGetLeaderboardExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[AppsLeaderboard]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserMin]] = pydantic.Field(
        None, description="",
    )


class AppsGetLeaderboardExtendedResponse(pydantic.BaseModel):
    response: "AppsGetLeaderboardExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsGetLeaderboardResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[AppsLeaderboard]] = pydantic.Field(
        None, description="",
    )


class AppsGetLeaderboardResponse(pydantic.BaseModel):
    response: "AppsGetLeaderboardResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsGetScopesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[AppsScope] = pydantic.Field(
        ..., description="",
    )


class AppsGetScopesResponse(pydantic.BaseModel):
    response: "AppsGetScopesResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsGetScoreResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Score number",
    )


class AppsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[AppsApp]] = pydantic.Field(
        None, description="",
    )


class AppsGetResponse(pydantic.BaseModel):
    response: "AppsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class AppsSendRequestResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Request ID",
    )


class AuthRestoreResponseModel(pydantic.BaseModel):
    success: typing.Optional[int] = pydantic.Field(
        None, description="1 if success",
    )
    sid: typing.Optional[str] = pydantic.Field(
        None, description="Parameter needed to grant access by code",
    )


class AuthRestoreResponse(pydantic.BaseModel):
    response: "AuthRestoreResponseModel" = pydantic.Field(
        ..., description="",
    )


class BaseBoolResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="",
    )


class BaseGetUploadServerResponse(pydantic.BaseModel):
    response: "BaseUploadServer" = pydantic.Field(
        ..., description="",
    )


class BoardAddTopicResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Topic ID",
    )


class BoardCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Comment ID",
    )


class BoardGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[BoardTopicComment] = pydantic.Field(
        ..., description="",
    )
    poll: typing.Optional[BoardTopicPoll] = pydantic.Field(
        None, description="",
    )
    profiles: typing.List[UsersUser] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class BoardGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class BoardGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[BoardTopicComment] = pydantic.Field(
        ..., description="",
    )
    poll: typing.Optional[BoardTopicPoll] = pydantic.Field(
        None, description="",
    )


class BoardGetCommentsResponse(pydantic.BaseModel):
    response: "BoardGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class BoardGetTopicsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[BoardTopic] = pydantic.Field(
        ..., description="",
    )
    default_order: BoardDefaultOrder = pydantic.Field(
        ..., description="",
    )
    can_add_topics: BaseBoolInt = pydantic.Field(
        ..., description="Information whether current user can add topic",
    )
    profiles: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )


class BoardGetTopicsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetTopicsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class BoardGetTopicsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[BoardTopic] = pydantic.Field(
        ..., description="",
    )
    default_order: BoardDefaultOrder = pydantic.Field(
        ..., description="",
    )
    can_add_topics: BaseBoolInt = pydantic.Field(
        ..., description="Information whether current user can add topic",
    )


class BoardGetTopicsResponse(pydantic.BaseModel):
    response: "BoardGetTopicsResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetChairsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[BaseObject]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetChairsResponse(pydantic.BaseModel):
    response: "DatabaseGetChairsResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetCitiesByIdResponse(pydantic.BaseModel):
    response: typing.List["BaseObject"] = pydantic.Field(
        ..., description="",
    )


class DatabaseGetCitiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseCity]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCitiesResponse(pydantic.BaseModel):
    response: "DatabaseGetCitiesResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetCountriesByIdResponse(pydantic.BaseModel):
    response: typing.List["BaseCountry"] = pydantic.Field(
        ..., description="",
    )


class DatabaseGetCountriesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[BaseCountry]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCountriesResponse(pydantic.BaseModel):
    response: "DatabaseGetCountriesResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetFacultiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseFaculty]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetFacultiesResponse(pydantic.BaseModel):
    response: "DatabaseGetFacultiesResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetMetroStationsByIdResponse(pydantic.BaseModel):
    response: typing.List["DatabaseStation"] = pydantic.Field(
        ..., description="",
    )


class DatabaseGetMetroStationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseStation]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetMetroStationsResponse(pydantic.BaseModel):
    response: "DatabaseGetMetroStationsResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetRegionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseRegion]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetRegionsResponse(pydantic.BaseModel):
    response: "DatabaseGetRegionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetSchoolClassesResponse(pydantic.BaseModel):
    response: typing.List[typing.List[typing.Union[str, int]]] = pydantic.Field(
        ..., description="",
    )


class DatabaseGetSchoolsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseSchool]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetSchoolsResponse(pydantic.BaseModel):
    response: "DatabaseGetSchoolsResponseModel" = pydantic.Field(
        ..., description="",
    )


class DatabaseGetUniversitiesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DatabaseUniversity]] = pydantic.Field(
        None, description="",
    )


class DatabaseGetUniversitiesResponse(pydantic.BaseModel):
    response: "DatabaseGetUniversitiesResponseModel" = pydantic.Field(
        ..., description="",
    )


class DocsAddResponseModel(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Doc ID",
    )


class DocsAddResponse(pydantic.BaseModel):
    response: "DocsAddResponseModel" = pydantic.Field(
        ..., description="",
    )


class DocsGetByIdResponse(pydantic.BaseModel):
    response: typing.List["DocsDoc"] = pydantic.Field(
        ..., description="",
    )


class DocsGetTypesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[DocsDocTypes]] = pydantic.Field(
        None, description="",
    )


class DocsGetTypesResponse(pydantic.BaseModel):
    response: "DocsGetTypesResponseModel" = pydantic.Field(
        ..., description="",
    )


class DocsGetUploadServer(pydantic.BaseModel):
    response: "BaseUploadServer" = pydantic.Field(
        ..., description="",
    )


class DocsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[DocsDoc] = pydantic.Field(
        ..., description="",
    )


class DocsGetResponse(pydantic.BaseModel):
    response: "DocsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class DocsSaveResponseModel(pydantic.BaseModel):
    type: typing.Optional[DocsDocAttachmentType] = pydantic.Field(
        None, description="",
    )
    audio_message: typing.Optional[MessagesAudioMessage] = pydantic.Field(
        None, description="",
    )
    doc: typing.Optional[DocsDoc] = pydantic.Field(
        None, description="",
    )
    graffiti: typing.Optional[MessagesGraffiti] = pydantic.Field(
        None, description="",
    )


class DocsSaveResponse(pydantic.BaseModel):
    response: "DocsSaveResponseModel" = pydantic.Field(
        ..., description="",
    )


class DocsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[DocsDoc] = pydantic.Field(
        ..., description="",
    )


class DocsSearchResponse(pydantic.BaseModel):
    response: "DocsSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class FaveAddTagResponse(pydantic.BaseModel):
    response: "FaveTag" = pydantic.Field(
        ..., description="",
    )


class FaveGetPagesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    items: typing.Optional[typing.List[FavePage]] = pydantic.Field(
        None, description="",
    )


class FaveGetPagesResponse(pydantic.BaseModel):
    response: "FaveGetPagesResponseModel" = pydantic.Field(
        ..., description="",
    )


class FaveGetTagsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    items: typing.Optional[typing.List[FaveTag]] = pydantic.Field(
        None, description="",
    )


class FaveGetTagsResponse(pydantic.BaseModel):
    response: "FaveGetTagsResponseModel" = pydantic.Field(
        ..., description="",
    )


class FaveGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[FaveBookmark]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroup]] = pydantic.Field(
        None, description="",
    )


class FaveGetExtendedResponse(pydantic.BaseModel):
    response: "FaveGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class FaveGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[FaveBookmark]] = pydantic.Field(
        None, description="",
    )


class FaveGetResponse(pydantic.BaseModel):
    response: "FaveGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsAddListResponseModel(pydantic.BaseModel):
    list_id: int = pydantic.Field(
        ..., description="List ID",
    )


class FriendsAddListResponse(pydantic.BaseModel):
    response: "FriendsAddListResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsAddResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Friend request status",
    )


class FriendsAreFriendsResponse(pydantic.BaseModel):
    response: typing.List["FriendsFriendStatus"] = pydantic.Field(
        ..., description="",
    )


class FriendsDeleteResponseModel(pydantic.BaseModel):
    success: BaseOkResponse = pydantic.Field(
        ..., description="",
    )
    friend_deleted: typing.Optional[int] = pydantic.Field(
        None, description="Returns 1 if friend has been deleted",
    )
    out_request_deleted: typing.Optional[int] = pydantic.Field(
        None, description="Returns 1 if out request has been canceled",
    )
    in_request_deleted: typing.Optional[int] = pydantic.Field(
        None, description="Returns 1 if incoming request has been declined",
    )
    suggestion_deleted: typing.Optional[int] = pydantic.Field(
        None, description="Returns 1 if suggestion has been declined",
    )


class FriendsDeleteResponse(pydantic.BaseModel):
    response: "FriendsDeleteResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetAppUsersResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class FriendsGetByPhonesResponse(pydantic.BaseModel):
    response: typing.List["FriendsUserXtrPhone"] = pydantic.Field(
        ..., description="",
    )


class FriendsGetListsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[FriendsFriendsList] = pydantic.Field(
        ..., description="",
    )


class FriendsGetListsResponse(pydantic.BaseModel):
    response: "FriendsGetListsResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetMutualResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class FriendsGetMutualTargetUidsResponse(pydantic.BaseModel):
    response: typing.List["FriendsMutualFriend"] = pydantic.Field(
        ..., description="",
    )


class FriendsGetOnlineOnlineMobileResponseModel(pydantic.BaseModel):
    online: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    online_mobile: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class FriendsGetOnlineOnlineMobileResponse(pydantic.BaseModel):
    response: "FriendsGetOnlineOnlineMobileResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetOnlineResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class FriendsGetRecentResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class FriendsGetRequestsExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total requests number",
    )
    items: typing.Optional[typing.List[FriendsRequestsXtrMessage]] = pydantic.Field(
        None, description="",
    )


class FriendsGetRequestsExtendedResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetRequestsNeedMutualResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total requests number",
    )
    items: typing.Optional[typing.List[FriendsRequests]] = pydantic.Field(
        None, description="",
    )


class FriendsGetRequestsNeedMutualResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsNeedMutualResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetRequestsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total requests number",
    )
    items: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    count_unread: typing.Optional[int] = pydantic.Field(
        None, description="Total unread requests number",
    )


class FriendsGetRequestsResponse(pydantic.BaseModel):
    response: "FriendsGetRequestsResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetSuggestionsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total results number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class FriendsGetSuggestionsResponse(pydantic.BaseModel):
    response: "FriendsGetSuggestionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total friends number",
    )
    items: typing.List[FriendsUserXtrLists] = pydantic.Field(
        ..., description="",
    )


class FriendsGetFieldsResponse(pydantic.BaseModel):
    response: "FriendsGetFieldsResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total friends number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class FriendsGetResponse(pydantic.BaseModel):
    response: "FriendsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class FriendsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class FriendsSearchResponse(pydantic.BaseModel):
    response: "FriendsSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class GiftsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[GiftsGift]] = pydantic.Field(
        None, description="",
    )


class GiftsGetResponse(pydantic.BaseModel):
    response: "GiftsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsAddCallbackServerResponseModel(pydantic.BaseModel):
    server_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class GroupsAddCallbackServerResponse(pydantic.BaseModel):
    response: "GroupsAddCallbackServerResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsAddLinkResponse(pydantic.BaseModel):
    response: "GroupsGroupLink" = pydantic.Field(
        ..., description="",
    )


class GroupsAddAddressResponse(pydantic.BaseModel):
    response: "GroupsAddress" = pydantic.Field(
        ..., description="",
    )


class GroupsCreateResponse(pydantic.BaseModel):
    response: "GroupsGroup" = pydantic.Field(
        ..., description="",
    )


class GroupsEditAddressResponse(pydantic.BaseModel):
    response: "GroupsAddress" = pydantic.Field(
        ..., description="Result",
    )


class GroupsGetAddressesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total count of addresses",
    )
    items: typing.List[GroupsAddress] = pydantic.Field(
        ..., description="",
    )


class GroupsGetAddressesResponse(pydantic.BaseModel):
    response: "GroupsGetAddressesResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total users number",
    )
    items: typing.List[GroupsBannedItem] = pydantic.Field(
        ..., description="",
    )


class GroupsGetBannedResponse(pydantic.BaseModel):
    response: "GroupsGetBannedResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetByIdResponse(pydantic.BaseModel):
    response: typing.List["GroupsGroupFull"] = pydantic.Field(
        ..., description="",
    )


class GroupsGetCallbackConfirmationCodeResponseModel(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(
        None, description="Confirmation code",
    )


class GroupsGetCallbackConfirmationCodeResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackConfirmationCodeResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetCallbackServersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="",
    )
    items: typing.List[GroupsCallbackServer] = pydantic.Field(
        ..., description="",
    )


class GroupsGetCallbackServersResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackServersResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetCallbackSettingsResponse(pydantic.BaseModel):
    response: "GroupsCallbackSettings" = pydantic.Field(
        ..., description="",
    )


class GroupsGetCatalogInfoExtendedResponseModel(pydantic.BaseModel):
    enabled: int = pydantic.Field(
        ..., description="Information whether catalog is enabled for current user",
    )
    categories: typing.Optional[GroupsGroupCategoryFull] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetCatalogInfoResponseModel(pydantic.BaseModel):
    enabled: int = pydantic.Field(
        ..., description="Information whether catalog is enabled for current user",
    )
    categories: typing.Optional[GroupsGroupCategory] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetCatalogResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class GroupsGetCatalogResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitedUsersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitedUsersResponse(pydantic.BaseModel):
    response: "GroupsGetInvitedUsersResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitesExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[GroupsGroupXtrInvitedBy] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitesExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[GroupsGroupXtrInvitedBy] = pydantic.Field(
        ..., description="",
    )


class GroupsGetInvitesResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetLongPollServerResponse(pydantic.BaseModel):
    response: "GroupsLongPollServer" = pydantic.Field(
        ..., description="",
    )


class GroupsGetLongPollSettingsResponse(pydantic.BaseModel):
    response: "GroupsLongPollSettings" = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total members number",
    )
    items: typing.List[GroupsUserXtrRole] = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFieldsResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersFilterResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total members number",
    )
    items: typing.List[GroupsMemberRole] = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersFilterResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFilterResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total members number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class GroupsGetMembersResponse(pydantic.BaseModel):
    response: "GroupsGetMembersResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetRequestsFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class GroupsGetRequestsFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsFieldsResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetRequestsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class GroupsGetRequestsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetSettingsResponse(pydantic.BaseModel):
    response: "GroupsGroupSettings" = pydantic.Field(
        ..., description="",
    )


class GroupsGetTokenPermissionsResponseModel(pydantic.BaseModel):
    mask: int = pydantic.Field(
        ..., description="",
    )
    permissions: GroupsTokenPermissionSetting = pydantic.Field(
        ..., description="",
    )


class GroupsGetTokenPermissionsResponse(pydantic.BaseModel):
    response: "GroupsGetTokenPermissionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class GroupsGetExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class GroupsGetResponse(pydantic.BaseModel):
    response: "GroupsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsIsMemberExtendedResponseModel(pydantic.BaseModel):
    member: BaseBoolInt = pydantic.Field(
        ..., description="Information whether user is a member of the group",
    )
    invitation: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user has been invited to the group",
    )
    can_invite: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user can be invited",
    )
    can_recall: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user's invite to the group can be recalled",
    )
    request: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user has sent request to the group",
    )


class GroupsIsMemberExtendedResponse(pydantic.BaseModel):
    response: "GroupsIsMemberExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class GroupsIsMemberResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Information whether user is a member of the group",
    )


class GroupsIsMemberUserIdsExtendedResponse(pydantic.BaseModel):
    response: typing.List["GroupsMemberStatusFull"] = pydantic.Field(
        ..., description="",
    )


class GroupsIsMemberUserIdsResponse(pydantic.BaseModel):
    response: typing.List["GroupsMemberStatus"] = pydantic.Field(
        ..., description="",
    )


class GroupsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total communities number",
    )
    items: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class GroupsSearchResponse(pydantic.BaseModel):
    response: "GroupsSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class LeadsCheckUserResponse(pydantic.BaseModel):
    response: "LeadsChecked" = pydantic.Field(
        ..., description="",
    )


class LeadsCompleteResponse(pydantic.BaseModel):
    response: "LeadsComplete" = pydantic.Field(
        ..., description="",
    )


class LeadsGetStatsResponse(pydantic.BaseModel):
    response: "LeadsLead" = pydantic.Field(
        ..., description="",
    )


class LeadsGetUsersResponse(pydantic.BaseModel):
    response: typing.List["LeadsEntry"] = pydantic.Field(
        ..., description="",
    )


class LeadsMetricHitResponseModel(pydantic.BaseModel):
    result: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether request has been processed successfully",
    )
    redirect_link: typing.Optional[str] = pydantic.Field(
        None, description="Redirect link",
    )


class LeadsMetricHitResponse(pydantic.BaseModel):
    response: "LeadsMetricHitResponseModel" = pydantic.Field(
        ..., description="",
    )


class LeadsStartResponse(pydantic.BaseModel):
    response: "LeadsStart" = pydantic.Field(
        ..., description="",
    )


class LikesAddResponseModel(pydantic.BaseModel):
    likes: int = pydantic.Field(
        ..., description="Total likes number",
    )


class LikesAddResponse(pydantic.BaseModel):
    response: "LikesAddResponseModel" = pydantic.Field(
        ..., description="",
    )


class LikesDeleteResponseModel(pydantic.BaseModel):
    likes: int = pydantic.Field(
        ..., description="Total likes number",
    )


class LikesDeleteResponse(pydantic.BaseModel):
    response: "LikesDeleteResponseModel" = pydantic.Field(
        ..., description="",
    )


class LikesGetListExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )


class LikesGetListExtendedResponse(pydantic.BaseModel):
    response: "LikesGetListExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class LikesGetListResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class LikesGetListResponse(pydantic.BaseModel):
    response: "LikesGetListResponseModel" = pydantic.Field(
        ..., description="",
    )


class LikesIsLikedResponseModel(pydantic.BaseModel):
    liked: BaseBoolInt = pydantic.Field(
        ..., description="Information whether user liked the object",
    )
    copied: BaseBoolInt = pydantic.Field(
        ..., description="Information whether user reposted the object",
    )


class LikesIsLikedResponse(pydantic.BaseModel):
    response: "LikesIsLikedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketAddAlbumResponseModel(pydantic.BaseModel):
    market_album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )


class MarketAddAlbumResponse(pydantic.BaseModel):
    response: "MarketAddAlbumResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketAddResponseModel(pydantic.BaseModel):
    market_item_id: typing.Optional[int] = pydantic.Field(
        None, description="Item ID",
    )


class MarketAddResponse(pydantic.BaseModel):
    response: "MarketAddResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Comment ID",
    )


class MarketDeleteCommentResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully (0 if the comment is not found)",
    )


class MarketGetAlbumByIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketAlbum]] = pydantic.Field(
        None, description="",
    )


class MarketGetAlbumByIdResponse(pydantic.BaseModel):
    response: "MarketGetAlbumByIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetAlbumsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketAlbum]] = pydantic.Field(
        None, description="",
    )


class MarketGetAlbumsResponse(pydantic.BaseModel):
    response: "MarketGetAlbumsResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItemFull]] = pydantic.Field(
        None, description="",
    )


class MarketGetByIdExtendedResponse(pydantic.BaseModel):
    response: "MarketGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetByIdResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItem]] = pydantic.Field(
        None, description="",
    )


class MarketGetByIdResponse(pydantic.BaseModel):
    response: "MarketGetByIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetCategoriesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketCategory]] = pydantic.Field(
        None, description="",
    )


class MarketGetCategoriesResponse(pydantic.BaseModel):
    response: "MarketGetCategoriesResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[WallWallComment]] = pydantic.Field(
        None, description="",
    )


class MarketGetCommentsResponse(pydantic.BaseModel):
    response: "MarketGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItemFull]] = pydantic.Field(
        None, description="",
    )


class MarketGetExtendedResponse(pydantic.BaseModel):
    response: "MarketGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItem]] = pydantic.Field(
        None, description="",
    )


class MarketGetResponse(pydantic.BaseModel):
    response: "MarketGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketRestoreCommentResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully (0 if the comment is not found)",
    )


class MarketSearchExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItemFull]] = pydantic.Field(
        None, description="",
    )


class MarketSearchExtendedResponse(pydantic.BaseModel):
    response: "MarketSearchExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MarketSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[MarketMarketItem]] = pydantic.Field(
        None, description="",
    )


class MarketSearchResponse(pydantic.BaseModel):
    response: "MarketSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesCreateChatResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Chat ID",
    )


class MessagesDeleteChatPhotoResponseModel(pydantic.BaseModel):
    message_id: typing.Optional[int] = pydantic.Field(
        None, description="Service message ID",
    )
    chat: typing.Optional[MessagesChat] = pydantic.Field(
        None, description="",
    )


class MessagesDeleteChatPhotoResponse(pydantic.BaseModel):
    response: "MessagesDeleteChatPhotoResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesDeleteConversationResponseModel(pydantic.BaseModel):
    last_deleted_id: int = pydantic.Field(
        ..., description="Id of the last message, that was deleted",
    )


class MessagesDeleteConversationResponse(pydantic.BaseModel):
    response: "MessagesDeleteConversationResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesDeleteResponse(pydantic.BaseModel):
    response: dict = pydantic.Field(
        ..., description="",
    )


class MessagesEditResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class MessagesGetByConversationMessageIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        ..., description="",
    )


class MessagesGetByConversationMessageIdResponse(pydantic.BaseModel):
    response: "MessagesGetByConversationMessageIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        ..., description="",
    )


class MessagesGetByIdResponse(pydantic.BaseModel):
    response: "MessagesGetByIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetChatPreviewResponseModel(pydantic.BaseModel):
    preview: typing.Optional[MessageChatPreview] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatPreviewResponse(pydantic.BaseModel):
    response: "MessagesGetChatPreviewResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetChatChatIdsFieldsResponse(pydantic.BaseModel):
    response: typing.List["MessagesChatFull"] = pydantic.Field(
        ..., description="",
    )


class MessagesGetChatChatIdsResponse(pydantic.BaseModel):
    response: typing.List["MessagesChat"] = pydantic.Field(
        ..., description="",
    )


class MessagesGetChatFieldsResponse(pydantic.BaseModel):
    response: "MessagesChatFull" = pydantic.Field(
        ..., description="",
    )


class MessagesGetChatResponse(pydantic.BaseModel):
    response: "MessagesChat" = pydantic.Field(
        ..., description="",
    )


class MessagesGetConversationMembersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Chat members count",
    )
    items: typing.List[MessagesConversationMember] = pydantic.Field(
        ..., description="",
    )
    chat_restrictions: typing.Optional[MessagesChatRestrictions] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationMembersResponse(pydantic.BaseModel):
    response: "MessagesGetConversationMembersResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetConversationsByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesConversation] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.Optional[typing.List[UsersUser]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsByIdExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetConversationsByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesConversation] = pydantic.Field(
        ..., description="",
    )


class MessagesGetConversationsByIdResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsByIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetConversationsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    unread_count: typing.Optional[int] = pydantic.Field(
        None, description="Unread dialogs number",
    )
    items: typing.List[MessagesConversationWithMessage] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetHistoryAttachmentsResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[MessagesHistoryAttachment]] = pydantic.Field(
        None, description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="Value for pagination",
    )


class MessagesGetHistoryAttachmentsResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryAttachmentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetHistoryResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesGetHistoryResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetInviteLinkResponseModel(pydantic.BaseModel):
    link: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class MessagesGetInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesGetInviteLinkResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetLastActivityResponse(pydantic.BaseModel):
    response: "MessagesLastActivity" = pydantic.Field(
        ..., description="",
    )


class MessagesGetLongPollHistoryResponseModel(pydantic.BaseModel):
    history: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroup]] = pydantic.Field(
        None, description="",
    )
    messages: typing.Optional[MessagesLongpollMessages] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    chats: typing.Optional[MessagesChat] = pydantic.Field(
        None, description="",
    )
    new_pts: typing.Optional[int] = pydantic.Field(
        None, description="Persistence timestamp",
    )
    more: typing.Optional[bool] = pydantic.Field(
        None, description="Has more",
    )
    conversations: typing.Optional[MessagesConversation] = pydantic.Field(
        None, description="",
    )


class MessagesGetLongPollHistoryResponse(pydantic.BaseModel):
    response: "MessagesGetLongPollHistoryResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesGetLongPollServerResponse(pydantic.BaseModel):
    response: "MessagesLongpollParams" = pydantic.Field(
        ..., description="",
    )


class MessagesIsMessagesFromGroupAllowedResponseModel(pydantic.BaseModel):
    is_allowed: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="",
    )


class MessagesIsMessagesFromGroupAllowedResponse(pydantic.BaseModel):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesJoinChatByInviteLinkResponseModel(pydantic.BaseModel):
    chat_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class MessagesJoinChatByInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesJoinChatByInviteLinkResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesMarkAsImportantResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class MessagesPinResponse(pydantic.BaseModel):
    response: "MessagesPinnedMessage" = pydantic.Field(
        ..., description="",
    )


class MessagesSearchConversationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total results number",
    )
    items: typing.Optional[typing.List[MessagesConversation]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class MessagesSearchConversationsResponse(pydantic.BaseModel):
    response: "MessagesSearchConversationsResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        ..., description="",
    )


class MessagesSearchResponse(pydantic.BaseModel):
    response: "MessagesSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class MessagesSendResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Message ID",
    )


class MessagesSendUserIdsResponse(pydantic.BaseModel):
    response: typing.List[dict] = pydantic.Field(
        ..., description="",
    )


class MessagesSetChatPhotoResponseModel(pydantic.BaseModel):
    message_id: typing.Optional[int] = pydantic.Field(
        None, description="Service message ID",
    )
    chat: typing.Optional[MessagesChat] = pydantic.Field(
        None, description="",
    )


class MessagesSetChatPhotoResponse(pydantic.BaseModel):
    response: "MessagesSetChatPhotoResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetBannedExtendedResponseModel(pydantic.BaseModel):
    groups: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetBannedResponseModel(pydantic.BaseModel):
    groups: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )
    members: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetCommentsResponseModel(pydantic.BaseModel):
    items: typing.List[NewsfeedNewsfeedItem] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="New from value",
    )


class NewsfeedGetCommentsResponse(pydantic.BaseModel):
    response: "NewsfeedGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetListsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[NewsfeedListFull] = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetListsExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetListsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[NewsfeedList] = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetListsResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetMentionsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallpostToId] = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetMentionsResponse(pydantic.BaseModel):
    response: "NewsfeedGetMentionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetRecommendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[NewsfeedNewsfeedItem]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )
    new_offset: typing.Optional[str] = pydantic.Field(
        None, description="New offset value",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="Next from value",
    )


class NewsfeedGetRecommendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetRecommendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetSuggestedSourcesResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[
        typing.List[typing.Union[GroupsGroupFull, UsersUserXtrType,]]
    ] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetSuggestedSourcesResponse(pydantic.BaseModel):
    response: "NewsfeedGetSuggestedSourcesResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedGetResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[NewsfeedNewsfeedItem]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="New from value",
    )


class NewsfeedGetResponse(pydantic.BaseModel):
    response: "NewsfeedGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedSaveListResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="List ID",
    )


class NewsfeedSearchExtendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[WallWallpostFull]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroupFull]] = pydantic.Field(
        None, description="",
    )
    count: typing.Optional[int] = pydantic.Field(
        None, description="Filtered number",
    )
    total_count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class NewsfeedSearchExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedSearchExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class NewsfeedSearchResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[WallWallpostFull]] = pydantic.Field(
        None, description="",
    )
    suggested_queries: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class NewsfeedSearchResponse(pydantic.BaseModel):
    response: "NewsfeedSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class NotesAddResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Note ID",
    )


class NotesCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Comment ID",
    )


class NotesGetByIdResponse(pydantic.BaseModel):
    response: "NotesNote" = pydantic.Field(
        ..., description="",
    )


class NotesGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[NotesNoteComment] = pydantic.Field(
        ..., description="",
    )


class NotesGetCommentsResponse(pydantic.BaseModel):
    response: "NotesGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class NotesGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[NotesNote] = pydantic.Field(
        ..., description="",
    )


class NotesGetResponse(pydantic.BaseModel):
    response: "NotesGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class NotificationsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    profiles: typing.Optional[typing.List[UsersUser]] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[typing.List[GroupsGroup]] = pydantic.Field(
        None, description="",
    )
    last_viewed: typing.Optional[int] = pydantic.Field(
        None, description="Time when user has been checked notifications last time",
    )
    photos: typing.Optional[PhotosPhoto] = pydantic.Field(
        None, description="",
    )
    videos: typing.Optional[VideoVideo] = pydantic.Field(
        None, description="",
    )
    apps: typing.Optional[AppsApp] = pydantic.Field(
        None, description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    ttl: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class NotificationsGetResponse(pydantic.BaseModel):
    response: "NotificationsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class NotificationsMarkAsViewedResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class NotificationsSendMessageResponse(pydantic.BaseModel):
    response: typing.List["NotificationsSendMessageItem"] = pydantic.Field(
        ..., description="",
    )


class OkResponse(pydantic.BaseModel):
    response: "BaseOkResponse" = pydantic.Field(
        ..., description="",
    )


class OrdersCancelSubscriptionResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class OrdersChangeStateResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="New state",
    )


class OrdersGetAmountResponse(pydantic.BaseModel):
    response: "OrdersAmount" = pydantic.Field(
        ..., description="",
    )


class OrdersGetByIdResponse(pydantic.BaseModel):
    response: typing.List["OrdersOrder"] = pydantic.Field(
        ..., description="",
    )


class OrdersGetUserSubscriptionByIdResponse(pydantic.BaseModel):
    response: "OrdersSubscription" = pydantic.Field(
        ..., description="",
    )


class OrdersGetUserSubscriptionsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[OrdersSubscription]] = pydantic.Field(
        None, description="",
    )


class OrdersGetUserSubscriptionsResponse(pydantic.BaseModel):
    response: "OrdersGetUserSubscriptionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class OrdersGetResponse(pydantic.BaseModel):
    response: typing.List["OrdersOrder"] = pydantic.Field(
        ..., description="",
    )


class OrdersUpdateSubscriptionResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class PagesGetHistoryResponse(pydantic.BaseModel):
    response: typing.List["PagesWikipageHistory"] = pydantic.Field(
        ..., description="",
    )


class PagesGetTitlesResponse(pydantic.BaseModel):
    response: typing.List["PagesWikipage"] = pydantic.Field(
        ..., description="",
    )


class PagesGetVersionResponse(pydantic.BaseModel):
    response: "PagesWikipageFull" = pydantic.Field(
        ..., description="",
    )


class PagesGetResponse(pydantic.BaseModel):
    response: "PagesWikipageFull" = pydantic.Field(
        ..., description="",
    )


class PagesParseWikiResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="HTML source",
    )


class PagesSaveAccessResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Page ID",
    )


class PagesSaveResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Page ID",
    )


class PhotosCopyResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Photo ID",
    )


class PhotosCreateAlbumResponse(pydantic.BaseModel):
    response: "PhotosPhotoAlbumFull" = pydantic.Field(
        ..., description="",
    )


class PhotosCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Created comment ID",
    )


class PhotosDeleteCommentResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosGetAlbumsCountResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Albums number",
    )


class PhotosGetAlbumsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhotoAlbumFull] = pydantic.Field(
        ..., description="",
    )


class PhotosGetAlbumsResponse(pydantic.BaseModel):
    response: "PhotosGetAlbumsResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetAllCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[PhotosCommentXtrPid]] = pydantic.Field(
        None, description="",
    )


class PhotosGetAllCommentsResponse(pydantic.BaseModel):
    response: "PhotosGetAllCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetAllExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[PhotosPhotoFullXtrRealOffset]] = pydantic.Field(
        None, description="",
    )
    more: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether next page is presented",
    )


class PhotosGetAllExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetAllExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetAllResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[PhotosPhotoXtrRealOffset]] = pydantic.Field(
        None, description="",
    )
    more: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether next page is presented",
    )


class PhotosGetAllResponse(pydantic.BaseModel):
    response: "PhotosGetAllResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhotoFull"] = pydantic.Field(
        ..., description="",
    )


class PhotosGetByIdResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real offset of the comments",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class PhotosGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetCommentsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real offset of the comments",
    )
    items: typing.Optional[typing.List[WallWallComment]] = pydantic.Field(
        None, description="",
    )


class PhotosGetCommentsResponse(pydantic.BaseModel):
    response: "PhotosGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetMarketUploadServerResponse(pydantic.BaseModel):
    response: "BaseUploadServer" = pydantic.Field(
        ..., description="",
    )


class PhotosGetMessagesUploadServerResponse(pydantic.BaseModel):
    response: "PhotosPhotoUpload" = pydantic.Field(
        ..., description="",
    )


class PhotosGetNewTagsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhotoXtrTagInfo] = pydantic.Field(
        ..., description="",
    )


class PhotosGetNewTagsResponse(pydantic.BaseModel):
    response: "PhotosGetNewTagsResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetTagsResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhotoTag"] = pydantic.Field(
        ..., description="",
    )


class PhotosGetUploadServerResponse(pydantic.BaseModel):
    response: "PhotosPhotoUpload" = pydantic.Field(
        ..., description="",
    )


class PhotosGetUserPhotosExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhotoFull] = pydantic.Field(
        ..., description="",
    )


class PhotosGetUserPhotosExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetUserPhotosExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetUserPhotosResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhoto] = pydantic.Field(
        ..., description="",
    )


class PhotosGetUserPhotosResponse(pydantic.BaseModel):
    response: "PhotosGetUserPhotosResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetWallUploadServerResponse(pydantic.BaseModel):
    response: "PhotosPhotoUpload" = pydantic.Field(
        ..., description="",
    )


class PhotosGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhotoFull] = pydantic.Field(
        ..., description="",
    )


class PhotosGetExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PhotosPhoto] = pydantic.Field(
        ..., description="",
    )


class PhotosGetResponse(pydantic.BaseModel):
    response: "PhotosGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosPutTagResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Created tag ID",
    )


class PhotosRestoreCommentResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosSaveMarketAlbumPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosSaveMarketPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosSaveMessagesPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosSaveOwnerCoverPhotoResponse(pydantic.BaseModel):
    response: typing.List["BaseImage"] = pydantic.Field(
        ..., description="",
    )


class PhotosSaveOwnerPhotoResponseModel(pydantic.BaseModel):
    photo_hash: str = pydantic.Field(
        ..., description="Photo hash",
    )
    photo_src: str = pydantic.Field(
        ..., description="Uploaded image url",
    )
    photo_src_big: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded image url",
    )
    photo_src_small: typing.Optional[str] = pydantic.Field(
        None, description="Uploaded image url",
    )
    saved: typing.Optional[int] = pydantic.Field(
        None, description="Returns 1 if profile photo is saved",
    )
    post_id: typing.Optional[int] = pydantic.Field(
        None, description="Created post ID",
    )


class PhotosSaveOwnerPhotoResponse(pydantic.BaseModel):
    response: "PhotosSaveOwnerPhotoResponseModel" = pydantic.Field(
        ..., description="",
    )


class PhotosSaveWallPhotoResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosSaveResponse(pydantic.BaseModel):
    response: typing.List["PhotosPhoto"] = pydantic.Field(
        ..., description="",
    )


class PhotosSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[PhotosPhoto]] = pydantic.Field(
        None, description="",
    )


class PhotosSearchResponse(pydantic.BaseModel):
    response: "PhotosSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class PollsAddVoteResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class PollsCreateResponse(pydantic.BaseModel):
    response: "PollsPoll" = pydantic.Field(
        ..., description="",
    )


class PollsDeleteVoteResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Result",
    )


class PollsGetByIdResponse(pydantic.BaseModel):
    response: "PollsPoll" = pydantic.Field(
        ..., description="",
    )


class PollsGetVotersResponse(pydantic.BaseModel):
    response: typing.List["PollsVoters"] = pydantic.Field(
        ..., description="",
    )


class PrettyCardsCreateResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ..., description="Owner ID of created pretty card",
    )
    card_id: str = pydantic.Field(
        ..., description="Card ID of created pretty card",
    )


class PrettyCardsCreateResponse(pydantic.BaseModel):
    response: "PrettyCardsCreateResponseModel" = pydantic.Field(
        ..., description="",
    )


class PrettyCardsDeleteResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ..., description="Owner ID of deleted pretty card",
    )
    card_id: str = pydantic.Field(
        ..., description="Card ID of deleted pretty card",
    )
    error: typing.Optional[str] = pydantic.Field(
        None, description="Error reason if error happened",
    )


class PrettyCardsDeleteResponse(pydantic.BaseModel):
    response: "PrettyCardsDeleteResponseModel" = pydantic.Field(
        ..., description="",
    )


class PrettyCardsEditResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        ..., description="Owner ID of edited pretty card",
    )
    card_id: str = pydantic.Field(
        ..., description="Card ID of edited pretty card",
    )


class PrettyCardsEditResponse(pydantic.BaseModel):
    response: "PrettyCardsEditResponseModel" = pydantic.Field(
        ..., description="",
    )


class PrettyCardsGetByIdResponse(pydantic.BaseModel):
    response: typing.List["PrettyCardsPrettyCard"] = pydantic.Field(
        ..., description="",
    )


class PrettyCardsGetUploadURLResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="Upload URL",
    )


class PrettyCardsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[PrettyCardsPrettyCard] = pydantic.Field(
        ..., description="",
    )


class PrettyCardsGetResponse(pydantic.BaseModel):
    response: "PrettyCardsGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class SearchGetHintsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="",
    )
    items: typing.List[SearchHint] = pydantic.Field(
        ..., description="",
    )
    suggested_queries: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class SearchGetHintsResponse(pydantic.BaseModel):
    response: "SearchGetHintsResponseModel" = pydantic.Field(
        ..., description="",
    )


class SecureCheckTokenResponse(pydantic.BaseModel):
    response: "SecureTokenChecked" = pydantic.Field(
        ..., description="",
    )


class SecureGetAppBalanceResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="App balance",
    )


class SecureGetSMSHistoryResponse(pydantic.BaseModel):
    response: typing.List["SecureSmsNotification"] = pydantic.Field(
        ..., description="",
    )


class SecureGetTransactionsHistoryResponse(pydantic.BaseModel):
    response: typing.List["SecureTransaction"] = pydantic.Field(
        ..., description="",
    )


class SecureGetUserLevelResponse(pydantic.BaseModel):
    response: typing.List["SecureLevel"] = pydantic.Field(
        ..., description="",
    )


class SecureGiveEventStickerResponse(pydantic.BaseModel):
    response: typing.List[dict] = pydantic.Field(
        ..., description="",
    )


class SecureSendNotificationResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class StatsGetPostReachResponse(pydantic.BaseModel):
    response: typing.List["StatsWallpostStat"] = pydantic.Field(
        ..., description="",
    )


class StatsGetResponse(pydantic.BaseModel):
    response: typing.List["StatsPeriod"] = pydantic.Field(
        ..., description="",
    )


class StatusGetResponse(pydantic.BaseModel):
    response: "StatusStatus" = pydantic.Field(
        ..., description="",
    )


class StorageGetKeysResponse(pydantic.BaseModel):
    response: typing.List[str] = pydantic.Field(
        ..., description="",
    )


class StorageGetKeysResponseStorageValue(pydantic.BaseModel):
    response: typing.List["StorageValue"] = pydantic.Field(
        ..., description="",
    )


class StorageGetResponse(pydantic.BaseModel):
    response: str = pydantic.Field(
        ..., description="Value of key",
    )


class StoriesGetBannedExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class StoriesGetBannedExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class StoriesGetBannedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class StoriesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        ..., description="",
    )


class StoriesGetByIdResponse(pydantic.BaseModel):
    response: "StoriesGetByIdResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetPhotoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: str = pydantic.Field(
        ..., description="Upload URL",
    )
    user_ids: int = pydantic.Field(
        ..., description="Users ID who can to see story.",
    )


class StoriesGetPhotoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetPhotoUploadServerResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetRepliesExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class StoriesGetRepliesExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetRepliesExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetRepliesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        ..., description="",
    )


class StoriesGetRepliesResponse(pydantic.BaseModel):
    response: "StoriesGetRepliesResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetStatsResponse(pydantic.BaseModel):
    response: "StoriesStoryStats" = pydantic.Field(
        ..., description="",
    )


class StoriesGetVideoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: str = pydantic.Field(
        ..., description="Upload URL",
    )
    user_ids: int = pydantic.Field(
        ..., description="Users ID who can to see story.",
    )


class StoriesGetVideoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetVideoUploadServerResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetViewersExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Viewers count",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class StoriesGetViewersExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetViewersExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetViewersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Viewers count",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class StoriesGetViewersResponse(pydantic.BaseModel):
    response: "StoriesGetViewersResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUser] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class StoriesGetExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        ..., description="",
    )
    promo_data: typing.Optional[StoriesPromoBlock] = pydantic.Field(
        None, description="",
    )


class StoriesGetResponse(pydantic.BaseModel):
    response: "StoriesGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesUploadResponseModel(pydantic.BaseModel):
    story: StoriesStory = pydantic.Field(
        ..., description="",
    )


class StoriesUploadResponse(pydantic.BaseModel):
    response: "StoriesUploadResponseModel" = pydantic.Field(
        ..., description="",
    )


class StreamingGetServerUrlResponseModel(pydantic.BaseModel):
    endpoint: typing.Optional[str] = pydantic.Field(
        None, description="Server host",
    )
    key: typing.Optional[str] = pydantic.Field(
        None, description="Access key",
    )


class StreamingGetServerUrlResponse(pydantic.BaseModel):
    response: "StreamingGetServerUrlResponseModel" = pydantic.Field(
        ..., description="",
    )


class UsersGetFollowersFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number of available results",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )


class UsersGetFollowersFieldsResponse(pydantic.BaseModel):
    response: "UsersGetFollowersFieldsResponseModel" = pydantic.Field(
        ..., description="",
    )


class UsersGetFollowersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total friends number",
    )
    items: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class UsersGetFollowersResponse(pydantic.BaseModel):
    response: "UsersGetFollowersResponseModel" = pydantic.Field(
        ..., description="",
    )


class UsersGetSubscriptionsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number of available results",
    )
    items: typing.List[UsersSubscriptionsItem] = pydantic.Field(
        ..., description="",
    )


class UsersGetSubscriptionsExtendedResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class UsersGetSubscriptionsResponseModel(pydantic.BaseModel):
    users: UsersUsersArray = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupsArray] = pydantic.Field(
        ..., description="",
    )


class UsersGetSubscriptionsResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsResponseModel" = pydantic.Field(
        ..., description="",
    )


class UsersGetResponse(pydantic.BaseModel):
    response: typing.List["UsersUserXtrCounters"] = pydantic.Field(
        ..., description="",
    )


class UsersIsAppUserResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ..., description="Information whether the user have installed an app",
    )


class UsersSearchResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number of available results",
    )
    items: typing.Optional[typing.List[UsersUserFull]] = pydantic.Field(
        None, description="",
    )


class UsersSearchResponse(pydantic.BaseModel):
    response: "UsersSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class UtilsCheckLinkResponse(pydantic.BaseModel):
    response: "UtilsLinkChecked" = pydantic.Field(
        ..., description="",
    )


class UtilsGetLastShortenedLinksResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number of available results",
    )
    items: typing.Optional[typing.List[UtilsLastShortenedLink]] = pydantic.Field(
        None, description="",
    )


class UtilsGetLastShortenedLinksResponse(pydantic.BaseModel):
    response: "UtilsGetLastShortenedLinksResponseModel" = pydantic.Field(
        ..., description="",
    )


class UtilsGetLinkStatsExtendedResponse(pydantic.BaseModel):
    response: "UtilsLinkStatsExtended" = pydantic.Field(
        ..., description="",
    )


class UtilsGetLinkStatsResponse(pydantic.BaseModel):
    response: "UtilsLinkStats" = pydantic.Field(
        ..., description="",
    )


class UtilsGetServerTimeResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Time as Unixtime",
    )


class UtilsGetShortLinkResponse(pydantic.BaseModel):
    response: "UtilsShortLink" = pydantic.Field(
        ..., description="",
    )


class UtilsResolveScreenNameResponse(pydantic.BaseModel):
    response: "UtilsDomainResolved" = pydantic.Field(
        ..., description="",
    )


class VideoAddAlbumResponseModel(pydantic.BaseModel):
    album_id: int = pydantic.Field(
        ..., description="Created album ID",
    )


class VideoAddAlbumResponse(pydantic.BaseModel):
    response: "VideoAddAlbumResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoCreateCommentResponse(pydantic.BaseModel):
    response: int = pydantic.Field(
        ..., description="Created comment ID",
    )


class VideoGetAlbumByIdResponse(pydantic.BaseModel):
    response: "VideoVideoAlbumFull" = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsByVideoExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[VideoVideoAlbumFull]] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsByVideoExtendedResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsByVideoExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsByVideoResponse(pydantic.BaseModel):
    response: typing.List[int] = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideoAlbumFull] = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideoAlbumFull] = pydantic.Field(
        ..., description="",
    )


class VideoGetAlbumsResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class VideoGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        ..., description="",
    )


class VideoGetCommentsResponse(pydantic.BaseModel):
    response: "VideoGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideoFull] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class VideoGetExtendedResponse(pydantic.BaseModel):
    response: "VideoGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        ..., description="",
    )


class VideoGetResponse(pydantic.BaseModel):
    response: "VideoGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoRestoreCommentResponse(pydantic.BaseModel):
    response: "BaseBoolInt" = pydantic.Field(
        ...,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class VideoSaveResponse(pydantic.BaseModel):
    response: "VideoSaveResult" = pydantic.Field(
        ..., description="",
    )


class VideoSearchExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserMin] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class VideoSearchExtendedResponse(pydantic.BaseModel):
    response: "VideoSearchExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class VideoSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        ..., description="",
    )


class VideoSearchResponse(pydantic.BaseModel):
    response: "VideoSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallCreateCommentResponseModel(pydantic.BaseModel):
    comment_id: int = pydantic.Field(
        ..., description="Created comment ID",
    )


class WallCreateCommentResponse(pydantic.BaseModel):
    response: "WallCreateCommentResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallEditResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        ..., description="Edited post ID",
    )


class WallEditResponse(pydantic.BaseModel):
    response: "WallEditResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetByIdExtendedResponseModel(pydantic.BaseModel):
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class WallGetByIdExtendedResponse(pydantic.BaseModel):
    response: "WallGetByIdExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetByIdResponse(pydantic.BaseModel):
    response: typing.List["WallWallpostFull"] = pydantic.Field(
        ..., description="",
    )


class WallGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        ..., description="",
    )
    show_reply_button: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether current user can comment the post",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether groups can comment the post",
    )
    current_level_count: typing.Optional[int] = pydantic.Field(
        None, description="Count of replies of current level",
    )
    profiles: typing.List[UsersUser] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class WallGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "WallGetCommentsExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        ..., description="",
    )
    can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether current user can comment the post",
    )
    groups_can_post: typing.Optional[bool] = pydantic.Field(
        None, description="Information whether groups can comment the post",
    )
    current_level_count: typing.Optional[int] = pydantic.Field(
        None, description="Count of replies of current level",
    )


class WallGetCommentsResponse(pydantic.BaseModel):
    response: "WallGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetRepostsResponseModel(pydantic.BaseModel):
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUser] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroup] = pydantic.Field(
        ..., description="",
    )


class WallGetRepostsResponse(pydantic.BaseModel):
    response: "WallGetRepostsResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class WallGetExtendedResponse(pydantic.BaseModel):
    response: "WallGetExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )


class WallGetResponse(pydantic.BaseModel):
    response: "WallGetResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallPostAdsStealthResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        ..., description="Created post ID",
    )


class WallPostAdsStealthResponse(pydantic.BaseModel):
    response: "WallPostAdsStealthResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallPostResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        ..., description="Created post ID",
    )


class WallPostResponse(pydantic.BaseModel):
    response: "WallPostResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallRepostResponseModel(pydantic.BaseModel):
    success: BaseOkResponse = pydantic.Field(
        ..., description="",
    )
    post_id: int = pydantic.Field(
        ..., description="Created post ID",
    )
    reposts_count: int = pydantic.Field(
        ..., description="Reposts number",
    )
    likes_count: int = pydantic.Field(
        ..., description="Reposts number",
    )


class WallRepostResponse(pydantic.BaseModel):
    response: "WallRepostResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallSearchExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )
    profiles: typing.List[UsersUserFull] = pydantic.Field(
        ..., description="",
    )
    groups: typing.List[GroupsGroupFull] = pydantic.Field(
        ..., description="",
    )


class WallSearchExtendedResponse(pydantic.BaseModel):
    response: "WallSearchExtendedResponseModel" = pydantic.Field(
        ..., description="",
    )


class WallSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        ..., description="",
    )


class WallSearchResponse(pydantic.BaseModel):
    response: "WallSearchResponseModel" = pydantic.Field(
        ..., description="",
    )


class WidgetsGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    posts: WidgetsWidgetComment = pydantic.Field(
        ..., description="",
    )


class WidgetsGetCommentsResponse(pydantic.BaseModel):
    response: "WidgetsGetCommentsResponseModel" = pydantic.Field(
        ..., description="",
    )


class WidgetsGetPagesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        ..., description="Total number",
    )
    pages: WidgetsWidgetPage = pydantic.Field(
        ..., description="",
    )


class WidgetsGetPagesResponse(pydantic.BaseModel):
    response: "WidgetsGetPagesResponseModel" = pydantic.Field(
        ..., description="",
    )


class StoriesSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        None, description="",
    )

    profiles: typing.List[UsersUser] = pydantic.Field(
        None, description="",
    )
    groups: typing.List[GroupsGroup] = pydantic.Field(
        None, description="",
    )


class ExecuteResponse(pydantic.BaseModel):
    response: typing.Any = pydantic.Field(..., description="")
