from vkwave_types.responses import *
from ._category import Category


class Notifications(Category):
    def get(
        self,
        count: typing.Optional[int],
        start_from: typing.Optional[str],
        filters: typing.Optional[typing.List[str]],
        start_time: typing.Optional[int],
        end_time: typing.Optional[int],
    ) -> NotificationsGetResponse:
        """
        :param count: - Number of notifications to return.
        :param start_from:
        :param filters: - Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: - Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("get", params)
        result = NotificationsGetResponse(**raw_result)
        return result

    def mark_as_viewed(self,) -> NotificationsMarkAsViewedResponse:
        """
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("markAsViewed", params)
        result = NotificationsMarkAsViewedResponse(**raw_result)
        return result

    def send_message(
        self,
        user_ids: typing.Optional[typing.List[int]],
        message: typing.Optional[str],
        fragment: typing.Optional[str],
        group_id: typing.Optional[int],
    ) -> NotificationsSendMessageResponse:
        """
        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :return:
        """

        params = {k: v for k, v in locals().items() if k != "self" and v is not None}
        raw_result = await self.api_request("sendMessage", params)
        result = NotificationsSendMessageResponse(**raw_result)
        return result
