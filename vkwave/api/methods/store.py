from vkwave.types.responses import *
from typing import Optional, List, Union
from ._category import Category
from ._utils import get_params


class Store(Category):
    async def add_stickers_to_favorite(
        self,
        sticker_ids: Optional[List[int]] = None,
        return_raw_response: Optional[bool] = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param sticker_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addStickersToFavorite", params)
        if return_raw_response:
            return raw_result

        return BaseOkResponse(**raw_result)


    async def get_favorite_stickers(
        self,
        return_raw_response: bool = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFavoriteStickers", params)
        if return_raw_response:
            return raw_result

        return BaseOkResponse(**raw_result)


    async def get_products(
        self,
        type: Optional[str] = None,
        merchant: Optional[str] = None,
        section: Optional[str] = None,
        filters: Optional[str] = None,
        user_id: Optional[int] = None,
        extended: Optional[BaseBoolInt] = None,
        return_raw_response: Optional[bool] = False,
    ) -> Union[dict, StoreGetProductsResponse]:
        """
        :param type:
        :param merchant:
        :param section:
        :param filters:
        :param user_id: - hidden param
        :param extended:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getProducts", params)
        if return_raw_response:
            return raw_result

        return BaseOkResponse(**raw_result)


    async def get_stickers_keywords(
        self,
        stickers_ids: Optional[List[int]] = None,
        products_ids: Optional[List[int]] = None,
        aliases: Optional[BaseBoolInt] = None,
        all_products: Optional[BaseBoolInt] = None,
        need_stickers: Optional[BaseBoolInt] = None,
        return_raw_response: Optional[bool] = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param stickers_ids:
        :param products_ids:
        :param aliases:
        :param all_products:
        :param need_stickers:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getStickersKeywords", params)
        if return_raw_response:
            return raw_result

        return BaseOkResponse(**raw_result)


    async def remove_stickers_from_favorite(
        self,
        stickers_ids: Optional[List[int]] = None,
        return_raw_response: Optional[bool] = False,
    ) -> Union[dict, BaseOkResponse]:
        """
        :param stickers_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeStickersFromFavorite", params)
        if return_raw_response:
            return raw_result

        return BaseOkResponse(**raw_result)
