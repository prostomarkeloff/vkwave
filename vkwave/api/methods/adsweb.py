from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Adsweb(Category):
    async def get_ad_categories(
        self,
        office_id: int,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AdswebGetAdCategoriesResponse]:
        """
        :param office_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAdCategories", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetAdCategoriesResponse(**raw_result)
        return result

    async def get_ad_unit_code(
        self,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AdswebGetAdUnitCodeResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAdUnitCode", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetAdUnitCodeResponse(**raw_result)
        return result

    async def get_ad_units(
        self,
        office_id: int,
        return_raw_response: bool = False,
        sites_ids: typing.Optional[str] = None,
        ad_units_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdswebGetAdUnitsResponse]:
        """
        :param office_id:
        :param sites_ids:
        :param ad_units_ids:
        :param fields:
        :param limit:
        :param offset:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAdUnits", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetAdUnitsResponse(**raw_result)
        return result

    async def get_fraud_history(
        self,
        office_id: int,
        return_raw_response: bool = False,
        sites_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdswebGetFraudHistoryResponse]:
        """
        :param office_id:
        :param sites_ids:
        :param limit:
        :param offset:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFraudHistory", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetFraudHistoryResponse(**raw_result)
        return result

    async def get_sites(
        self,
        office_id: int,
        return_raw_response: bool = False,
        sites_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[dict, AdswebGetSitesResponse]:
        """
        :param office_id:
        :param sites_ids:
        :param fields:
        :param limit:
        :param offset:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSites", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetSitesResponse(**raw_result)
        return result

    async def get_statistics(
        self,
        office_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        return_raw_response: bool = False,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
    ) -> typing.Union[dict, AdswebGetStatisticsResponse]:
        """
        :param office_id:
        :param ids_type:
        :param ids:
        :param period:
        :param date_from:
        :param date_to:
        :param fields:
        :param limit:
        :param page_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getStatistics", params)
        if return_raw_response:
            return raw_result

        result = AdswebGetStatisticsResponse(**raw_result)
        return result
