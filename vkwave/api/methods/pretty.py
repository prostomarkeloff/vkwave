from vkwave.types.responses import *

from ._category import Category


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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("create", params)
        result = PrettyCardsCreateResponse(**raw_result)
        return result

    async def cards_delete(
        self, owner_id: int = None, card_id: int = None,
    ) -> PrettyCardsDeleteResponse:
        """
        :param owner_id:
        :param card_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("delete", params)
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("edit", params)
        result = PrettyCardsEditResponse(**raw_result)
        return result

    async def cards_get(
        self,
        owner_id: int = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> PrettyCardsGetResponse:
        """
        :param owner_id:
        :param offset:
        :param count:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = PrettyCardsGetResponse(**raw_result)
        return result

    async def cards_get_by_id(
        self, owner_id: int = None, card_ids: typing.List[int] = None,
    ) -> PrettyCardsGetByIdResponse:
        """
        :param owner_id:
        :param card_ids:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getById", params)
        result = PrettyCardsGetByIdResponse(**raw_result)
        return result

    async def cards_get_upload_u_r_l(self,) -> PrettyCardsGetUploadURLResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getUploadURL", params)
        result = PrettyCardsGetUploadURLResponse(**raw_result)
        return result
