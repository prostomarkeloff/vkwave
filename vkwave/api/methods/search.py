from vkwave.types.responses import *
from ._category import Category


class Search(Category):
    async def get_hints(
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
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("getHints", params)
        result = SearchGetHintsResponse(**raw_result)
        return result
