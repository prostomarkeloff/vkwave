import pydantic
import typing
import enum
from .objects import MessagesKeyboard


class KeyboardData(pydantic.BaseModel):
    one_time: typing.Optional[bool]
    inline: typing.Optional[bool]
    buttons: typing.Optional[MessagesKeyboard]


class ServiceMessageData(pydantic.BaseModel):
    source_act: typing.Optional[str]
    source_mid: typing.Optional[str]
    source_message: typing.Optional[str]
    source_chat_local_id: typing.Optional[str]


class MessageData(pydantic.BaseModel):
    title: typing.Optional[str]
    emoji: typing.Optional[str]
    from_id: typing.Optional[str] = pydantic.Field(None, alias="from")
    fwd_count: typing.Optional[int]
    has_template: typing.Optional[str]
    mentions: typing.Optional[list]
    marked_users: typing.Optional[list]  # useless
    keyboard: typing.Optional[KeyboardData]
    service_message: typing.Optional[ServiceMessageData]


class MessageEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    flags: typing.Optional[int]
    peer_id: typing.Optional[int]
    timestamp: typing.Optional[int]
    text: typing.Optional[str]
    message_data: typing.Optional[MessageData]
    extra_message_data: typing.Optional[typing.Dict[str, str]]
    random_id: typing.Optional[int]
    conversation_message_id: typing.Optional[int]
    edit_time: typing.Optional[int]


class MessageEventModel(pydantic.BaseModel):
    object: typing.Optional[MessageEventObject] = pydantic.Field(None)


class SetFlagsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    flags: typing.Optional[int]
    peer_id: typing.Optional[int]


class SetFlagsEventModel(pydantic.BaseModel):
    object: SetFlagsEventObject = pydantic.Field(None)


class ReadIncomingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]


class ReadIncomingMessagesModel(pydantic.BaseModel):
    object: ReadIncomingMessagesEventObject = pydantic.Field(None)


class ReadOutgoingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]


class ReadOutgoingMessagesModel(pydantic.BaseModel):
    object: ReadOutgoingMessagesEventObject = pydantic.Field(None)


class PlatformEnum(int, enum.Enum):
    MOBILE_CLIENT = 1
    IPHONE = 2
    IPAD = 3
    ANDROID = 4
    WINDOWS_PHONE = 5
    WINDOWS_EIGHT = 6
    OFFICIAL_VK_OR_DESKTOP = 7


class FriendOnlineEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    user_id: typing.Optional[int]
    platform: typing.Optional[PlatformEnum]
    timestamp: typing.Optional[int]
    app_id: typing.Optional[int]


class FriendOnlineModel(pydantic.BaseModel):
    object: FriendOnlineEventObject = pydantic.Field(None)


class TimeoutUserEnum(int, enum.Enum):
    LEAVED_FROM_SITE = 0
    OFFLINE_FIVE_MINUTES = 1


class FriendOfflineEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    is_timeout: typing.Optional[TimeoutUserEnum]
    platform: typing.Optional[PlatformEnum]
    timestamp: typing.Optional[int]
    app_id: typing.Optional[int]


class FriendOfflineModel(pydantic.BaseModel):
    object: FriendOfflineEventObject = pydantic.Field(None)


class SeenMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[int]


class SeenMentionInChatModel(pydantic.BaseModel):
    object: SeenMentionInChatEventObject = pydantic.Field(None)


class NewMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[int]


class NewMentionInChatModel(pydantic.BaseModel):
    object: NewMentionInChatEventObject = pydantic.Field(None)


class DeletedAllMessagesInDialogEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    last_message_id: typing.Optional[int]


class DeletedAllMessagesInDialogModel(pydantic.BaseModel):
    object: DeletedAllMessagesInDialogEventObject = pydantic.Field(None)


class DropMessageCacheEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]


class DropMessageCacheModel(pydantic.BaseModel):
    object: DropMessageCacheEventObject = pydantic.Field(None)


class ChangedChatSettingsType(int, enum.Enum):
    CHANGED_CHAT_TITLE = 1
    CHANGED_CHAT_PICTURE = 2
    NEW_ADMINISTRATOR = 3
    CHANGED_RULES = 4
    PIN_OR_UNPIN_MESSAGE = 5
    JOIN_TO_CHAT = 6
    LEAVE_FROM_CHAT = 7
    KICK_FROM_CHAT = 8
    REMOVED_ADMINISTRATOR = 9
    SHOW_OR_REMOVED_KEYBOARD = 10


class ChangedChatSettingsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    type: typing.Optional[ChangedChatSettingsType]
    peer_id: typing.Optional[int]
    extra: typing.Optional[
        int
    ]  # https://github.com/danyadev/longpoll-doc#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-52-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%87%D0%B0%D1%82%D0%B0


class ChangedChatSettingsModel(pydantic.BaseModel):
    object: ChangedChatSettingsEventObject = pydantic.Field(None)


class TypingOrVoiceEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    from_ids: typing.Optional[typing.List[int]]
    from_ids_count: typing.Optional[int]
    timestamp: typing.Optional[int]


class TypingOrVoiceModel(pydantic.BaseModel):
    object: TypingOrVoiceEventObject = pydantic.Field(None)


class ChangedUnreadDialogsCountEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    count: typing.Optional[int]
    count_with_notifications: typing.Optional[int]


class ChangedUnreadDialogsCountModel(pydantic.BaseModel):
    object: ChangedUnreadDialogsCountEventObject = pydantic.Field(None)


class EventId:
    MESSAGE_EVENT = (3, 4, 5, 18)
    SET_FLAGS = 2
    READ_INCOMING_MESSAGES = 6
    READ_OUTGOING_MESSAGES = 7
    FRIEND_ONLINE = 8
    FRIEND_OFFLINE = 9
    SEEN_MENTION_IN_CHAT = 10
    NEW_MENTION_IN_CHAT = 12
    DELETED_ALL_MESSAGES_IN_DIALOG = 13
    DROP_MESSAGE_CACHE = 19
    CHANGE_CHAT_SETTINGS = 52
    USER_TYPING_OR_MAKING_VOICE_MESSAGE = (63, 64)
    CHANGED_UNREAD_DIALOGS_COUNT = 80

    # events after this are very strange and not typed yet
    CHANGED_USER_INVISIBLE_STATE: int = 81
    CHANGED_PUSH_SETTINGS_IN_CHAT: int = 114
    VOICE_CALL: int = 115  # ¯\_(ツ)_/¯


_message_event = {
    0: "event_id",
    1: "message_id",
    2: "flags",
    3: "peer_id",
    4: "timestamp",
    5: "text",
    6: "message_data",
    7: "extra_message_data",
    8: "random_id",
    9: "conversation_message_id",
    10: "edit_time",
}

_set_flags_event = {
    0: "event_id",
    1: "message_id",
    2: "flags",
    3: "peer_id",
}

_read_incoming_messages = {0: "event_id", 1: "peer_id", 2: "message_id",
                           3: "count"}

_read_outgoing_messages = {0: "event_id", 1: "peer_id", 2: "message_id",
                           3: "count"}

_friend_online = {
    0: "event_id",
    1: "user_id",
    2: "platform",
    3: "timestamp",
    4: "app_id",
}

_friend_offline = {
    0: "event_id",
    1: "user_id",
    2: "is_timeout",
    3: "timestamp",
    4: "app_id",
    5: "unexpected",
    6: "unexpected"
}

_seen_mention_in_chat = {
    0: "event_id",
    1: "peer_id",
    2: "flags",
}

_new_mention_in_chat = {
    0: "event_id",
    1: "peer_id",
    2: "flags",
}

_deleted_all_messages_in_chat = {
    0: "event_id",
    1: "peer_id",
    2: "last_message_id",
}

_drop_message_cache = {
    0: "event_id",
    1: "message_id",
}

_changed_chat_settings = {0: "event_id", 1: "type", 2: "peer_id", 3: "extra"}

_typing_or_voice = {
    0: "event_id",
    1: "peer_id",
    2: "from_ids",
    3: "from_ids_count",
    4: "timestamp",
}

_changed_unread_dialogs_count = {
    0: "event_id",
    1: "count",
    2: "count_with_notifications",
}

_events_dict = {
    EventId.MESSAGE_EVENT: _message_event,
    EventId.SET_FLAGS: _set_flags_event,
    EventId.READ_INCOMING_MESSAGES: _read_incoming_messages,
    EventId.READ_OUTGOING_MESSAGES: _read_outgoing_messages,
    EventId.FRIEND_ONLINE: _friend_online,
    EventId.FRIEND_OFFLINE: _friend_offline,
    EventId.SEEN_MENTION_IN_CHAT: _seen_mention_in_chat,
    EventId.NEW_MENTION_IN_CHAT: _new_mention_in_chat,
    EventId.DELETED_ALL_MESSAGES_IN_DIALOG: _deleted_all_messages_in_chat,
    EventId.DROP_MESSAGE_CACHE: _drop_message_cache,
    EventId.CHANGE_CHAT_SETTINGS: _changed_chat_settings,
    EventId.CHANGED_UNREAD_DIALOGS_COUNT: _changed_unread_dialogs_count,
}


def get_event_object(raw_event: list):
    event = {}
    event_type = raw_event[0]

    if event_type in EventId.MESSAGE_EVENT:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.MESSAGE_EVENT][event_number]
            ] = event_param

        print(event)
        return MessageEventModel(object=MessageEventObject(**event))
    elif event_type == EventId.SET_FLAGS:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.SET_FLAGS][
                event_number]] = event_param
        return SetFlagsEventModel(object=(SetFlagsEventObject(**event)))
    elif event_type == EventId.READ_INCOMING_MESSAGES:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.READ_INCOMING_MESSAGES][event_number]
            ] = event_param
        return ReadIncomingMessagesModel(
            object=(ReadIncomingMessagesEventObject(**event))
        )
    elif event_type == EventId.READ_OUTGOING_MESSAGES:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.READ_OUTGOING_MESSAGES][event_number]
            ] = event_param
        return ReadOutgoingMessagesModel(
            object=(ReadOutgoingMessagesEventObject(**event))
        )
    elif event_type == EventId.FRIEND_ONLINE:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.FRIEND_ONLINE][event_number]
            ] = event_param
        return FriendOnlineModel(object=(FriendOnlineEventObject(**event)))
    elif event_type == EventId.FRIEND_OFFLINE:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.FRIEND_OFFLINE][event_number]
            ] = event_param
        return FriendOfflineModel(object=(FriendOfflineEventObject(**event)))
    elif event_type == EventId.SEEN_MENTION_IN_CHAT:
        for event_number, event_param in enumerate(raw_event):
            event[
               _events_dict[EventId.SEEN_MENTION_IN_CHAT][event_number]
            ] = event_param
        return SeenMentionInChatModel(
            object=(SeenMentionInChatEventObject(**event))
        )
    elif event_type == EventId.NEW_MENTION_IN_CHAT:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.NEW_MENTION_IN_CHAT][event_number]
            ] = event_param
        return NewMentionInChatModel(
            object=(NewMentionInChatEventObject(**event)))
    elif event_type == EventId.DELETED_ALL_MESSAGES_IN_DIALOG:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.DELETED_ALL_MESSAGES_IN_DIALOG][
                    event_number
                ]
            ] = event_param
        return DeletedAllMessagesInDialogModel(
            object=(DeletedAllMessagesInDialogEventObject(**event))
        )
    elif event_type == EventId.DROP_MESSAGE_CACHE:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.DROP_MESSAGE_CACHE][event_number]
            ] = event_param
        return DropMessageCacheModel(
            object=(DropMessageCacheEventObject(**event)))
    elif event_type == EventId.CHANGE_CHAT_SETTINGS:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.CHANGE_CHAT_SETTINGS][event_number]
            ] = event_param
        return ChangedChatSettingsModel(
            object=(ChangedChatSettingsEventObject(**event))
        )
    elif event_type in EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE:
        for event_number, event_param in enumerate(raw_event):
            event[
               _events_dict[EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE][
                    event_number
                ]
            ] = event_param
        return TypingOrVoiceModel(object=(TypingOrVoiceEventObject(**event)))
    elif event_type == EventId.CHANGED_UNREAD_DIALOGS_COUNT:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.CHANGED_UNREAD_DIALOGS_COUNT][
                    event_number]
            ] = event_param
        return ChangedUnreadDialogsCountModel(
            object=(ChangedUnreadDialogsCountEventObject(**event))
        )
