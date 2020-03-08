from vkwave_types.responses import *
from ._category import Category


class Search(Category):
    def get_hints(
        self,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        search_global: typing.Optional[bool] = None,
    ) -> SearchGetHintsResponse:
        """
        :param q: - Search query string.
        :param offset: - Offset for querying specific result subset
        :param limit: - Maximum number of results to return.
        :param filters:
        :param fields:
        :param search_global:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getHints", params)
        result = SearchGetHintsResponse(**raw_result)
        return result
