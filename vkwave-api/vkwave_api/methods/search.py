from vkwave_types.responses import *
from ._category import Category


class Search(Category):
    def get_hints(
        self,
        q: typing.Optional[str],
        offset: typing.Optional[int],
        limit: typing.Optional[int],
        filters: typing.Optional[typing.List[str]],
        fields: typing.Optional[typing.List[str]],
        search_global: typing.Optional[bool],
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

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getHints", params)
        result = SearchGetHintsResponse(**raw_result)
        return result
