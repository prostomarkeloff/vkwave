from vkwave_types.responses import *
from ._category import Category


class Widgets(Category):
    def get_comments(
        self,
        widget_api_id: typing.Optional[int] = None,
        url: typing.Optional[str] = None,
        page_id: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
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

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getComments", params)
        result = WidgetsGetCommentsResponse(**raw_result)
        return result

    def get_pages(
        self,
        widget_api_id: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> WidgetsGetPagesResponse:
        """
        :param widget_api_id:
        :param order:
        :param period:
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

        raw_result = await self.api_request("getPages", params)
        result = WidgetsGetPagesResponse(**raw_result)
        return result
