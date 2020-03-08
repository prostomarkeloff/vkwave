from vkwave_types.responses import *
from ._category import Category


class Pretty(Category):
    def cards_create(
        self,
        owner_id: typing.Optional[int],
        photo: typing.Optional[str],
        title: typing.Optional[str],
        link: typing.Optional[str],
        price: typing.Optional[str],
        price_old: typing.Optional[str],
        button: typing.Optional[str],
    ) -> PrettyCardsCreateResponse:
        """
        :param owner_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("create", params)
        result = PrettyCardsCreateResponse(**raw_result)
        return result

    def cards_delete(
        self, owner_id: typing.Optional[int], card_id: typing.Optional[int],
    ) -> PrettyCardsDeleteResponse:
        """
        :param owner_id:
        :param card_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("delete", params)
        result = PrettyCardsDeleteResponse(**raw_result)
        return result

    def cards_edit(
        self,
        owner_id: typing.Optional[int],
        card_id: typing.Optional[int],
        photo: typing.Optional[str],
        title: typing.Optional[str],
        link: typing.Optional[str],
        price: typing.Optional[str],
        price_old: typing.Optional[str],
        button: typing.Optional[str],
    ) -> PrettyCardsEditResponse:
        """
        :param owner_id:
        :param card_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("edit", params)
        result = PrettyCardsEditResponse(**raw_result)
        return result

    def cards_get(
        self,
        owner_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> PrettyCardsGetResponse:
        """
        :param owner_id:
        :param offset:
        :param count:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = PrettyCardsGetResponse(**raw_result)
        return result

    def cards_get_by_id(
        self,
        owner_id: typing.Optional[int],
        card_ids: typing.Optional[typing.List[int]],
    ) -> PrettyCardsGetByIdResponse:
        """
        :param owner_id:
        :param card_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getById", params)
        result = PrettyCardsGetByIdResponse(**raw_result)
        return result

    def cards_get_upload_u_r_l(self,) -> PrettyCardsGetUploadURLResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUploadURL", params)
        result = PrettyCardsGetUploadURLResponse(**raw_result)
        return result
