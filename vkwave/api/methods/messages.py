from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class Messages(Category):
    async def add_chat_user(
        self,
        chat_id: int,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param chat_id: - Chat ID.
        :param user_id: - ID of the user to be added to the chat.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("addChatUser", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def allow_messages_from_group(
        self, group_id: int, return_raw_response: bool = False, key: typing.Optional[str] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Group ID.
        :param key:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("allowMessagesFromGroup", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def create_chat(
        self,
        return_raw_response: bool = False,
        user_ids: typing.Optional[typing.List[int]] = None,
        title: typing.Optional[str] = None,
    ) -> typing.Union[dict, MessagesCreateChatResponse]:
        """
        :param user_ids: - IDs of the users to be added to the chat.
        :param title: - Chat title.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("createChat", params)
        if return_raw_response:
            return raw_result

        result = MessagesCreateChatResponse(**raw_result)
        return result

    async def delete(
        self,
        return_raw_response: bool = False,
        message_ids: typing.Optional[typing.List[int]] = None,
        spam: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
        delete_for_all: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, MessagesDeleteResponse]:
        """
        :param message_ids: - Message IDs.
        :param spam: - '1' — to mark message as spam.
        :param group_id: - Group ID (for group messages with user access token)
        :param delete_for_all: - '1' — delete message for for all.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = MessagesDeleteResponse(**raw_result)
        return result

    async def delete_chat_photo(
        self,
        chat_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesDeleteChatPhotoResponse]:
        """
        :param chat_id: - Chat ID.
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteChatPhoto", params)
        if return_raw_response:
            return raw_result

        result = MessagesDeleteChatPhotoResponse(**raw_result)
        return result

    async def delete_conversation(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesDeleteConversationResponse]:
        """
        :param user_id: - User ID. To clear a chat history use 'chat_id'
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: - Group ID (for group messages with user access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("deleteConversation", params)
        if return_raw_response:
            return raw_result

        result = MessagesDeleteConversationResponse(**raw_result)
        return result

    async def deny_messages_from_group(
        self, group_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param group_id: - Group ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("denyMessagesFromGroup", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def edit(
        self,
        peer_id: BaseBoolInt,
        message_id: int,
        return_raw_response: bool = False,
        message: typing.Optional[str] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        attachment: typing.Optional[BaseBoolInt] = None,
        keep_forward_messages: typing.Optional[BaseBoolInt] = None,
        keep_snippets: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
        dont_parse_links: typing.Optional[bool] = None,
    ) -> typing.Union[dict, MessagesEditResponse]:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: - (Required if 'attachments' is not set.) Text of the message.
        :param message_id:
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: - '1' — to keep forwarded, messages.
        :param keep_snippets: - '1' — to keep attached snippets.
        :param group_id: - Group ID (for group messages with user access token)
        :param dont_parse_links:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("edit", params)
        if return_raw_response:
            return raw_result

        result = MessagesEditResponse(**raw_result)
        return result

    async def edit_chat(
        self, chat_id: int, title: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param chat_id: - Chat ID.
        :param title: - New title of the chat.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("editChat", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def get_by_conversation_message_id(
        self,
        peer_id: BaseBoolInt,
        conversation_message_ids: typing.List[int],
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetByConversationMessageIdResponse]:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: - Conversation message IDs.
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getByConversationMessageId", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetByConversationMessageIdResponse(**raw_result)
        return result

    async def get_by_id(
        self,
        message_ids: typing.List[int],
        return_raw_response: bool = False,
        preview_length: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetByIdResponse, MessagesGetByIdExtendedResponse]:
        """
        :param message_ids: - Message IDs.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getById", params)
        if return_raw_response:
            return raw_result

        result = (
            MessagesGetByIdResponse(**raw_result)
            if not extended
            else MessagesGetByIdExtendedResponse(**raw_result)
        )
        return result

    async def get_chat_preview(
        self,
        return_raw_response: bool = False,
        peer_id: typing.Optional[int] = None,
        link: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
    ) -> typing.Union[dict, MessagesGetChatPreviewResponse]:
        """
        :param peer_id:
        :param link: - Invitation link.
        :param fields: - Profile fields to return.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getChatPreview", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetChatPreviewResponse(**raw_result)
        return result

    async def get_conversation_members(
        self,
        peer_id: int,
        return_raw_response: bool = False,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetConversationMembersResponse]:
        """
        :param peer_id: - Peer ID.
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getConversationMembers", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetConversationMembersResponse(**raw_result)
        return result

    async def get_conversations(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        start_message_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetConversationsResponse]:
        """
        :param offset: - Offset needed to return a specific subset of conversations.
        :param count: - Number of conversations to return.
        :param filter: - Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
        :param extended: - '1' — return extra information about users and communities
        :param start_message_id: - ID of the message from what to return dialogs.
        :param fields: - Profile and communities fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getConversations", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetConversationsResponse(**raw_result)
        return result

    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        return_raw_response: bool = False,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[
        dict, MessagesGetConversationsByIdResponse, MessagesGetConversationsByIdExtendedResponse,
    ]:
        """
        :param peer_ids: - Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: - Return extended properties
        :param fields: - Profile and communities fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getConversationsById", params)
        if return_raw_response:
            return raw_result

        result = (
            MessagesGetConversationsByIdResponse(**raw_result)
            if not extended
            else MessagesGetConversationsByIdExtendedResponse(**raw_result)
        )
        return result

    async def get_history(
        self,
        return_raw_response: bool = False,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        rev: typing.Optional[BaseBoolInt] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetHistoryResponse]:
        """
        :param offset: - Offset needed to return a specific subset of messages.
        :param count: - Number of messages to return.
        :param user_id: - ID of the user whose message history you want to return.
        :param peer_id:
        :param start_message_id: - Starting message ID from which to return history.
        :param rev: - Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
        :param extended: - Information whether the response should be extended
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getHistory", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetHistoryResponse(**raw_result)
        return result

    async def get_history_attachments(
        self,
        peer_id: BaseBoolInt,
        return_raw_response: bool = False,
        media_type: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        photo_sizes: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        preserve_order: typing.Optional[bool] = None,
        max_forwards_level: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetHistoryAttachmentsResponse]:
        """
        :param peer_id: - Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param media_type: - Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: - Message ID to start return results from.
        :param count: - Number of objects to return.
        :param photo_sizes: - '1' — to return photo sizes in a
        :param fields: - Additional profile [vk.com/dev/fields|fields] to return. 
        :param group_id: - Group ID (for group messages with group access token)
        :param preserve_order:
        :param max_forwards_level:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getHistoryAttachments", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetHistoryAttachmentsResponse(**raw_result)
        return result

    async def get_invite_link(
        self,
        peer_id: int,
        return_raw_response: bool = False,
        reset: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetInviteLinkResponse]:
        """
        :param peer_id: - Destination ID.
        :param reset: - 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: - Group ID
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getInviteLink", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetInviteLinkResponse(**raw_result)
        return result

    async def get_last_activity(
        self, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, MessagesGetLastActivityResponse]:
        """
        :param user_id: - User ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLastActivity", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetLastActivityResponse(**raw_result)
        return result

    async def get_long_poll_history(
        self,
        return_raw_response: bool = False,
        ts: typing.Optional[int] = None,
        pts: typing.Optional[int] = None,
        preview_length: typing.Optional[BaseBoolInt] = None,
        onlines: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        events_limit: typing.Optional[int] = None,
        msgs_limit: typing.Optional[int] = None,
        max_msg_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        last_n: typing.Optional[int] = None,
        credentials: typing.Optional[bool] = None,
    ) -> typing.Union[dict, MessagesGetLongPollHistoryResponse]:
        """
        :param ts: - Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: - Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: - '1' — to return history with online users only.
        :param fields: - Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: - Maximum number of events to return.
        :param msgs_limit: - Maximum number of messages to return.
        :param max_msg_id: - Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: - Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLongPollHistory", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetLongPollHistoryResponse(**raw_result)
        return result

    async def get_long_poll_server(
        self,
        return_raw_response: bool = False,
        need_pts: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesGetLongPollServerResponse]:
        """
        :param need_pts: - '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: - Group ID (for group messages with user access token)
        :param lp_version: - Long poll version
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getLongPollServer", params)
        if return_raw_response:
            return raw_result

        result = MessagesGetLongPollServerResponse(**raw_result)
        return result

    async def is_messages_from_group_allowed(
        self, group_id: int, user_id: int, return_raw_response: bool = False,
    ) -> typing.Union[dict, MessagesIsMessagesFromGroupAllowedResponse]:
        """
        :param group_id: - Group ID.
        :param user_id: - User ID.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("isMessagesFromGroupAllowed", params)
        if return_raw_response:
            return raw_result

        result = MessagesIsMessagesFromGroupAllowedResponse(**raw_result)
        return result

    async def join_chat_by_invite_link(
        self, link: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, MessagesJoinChatByInviteLinkResponse]:
        """
        :param link: - Invitation link.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("joinChatByInviteLink", params)
        if return_raw_response:
            return raw_result

        result = MessagesJoinChatByInviteLinkResponse(**raw_result)
        return result

    async def mark_as_answered_conversation(
        self,
        peer_id: int,
        return_raw_response: bool = False,
        answered: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param peer_id: - ID of conversation to mark as important.
        :param answered: - '1' — to mark as answered, '0' — to remove the mark
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markAsAnsweredConversation", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def mark_as_important(
        self,
        return_raw_response: bool = False,
        message_ids: typing.Optional[typing.List[int]] = None,
        important: typing.Optional[BaseBoolInt] = None,
    ) -> typing.Union[dict, MessagesMarkAsImportantResponse]:
        """
        :param message_ids: - IDs of messages to mark as important.
        :param important: - '1' — to add a star (mark as important), '0' — to remove the star
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markAsImportant", params)
        if return_raw_response:
            return raw_result

        result = MessagesMarkAsImportantResponse(**raw_result)
        return result

    async def mark_as_important_conversation(
        self,
        peer_id: int,
        return_raw_response: bool = False,
        important: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param peer_id: - ID of conversation to mark as important.
        :param important: - '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markAsImportantConversation", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def mark_as_read(
        self,
        return_raw_response: bool = False,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        start_message_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param message_ids: - IDs of messages to mark as read.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: - Message ID to start from.
        :param group_id: - Group ID (for group messages with user access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("markAsRead", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def pin(
        self,
        peer_id: BaseBoolInt,
        return_raw_response: bool = False,
        message_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesPinResponse]:
        """
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("pin", params)
        if return_raw_response:
            return raw_result

        result = MessagesPinResponse(**raw_result)
        return result

    async def remove_chat_user(
        self,
        chat_id: int,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        member_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param chat_id: - Chat ID.
        :param user_id: - ID of the user to be removed from the chat.
        :param member_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("removeChatUser", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def restore(
        self,
        message_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param message_id: - ID of a previously-deleted message to restore.
        :param group_id: - Group ID (for group messages with user access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("restore", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def search(
        self,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        date: typing.Optional[int] = None,
        preview_length: typing.Optional[BaseBoolInt] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesSearchResponse]:
        """
        :param q: - Search query string.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param date: - Date to search message before in Unixtime.
        :param preview_length: - Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param offset: - Offset needed to return a specific subset of messages.
        :param count: - Number of messages to return.
        :param extended:
        :param fields:
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("search", params)
        if return_raw_response:
            return raw_result

        result = MessagesSearchResponse(**raw_result)
        return result

    async def search_conversations(
        self,
        return_raw_response: bool = False,
        q: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[BaseBoolInt] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, MessagesSearchConversationsResponse]:
        """
        :param q: - Search query string.
        :param count: - Maximum number of results.
        :param extended: - '1' — return extra information about users and communities
        :param fields: - Profile fields to return.
        :param group_id: - Group ID (for group messages with user access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("searchConversations", params)
        if return_raw_response:
            return raw_result

        result = MessagesSearchConversationsResponse(**raw_result)
        return result

    async def send(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        domain: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        message: typing.Optional[str] = None,
        lat: typing.Optional[BaseBoolInt] = None,
        long: typing.Optional[BaseBoolInt] = None,
        attachment: typing.Optional[BaseBoolInt] = None,
        reply_to: typing.Optional[int] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        forward: typing.Optional[str] = None,
        sticker_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        keyboard: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
    ) -> typing.Union[dict, MessagesSendResponse]:
        """
        :param user_id: - User ID (by default — current user).
        :param random_id: - Unique identifier to avoid resending the message.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param domain: - User's short address (for example, 'illarionov').
        :param chat_id: - ID of conversation the message will relate to.
        :param user_ids: - IDs of message recipients (if new conversation shall be started).
        :param message: - (Required if 'attachments' is not set.) Text of the message.
        :param lat: - Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: - Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: - (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: - ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param forward:
        :param sticker_id: - Sticker id.
        :param group_id: - Group ID (for group messages with group access token)
        :param keyboard:
        :param payload:
        :param dont_parse_links:
        :param disable_mentions:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("send", params)
        if return_raw_response:
            return raw_result

        result = MessagesSendResponse(**raw_result)
        return result

    async def set_activity(
        self,
        return_raw_response: bool = False,
        user_id: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        peer_id: typing.Optional[BaseBoolInt] = None,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param user_id: - User ID.
        :param type: - 'typing' — user has started to type.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: - Group ID (for group messages with group access token)
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setActivity", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result

    async def set_chat_photo(
        self, file: str, return_raw_response: bool = False,
    ) -> typing.Union[dict, MessagesSetChatPhotoResponse]:
        """
        :param file: - Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("setChatPhoto", params)
        if return_raw_response:
            return raw_result

        result = MessagesSetChatPhotoResponse(**raw_result)
        return result

    async def unpin(
        self,
        peer_id: int,
        return_raw_response: bool = False,
        group_id: typing.Optional[int] = None,
    ) -> typing.Union[dict, OkResponse]:
        """
        :param peer_id:
        :param group_id:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("unpin", params)
        if return_raw_response:
            return raw_result

        result = OkResponse(**raw_result)
        return result
