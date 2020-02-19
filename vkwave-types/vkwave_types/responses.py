from .objects import *


class AccountChangePasswordResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AccountGetActiveOffersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AccountGetAppPermissionsResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Permissions mask",
    )


class AccountGetBannedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class AccountSaveProfileInfoResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsCreateCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsCreateClientsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsCreateTargetGroupResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AdsDeleteAdsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsLayoutResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsTargetingResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetAdsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetBudgetResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Budget",
    )


class AdsGetCampaignsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetCategoriesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AdsGetClientsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetDemographicsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetFloodStatsResponse(pydantic.BaseModel):
    response: typing.Optional["AdsFloodStats"] = pydantic.Field(
        None, description="",
    )


class AdsGetOfficeUsersResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetPostsReachResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetRejectionReasonResponse(pydantic.BaseModel):
    response: typing.Optional["AdsRejectReason"] = pydantic.Field(
        None, description="",
    )


class AdsGetStatisticsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsCitiesResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsRegionsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetSuggestionsSchoolsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class AdsGetTargetGroupsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
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


class AppsGetCatalogResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsGetFriendsListResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsGetLeaderboardExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsGetLeaderboardResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsGetScopesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsGetScoreResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Score number",
    )


class AppsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class AppsSendRequestResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Request ID",
    )


class AuthRestoreResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class BoardGetCommentsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class BoardGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class BoardGetTopicsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class BoardGetTopicsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetChairsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCitiesByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCitiesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCountriesByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class DatabaseGetCountriesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetFacultiesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetMetroStationsByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class DatabaseGetMetroStationsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetRegionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetSchoolClassesResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class DatabaseGetSchoolsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DatabaseGetUniversitiesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DocsAddResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DocsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class DocsGetTypesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DocsGetUploadServer(pydantic.BaseModel):
    response: typing.Optional["BaseUploadServer"] = pydantic.Field(
        None, description="",
    )


class DocsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DocsSaveResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class DocsSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FaveAddTagResponse(pydantic.BaseModel):
    response: typing.Optional["FaveTag"] = pydantic.Field(
        None, description="",
    )


class FaveGetPagesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FaveGetTagsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FaveGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FaveGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsAddListResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsAddResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Friend request status",
    )


class FriendsAreFriendsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsDeleteResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetAppUsersResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetByPhonesResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetListsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetMutualResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetMutualTargetUidsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetOnlineOnlineMobileResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetOnlineResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetRecentResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class FriendsGetRequestsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetRequestsNeedMutualResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetRequestsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetSuggestionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class FriendsSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GiftsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsAddCallbackServerResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class GroupsGetAddressesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetBannedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackConfirmationCodeResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackServersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetCallbackSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsCallbackSettings"] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogInfoResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetCatalogResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitedUsersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetInvitesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class GroupsGetMembersFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersFilterResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetMembersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetRequestsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetSettingsResponse(pydantic.BaseModel):
    response: typing.Optional["GroupsGroupSettings"] = pydantic.Field(
        None, description="",
    )


class GroupsGetTokenPermissionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether user is a member of the group",
    )


class GroupsIsMemberUserIdsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class GroupsIsMemberUserIdsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class GroupsSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class LeadsMetricHitResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class LeadsStartResponse(pydantic.BaseModel):
    response: typing.Optional["LeadsStart"] = pydantic.Field(
        None, description="",
    )


class LikesAddResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class LikesDeleteResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class LikesGetListExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class LikesGetListResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class LikesIsLikedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketAddAlbumResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketAddResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class MarketGetAlbumByIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetAlbumsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetCategoriesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketRestoreCommentResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None,
        description="Returns 1 if request has been processed successfully (0 if the comment is not found)",
    )


class MarketSearchExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MarketSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesCreateChatResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Chat ID",
    )


class MessagesDeleteChatPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesDeleteConversationResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesDeleteResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesEditResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class MessagesGetByConversationMessageIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatPreviewResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatChatIdsFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class MessagesGetChatChatIdsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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


class MessagesGetConversationMembersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsByIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetConversationsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetHistoryAttachmentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetInviteLinkResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetLastActivityResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesLastActivity"] = pydantic.Field(
        None, description="",
    )


class MessagesGetLongPollHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesGetLongPollServerResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesLongpollParams"] = pydantic.Field(
        None, description="",
    )


class MessagesIsMessagesFromGroupAllowedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesJoinChatByInviteLinkResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesMarkAsImportantResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class MessagesPinResponse(pydantic.BaseModel):
    response: typing.Optional["MessagesPinnedMessage"] = pydantic.Field(
        None, description="",
    )


class MessagesSearchConversationsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class MessagesSendResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="Message ID",
    )


class MessagesSendUserIdsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class MessagesSetChatPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetBannedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetListsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetMentionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetRecommendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetSuggestedSourcesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedSaveListResponse(pydantic.BaseModel):
    response: typing.Optional[int] = pydantic.Field(
        None, description="List ID",
    )


class NewsfeedSearchExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NewsfeedSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class NotesGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NotesGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NotificationsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class NotificationsMarkAsViewedResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class NotificationsSendMessageResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class OrdersGetUserSubscriptionByIdResponse(pydantic.BaseModel):
    response: typing.Optional["OrdersSubscription"] = pydantic.Field(
        None, description="",
    )


class OrdersGetUserSubscriptionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class OrdersGetResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class OrdersUpdateSubscriptionResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Result",
    )


class PagesGetHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PagesGetTitlesResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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


class PhotosGetAlbumsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetAllCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetAllExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetAllResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosGetCommentsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class PhotosGetNewTagsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetTagsResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosGetUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoUpload"] = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetUserPhotosResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetWallUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional["PhotosPhotoUpload"] = pydantic.Field(
        None, description="",
    )


class PhotosGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSaveMarketPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSaveMessagesPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSaveOwnerCoverPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSaveOwnerPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PhotosSaveWallPhotoResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSaveResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PhotosSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PrettyCardsCreateResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PrettyCardsDeleteResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PrettyCardsEditResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class PrettyCardsGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class PrettyCardsGetUploadURLResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Upload URL",
    )


class PrettyCardsGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class SearchGetHintsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class SecureGetTransactionsHistoryResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class SecureGetUserLevelResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class SecureGiveEventStickerResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class SecureSendNotificationResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class StatsGetPostReachResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class StatsGetResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
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


class StorageGetKeysResponseWithStorageValue(pydantic.BaseModel):
    response: typing.Optional[typing.List["StorageValue"]] = pydantic.Field(
        None, description="",
    )


class StorageGetResponse(pydantic.BaseModel):
    response: typing.Optional[str] = pydantic.Field(
        None, description="Value of key",
    )


class StoriesGetBannedExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetBannedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetPhotoUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetRepliesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetStatsResponse(pydantic.BaseModel):
    response: typing.Optional["StoriesStoryStats"] = pydantic.Field(
        None, description="",
    )


class StoriesGetVideoUploadServerResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetViewersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StoriesUploadResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class StreamingGetServerUrlResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UsersGetFollowersFieldsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UsersGetFollowersResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UsersGetSubscriptionsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UsersGetResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class UsersIsAppUserResponse(pydantic.BaseModel):
    response: typing.Optional["BaseBoolInt"] = pydantic.Field(
        None, description="Information whether the user have installed an app",
    )


class UsersSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class UtilsCheckLinkResponse(pydantic.BaseModel):
    response: typing.Optional["UtilsLinkChecked"] = pydantic.Field(
        None, description="",
    )


class UtilsGetLastShortenedLinksResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class VideoAddAlbumResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class VideoGetAlbumsByVideoExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsByVideoResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetAlbumsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
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


class VideoSearchExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class VideoSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallCreateCommentResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallEditResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetByIdExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetByIdResponse(pydantic.BaseModel):
    response: typing.Optional[list] = pydantic.Field(
        None, description="",
    )


class WallGetCommentsExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetRepostsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallGetResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallPostAdsStealthResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallPostResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallRepostResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallSearchExtendedResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WallSearchResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WidgetsGetCommentsResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class WidgetsGetPagesResponse(pydantic.BaseModel):
    response: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )
