from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Polls(Category):
    async def add_vote(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
    ) -> typing.Union[dict, PollsAddVoteResponse]:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: - Poll ID.
        :param answer_ids:
        :param is_board:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addVote", params)
        if return_raw_response:
            return raw_result

        result = PollsAddVoteResponse(**raw_result)
        return result

    async def create(
        self,
        return_raw_response: bool = False,
        question: typing.Optional[str] = None,
        is_anonymous: typing.Optional[BaseBoolInt] = None,
        is_multiple: typing.Optional[bool] = None,
        end_date: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        add_answers: typing.Optional[BaseBoolInt] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
    ) -> typing.Union[dict, PollsCreateResponse]:
        """
        :param question: - question text
        :param is_anonymous: - '1' – anonymous poll, participants list is hidden,, '0' – public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param end_date:
        :param owner_id: - If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param add_answers: - available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param photo_id:
        :param background_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("create", params)
        if return_raw_response:
            return raw_result

        result = PollsCreateResponse(**raw_result)
        return result

    async def delete_vote(
        self,
        poll_id: int,
        answer_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
    ) -> typing.Union[dict, PollsDeleteVoteResponse]:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: - Poll ID.
        :param answer_id: - Answer ID.
        :param is_board:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteVote", params)
        if return_raw_response:
            return raw_result

        result = PollsDeleteVoteResponse(**raw_result)
        return result

    async def edit(
        self,
        poll_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        question: typing.Optional[str] = None,
        add_answers: typing.Optional[str] = None,
        edit_answers: typing.Optional[BaseBoolInt] = None,
        delete_answers: typing.Optional[BaseBoolInt] = None,
        end_date: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param owner_id: - poll owner id
        :param poll_id: - edited poll's id
        :param question: - new question text
        :param add_answers: - answers list, for example: , "["yes","no","maybe"]"
        :param edit_answers: - object containing answers that need to be edited,, key – answer id, value – new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param delete_answers: - list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param end_date:
        :param photo_id:
        :param background_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        poll_id: int,
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        friends_count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
    ) -> typing.Union[dict, PollsGetByIdResponse]:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: - '1' – poll is in a board, '0' – poll is on a wall. '0' by default.
        :param poll_id: - Poll ID.
        :param extended:
        :param friends_count:
        :param fields:
        :param name_case:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = PollsGetByIdResponse(**raw_result)
        return result

    async def get_voters(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        return_raw_response: bool = False,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        friends_only: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[BaseBoolInt] = None,
        count: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
    ) -> typing.Union[dict, PollsGetVotersResponse]:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: - Poll ID.
        :param answer_ids: - Answer IDs.
        :param is_board:
        :param friends_only: - '1' — to return only current user's friends, '0' — to return all users (default),
        :param offset: - Offset needed to return a specific subset of voters. '0' — (default)
        :param count: - Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' — (default)
        :param fields: - Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: - Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getVoters", params)
        if return_raw_response:
            return raw_result

        result = PollsGetVotersResponse(**raw_result)
        return result
