from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Users(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        user_ids: Optional[List[str]] = None,
        fields: Optional[List[UsersFields]] = None,
        name_case: Optional[str] = None,
    ) -> Union[dict, UsersGetResponse]:
        """
        :param user_ids: - User IDs or screen names ('screen_name'). By default, current user ID.
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = UsersGetResponse(**raw_result)
        return result

    async def get_followers(
        self,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
        name_case: Optional[str] = None,
    ) -> Union[dict, UsersGetFollowersResponse, UsersGetFollowersFieldsResponse]:
        """
        :param user_id: - User ID.
        :param offset: - Offset needed to return a specific subset of followers.
        :param count: - Number of followers to return.
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
        :param name_case: - Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFollowers", params)
        if return_raw_response:
            return raw_result

        result = (
            UsersGetFollowersResponse(**raw_result)
            if not fields
            else UsersGetFollowersFieldsResponse(**raw_result)
        )
        return result

    async def get_subscriptions(
        self,
        return_raw_response: bool = False,
        user_id: Optional[int] = None,
        extended: Optional[BaseBoolInt] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
    ) -> Union[dict, UsersGetSubscriptionsResponse, UsersGetSubscriptionsExtendedResponse]:
        """
        :param user_id: - User ID.
        :param extended: - '1' — to return a combined list of users and communities, '0' — to return separate lists of users and communities (default)
        :param offset: - Offset needed to return a specific subset of subscriptions.
        :param count: - Number of users and communities to return.
        :param fields:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSubscriptions", params)
        if return_raw_response:
            return raw_result

        result = (
            UsersGetSubscriptionsResponse(**raw_result)
            if not extended
            else UsersGetSubscriptionsExtendedResponse(**raw_result)
        )
        return result

    async def report(
        self,
        user_id: int,
        type: str,
        return_raw_response: bool = False,
        comment: Optional[str] = None,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param user_id: - ID of the user about whom a complaint is being made.
        :param type: - Type of complaint: 'porn' – pornography, 'spam' – spamming, 'insult' – abusive behavior, 'advertisement' – disruptive advertisements
        :param comment: - Comment describing the complaint.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("report", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result

    async def search(
        self,
        return_raw_response: bool = False,
        q: Optional[str] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List[UsersFields]] = None,
        city: Optional[int] = None,
        country: Optional[int] = None,
        hometown: Optional[str] = None,
        university_country: Optional[int] = None,
        university: Optional[int] = None,
        university_year: Optional[int] = None,
        university_faculty: Optional[int] = None,
        university_chair: Optional[int] = None,
        sex: Optional[int] = None,
        status: Optional[int] = None,
        age_from: Optional[int] = None,
        age_to: Optional[int] = None,
        birth_day: Optional[int] = None,
        birth_month: Optional[int] = None,
        birth_year: Optional[int] = None,
        online: Optional[BaseBoolInt] = None,
        has_photo: Optional[BaseBoolInt] = None,
        school_country: Optional[int] = None,
        school_city: Optional[int] = None,
        school_class: Optional[int] = None,
        school: Optional[int] = None,
        school_year: Optional[int] = None,
        religion: Optional[str] = None,
        company: Optional[str] = None,
        position: Optional[str] = None,
        group_id: Optional[int] = None,
        from_list: Optional[List[str]] = None,
    ) -> Union[dict, UsersSearchResponse]:
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
        :param company: - Name of the company where users work.
        :param position: - Job position.
        :param group_id: - ID of a community to search in communities.
        :param from_list:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = UsersSearchResponse(**raw_result)
        return result
