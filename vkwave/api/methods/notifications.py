from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Notifications(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        count: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        filters: typing.Optional[typing.List[str]] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
    ) -> typing.Union[dict, NotificationsGetResponse]:
        """
        :param count: - Number of notifications to return.
        :param start_from:
        :param filters: - Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: - Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = NotificationsGetResponse(**raw_result)
        return result

    async def mark_as_viewed(
        self, return_raw_response: bool = False,
    ) -> typing.Union[dict, NotificationsMarkAsViewedResponse]:
        """
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markAsViewed", params)
        if return_raw_response:
            return raw_result

        result = NotificationsMarkAsViewedResponse(**raw_result)
        return result

    async def send_message(
        self,
        user_ids: typing.List[int],
        message: str,
        return_raw_response: bool = False,
        fragment: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, NotificationsSendMessageResponse]:
        """
        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendMessage", params)
        if return_raw_response:
            return raw_result

        result = NotificationsSendMessageResponse(**raw_result)
        return result
