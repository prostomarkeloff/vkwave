from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class PrettyCards(Category):
    async def cards_create(
        self,
        owner_id: int,
        photo: str,
        title: str,
        link: str,
        return_raw_response: bool = False,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
    ) -> typing.Union[dict, PrettyCardsCreateResponse]:
        """
        :param owner_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("create", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsCreateResponse(**raw_result)

    async def cards_delete(
        self,
        owner_id: int,
        card_id: int,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, PrettyCardsDeleteResponse]:
        """
        :param owner_id:
        :param card_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsDeleteResponse(**raw_result)

    async def cards_edit(
        self,
        owner_id: int,
        card_id: int,
        return_raw_response: bool = False,
        photo: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
    ) -> typing.Union[dict, PrettyCardsEditResponse]:
        """
        :param owner_id:
        :param card_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsEditResponse(**raw_result)

    async def cards_get(
        self,
        owner_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, PrettyCardsGetResponse]:
        """
        :param owner_id:
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsGetResponse(**raw_result)

    async def cards_get_by_id(
        self,
        owner_id: int,
        card_ids: typing.List[int],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, PrettyCardsGetByIdResponse]:
        """
        :param owner_id:
        :param card_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsGetByIdResponse(**raw_result)

    async def cards_get_upload_u_r_l(
        self,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, PrettyCardsGetUploadURLResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUploadURL", params)
        if return_raw_response:
            return raw_result

        return PrettyCardsGetUploadURLResponse(**raw_result)
