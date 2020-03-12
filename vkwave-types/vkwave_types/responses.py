from .objects import *


class AccountChangePasswordResponseModel(pydantic.BaseModel):
    token: str = pydantic.Field(
        None, description="New token",
    )
    secret: typing.Optional[str] = pydantic.Field(
        None, description="New secret",
    )


class AccountChangePasswordResponse(pydantic.BaseModel):
    response: "AccountChangePasswordResponseModel" = pydantic.Field(
        None, description="",
    )


class AccountGetActiveOffersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[AccountOffer] = pydantic.Field(
        None, description="",
    )


class AccountGetActiveOffersResponse(pydantic.BaseModel):
    response: "AccountGetActiveOffersResponseModel" = pydantic.Field(
        None, description="",
    )


class AccountGetAppPermissionsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Permissions mask",
    )


class AccountGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserMin] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroup] = pydantic.Field(
        None, description="",
    )


class AccountGetBannedResponse(pydantic.BaseModel):
    response: "AccountGetBannedResponseModel" = pydantic.Field(
        None, description="",
    )


class AccountGetCountersResponse(pydantic.BaseModel):
    response: typing.Optional["AccountAccountCounters"] = pydantic.Field(
        None, description="",
    )


class AccountGetInfoResponse(pydantic.BaseModel):
    response: typing.Optional["AccountInfo"] = pydantic.Field(
        None, description="",
    )


class AccountGetProfileInfoResponse(pydantic.BaseModel):
    response: typing.Optional["AccountUserSettings"] = pydantic.Field(
        None, description="",
    )


class AccountGetPushSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["AccountPushSettings"] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class AdsAddOfficeUsersResponse(pydantic.BaseModel):
    response: typing.Optional[bool] = pydantic.Field(
        None, description="true if success",
    )


class AdsCheckLinkResponse(pydantic.BaseModel):
    response: typing.Optional["AdsLinkStatus"] = pydantic.Field(
        None, description="",
    )


class AdsCreateAdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class AdsCreateCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class AdsCreateClientsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class AdsDeleteAdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class AdsDeleteCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="0 if success",
    )


class AdsDeleteClientsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="0 if sucess",
    )


class AdsGetAccountsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsAccount"]] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsLayoutResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsAdLayout"]] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsTargetingResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsTargSettings"]] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsAd"]] = pydantic.Field(
        None, description="",
    )


class AdsGetBudgetResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Budget",
    )


class AdsGetCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsCampaign"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class AdsGetClientsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsClient"]] = pydantic.Field(
        None, description="",
    )


class AdsGetDemographicsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsDemoStats"]] = pydantic.Field(
        None, description="",
    )


class AdsGetFloodStatsResponse(pydantic.BaseModel):
    response: typing.Optional["AdsFloodStats"] = pydantic.Field(
        None, description="",
    )


class AdsGetOfficeUsersResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsUsers"]] = pydantic.Field(
        None, description="",
    )


class AdsGetPostsReachResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsPromotedPostReach"]] = pydantic.Field(
        None, description="",
    )


class AdsGetRejectionReasonResponse(pydantic.BaseModel):
    response: typing.Optional["AdsRejectReason"] = pydantic.Field(
        None, description="",
    )


class AdsGetStatisticsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsStats"]] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsCitiesResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsTargSuggestionsCities"]] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsRegionsResponse(pydantic.BaseModel):
    response: typing.Optional[
        typing.List["AdsTargSuggestionsRegions"]
    ] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsTargSuggestions"]] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsSchoolsResponse(pydantic.BaseModel):
    response: typing.Optional[
        typing.List["AdsTargSuggestionsSchools"]
    ] = pydantic.Field(
        None, description="",
    )


class AdsGetTargetGroupsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["AdsTargetGroup"]] = pydantic.Field(
        None, description="",
    )


class AdsGetTargetingStatsResponse(pydantic.BaseModel):
    response: typing.Optional["AdsTargStats"] = pydantic.Field(
        None, description="",
    )


class AdsGetUploadURLResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Photo upload URL",
    )


class AdsGetVideoUploadURLResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Video upload URL",
    )


class AdsImportTargetContactsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Imported contacts number",
    )


class AdsRemoveOfficeUsersResponse(pydantic.BaseModel):
    response: typing.Optional[bool] = pydantic.Field(
        None, description="true if success",
    )


class AdsUpdateAdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class AdsUpdateCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Campaign ID",
    )


class AdsUpdateClientsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Client ID",
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
        None, description="",
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
        None, description="",
    )


class AppsGetLeaderboardExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[AppsLeaderboard]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserMin] = pydantic.Field(
        None, description="",
    )


class AppsGetLeaderboardExtendedResponse(pydantic.BaseModel):
    response: "AppsGetLeaderboardExtendedResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class AppsGetScopesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[AppsScope] = pydantic.Field(
        None, description="",
    )


class AppsGetScopesResponse(pydantic.BaseModel):
    response: "AppsGetScopesResponseModel" = pydantic.Field(
        None, description="",
    )


class AppsGetScoreResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Score number",
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
        None, description="",
    )


class AppsSendRequestResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Request ID",
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
        None, description="",
    )


class BaseBoolResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="",
    )


class BaseGetUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["BaseUploadServer"] = pydantic.Field(
        None, description="",
    )


class BoardAddTopicResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Topic ID",
    )


class BoardCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )


class BoardGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[BoardTopicComment] = pydantic.Field(
        None, description="",
    )
    poll: typing.Optional[BoardTopicPoll] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUser = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroup = pydantic.Field(
        None, description="",
    )


class BoardGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetCommentsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class BoardGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[BoardTopicComment] = pydantic.Field(
        None, description="",
    )
    poll: typing.Optional[BoardTopicPoll] = pydantic.Field(
        None, description="",
    )


class BoardGetCommentsResponse(pydantic.BaseModel):
    response: "BoardGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class BoardGetTopicsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[BoardTopic] = pydantic.Field(
        None, description="",
    )
    default_order: BoardDefaultOrder = pydantic.Field(
        None, description="",
    )
    can_add_topics: BaseBoolInt = pydantic.Field(
        None, description="Information whether current user can add topic",
    )
    profiles: UsersUserMin = pydantic.Field(
        None, description="",
    )


class BoardGetTopicsExtendedResponse(pydantic.BaseModel):
    response: "BoardGetTopicsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class BoardGetTopicsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[BoardTopic] = pydantic.Field(
        None, description="",
    )
    default_order: BoardDefaultOrder = pydantic.Field(
        None, description="",
    )
    can_add_topics: BaseBoolInt = pydantic.Field(
        None, description="Information whether current user can add topic",
    )


class BoardGetTopicsResponse(pydantic.BaseModel):
    response: "BoardGetTopicsResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class DatabaseGetCitiesByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["BaseObject"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class DatabaseGetCountriesByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["BaseCountry"]] = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class DatabaseGetMetroStationsByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["DatabaseStation"]] = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class DatabaseGetSchoolClassesResponse(pydantic.BaseModel):
    response: typing.Optional[
        typing.List[typing.List[typing.Union[str, int]]]
    ] = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class DocsAddResponseModel(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None, description="Doc ID",
    )


class DocsAddResponse(pydantic.BaseModel):
    response: "DocsAddResponseModel" = pydantic.Field(
        None, description="",
    )


class DocsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["DocsDoc"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class DocsGetUploadServer(pydantic.BaseModel):
    response: typing.Optional["BaseUploadServer"] = pydantic.Field(
        None, description="",
    )


class DocsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[DocsDoc] = pydantic.Field(
        None, description="",
    )


class DocsGetResponse(pydantic.BaseModel):
    response: "DocsGetResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class DocsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[DocsDoc] = pydantic.Field(
        None, description="",
    )


class DocsSearchResponse(pydantic.BaseModel):
    response: "DocsSearchResponseModel" = pydantic.Field(
        None, description="",
    )


class FaveAddTagResponse(pydantic.BaseModel):
    response: typing.Optional["FaveTag"] = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class FaveGetExtendedResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    items: typing.Optional[typing.List[FaveBookmark]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroup] = pydantic.Field(
        None, description="",
    )


class FaveGetExtendedResponse(pydantic.BaseModel):
    response: "FaveGetExtendedResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class FriendsAddListResponseModel(pydantic.BaseModel):
    list_id: int = pydantic.Field(
        None, description="List ID",
    )


class FriendsAddListResponse(pydantic.BaseModel):
    response: "FriendsAddListResponseModel" = pydantic.Field(
        None, description="",
    )


class FriendsAddResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Friend request status",
    )


class FriendsAreFriendsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["FriendsFriendStatus"]] = pydantic.Field(
        None, description="",
    )


class FriendsDeleteResponseModel(pydantic.BaseModel):
    success: BaseOkResponse = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class FriendsGetAppUsersResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class FriendsGetByPhonesResponse(pydantic.BaseModel):
    response: typing.List["FriendsUserXtrPhone"] = pydantic.Field(
        None, description="",
    )


class FriendsGetListsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[FriendsFriendsList] = pydantic.Field(
        None, description="",
    )


class FriendsGetListsResponse(pydantic.BaseModel):
    response: "FriendsGetListsResponseModel" = pydantic.Field(
        None, description="",
    )


class FriendsGetMutualResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class FriendsGetMutualTargetUidsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["FriendsMutualFriend"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class FriendsGetOnlineResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class FriendsGetRecentResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class FriendsGetSuggestionsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total results number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class FriendsGetSuggestionsResponse(pydantic.BaseModel):
    response: "FriendsGetSuggestionsResponseModel" = pydantic.Field(
        None, description="",
    )


class FriendsGetFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total friends number",
    )
    items: typing.List[FriendsUserXtrLists] = pydantic.Field(
        None, description="",
    )


class FriendsGetFieldsResponse(pydantic.BaseModel):
    response: "FriendsGetFieldsResponseModel" = pydantic.Field(
        None, description="",
    )


class FriendsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total friends number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class FriendsGetResponse(pydantic.BaseModel):
    response: "FriendsGetResponseModel" = pydantic.Field(
        None, description="",
    )


class FriendsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class FriendsSearchResponse(pydantic.BaseModel):
    response: "FriendsSearchResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class GroupsAddCallbackServerResponseModel(pydantic.BaseModel):
    server_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class GroupsAddCallbackServerResponse(pydantic.BaseModel):
    response: "GroupsAddCallbackServerResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsAddLinkResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsGroupLink"] = pydantic.Field(
        None, description="",
    )


class GroupsAddAddressResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsAddress"] = pydantic.Field(
        None, description="",
    )


class GroupsCreateResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsGroup"] = pydantic.Field(
        None, description="",
    )


class GroupsEditAddressResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsAddress"] = pydantic.Field(
        None, description="Result",
    )


class GroupsGetAddressesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total count of addresses",
    )
    items: typing.List[GroupsAddress] = pydantic.Field(
        None, description="",
    )


class GroupsGetAddressesResponse(pydantic.BaseModel):
    response: "GroupsGetAddressesResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total users number",
    )
    items: typing.List[GroupsBannedItem] = pydantic.Field(
        None, description="",
    )


class GroupsGetBannedResponse(pydantic.BaseModel):
    response: "GroupsGetBannedResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["GroupsGroupFull"]] = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackConfirmationCodeResponseModel(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(
        None, description="Confirmation code",
    )


class GroupsGetCallbackConfirmationCodeResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackConfirmationCodeResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackServersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="",
    )
    items: typing.List[GroupsCallbackServer] = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackServersResponse(pydantic.BaseModel):
    response: "GroupsGetCallbackServersResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsCallbackSettings"] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoExtendedResponseModel(pydantic.BaseModel):
    enabled: int = pydantic.Field(
        None, description="Information whether catalog is enabled for current user",
    )
    categories: typing.Optional[GroupsGroupCategoryFull] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoResponseModel(pydantic.BaseModel):
    enabled: int = pydantic.Field(
        None, description="Information whether catalog is enabled for current user",
    )
    categories: typing.Optional[GroupsGroupCategory] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogInfoResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[GroupsGroup] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogResponse(pydantic.BaseModel):
    response: "GroupsGetCatalogResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitedUsersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitedUsersResponse(pydantic.BaseModel):
    response: "GroupsGetInvitedUsersResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[GroupsGroupXtrInvitedBy] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserMin = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[GroupsGroupXtrInvitedBy] = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesResponse(pydantic.BaseModel):
    response: "GroupsGetInvitesResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetLongPollServerResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsLongPollServer"] = pydantic.Field(
        None, description="",
    )


class GroupsGetLongPollSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsLongPollSettings"] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total members number",
    )
    items: typing.List[GroupsUserXtrRole] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFieldsResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersFilterResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total members number",
    )
    items: typing.List[GroupsMemberRole] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersFilterResponse(pydantic.BaseModel):
    response: "GroupsGetMembersFilterResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total members number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersResponse(pydantic.BaseModel):
    response: "GroupsGetMembersResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsFieldsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsFieldsResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsResponse(pydantic.BaseModel):
    response: "GroupsGetRequestsResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsGroupSettings"] = pydantic.Field(
        None, description="",
    )


class GroupsGetTokenPermissionsResponseModel(pydantic.BaseModel):
    mask: int = pydantic.Field(
        None, description="",
    )
    permissions: GroupsTokenPermissionSetting = pydantic.Field(
        None, description="",
    )


class GroupsGetTokenPermissionsResponse(pydantic.BaseModel):
    response: "GroupsGetTokenPermissionsResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class GroupsGetExtendedResponse(pydantic.BaseModel):
    response: "GroupsGetExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class GroupsGetResponse(pydantic.BaseModel):
    response: "GroupsGetResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberExtendedResponseModel(pydantic.BaseModel):
    member: BaseBoolInt = pydantic.Field(
        None, description="Information whether user is a member of the group",
    )
    invitation: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user has been invited to the group",
    )
    can_invite: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user can be invited",
    )
    can_recall: typing.Optional[BaseBoolInt] = pydantic.Field(
        None,
        description="Information whether user's invite to the group can be recalled",
    )
    request: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="Information whether user has sent request to the group",
    )


class GroupsIsMemberExtendedResponse(pydantic.BaseModel):
    response: "GroupsIsMemberExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user is a member of the group",
    )


class GroupsIsMemberUserIdsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["GroupsMemberStatusFull"]] = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberUserIdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["GroupsMemberStatus"]] = pydantic.Field(
        None, description="",
    )


class GroupsSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total communities number",
    )
    items: typing.List[GroupsGroup] = pydantic.Field(
        None, description="",
    )


class GroupsSearchResponse(pydantic.BaseModel):
    response: "GroupsSearchResponseModel" = pydantic.Field(
        None, description="",
    )


class LeadsCheckUserResponse(pydantic.BaseModel):
    response: typing.Optional["LeadsChecked"] = pydantic.Field(
        None, description="",
    )


class LeadsCompleteResponse(pydantic.BaseModel):
    response: typing.Optional["LeadsComplete"] = pydantic.Field(
        None, description="",
    )


class LeadsGetStatsResponse(pydantic.BaseModel):
    response: typing.Optional["LeadsLead"] = pydantic.Field(
        None, description="",
    )


class LeadsGetUsersResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["LeadsEntry"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class LeadsStartResponse(pydantic.BaseModel):
    response: typing.Optional["LeadsStart"] = pydantic.Field(
        None, description="",
    )


class LikesAddResponseModel(pydantic.BaseModel):
    likes: int = pydantic.Field(
        None, description="Total likes number",
    )


class LikesAddResponse(pydantic.BaseModel):
    response: "LikesAddResponseModel" = pydantic.Field(
        None, description="",
    )


class LikesDeleteResponseModel(pydantic.BaseModel):
    likes: int = pydantic.Field(
        None, description="Total likes number",
    )


class LikesDeleteResponse(pydantic.BaseModel):
    response: "LikesDeleteResponseModel" = pydantic.Field(
        None, description="",
    )


class LikesGetListExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[UsersUserMin] = pydantic.Field(
        None, description="",
    )


class LikesGetListExtendedResponse(pydantic.BaseModel):
    response: "LikesGetListExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class LikesGetListResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class LikesGetListResponse(pydantic.BaseModel):
    response: "LikesGetListResponseModel" = pydantic.Field(
        None, description="",
    )


class LikesIsLikedResponseModel(pydantic.BaseModel):
    liked: BaseBoolInt = pydantic.Field(
        None, description="Information whether user liked the object",
    )
    copied: BaseBoolInt = pydantic.Field(
        None, description="Information whether user reposted the object",
    )


class LikesIsLikedResponse(pydantic.BaseModel):
    response: "LikesIsLikedResponseModel" = pydantic.Field(
        None, description="",
    )


class MarketAddAlbumResponseModel(pydantic.BaseModel):
    market_album_id: typing.Optional[int] = pydantic.Field(
        None, description="Album ID",
    )


class MarketAddAlbumResponse(pydantic.BaseModel):
    response: "MarketAddAlbumResponseModel" = pydantic.Field(
        None, description="",
    )


class MarketAddResponseModel(pydantic.BaseModel):
    market_item_id: typing.Optional[int] = pydantic.Field(
        None, description="Item ID",
    )


class MarketAddResponse(pydantic.BaseModel):
    response: "MarketAddResponseModel" = pydantic.Field(
        None, description="",
    )


class MarketCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )


class MarketDeleteCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
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
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class MarketRestoreCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
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
        None, description="",
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
        None, description="",
    )


class MessagesCreateChatResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Chat ID",
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
        None, description="",
    )


class MessagesDeleteConversationResponseModel(pydantic.BaseModel):
    last_deleted_id: int = pydantic.Field(
        None, description="Id of the last message, that was deleted",
    )


class MessagesDeleteConversationResponse(pydantic.BaseModel):
    response: "MessagesDeleteConversationResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesDeleteResponse(pydantic.BaseModel):
    response: dict = pydantic.Field(
        None, description="",
    )


class MessagesEditResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class MessagesGetByConversationMessageIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        None, description="",
    )


class MessagesGetByConversationMessageIdResponse(pydantic.BaseModel):
    response: "MessagesGetByConversationMessageIdResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetByIdExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdResponse(pydantic.BaseModel):
    response: "MessagesGetByIdResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetChatPreviewResponseModel(pydantic.BaseModel):
    preview: typing.Optional[MessageChatPreview] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatPreviewResponse(pydantic.BaseModel):
    response: "MessagesGetChatPreviewResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetChatChatIdsFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["MessagesChatFull"]] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatChatIdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["MessagesChat"]] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatFieldsResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesChatFull"] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesChat"] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationMembersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Chat members count",
    )
    items: typing.List[MessagesConversationMember] = pydantic.Field(
        None, description="",
    )
    chat_restrictions: typing.Optional[MessagesChatRestrictions] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationMembersResponse(pydantic.BaseModel):
    response: "MessagesGetConversationMembersResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesConversation] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUser] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdExtendedResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsByIdExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesConversation] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsByIdResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    unread_count: typing.Optional[int] = pydantic.Field(
        None, description="Unread dialogs number",
    )
    items: typing.List[MessagesConversationWithMessage] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsResponse(pydantic.BaseModel):
    response: "MessagesGetConversationsResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class MessagesGetHistoryResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class MessagesGetHistoryResponse(pydantic.BaseModel):
    response: "MessagesGetHistoryResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetInviteLinkResponseModel(pydantic.BaseModel):
    link: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class MessagesGetInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesGetInviteLinkResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesGetLastActivityResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesLastActivity"] = pydantic.Field(
        None, description="",
    )


class MessagesGetLongPollHistoryResponseModel(pydantic.BaseModel):
    history: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroup] = pydantic.Field(
        None, description="",
    )
    messages: typing.Optional[MessagesLongpollMessages] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
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
        None, description="",
    )


class MessagesGetLongPollServerResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesLongpollParams"] = pydantic.Field(
        None, description="",
    )


class MessagesIsMessagesFromGroupAllowedResponseModel(pydantic.BaseModel):
    is_allowed: typing.Optional[BaseBoolInt] = pydantic.Field(
        None, description="",
    )


class MessagesIsMessagesFromGroupAllowedResponse(pydantic.BaseModel):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesJoinChatByInviteLinkResponseModel(pydantic.BaseModel):
    chat_id: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class MessagesJoinChatByInviteLinkResponse(pydantic.BaseModel):
    response: "MessagesJoinChatByInviteLinkResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesMarkAsImportantResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class MessagesPinResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesPinnedMessage"] = pydantic.Field(
        None, description="",
    )


class MessagesSearchConversationsResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total results number",
    )
    items: typing.Optional[typing.List[MessagesConversation]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class MessagesSearchConversationsResponse(pydantic.BaseModel):
    response: "MessagesSearchConversationsResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[MessagesMessage] = pydantic.Field(
        None, description="",
    )


class MessagesSearchResponse(pydantic.BaseModel):
    response: "MessagesSearchResponseModel" = pydantic.Field(
        None, description="",
    )


class MessagesSendResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )


class MessagesSendUserIdsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[dict]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class NewsfeedGetBannedExtendedResponseModel(pydantic.BaseModel):
    groups: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedResponseModel(pydantic.BaseModel):
    groups: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    members: typing.Optional[int] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedResponse(pydantic.BaseModel):
    response: "NewsfeedGetBannedResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetCommentsResponseModel(pydantic.BaseModel):
    items: typing.List[NewsfeedNewsfeedItem] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="New from value",
    )


class NewsfeedGetCommentsResponse(pydantic.BaseModel):
    response: "NewsfeedGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[NewsfeedListFull] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsExtendedResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[NewsfeedList] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsResponse(pydantic.BaseModel):
    response: "NewsfeedGetListsResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetMentionsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallpostToId] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetMentionsResponse(pydantic.BaseModel):
    response: "NewsfeedGetMentionsResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedGetRecommendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[NewsfeedNewsfeedItem]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
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
        None, description="",
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
        None, description="",
    )


class NewsfeedGetResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[NewsfeedNewsfeedItem]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
        None, description="",
    )
    next_from: typing.Optional[str] = pydantic.Field(
        None, description="New from value",
    )


class NewsfeedGetResponse(pydantic.BaseModel):
    response: "NewsfeedGetResponseModel" = pydantic.Field(
        None, description="",
    )


class NewsfeedSaveListResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="List ID",
    )


class NewsfeedSearchExtendedResponseModel(pydantic.BaseModel):
    items: typing.Optional[typing.List[WallWallpostFull]] = pydantic.Field(
        None, description="",
    )
    profiles: typing.Optional[UsersUserFull] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroupFull] = pydantic.Field(
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
        None, description="",
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
        None, description="",
    )


class NotesAddResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Note ID",
    )


class NotesCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Comment ID",
    )


class NotesGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional["NotesNote"] = pydantic.Field(
        None, description="",
    )


class NotesGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[NotesNoteComment] = pydantic.Field(
        None, description="",
    )


class NotesGetCommentsResponse(pydantic.BaseModel):
    response: "NotesGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class NotesGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[NotesNote] = pydantic.Field(
        None, description="",
    )


class NotesGetResponse(pydantic.BaseModel):
    response: "NotesGetResponseModel" = pydantic.Field(
        None, description="",
    )


class NotificationsGetResponseModel(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(
        None, description="Total number",
    )
    profiles: typing.Optional[UsersUser] = pydantic.Field(
        None, description="",
    )
    groups: typing.Optional[GroupsGroup] = pydantic.Field(
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
        None, description="",
    )


class NotificationsMarkAsViewedResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class NotificationsSendMessageResponse(pydantic.BaseModel):
    response: typing.Optional[
        typing.List["NotificationsSendMessageItem"]
    ] = pydantic.Field(
        None, description="",
    )


class OkResponse(pydantic.BaseModel):
    response: typing.Optional["BaseOkResponse"] = pydantic.Field(
        None, description="",
    )


class OrdersCancelSubscriptionResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class OrdersChangeStateResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="New state",
    )


class OrdersGetAmountResponse(pydantic.BaseModel):
    response: typing.Optional["OrdersAmount"] = pydantic.Field(
        None, description="",
    )


class OrdersGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["OrdersOrder"]] = pydantic.Field(
        None, description="",
    )


class OrdersGetUserSubscriptionByIdResponse(pydantic.BaseModel):
    response: typing.Optional["OrdersSubscription"] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class OrdersGetResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["OrdersOrder"]] = pydantic.Field(
        None, description="",
    )


class OrdersUpdateSubscriptionResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class PagesGetHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PagesWikipageHistory"]] = pydantic.Field(
        None, description="",
    )


class PagesGetTitlesResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PagesWikipage"]] = pydantic.Field(
        None, description="",
    )


class PagesGetVersionResponse(pydantic.BaseModel):
    response: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None, description="",
    )


class PagesGetResponse(pydantic.BaseModel):
    response: typing.Optional["PagesWikipageFull"] = pydantic.Field(
        None, description="",
    )


class PagesParseWikiResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="HTML source",
    )


class PagesSaveAccessResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Page ID",
    )


class PagesSaveResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Page ID",
    )


class PhotosCopyResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Photo ID",
    )


class PhotosCreateAlbumResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoAlbumFull"] = pydantic.Field(
        None, description="",
    )


class PhotosCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Created comment ID",
    )


class PhotosDeleteCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosGetAlbumsCountResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Albums number",
    )


class PhotosGetAlbumsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhotoAlbumFull] = pydantic.Field(
        None, description="",
    )


class PhotosGetAlbumsResponse(pydantic.BaseModel):
    response: "PhotosGetAlbumsResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
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
        None, description="",
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
        None, description="",
    )


class PhotosGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhotoFull"]] = pydantic.Field(
        None, description="",
    )


class PhotosGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )


class PhotosGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    real_offset: typing.Optional[int] = pydantic.Field(
        None, description="Real offset of the comments",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class PhotosGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetCommentsExtendedResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class PhotosGetMarketUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["BaseUploadServer"] = pydantic.Field(
        None, description="",
    )


class PhotosGetMessagesUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoUpload"] = pydantic.Field(
        None, description="",
    )


class PhotosGetNewTagsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhotoXtrTagInfo] = pydantic.Field(
        None, description="",
    )


class PhotosGetNewTagsResponse(pydantic.BaseModel):
    response: "PhotosGetNewTagsResponseModel" = pydantic.Field(
        None, description="",
    )


class PhotosGetTagsResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhotoTag"]] = pydantic.Field(
        None, description="",
    )


class PhotosGetUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoUpload"] = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhotoFull] = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetUserPhotosExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhoto] = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosResponse(pydantic.BaseModel):
    response: "PhotosGetUserPhotosResponseModel" = pydantic.Field(
        None, description="",
    )


class PhotosGetWallUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoUpload"] = pydantic.Field(
        None, description="",
    )


class PhotosGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhotoFull] = pydantic.Field(
        None, description="",
    )


class PhotosGetExtendedResponse(pydantic.BaseModel):
    response: "PhotosGetExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class PhotosGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PhotosPhoto] = pydantic.Field(
        None, description="",
    )


class PhotosGetResponse(pydantic.BaseModel):
    response: "PhotosGetResponseModel" = pydantic.Field(
        None, description="",
    )


class PhotosPutTagResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Created tag ID",
    )


class PhotosRestoreCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class PhotosSaveMarketAlbumPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )


class PhotosSaveMarketPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )


class PhotosSaveMessagesPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )


class PhotosSaveOwnerCoverPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["BaseImage"]] = pydantic.Field(
        None, description="",
    )


class PhotosSaveOwnerPhotoResponseModel(pydantic.BaseModel):
    photo_hash: str = pydantic.Field(
        None, description="Photo hash",
    )
    photo_src: str = pydantic.Field(
        None, description="Uploaded image url",
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
        None, description="",
    )


class PhotosSaveWallPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
    )


class PhotosSaveResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PhotosPhoto"]] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class PollsAddVoteResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class PollsCreateResponse(pydantic.BaseModel):
    response: typing.Optional["PollsPoll"] = pydantic.Field(
        None, description="",
    )


class PollsDeleteVoteResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class PollsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional["PollsPoll"] = pydantic.Field(
        None, description="",
    )


class PollsGetVotersResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PollsVoters"]] = pydantic.Field(
        None, description="",
    )


class PrettyCardsCreateResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        None, description="Owner ID of created pretty card",
    )
    card_id: str = pydantic.Field(
        None, description="Card ID of created pretty card",
    )


class PrettyCardsCreateResponse(pydantic.BaseModel):
    response: "PrettyCardsCreateResponseModel" = pydantic.Field(
        None, description="",
    )


class PrettyCardsDeleteResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        None, description="Owner ID of deleted pretty card",
    )
    card_id: str = pydantic.Field(
        None, description="Card ID of deleted pretty card",
    )
    error: typing.Optional[str] = pydantic.Field(
        None, description="Error reason if error happened",
    )


class PrettyCardsDeleteResponse(pydantic.BaseModel):
    response: "PrettyCardsDeleteResponseModel" = pydantic.Field(
        None, description="",
    )


class PrettyCardsEditResponseModel(pydantic.BaseModel):
    owner_id: int = pydantic.Field(
        None, description="Owner ID of edited pretty card",
    )
    card_id: str = pydantic.Field(
        None, description="Card ID of edited pretty card",
    )


class PrettyCardsEditResponse(pydantic.BaseModel):
    response: "PrettyCardsEditResponseModel" = pydantic.Field(
        None, description="",
    )


class PrettyCardsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["PrettyCardsPrettyCard"]] = pydantic.Field(
        None, description="",
    )


class PrettyCardsGetUploadURLResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Upload URL",
    )


class PrettyCardsGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[PrettyCardsPrettyCard] = pydantic.Field(
        None, description="",
    )


class PrettyCardsGetResponse(pydantic.BaseModel):
    response: "PrettyCardsGetResponseModel" = pydantic.Field(
        None, description="",
    )


class SearchGetHintsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="",
    )
    items: typing.List[SearchHint] = pydantic.Field(
        None, description="",
    )
    suggested_queries: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class SearchGetHintsResponse(pydantic.BaseModel):
    response: "SearchGetHintsResponseModel" = pydantic.Field(
        None, description="",
    )


class SecureCheckTokenResponse(pydantic.BaseModel):
    response: typing.Optional["SecureTokenChecked"] = pydantic.Field(
        None, description="",
    )


class SecureGetAppBalanceResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="App balance",
    )


class SecureGetSMSHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["SecureSmsNotification"]] = pydantic.Field(
        None, description="",
    )


class SecureGetTransactionsHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["SecureTransaction"]] = pydantic.Field(
        None, description="",
    )


class SecureGetUserLevelResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["SecureLevel"]] = pydantic.Field(
        None, description="",
    )


class SecureGiveEventStickerResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[dict]] = pydantic.Field(
        None, description="",
    )


class SecureSendNotificationResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class StatsGetPostReachResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["StatsWallpostStat"]] = pydantic.Field(
        None, description="",
    )


class StatsGetResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["StatsPeriod"]] = pydantic.Field(
        None, description="",
    )


class StatusGetResponse(pydantic.BaseModel):
    response: typing.Optional["StatusStatus"] = pydantic.Field(
        None, description="",
    )


class StorageGetKeysResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )


# fixme maybe for storage.get?
# class StorageGetKeysResponse(pydantic.BaseModel):
#     response: typing.Optional[typing.List["StorageValue"]] = pydantic.Field(
#         None, description="",
#     )


class StorageGetResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Value of key",
    )


class StoriesGetBannedExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class StoriesGetBannedExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetBannedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class StoriesGetBannedResponse(pydantic.BaseModel):
    response: "StoriesGetBannedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetByIdExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdResponse(pydantic.BaseModel):
    response: "StoriesGetByIdResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetPhotoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: str = pydantic.Field(
        None, description="Upload URL",
    )
    user_ids: int = pydantic.Field(
        None, description="Users ID who can to see story.",
    )


class StoriesGetPhotoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetPhotoUploadServerResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetRepliesExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesResponse(pydantic.BaseModel):
    response: "StoriesGetRepliesResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetStatsResponse(pydantic.BaseModel):
    response: typing.Optional["StoriesStoryStats"] = pydantic.Field(
        None, description="",
    )


class StoriesGetVideoUploadServerResponseModel(pydantic.BaseModel):
    upload_url: str = pydantic.Field(
        None, description="Upload URL",
    )
    user_ids: int = pydantic.Field(
        None, description="Users ID who can to see story.",
    )


class StoriesGetVideoUploadServerResponse(pydantic.BaseModel):
    response: "StoriesGetVideoUploadServerResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Viewers count",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetViewersExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Viewers count",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersResponse(pydantic.BaseModel):
    response: "StoriesGetViewersResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[list] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUser = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroup = pydantic.Field(
        None, description="",
    )


class StoriesGetExtendedResponse(pydantic.BaseModel):
    response: "StoriesGetExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Stories count",
    )
    items: typing.List[StoriesStory] = pydantic.Field(
        None, description="",
    )
    promo_data: typing.Optional[StoriesPromoBlock] = pydantic.Field(
        None, description="",
    )


class StoriesGetResponse(pydantic.BaseModel):
    response: "StoriesGetResponseModel" = pydantic.Field(
        None, description="",
    )


class StoriesUploadResponseModel(pydantic.BaseModel):
    story: StoriesStory = pydantic.Field(
        None, description="",
    )


class StoriesUploadResponse(pydantic.BaseModel):
    response: "StoriesUploadResponseModel" = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class UsersGetFollowersFieldsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number of available results",
    )
    items: typing.List[UsersUserFull] = pydantic.Field(
        None, description="",
    )


class UsersGetFollowersFieldsResponse(pydantic.BaseModel):
    response: "UsersGetFollowersFieldsResponseModel" = pydantic.Field(
        None, description="",
    )


class UsersGetFollowersResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total friends number",
    )
    items: typing.List[int] = pydantic.Field(
        None, description="",
    )


class UsersGetFollowersResponse(pydantic.BaseModel):
    response: "UsersGetFollowersResponseModel" = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number of available results",
    )
    items: typing.List[UsersSubscriptionsItem] = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsExtendedResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsResponseModel(pydantic.BaseModel):
    users: UsersUsersArray = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupsArray = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsResponse(pydantic.BaseModel):
    response: "UsersGetSubscriptionsResponseModel" = pydantic.Field(
        None, description="",
    )


class UsersGetResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["UsersUserXtrCounters"]] = pydantic.Field(
        None, description="",
    )


class UsersIsAppUserResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user have installed an app",
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
        None, description="",
    )


class UtilsCheckLinkResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsLinkChecked"] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class UtilsGetLinkStatsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsLinkStatsExtended"] = pydantic.Field(
        None, description="",
    )


class UtilsGetLinkStatsResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsLinkStats"] = pydantic.Field(
        None, description="",
    )


class UtilsGetServerTimeResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Time as Unixtime",
    )


class UtilsGetShortLinkResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsShortLink"] = pydantic.Field(
        None, description="",
    )


class UtilsResolveScreenNameResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsDomainResolved"] = pydantic.Field(
        None, description="",
    )


class VideoAddAlbumResponseModel(pydantic.BaseModel):
    album_id: int = pydantic.Field(
        None, description="Created album ID",
    )


class VideoAddAlbumResponse(pydantic.BaseModel):
    response: "VideoAddAlbumResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Created comment ID",
    )


class VideoGetAlbumByIdResponse(pydantic.BaseModel):
    response: typing.Optional["VideoVideoAlbumFull"] = pydantic.Field(
        None, description="",
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
        None, description="",
    )


class VideoGetAlbumsByVideoResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List[int]] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideoAlbumFull] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideoAlbumFull] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsResponse(pydantic.BaseModel):
    response: "VideoGetAlbumsResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserMin = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "VideoGetCommentsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsResponse(pydantic.BaseModel):
    response: "VideoGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideoFull] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserMin = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class VideoGetExtendedResponse(pydantic.BaseModel):
    response: "VideoGetExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        None, description="",
    )


class VideoGetResponse(pydantic.BaseModel):
    response: "VideoGetResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoRestoreCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Returns 1 if request has been processed successfully, 0 if the comment is not found",
    )


class VideoSaveResponse(pydantic.BaseModel):
    response: typing.Optional["VideoSaveResult"] = pydantic.Field(
        None, description="",
    )


class VideoSearchExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserMin = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class VideoSearchExtendedResponse(pydantic.BaseModel):
    response: "VideoSearchExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class VideoSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[VideoVideo] = pydantic.Field(
        None, description="",
    )


class VideoSearchResponse(pydantic.BaseModel):
    response: "VideoSearchResponseModel" = pydantic.Field(
        None, description="",
    )


class WallCreateCommentResponseModel(pydantic.BaseModel):
    comment_id: int = pydantic.Field(
        None, description="Created comment ID",
    )


class WallCreateCommentResponse(pydantic.BaseModel):
    response: "WallCreateCommentResponseModel" = pydantic.Field(
        None, description="",
    )


class WallEditResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        None, description="Edited post ID",
    )


class WallEditResponse(pydantic.BaseModel):
    response: "WallEditResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetByIdExtendedResponseModel(pydantic.BaseModel):
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class WallGetByIdExtendedResponse(pydantic.BaseModel):
    response: "WallGetByIdExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[typing.List["WallWallpostFull"]] = pydantic.Field(
        None, description="",
    )


class WallGetCommentsExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
        None, description="",
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
    profiles: UsersUser = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroup = pydantic.Field(
        None, description="",
    )


class WallGetCommentsExtendedResponse(pydantic.BaseModel):
    response: "WallGetCommentsExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallComment] = pydantic.Field(
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


class WallGetCommentsResponse(pydantic.BaseModel):
    response: "WallGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetRepostsResponseModel(pydantic.BaseModel):
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUser = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroup = pydantic.Field(
        None, description="",
    )


class WallGetRepostsResponse(pydantic.BaseModel):
    response: "WallGetRepostsResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class WallGetExtendedResponse(pydantic.BaseModel):
    response: "WallGetExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class WallGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )


class WallGetResponse(pydantic.BaseModel):
    response: "WallGetResponseModel" = pydantic.Field(
        None, description="",
    )


class WallPostAdsStealthResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        None, description="Created post ID",
    )


class WallPostAdsStealthResponse(pydantic.BaseModel):
    response: "WallPostAdsStealthResponseModel" = pydantic.Field(
        None, description="",
    )


class WallPostResponseModel(pydantic.BaseModel):
    post_id: int = pydantic.Field(
        None, description="Created post ID",
    )


class WallPostResponse(pydantic.BaseModel):
    response: "WallPostResponseModel" = pydantic.Field(
        None, description="",
    )


class WallRepostResponseModel(pydantic.BaseModel):
    success: BaseOkResponse = pydantic.Field(
        None, description="",
    )
    post_id: int = pydantic.Field(
        None, description="Created post ID",
    )
    reposts_count: int = pydantic.Field(
        None, description="Reposts number",
    )
    likes_count: int = pydantic.Field(
        None, description="Reposts number",
    )


class WallRepostResponse(pydantic.BaseModel):
    response: "WallRepostResponseModel" = pydantic.Field(
        None, description="",
    )


class WallSearchExtendedResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )
    profiles: UsersUserFull = pydantic.Field(
        None, description="",
    )
    groups: GroupsGroupFull = pydantic.Field(
        None, description="",
    )


class WallSearchExtendedResponse(pydantic.BaseModel):
    response: "WallSearchExtendedResponseModel" = pydantic.Field(
        None, description="",
    )


class WallSearchResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    items: typing.List[WallWallpostFull] = pydantic.Field(
        None, description="",
    )


class WallSearchResponse(pydantic.BaseModel):
    response: "WallSearchResponseModel" = pydantic.Field(
        None, description="",
    )


class WidgetsGetCommentsResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    posts: WidgetsWidgetComment = pydantic.Field(
        None, description="",
    )


class WidgetsGetCommentsResponse(pydantic.BaseModel):
    response: "WidgetsGetCommentsResponseModel" = pydantic.Field(
        None, description="",
    )


class WidgetsGetPagesResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(
        None, description="Total number",
    )
    pages: WidgetsWidgetPage = pydantic.Field(
        None, description="",
    )


class WidgetsGetPagesResponse(pydantic.BaseModel):
    response: "WidgetsGetPagesResponseModel" = pydantic.Field(
        None, description="",
    )
