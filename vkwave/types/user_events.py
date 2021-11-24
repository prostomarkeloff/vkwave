import enum
import typing

import logging
import pydantic

from .objects import MessagesKeyboard

logger = logging.getLogger(__name__)
RAW_EVENT_TYPE = typing.List[typing.Union[str, typing.Any]]


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
    UNREAD = 1 << 0
    OUTBOX = 1 << 1
    REPLIED = 1 << 2
    IMPORTANT = 1 << 3
    FROM_CHAT = 1 << 4
    FROM_FRIEND = 1 << 5
    MARKED_SPAM = 1 << 6
    DELETED = 1 << 7
    CHECKED_SPAM = 1 << 8
    ATTACHMENT = 1 << 9
    AUDIO_LISTENED = 1 << 12
    FROM_CHAT2 = 1 << 13
    CANCEL_SPAM = 1 << 15
    HIDDEN = 1 << 16
    DELETED_ALL = 1 << 17
    CHAT_IN = 1 << 19
    SILENT = 1 << 20
    REPLY_MSG = 1 << 21


def normalize_flags(flags: int) -> typing.List[typing.Union[MessageFlag, int]]:
    return [flag for flag in MessageFlag if flags & flag.value] + [flags]


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
    unused_fields: typing.Optional[typing.List]

    _normalize_flags = pydantic.validator("flags", allow_reuse=True)(normalize_flags)


class MessageEventModel(BaseUserEvent):
    object: MessageEventObject = pydantic.Field(None)


class SetFlagsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    flags: typing.Optional[typing.Union[int, typing.List[MessageFlag]]]
    peer_id: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]

    _normalize_flags = pydantic.validator("flags", allow_reuse=True)(normalize_flags)


class SetFlagsEventModel(BaseUserEvent):
    object: SetFlagsEventObject = pydantic.Field(None)


class ReadIncomingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class ReadIncomingMessagesModel(BaseUserEvent):
    object: ReadIncomingMessagesEventObject = pydantic.Field(None)


class ReadOutgoingMessagesEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    count: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


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
    OTHER = 8


class FriendOnlineEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    user_id: typing.Optional[int]
    platform: typing.Optional[PlatformEnum]
    timestamp: typing.Optional[int]
    app_id: typing.Optional[int]
    is_mobile: typing.Optional[int]
    has_invisible_mode: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


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
    is_mobile: typing.Optional[int]
    has_invisible_mode: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class FriendOfflineModel(BaseUserEvent):
    object: FriendOfflineEventObject = pydantic.Field(None)


class SeenMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[typing.Union[int, typing.List[MessageFlag]]]
    unused_fields: typing.Optional[typing.List]

    _normalize_flags = pydantic.validator("flags", allow_reuse=True)(normalize_flags)


class SeenMentionInChatModel(BaseUserEvent):
    object: SeenMentionInChatEventObject = pydantic.Field(None)


class NewMentionInChatEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    flags: typing.Optional[typing.Union[int, typing.List[MessageFlag]]]
    unused_fields: typing.Optional[typing.List]

    _normalize_flags = pydantic.validator("flags", allow_reuse=True)(normalize_flags)


class NewMentionInChatModel(BaseUserEvent):
    object: NewMentionInChatEventObject = pydantic.Field(None)


class DeletedAllMessagesInDialogEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    last_message_id: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class DeletedAllMessagesInDialogModel(BaseUserEvent):
    object: DeletedAllMessagesInDialogEventObject = pydantic.Field(None)


class DropMessageCacheEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    message_id: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class DropMessageCacheModel(BaseUserEvent):
    object: DropMessageCacheEventObject = pydantic.Field(None)


class ChangedChatSettingsType(int, enum.Enum):
    PHATOM_CHAT_CREATED = 0
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
    CHAT_INVITE = 12
    CONVERT_CONTACT_TO_USER = 13
    BUSINESS_NOTIFICATION = 14
    REVOKED_INVITATION = 15
    USER_DECLINED_INVITATION = 16
    USER_ACCEPTED_INVITATION = 17
    USER_INVITED = 18
    GROUP_CALL = 19
    CHAT_NOT_NEW = 22


class ChangedChatSettingsEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    type: typing.Optional[ChangedChatSettingsType]
    peer_id: typing.Optional[int]

    # some id, which may be in event
    extra: typing.Optional[
        int
    ]  # https://github.com/danyadev/longpoll-doc#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-52-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%87%D0%B0%D1%82%D0%B0

    unused_fields: typing.Optional[typing.List]


class ChangedChatSettingsModel(BaseUserEvent):
    object: ChangedChatSettingsEventObject = pydantic.Field(None)


class ChangedChatSettingsUselessEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    chat_id: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class ChangedChatSettingsUselessModel(BaseUserEvent):
    object: ChangedChatSettingsUselessEventObject = pydantic.Field(None)


class TypingOrVoiceEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    peer_id: typing.Optional[int]
    from_ids: typing.Optional[typing.List[int]]
    from_ids_count: typing.Optional[int]
    timestamp: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class TypingOrVoiceModel(BaseUserEvent):
    object: TypingOrVoiceEventObject = pydantic.Field(None)


class ChangedUnreadDialogsCountEventObject(pydantic.BaseModel):
    event_id: typing.Optional[int]
    unread_count: typing.Optional[int]
    unread_unmuted_count: typing.Optional[int]
    show_only_muted: typing.Optional[bool]
    business_notify_unread_count: typing.Optional[int]
    header_unread_count: typing.Optional[int]
    header_unread_unmuted_count: typing.Optional[int]
    unused_fields: typing.Optional[typing.List]


class ChangedUnreadDialogsCountModel(BaseUserEvent):
    object: ChangedUnreadDialogsCountEventObject = pydantic.Field(None)


RESULT_EVENT_OBJECT_TYPE = typing.Union[
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
    ChangedChatSettingsUselessModel,
    ChangedUnreadDialogsCountModel,
]


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
    CHANGE_CHAT_SETTINGS_USELESS = 51
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
    5: "is_mobile",
    6: "has_invisible",
}

_friend_offline = {
    0: "event_id",
    1: "user_id",
    2: "is_timeout",
    3: "timestamp",
    4: "app_id",
    5: "is_mobile",
    6: "has_invisible",
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

_drop_message_cache = {0: "event_id", 1: "message_id", 2: "expire_time"}

_changed_chat_settings = {0: "event_id", 1: "type", 2: "peer_id", 3: "extra"}

_changed_chat_settings_useless = {0: "event_id", 1: "chat_id"}

_typing_or_voice = {
    0: "event_id",
    1: "peer_id",
    2: "from_ids",
    3: "from_ids_count",
    4: "timestamp",
}

_changed_unread_dialogs_count = {
    0: "event_id",
    1: "unread_count",
    2: "unread_unmuted_count",
    3: "show_only_muted",
    4: "business_notify_unread_count",
    5: "header_unread_count",
    6: "header_unread_unmuted_count",
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
    EventId.CHANGE_CHAT_SETTINGS_USELESS: _changed_chat_settings_useless,
    EventId.CHANGED_UNREAD_DIALOGS_COUNT: _changed_unread_dialogs_count,
    EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE: _typing_or_voice,
}


def _parse_event(
    raw_event: RAW_EVENT_TYPE,
    event_id: EventId,
    event_model: typing.Type[RESULT_EVENT_OBJECT_TYPE],
    event_object: typing.Type[pydantic.BaseModel],
) -> RESULT_EVENT_OBJECT_TYPE:
    event = {}
    _unused_fields = []
    for event_number, event_param in enumerate(raw_event):
        key = _events_dict[event_id].get(event_number)
        if key:
            event[key] = event_param
        else:
            _unused_fields.append(event_param)
            logger.warn(f"New param ({event_param}) in {event_model.__name__}")
        event["unused_fields"] = _unused_fields

    return event_model(object=event_object(**event))


_parse_event_dict = {
    EventId.SET_FLAGS.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.SET_FLAGS,
        event_model=SetFlagsEventModel,
        event_object=SetFlagsEventObject,
    ),
    EventId.READ_INCOMING_MESSAGES.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.READ_INCOMING_MESSAGES,
        event_model=ReadIncomingMessagesModel,
        event_object=ReadIncomingMessagesEventObject,
    ),
    EventId.READ_OUTGOING_MESSAGES.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.READ_OUTGOING_MESSAGES,
        event_model=ReadOutgoingMessagesModel,
        event_object=ReadOutgoingMessagesEventObject,
    ),
    EventId.FRIEND_ONLINE.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.FRIEND_ONLINE,
        event_model=FriendOnlineModel,
        event_object=FriendOnlineEventObject,
    ),
    EventId.FRIEND_OFFLINE.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.FRIEND_OFFLINE,
        event_model=FriendOfflineModel,
        event_object=FriendOfflineEventObject,
    ),
    EventId.SEEN_MENTION_IN_CHAT.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.SEEN_MENTION_IN_CHAT,
        event_model=SeenMentionInChatModel,
        event_object=SeenMentionInChatEventObject,
    ),
    EventId.NEW_MENTION_IN_CHAT.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.NEW_MENTION_IN_CHAT,
        event_model=NewMentionInChatModel,
        event_object=NewMentionInChatEventObject,
    ),
    EventId.DELETED_ALL_MESSAGES_IN_DIALOG.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.DELETED_ALL_MESSAGES_IN_DIALOG,
        event_model=DeletedAllMessagesInDialogModel,
        event_object=DeletedAllMessagesInDialogEventObject,
    ),
    EventId.DROP_MESSAGE_CACHE.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.DROP_MESSAGE_CACHE,
        event_model=DropMessageCacheModel,
        event_object=DropMessageCacheEventObject,
    ),
    EventId.CHANGE_CHAT_SETTINGS.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.CHANGE_CHAT_SETTINGS,
        event_model=ChangedChatSettingsModel,
        event_object=ChangedChatSettingsEventObject,
    ),
    EventId.CHANGE_CHAT_SETTINGS_USELESS.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.CHANGE_CHAT_SETTINGS_USELESS,
        event_model=ChangedChatSettingsUselessModel,
        event_object=ChangedChatSettingsUselessEventObject,
    ),
    EventId.CHANGED_UNREAD_DIALOGS_COUNT.value: lambda raw_event: _parse_event(
        raw_event=raw_event,
        event_id=EventId.CHANGED_UNREAD_DIALOGS_COUNT,
        event_model=ChangedUnreadDialogsCountModel,
        event_object=ChangedUnreadDialogsCountEventObject,
    ),
}


def get_event_object(
    raw_event: RAW_EVENT_TYPE,
) -> typing.Optional[RESULT_EVENT_OBJECT_TYPE]:
    event_type = raw_event[0]

    if event_type in EventId.MESSAGE_EVENT.value:
        return _parse_event(
            raw_event=raw_event,
            event_id=EventId.MESSAGE_EVENT,
            event_model=MessageEventModel,
            event_object=MessageEventObject,
        )
    if event_type in EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE.value:
        return _parse_event(
            raw_event=raw_event,
            event_id=EventId.USER_TYPING_OR_MAKING_VOICE_MESSAGE,
            event_model=TypingOrVoiceModel,
            event_object=TypingOrVoiceEventObject,
        )

    if event_type not in _parse_event_dict:
        return None

    return _parse_event_dict[event_type](raw_event)
