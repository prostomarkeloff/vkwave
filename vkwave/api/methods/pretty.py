from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Pretty(Category):
    async def cards_create(
        self,
        owner_id: int = None,
        photo: str = None,
        title: str = None,
        link: str = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[dict, PrettyCardsCreateResponse]:
        """
        :param owner_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("create", params)
        if raw:
            return raw_result

        result = PrettyCardsCreateResponse(**raw_result)
        return result

    async def cards_delete(
        self, owner_id: int = None, card_id: int = None, raw: bool = False,
    ) -> typing.Union[dict, PrettyCardsDeleteResponse]:
        """
        :param owner_id:
        :param card_id:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if raw:
            return raw_result

        result = PrettyCardsDeleteResponse(**raw_result)
        return result

    async def cards_edit(
        self,
        owner_id: int = None,
        card_id: int = None,
        photo: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
        raw: bool = False,
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
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if raw:
            return raw_result

        result = PrettyCardsEditResponse(**raw_result)
        return result

    async def cards_get(
        self,
        owner_id: int = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, PrettyCardsGetResponse]:
        """
        :param owner_id:
        :param offset:
        :param count:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if raw:
            return raw_result

        result = PrettyCardsGetResponse(**raw_result)
        return result

    async def cards_get_by_id(
        self,
        owner_id: int = None,
        card_ids: typing.List[int] = None,
        raw: bool = False,
    ) -> typing.Union[dict, PrettyCardsGetByIdResponse]:
        """
        :param owner_id:
        :param card_ids:
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if raw:
            return raw_result

        result = PrettyCardsGetByIdResponse(**raw_result)
        return result

    async def cards_get_upload_u_r_l(
        self, raw: bool = False,
    ) -> typing.Union[dict, PrettyCardsGetUploadURLResponse]:
        """
        :param raw: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUploadURL", params)
        if raw:
            return raw_result

        result = PrettyCardsGetUploadURLResponse(**raw_result)
        return result
