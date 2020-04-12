from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Friends(Category):
    async def add(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        text: typing.Optional[BaseBoolInt] = None,
        follow: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, FriendsAddResponse]:
        """
        :param user_id: - ID of the user whose friend request will be approved or to whom a friend request will be sent.
        :param text: - Text of the message (up to 500 characters) for the friend request, if any.
        :param follow: - '1' to pass an incoming request to followers list.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("add", params)
        if return_raw_response:
            return raw_result

        result = FriendsAddResponse(**raw_result)
        return result

    async def add_list(
        self,
        name: str,
        return_raw_response: bool = False,
        user_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, FriendsAddListResponse]:
        """
        :param name: - Name of the friend list.
        :param user_ids: - IDs of users to be added to the friend list.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addList", params)
        if return_raw_response:
            return raw_result

        result = FriendsAddListResponse(**raw_result)
        return result

    async def are_friends(
        self,
        user_ids: typing.List[int],
        return_raw_response: bool = False,
        need_sign: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, FriendsAreFriendsResponse]:
        """
        :param user_ids: - IDs of the users whose friendship status to check.
        :param need_sign: - '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("areFriends", params)
        if return_raw_response:
            return raw_result

        result = FriendsAreFriendsResponse(**raw_result)
        return result

    async def delete(
        self, return_raw_response: bool = False, user_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, FriendsDeleteResponse]:
        """
        :param user_id: - ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = FriendsDeleteResponse(**raw_result)
        return result

    async def delete_all_requests(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteAllRequests", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def delete_list(
        self, list_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param list_id: - ID of the friend list to delete.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteList", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        user_id: int,
        return_raw_response: bool = False,
        list_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id: - ID of the user whose friend list is to be edited.
        :param list_ids: - IDs of the friend lists to which to add the user.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit_list(
        self,
        list_id: int,
        return_raw_response: bool = False,
        name: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        add_user_ids: typing.Optional[typing.List[int]] = None,
        delete_user_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param name: - Name of the friend list.
        :param list_id: - Friend list ID.
        :param user_ids: - IDs of users in the friend list.
        :param add_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: - (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editList", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        list_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        ref: typing.Optional[str] = None,
    ) -> typing.Union[dict, FriendsGetResponse]:
        """
        :param user_id: - User ID. By default, the current user ID.
        :param order: - Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param list_id: - ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param count: - Number of friends to return.
        :param offset: - Offset needed to return a specific subset of friends.
        :param fields: - Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param ref:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetResponse(**raw_result)
        return result

    async def get_app_users(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, FriendsGetAppUsersResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAppUsers", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetAppUsersResponse(**raw_result)
        return result

    async def get_by_phones(
        self,
        return_raw_response: bool = False,
        phones: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, FriendsGetByPhonesResponse]:
        """
        :param phones: - List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getByPhones", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetByPhonesResponse(**raw_result)
        return result

    async def get_lists(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        return_system: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, FriendsGetListsResponse]:
        """
        :param user_id: - User ID.
        :param return_system: - '1' — to return system friend lists. By default: '0'.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLists", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetListsResponse(**raw_result)
        return result

    async def get_mutual(
        self,
        return_raw_response: bool = False,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        target_uids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, FriendsGetMutualResponse]:
        """
        :param source_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: - ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param target_uids: - IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param order: - Sort order: 'random' — random order
        :param count: - Number of mutual friends to return.
        :param offset: - Offset needed to return a specific subset of mutual friends.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMutual", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetMutualResponse(**raw_result)
        return result

    async def get_online(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        online_mobile: typing.Optional[BaseBoolInt] = None,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, FriendsGetOnlineResponse]:
        """
        :param user_id: - User ID.
        :param list_id: - Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param online_mobile: - '1' — to return an additional 'online_mobile' field, '0' — (default),
        :param order: - Sort order: 'random' — random order
        :param count: - Number of friends to return.
        :param offset: - Offset needed to return a specific subset of friends.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getOnline", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetOnlineResponse(**raw_result)
        return result

    async def get_recent(
        self, return_raw_response: bool = False, count: typing.Optional[int] = None,
    ) -> typing.Union[dict, FriendsGetRecentResponse]:
        """
        :param count: - Number of recently added friends to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRecent", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetRecentResponse(**raw_result)
        return result

    async def get_requests(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        need_mutual: typing.Optional[BaseBoolInt] = None,
        out: typing.Optional[BaseBoolInt] = None,
        sort: typing.Optional[BaseBoolInt] = None,
        need_viewed: typing.Optional[bool] = None,
        suggested: typing.Optional[BaseBoolInt] = None,
        ref: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, FriendsGetRequestsResponse, FriendsGetRequestsExtendedResponse]:
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
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRequests", params)
        if return_raw_response:
            return raw_result

        result = (
            FriendsGetRequestsResponse(**raw_result)
            if not extended
            else FriendsGetRequestsExtendedResponse(**raw_result)
        )
        return result

    async def get_suggestions(
        self,
        return_raw_response: bool = False,
        filter: typing.Optional[typing.List[str]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> typing.Union[dict, FriendsGetSuggestionsResponse]:
        """
        :param filter: - Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param count: - Number of suggestions to return.
        :param offset: - Offset needed to return a specific subset of suggestions.
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSuggestions", params)
        if return_raw_response:
            return raw_result

        result = FriendsGetSuggestionsResponse(**raw_result)
        return result

    async def search(
        self,
        user_id: int,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, FriendsSearchResponse]:
        """
        :param user_id: - User ID.
        :param q: - Search query string (e.g., 'Vasya Babich').
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param offset: - Offset needed to return a specific subset of friends.
        :param count: - Number of friends to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = FriendsSearchResponse(**raw_result)
        return result
