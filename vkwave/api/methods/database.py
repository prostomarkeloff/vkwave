from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Database(Category):
    async def get_chairs(
        self,
        faculty_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetChairsResponse]:
        """
        :param faculty_id: - id of the faculty to get chairs from
        :param offset: - offset required to get a certain subset of chairs
        :param count: - amount of chairs to get
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getChairs", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetChairsResponse(**raw_result)
        return result

    async def get_cities(
        self,
        country_id: int,
        return_raw_response: bool = False,
        region_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        need_all: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetCitiesResponse]:
        """
        :param country_id: - Country ID.
        :param region_id: - Region ID.
        :param q: - Search query.
        :param need_all: - '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: - Offset needed to return a specific subset of cities.
        :param count: - Number of cities to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCities", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetCitiesResponse(**raw_result)
        return result

    async def get_cities_by_id(
        self,
        return_raw_response: bool = False,
        city_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, DatabaseGetCitiesByIdResponse]:
        """
        :param city_ids: - City IDs.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCitiesById", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetCitiesByIdResponse(**raw_result)
        return result

    async def get_countries(
        self,
        return_raw_response: bool = False,
        need_all: typing.Optional[BaseBoolInt] = None,
        code: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetCountriesResponse]:
        """
        :param need_all: - '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: - Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: - Offset needed to return a specific subset of countries.
        :param count: - Number of countries to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCountries", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetCountriesResponse(**raw_result)
        return result

    async def get_countries_by_id(
        self,
        return_raw_response: bool = False,
        country_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, DatabaseGetCountriesByIdResponse]:
        """
        :param country_ids: - Country IDs.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getCountriesById", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetCountriesByIdResponse(**raw_result)
        return result

    async def get_faculties(
        self,
        university_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetFacultiesResponse]:
        """
        :param university_id: - University ID.
        :param offset: - Offset needed to return a specific subset of faculties.
        :param count: - Number of faculties to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getFaculties", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetFacultiesResponse(**raw_result)
        return result

    async def get_metro_stations(
        self,
        city_id: int,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, DatabaseGetMetroStationsResponse]:
        """
        :param city_id:
        :param offset:
        :param count:
        :param extended:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMetroStations", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetMetroStationsResponse(**raw_result)
        return result

    async def get_metro_stations_by_id(
        self,
        return_raw_response: bool = False,
        station_ids: typing.Optional[typing.List[int]] = None,
    ) -> typing.Union[dict, DatabaseGetMetroStationsByIdResponse]:
        """
        :param station_ids:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getMetroStationsById", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetMetroStationsByIdResponse(**raw_result)
        return result

    async def get_regions(
        self,
        country_id: int,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetRegionsResponse]:
        """
        :param country_id: - Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: - Search query.
        :param offset: - Offset needed to return specific subset of regions.
        :param count: - Number of regions to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getRegions", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetRegionsResponse(**raw_result)
        return result

    async def get_school_classes(
        self, return_raw_response: bool = False, country_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetSchoolClassesResponse]:
        """
        :param country_id: - Country ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSchoolClasses", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetSchoolClassesResponse(**raw_result)
        return result

    async def get_schools(
        self,
        city_id: int,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetSchoolsResponse]:
        """
        :param q: - Search query.
        :param city_id: - City ID.
        :param offset: - Offset needed to return a specific subset of schools.
        :param count: - Number of schools to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getSchools", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetSchoolsResponse(**raw_result)
        return result

    async def get_universities(
        self,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, DatabaseGetUniversitiesResponse]:
        """
        :param q: - Search query.
        :param country_id: - Country ID.
        :param city_id: - City ID.
        :param offset: - Offset needed to return a specific subset of universities.
        :param count: - Number of universities to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getUniversities", params)
        if return_raw_response:
            return raw_result

        result = DatabaseGetUniversitiesResponse(**raw_result)
        return result
