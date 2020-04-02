from vkwave.types.responses import *

from ._category import Category


class Apps(Category):
    async def delete_app_requests(self,) -> OkResponse:
        """
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("deleteAppRequests", params)
        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        app_id: typing.Optional[int] = None,
        app_ids: typing.Optional[typing.List[str]] = None,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
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

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("get", params)
        result = AppsGetResponse(**raw_result)
        return result

    async def get_catalog(
        self,
        sort: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: int = None,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        genre_id: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
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

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getCatalog", params)
        result = AppsGetCatalogResponse(**raw_result)
        return result

    async def get_friends_list(
        self,
        extended: typing.Optional[BaseBoolInt] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> AppsGetFriendsListResponse:
        """
        :param extended:
        :param count: - List size.
        :param offset:
        :param type: - List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
        :param fields: - Additional profile fields, see [vk.com/dev/fields|description].
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getFriendsList", params)
        result = AppsGetFriendsListResponse(**raw_result)
        return result

    async def get_leaderboard(
        self,
        type: str = None,
        global_: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[AppsGetLeaderboardResponse, AppsGetLeaderboardExtendedResponse]:
        """
        :param type: - Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
        :param global_: - Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
        :param extended: - 1 — to return additional info about users
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getLeaderboard", params)

        result = (
            AppsGetLeaderboardResponse(**raw_result)
            if not extended
            else AppsGetLeaderboardExtendedResponse(**raw_result)
        )
        return result

    async def get_scopes(self, type: typing.Optional[str] = None,) -> AppsGetScopesResponse:
        """
        :param type:
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getScopes", params)
        result = AppsGetScopesResponse(**raw_result)
        return result

    async def get_score(self, user_id: int = None,) -> AppsGetScoreResponse:
        """
        :param user_id:
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getScore", params)
        result = AppsGetScoreResponse(**raw_result)
        return result

    async def send_request(
        self,
        user_id: int = None,
        text: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        separate: typing.Optional[bool] = None,
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

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("sendRequest", params)
        result = AppsSendRequestResponse(**raw_result)
        return result
