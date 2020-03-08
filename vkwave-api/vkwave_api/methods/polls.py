from vkwave_types.responses import *
from ._category import Category


class Polls(Category):
    def add_vote(
        self,
        owner_id: typing.Optional[int],
        poll_id: typing.Optional[int],
        answer_ids: typing.Optional[typing.List[int]],
        is_board: typing.Optional[bool],
    ) -> PollsAddVoteResponse:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: - Poll ID.
        :param answer_ids:
        :param is_board:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("addVote", params)
        result = PollsAddVoteResponse(**raw_result)
        return result

    def create(
        self,
        question: typing.Optional[str],
        is_anonymous: typing.Optional[bool],
        is_multiple: typing.Optional[bool],
        end_date: typing.Optional[int],
        owner_id: typing.Optional[int],
        add_answers: typing.Optional[str],
        photo_id: typing.Optional[int],
        background_id: typing.Optional[str],
    ) -> PollsCreateResponse:
        """
        :param question: - question text
        :param is_anonymous: - '1' – anonymous poll, participants list is hidden,, '0' – public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param end_date:
        :param owner_id: - If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param add_answers: - available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param photo_id:
        :param background_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("create", params)
        result = PollsCreateResponse(**raw_result)
        return result

    def delete_vote(
        self,
        owner_id: typing.Optional[int],
        poll_id: typing.Optional[int],
        answer_id: typing.Optional[int],
        is_board: typing.Optional[bool],
    ) -> PollsDeleteVoteResponse:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: - Poll ID.
        :param answer_id: - Answer ID.
        :param is_board:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("deleteVote", params)
        result = PollsDeleteVoteResponse(**raw_result)
        return result

    def edit(
        self,
        owner_id: typing.Optional[int],
        poll_id: typing.Optional[int],
        question: typing.Optional[str],
        add_answers: typing.Optional[str],
        edit_answers: typing.Optional[str],
        delete_answers: typing.Optional[str],
        end_date: typing.Optional[int],
        photo_id: typing.Optional[int],
        background_id: typing.Optional[str],
    ) -> OkResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    def get_by_id(
        self,
        owner_id: typing.Optional[int],
        is_board: typing.Optional[bool],
        poll_id: typing.Optional[int],
        extended: typing.Optional[bool],
        friends_count: typing.Optional[int],
        fields: typing.Optional[typing.List[str]],
        name_case: typing.Optional[str],
    ) -> PollsGetByIdResponse:
        """
        :param owner_id: - ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: - '1' – poll is in a board, '0' – poll is on a wall. '0' by default.
        :param poll_id: - Poll ID.
        :param extended:
        :param friends_count:
        :param fields:
        :param name_case:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = PollsGetByIdResponse(**raw_result)
        return result

    def get_voters(
        self,
        owner_id: typing.Optional[int],
        poll_id: typing.Optional[int],
        answer_ids: typing.Optional[typing.List[int]],
        is_board: typing.Optional[bool],
        friends_only: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        fields: typing.Optional[typing.List[UsersFields]],
        name_case: typing.Optional[str],
    ) -> PollsGetVotersResponse:
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
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getVoters", params)
        result = PollsGetVotersResponse(**raw_result)
        return result
