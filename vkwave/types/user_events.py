import enum
import typing

import pydantic

from .objects import MessagesKeyboard


class BaseUserEvent(pydantic.BaseModel):
    object: typing.Union[
        "MessageEventObject",
        "SetFlagsEventObject",
        "ReadIncomingMessagesEventObject",
        "ReadOutgoingMessagesEventObject",
        "FriendOnlineEventObject",
        "FriendOfflineEventObject",
        "SeenMentionInChatEventObject",
        "NewMentionInChatEventObject",
        "DeletedAllMessagesInDialogEventObject",
        "DropMessageCacheEventObject",
        "ChangedChatSettingsEventObject",
        "TypingOrVoiceEventObject",
        "ChangedUnreadDialogsCountEventObject",
        "MessageEventObject",
    ]


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
    payload: typing.Optional[str]
    source_act: typing.Optional[str]
    source_mid: typing.Optional[str]
    mentions: typing.Optional[typing.List[int]]
    marked_users: typing.Optional[typing.Any]  # useless
    keyboard: typing.Optional[MessagesKeyboard]
    service_message: typing.Optional[ServiceMessageData]


class MessageFlag(enum.Enum):
    UNREAD = 1
    OUTBOX = 2
    REPLIED = 2 ** 2
    IMPORTANT = 2 ** 3
    FROM_CHAT = 2 ** 4
    FROM_FRIEND = 2 ** 5
    MARKED_SPAM = 2 ** 6
    DELETED = 2 ** 7
    CHECKED_SPAM = 2 ** 8
    ATTACHMENT = 2 ** 9
    HIDDEN = 2 ** 16
    DELETED_ALL = 2 ** 17


class MessageEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    flags: typing.Optional[typing.Union[int, typing.List[MessageFlag]]]
    peer_id: typing.Optional[int]
    timestamp: typing.Optional[int]
    text: typing.Optional[str]
    message_data: typing.Optional[MessageData]
    extra_message_data: typing.Optional[typing.Dict[str, str]]
    random_id: typing.Optional[int]
    conversation_message_id: typing.Optional[int]
    edit_time: typing.Optional[int]

    _normalize_flags = pydantic.validator("flags", allow_reuse=True)(
        lambda flags: [flag for flag in MessageFlag if flags & flag.value] + [flags]
    )


class MessageEventModel(BaseUserEvent):
    object: MessageEventObject = pydantic.Field(None)


class SetFlagsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    flags: typing.Optional[int]
    peer_id: typing.Optional[int]


class SetFlagsEventModel(BaseUserEvent):
    object: SetFlagsEventObject = pydantic.Field(None)


class ReadIncomingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]


class ReadIncomingMessagesModel(BaseUserEvent):
    object: ReadIncomingMessagesEventObject = pydantic.Field(None)


class ReadOutgoingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]


class ReadOutgoingMessagesModel(BaseUserEvent):
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


class FriendOnlineModel(BaseUserEvent):
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


class FriendOfflineModel(BaseUserEvent):
    object: FriendOfflineEventObject = pydantic.Field(None)


class SeenMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[int]


class SeenMentionInChatModel(BaseUserEvent):
    object: SeenMentionInChatEventObject = pydantic.Field(None)


class NewMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[int]


class NewMentionInChatModel(BaseUserEvent):
    object: NewMentionInChatEventObject = pydantic.Field(None)


class DeletedAllMessagesInDialogEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    last_message_id: typing.Optional[int]


class DeletedAllMessagesInDialogModel(BaseUserEvent):
    object: DeletedAllMessagesInDialogEventObject = pydantic.Field(None)


class DropMessageCacheEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]


class DropMessageCacheModel(BaseUserEvent):
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
    SHOW_OR_REMOVED_KEYBOARD = 11


class ChangedChatSettingsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    type: typing.Optional[ChangedChatSettingsType]
    peer_id: typing.Optional[int]

    # some id, which may be in event
    extra: typing.Optional[
        int
    ]  # https://github.com/danyadev/longpoll-doc#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-52-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%87%D0%B0%D1%82%D0%B0


class ChangedChatSettingsModel(BaseUserEvent):
    object: ChangedChatSettingsEventObject = pydantic.Field(None)


class TypingOrVoiceEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    from_ids: typing.Optional[typing.List[int]]
    from_ids_count: typing.Optional[int]
    timestamp: typing.Optional[int]


class TypingOrVoiceModel(BaseUserEvent):
    object: TypingOrVoiceEventObject = pydantic.Field(None)


class ChangedUnreadDialogsCountEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    count: typing.Optional[int]
    count_with_notifications: typing.Optional[int]


class ChangedUnreadDialogsCountModel(BaseUserEvent):
    object: ChangedUnreadDialogsCountEventObject = pydantic.Field(None)


class EventId(enum.Enum):
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

_read_incoming_messages = {0: "event_id", 1: "peer_id", 2: "message_id", 3: "count"}

_read_outgoing_messages = {0: "event_id", 1: "peer_id", 2: "message_id", 3: "count"}

_friend_online = {
    0: "event_id",
    1: "user_id",
    2: "platform",
    3: "timestamp",
    4: "app_id",
    5: "unexpected",
    6: "unexpected",
}

_friend_offline = {
    0: "event_id",
    1: "user_id",
    2: "is_timeout",
    3: "timestamp",
    4: "app_id",
    5: "unexpected",
    6: "unexpected",
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
    3: "extra",
    4: "extra2",
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
    EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE: _typing_or_voice,
}


def get_event_object(
    raw_event: typing.List[typing.Union[str, typing.Any]],
) -> typing.Optional[
    typing.Union[
        MessageEventModel,
        SetFlagsEventModel,
        ReadIncomingMessagesModel,
        ReadOutgoingMessagesModel,
        FriendOnlineModel,
        FriendOfflineModel,
        SeenMentionInChatModel,
        SeenMentionInChatModel,
        DeletedAllMessagesInDialogModel,
        DropMessageCacheModel,
        TypingOrVoiceModel,
        NewMentionInChatModel,
        ChangedChatSettingsModel,
        ChangedUnreadDialogsCountModel,
    ]
]:
    event = {}
    event_type = raw_event[0]

    if event_type in EventId.MESSAGE_EVENT.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.MESSAGE_EVENT][event_number]] = event_param
        return MessageEventModel(object=MessageEventObject(**event))
    if event_type == EventId.SET_FLAGS.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.SET_FLAGS][event_number]] = event_param
        return SetFlagsEventModel(object=(SetFlagsEventObject(**event)))
    if event_type == EventId.READ_INCOMING_MESSAGES.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.READ_INCOMING_MESSAGES][event_number]] = event_param
        return ReadIncomingMessagesModel(object=(ReadIncomingMessagesEventObject(**event)))
    if event_type == EventId.READ_OUTGOING_MESSAGES.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.READ_OUTGOING_MESSAGES][event_number]] = event_param
        return ReadOutgoingMessagesModel(object=(ReadOutgoingMessagesEventObject(**event)))
    if event_type == EventId.FRIEND_ONLINE.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.FRIEND_ONLINE][event_number]] = event_param
        return FriendOnlineModel(object=(FriendOnlineEventObject(**event)))
    if event_type == EventId.FRIEND_OFFLINE.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.FRIEND_OFFLINE][event_number]] = event_param
        return FriendOfflineModel(object=(FriendOfflineEventObject(**event)))
    if event_type == EventId.SEEN_MENTION_IN_CHAT.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.SEEN_MENTION_IN_CHAT][event_number]] = event_param
        return SeenMentionInChatModel(object=(SeenMentionInChatEventObject(**event)))
    if event_type == EventId.NEW_MENTION_IN_CHAT.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.NEW_MENTION_IN_CHAT][event_number]] = event_param
        return NewMentionInChatModel(object=(NewMentionInChatEventObject(**event)))
    if event_type == EventId.DELETED_ALL_MESSAGES_IN_DIALOG.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.DELETED_ALL_MESSAGES_IN_DIALOG][event_number]] = event_param
        return DeletedAllMessagesInDialogModel(
            object=(DeletedAllMessagesInDialogEventObject(**event))
        )
    if event_type == EventId.DROP_MESSAGE_CACHE.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.DROP_MESSAGE_CACHE][event_number]] = event_param
        return DropMessageCacheModel(object=(DropMessageCacheEventObject(**event)))
    if event_type == EventId.CHANGE_CHAT_SETTINGS.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.CHANGE_CHAT_SETTINGS][event_number]] = event_param
        return ChangedChatSettingsModel(object=(ChangedChatSettingsEventObject(**event)))
    if event_type in EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE.value:
        for event_number, event_param in enumerate(raw_event):
            event[
                _events_dict[EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE][event_number]
            ] = event_param
        return TypingOrVoiceModel(object=(TypingOrVoiceEventObject(**event)))
    if event_type == EventId.CHANGED_UNREAD_DIALOGS_COUNT.value:
        for event_number, event_param in enumerate(raw_event):
            event[_events_dict[EventId.CHANGED_UNREAD_DIALOGS_COUNT][event_number]] = event_param
        return ChangedUnreadDialogsCountModel(
            object=(ChangedUnreadDialogsCountEventObject(**event))
        )
    return None
