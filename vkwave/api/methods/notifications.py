from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Notifications(Category):
    async def get(
        self,
        return_raw_response: bool = False,
        count: Optional[int] = None,
        start_from: Optional[str] = None,
        filters: Optional[List[str]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ) -> Union[dict, NotificationsGetResponse]:
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
        self,
        return_raw_response: bool = False,
    ) -> Union[dict, NotificationsMarkAsViewedResponse]:
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
        user_ids: List[int],
        message: str,
        return_raw_response: bool = False,
        fragment: Optional[str] = None,
        group_id: Optional[int] = None,
        random_id: Optional[int] = None,
    ) -> Union[dict, NotificationsSendMessageResponse]:
        """
        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :param random_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendMessage", params)
        if return_raw_response:
            return raw_result

        result = NotificationsSendMessageResponse(**raw_result)
        return result
