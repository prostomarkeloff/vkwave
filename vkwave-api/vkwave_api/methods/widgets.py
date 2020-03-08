from vkwave_types.responses import *
from ._category import Category


class Widgets(Category):
    def get_comments(
        self,
        widget_api_id: typing.Optional[int],
        url: typing.Optional[str],
        page_id: typing.Optional[str],
        order: typing.Optional[str],
        fields: typing.Optional[typing.List[UsersFields]],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> WidgetsGetCommentsResponse:
        """
        :param widget_api_id:
        :param url:
        :param page_id:
        :param order:
        :param fields:
        :param offset:
        :param count:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getComments", params)
        result = WidgetsGetCommentsResponse(**raw_result)
        return result

    def get_pages(
        self,
        widget_api_id: typing.Optional[int],
        order: typing.Optional[str],
        period: typing.Optional[str],
        offset: typing.Optional[int],
        count: typing.Optional[int],
    ) -> WidgetsGetPagesResponse:
        """
        :param widget_api_id:
        :param order:
        :param period:
        :param offset:
        :param count:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("getPages", params)
        result = WidgetsGetPagesResponse(**raw_result)
        return result
