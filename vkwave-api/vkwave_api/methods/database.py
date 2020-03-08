from vkwave_types.responses import *
from ._category import Category


class Database(Category):
    def get_chairs(
        self,
        faculty_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetChairsResponse:
        """
        :param faculty_id: - id of the faculty to get chairs from
        :param offset: - offset required to get a certain subset of chairs
        :param count: - amount of chairs to get
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getChairs", params)
        result = DatabaseGetChairsResponse(**raw_result)
        return result

    def get_cities(
        self,
        country_id: typing.Optional[int],
        region_id: typing.Optional[int],
        q: typing.Optional[str],
        need_all: typing.Optional[bool],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetCitiesResponse:
        """
        :param country_id: - Country ID.
        :param region_id: - Region ID.
        :param q: - Search query.
        :param need_all: - '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: - Offset needed to return a specific subset of cities.
        :param count: - Number of cities to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCities", params)
        result = DatabaseGetCitiesResponse(**raw_result)
        return result

    def get_cities_by_id(
        self, city_ids: typing.Optional[typing.List[int]],
    ) -> DatabaseGetCitiesByIdResponse:
        """
        :param city_ids: - City IDs.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCitiesById", params)
        result = DatabaseGetCitiesByIdResponse(**raw_result)
        return result

    def get_countries(
        self,
        need_all: typing.Optional[bool],
        code: typing.Optional[str],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetCountriesResponse:
        """
        :param need_all: - '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: - Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: - Offset needed to return a specific subset of countries.
        :param count: - Number of countries to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCountries", params)
        result = DatabaseGetCountriesResponse(**raw_result)
        return result

    def get_countries_by_id(
        self, country_ids: typing.Optional[typing.List[int]],
    ) -> DatabaseGetCountriesByIdResponse:
        """
        :param country_ids: - Country IDs.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getCountriesById", params)
        result = DatabaseGetCountriesByIdResponse(**raw_result)
        return result

    def get_faculties(
        self,
        university_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetFacultiesResponse:
        """
        :param university_id: - University ID.
        :param offset: - Offset needed to return a specific subset of faculties.
        :param count: - Number of faculties to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getFaculties", params)
        result = DatabaseGetFacultiesResponse(**raw_result)
        return result

    def get_metro_stations(
        self,
        city_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
        extended: typing.Optional[bool],
    ) -> DatabaseGetMetroStationsResponse:
        """
        :param city_id:
        :param offset:
        :param count:
        :param extended:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMetroStations", params)
        result = DatabaseGetMetroStationsResponse(**raw_result)
        return result

    def get_metro_stations_by_id(
        self, station_ids: typing.Optional[typing.List[int]],
    ) -> DatabaseGetMetroStationsByIdResponse:
        """
        :param station_ids:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getMetroStationsById", params)
        result = DatabaseGetMetroStationsByIdResponse(**raw_result)
        return result

    def get_regions(
        self,
        country_id: typing.Optional[int],
        q: typing.Optional[str],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetRegionsResponse:
        """
        :param country_id: - Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: - Search query.
        :param offset: - Offset needed to return specific subset of regions.
        :param count: - Number of regions to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getRegions", params)
        result = DatabaseGetRegionsResponse(**raw_result)
        return result

    def get_school_classes(
        self, country_id: typing.Optional[int],
    ) -> DatabaseGetSchoolClassesResponse:
        """
        :param country_id: - Country ID.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSchoolClasses", params)
        result = DatabaseGetSchoolClassesResponse(**raw_result)
        return result

    def get_schools(
        self,
        q: typing.Optional[str],
        city_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetSchoolsResponse:
        """
        :param q: - Search query.
        :param city_id: - City ID.
        :param offset: - Offset needed to return a specific subset of schools.
        :param count: - Number of schools to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getSchools", params)
        result = DatabaseGetSchoolsResponse(**raw_result)
        return result

    def get_universities(
        self,
        q: typing.Optional[str],
        country_id: typing.Optional[int],
        city_id: typing.Optional[int],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> DatabaseGetUniversitiesResponse:
        """
        :param q: - Search query.
        :param country_id: - Country ID.
        :param city_id: - City ID.
        :param offset: - Offset needed to return a specific subset of universities.
        :param count: - Number of universities to return.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getUniversities", params)
        result = DatabaseGetUniversitiesResponse(**raw_result)
        return result
