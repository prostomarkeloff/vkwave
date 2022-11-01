from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Widgets(Category):
    async def get_comments(
        self,
        return_raw_response: bool = False,
        widget_api_id: typing.Optional[int] = None,
        url: typing.Optional[str] = None,
        page_id: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, WidgetsGetCommentsResponse]:
        """
        :param widget_api_id:
        :param url:
        :param page_id:
        :param order:
        :param fields:
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getComments", params)
        if return_raw_response:
            return raw_result

        result = WidgetsGetCommentsResponse(**raw_result)
        return result

    async def get_pages(
        self,
        return_raw_response: bool = False,
        widget_api_id: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
    ) -> typing.Union[dict, WidgetsGetPagesResponse]:
        """
        :param widget_api_id:
        :param order:
        :param period:
        :param offset:
        :param count:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getPages", params)
        if return_raw_response:
            return raw_result

        result = WidgetsGetPagesResponse(**raw_result)
        return result
