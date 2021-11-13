from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Widgets(Category):
    async def get_comments(
        self,
        return_raw_response: bool = False,
        widget_api_id: Optional[int] = None,
        url: Optional[str] = None,
        page_id: Optional[str] = None,
        order: Optional[str] = None,
        fields: Optional[List[UsersFields]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, WidgetsGetCommentsResponse]:
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
        widget_api_id: Optional[int] = None,
        order: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[dict, WidgetsGetPagesResponse]:
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
