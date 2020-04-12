from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Apps(Category):
    async def delete_app_requests(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteAppRequests", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        app_id: typing.Optional[int] = None,
        app_ids: typing.Optional[typing.List[str]] = None,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> typing.Union[dict, AppsGetResponse]:
        """
        :param app_id: - Application ID
        :param app_ids: - List of application ID
        :param platform: - platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
        :param extended:
        :param return_friends:
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = AppsGetResponse(**raw_result)
        return result

    async def get_catalog(
        self,
        count: int,
        return_raw_response: bool = False,
        sort: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        genre_id: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
    ) -> typing.Union[dict, AppsGetCatalogResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCatalog", params)
        if return_raw_response:
            return raw_result

        result = AppsGetCatalogResponse(**raw_result)
        return result

    async def get_friends_list(
        self,
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, AppsGetFriendsListResponse]:
        """
        :param extended:
        :param count: - List size.
        :param offset:
        :param type: - List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
        :param fields: - Additional profile fields, see [vk.com/dev/fields|description].
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFriendsList", params)
        if return_raw_response:
            return raw_result

        result = AppsGetFriendsListResponse(**raw_result)
        return result

    async def get_leaderboard(
        self,
        type: str,
        return_raw_response: bool = False,
        global_: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, AppsGetLeaderboardResponse, AppsGetLeaderboardExtendedResponse]:
        """
        :param type: - Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
        :param global_: - Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
        :param extended: - 1 — to return additional info about users
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLeaderboard", params)
        if return_raw_response:
            return raw_result

        result = (
            AppsGetLeaderboardResponse(**raw_result)
            if not extended
            else AppsGetLeaderboardExtendedResponse(**raw_result)
        )
        return result

    async def get_scopes(
        self, return_raw_response: bool = False, type: typing.Optional[str] = None,
    ) -> typing.Union[dict, AppsGetScopesResponse]:
        """
        :param type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getScopes", params)
        if return_raw_response:
            return raw_result

        result = AppsGetScopesResponse(**raw_result)
        return result

    async def get_score(
        self, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, AppsGetScoreResponse]:
        """
        :param user_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getScore", params)
        if return_raw_response:
            return raw_result

        result = AppsGetScoreResponse(**raw_result)
        return result

    async def send_request(
        self,
        user_id: int,
        return_raw_response: bool = False,
        text: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        separate: typing.Optional[bool] = None,
    ) -> typing.Union[dict, AppsSendRequestResponse]:
        """
        :param user_id: - id of the user to send a request
        :param text: - request text
        :param type: - request type. Values: 'invite' – if the request is sent to a user who does not have the app installed,, 'request' – if a user has already installed the app
        :param name:
        :param key: - special string key to be sent with the request
        :param separate:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendRequest", params)
        if return_raw_response:
            return raw_result

        result = AppsSendRequestResponse(**raw_result)
        return result
