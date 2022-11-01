from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class AppWidgets(Category):
    async def widgets_get_app_image_upload_server(
        self,
        image_type: str,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AppWidgetsGetAppImageUploadServerResponse]:
        """
        :param image_type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAppImageUploadServer", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsGetAppImageUploadServerResponse(**raw_result)
        return result

    async def widgets_get_app_images(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
    ) -> typing.Union[dict, AppWidgetsGetAppImagesResponse]:
        """
        :param offset: - Offset needed to return a specific subset of images.
        :param count: - Maximum count of results.
        :param image_type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getAppImages", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsGetAppImagesResponse(**raw_result)
        return result

    async def widgets_get_group_image_upload_server(
        self,
        image_type: str,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AppWidgetsGetGroupImageUploadServerResponse]:
        """
        :param image_type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getGroupImageUploadServer", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsGetGroupImageUploadServerResponse(**raw_result)
        return result

    async def widgets_get_group_images(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
    ) -> typing.Union[dict, AppWidgetsGetGroupImagesResponse]:
        """
        :param offset: - Offset needed to return a specific subset of images.
        :param count: - Maximum count of results.
        :param image_type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getGroupImages", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsGetGroupImagesResponse(**raw_result)
        return result

    async def widgets_get_images_by_id(
        self,
        images: typing.List[str],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AppWidgetsGetImagesByIdResponse]:
        """
        :param images: - List of images IDs
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getImagesById", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsGetImagesByIdResponse(**raw_result)
        return result

    async def widgets_save_app_image(
        self,
        hash: str,
        image: str,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AppWidgetsSaveAppImageResponse]:
        """
        :param hash: - Parameter returned when photo is uploaded to server
        :param image: - Parameter returned when photo is uploaded to server
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("saveAppImage", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsSaveAppImageResponse(**raw_result)
        return result

    async def widgets_save_group_image(
        self,
        hash: str,
        image: str,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, AppWidgetsSaveGroupImageResponse]:
        """
        :param hash: - Parameter returned when photo is uploaded to server
        :param image: - Parameter returned when photo is uploaded to server
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("saveGroupImage", params)
        if return_raw_response:
            return raw_result

        result = AppWidgetsSaveGroupImageResponse(**raw_result)
        return result

    async def widgets_update(
        self,
        code: str,
        type: str,
        return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param code:
        :param type:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("update", params)
        if return_raw_response:
            return raw_result

        result = BaseOkResponse(**raw_result)
        return result
