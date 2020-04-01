from vkwave.types.responses import *

from ._category import Category


class Notifications(Category):
    async def get(
        self,
        count: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        filters: typing.Optional[typing.List[str]] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
    ) -> NotificationsGetResponse:
        """
        :param count: - Number of notifications to return.
        :param start_from:
        :param filters: - Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: - Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: - Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = NotificationsGetResponse(**raw_result)
        return result

    async def mark_as_viewed(self,) -> NotificationsMarkAsViewedResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("markAsViewed", params)
        result = NotificationsMarkAsViewedResponse(**raw_result)
        return result

    async def send_message(
        self,
        user_ids: typing.List[int] = None,
        message: str = None,
        fragment: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
    ) -> NotificationsSendMessageResponse:
        """
        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("sendMessage", params)
        result = NotificationsSendMessageResponse(**raw_result)
        return result
