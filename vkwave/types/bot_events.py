import typing
from enum import Enum

import pydantic

from .objects import (
    AudioAudio,
    BoardTopicComment,
    CallbackGroupJoinType,
    MessagesMessage,
    PhotosPhoto,
    VideoVideo,
    WallWallComment,
    WallWallpost,
)


class BotEventType(str, Enum):
    MESSAGE_NEW = "message_new"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    AUDIO_NEW = "audio_new"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPOST = "wall_repost"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    POLL_VOTE_NEW = "poll_vote_new"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    VKPAY_TRANSACTION = "vkpay_transaction"
    APP_PAYLOAD = "app_payload"
    CALLBACK_CONFIRMATION = "confirmation"


class BaseBotEvent(pydantic.BaseModel):
    type: str
    group_id: int
    object: typing.Union[
        "MessageNewObject",
        "MessagesMessage",
        "MessagesMessage",
        "MessageAllowObject",
        "MessageDenyObject",
        "PhotosPhoto",
        "PhotoCommentObject",
        "PhotoCommentObject",
        "PhotoCommentObject",
        "PhotoCommentDeleteObject",
        "AudioAudio",
        "VideoVideo",
        "VideoCommentObject",
        "VideoCommentObject",
        "VideoCommentObject",
        "VideoCommentDeleteObject",
        "WallPostObject",
        "WallPostObject",
        "WallReplyObject",
        "WallReplyObject",
        "WallReplyObject",
        "WallReplyDeleteObject",
        "BoardPostObject",
        "BoardPostObject",
        "BoardPostObject",
        "BoardPostDeleteObject",
        "MarketCommentObject",
        "MarketCommentObject",
        "MarketCommentObject",
        "MarketCommentDeleteObject",
        "GroupLeaveObject",
        "GroupJoinObject",
        "UserBlockObject",
        "UserUnblockObject",
        "PollVoteNewObject",
        "GroupOfficersEditObject",
        "GroupChangeSettingsObject",
        "GroupChangePhotoObject",
        "VkpayTransactionObject",
        "AppPayloadObject",
        "MessageTypingStateObject",
        "BaseBotEvent",
    ]
    event_id: typing.Optional[str]


class ClientInfo(pydantic.BaseModel):
    button_actions: typing.List[str] = pydantic.Field(None, description="")
    keyboard: bool = pydantic.Field(None, description="")
    inline_keyboard: bool = pydantic.Field(None, description="")
    carousel: bool = pydantic.Field(None, description="")
    lang_id: int = pydantic.Field(None, description="")


class MessageNewObject(pydantic.BaseModel):
    message: MessagesMessage = pydantic.Field(None, description="")
    client_info: ClientInfo = pydantic.Field(None, description="")


class MessageNew(BaseBotEvent):
    object: MessageNewObject = pydantic.Field(None, description="")


class MessageReply(BaseBotEvent):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageEdit(BaseBotEvent):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageTypingStateObject(pydantic.BaseModel):
    state: str = pydantic.Field(None, description="")
    from_id: int = pydantic.Field(None, description="")
    to_id: int = pydantic.Field(None, description="")


class MessageTypingState(BaseBotEvent):
    object: MessageTypingStateObject = pydantic.Field(None, description="")


class MessageAllowObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    key: str = pydantic.Field(None, description="")


class MessageAllow(BaseBotEvent):
    object: MessageAllowObject = pydantic.Field(None, description="")


class MessageDenyObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")


class MessageDeny(BaseBotEvent):
    object: MessageDenyObject = pydantic.Field(None, description="")


class PhotoNew(BaseBotEvent):
    object: PhotosPhoto = pydantic.Field(None, description="")


class PhotoCommentThreadModel(pydantic.BaseModel):
    count: int = pydantic.Field(None, description="")


class PhotoCommentObject(pydantic.BaseModel):
    id: int = pydantic.Field(None, description="")
    photo_id: int = pydantic.Field(None, description="")
    photo_owner_id: int = pydantic.Field(None, description="")
    text: str = pydantic.Field(None, description="")
    date: int = pydantic.Field(None, description="")
    from_id: int = pydantic.Field(None, description="")
    thread: PhotoCommentThreadModel = pydantic.Field(None, description="")
    parents_stack: typing.List[int] = pydantic.Field(None, description="")


class PhotoCommentNew(BaseBotEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentEdit(BaseBotEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentRestore(BaseBotEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    photo_id: int = pydantic.Field(None, description="")


class PhotoCommentDelete(BaseBotEvent):
    object: PhotoCommentDeleteObject = pydantic.Field(None, description="")


class AudioNew(BaseBotEvent):
    object: AudioAudio = pydantic.Field(None, description="")


class VideoNew(BaseBotEvent):
    object: VideoVideo = pydantic.Field(None, description="")


class VideoCommentObject(pydantic.BaseModel):
    video_id: int = pydantic.Field(None, description="")
    video_owner_id: int = pydantic.Field(None, description="")


class VideoCommentNew(BaseBotEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentEdit(BaseBotEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentRestore(BaseBotEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    video_id: int = pydantic.Field(None, description="")


class VideoCommentDelete(BaseBotEvent):
    object: VideoCommentDeleteObject = pydantic.Field(None, description="")


class WallPostObject(WallWallpost):  # type: ignore
    postponed_id: int = pydantic.Field(None, description="")


class WallPostNew(BaseBotEvent):
    object: WallPostObject = pydantic.Field(None, description="")


class WallRepost(BaseBotEvent):
    object: WallPostObject = pydantic.Field(None, description="")


class WallReplyObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")
    post_owner_id: int = pydantic.Field(None, description="")


class WallReplyNew(BaseBotEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyEdit(BaseBotEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyRestore(BaseBotEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")


class WallReplyDelete(BaseBotEvent):
    object: WallReplyDeleteObject = pydantic.Field(None, description="")


class BoardPostObject(pydantic.BaseModel):
    comment: BoardTopicComment = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")
    topic_owner_id: int = pydantic.Field(None, description="")


class BoardPostNew(BaseBotEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostEdit(BaseBotEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostRestore(BaseBotEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostDeleteObject(pydantic.BaseModel):
    topic_owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")


class BoardPostDelete(BaseBotEvent):
    object: BoardPostDeleteObject = pydantic.Field(None, description="")


class MarketCommentObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    market_owner_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentNew(BaseBotEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentEdit(BaseBotEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentRestore(BaseBotEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentDelete(BaseBotEvent):
    object: MarketCommentDeleteObject = pydantic.Field(None, description="")


class GroupLeaveEnum(int, Enum):
    NOT_SELF_LEAVED = 0
    SELF_LEAVED = 1


class GroupLeaveObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    self: GroupLeaveEnum = pydantic.Field(None, description="")


class GroupLeave(BaseBotEvent):
    object: GroupLeaveObject = pydantic.Field(None, description="")


class GroupJoinObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    join_type: CallbackGroupJoinType = pydantic.Field(None, description="")


class GroupJoin(BaseBotEvent):
    object: GroupJoinObject = pydantic.Field(None, description="")


class BlockReasonEnum(int, Enum):
    OTHER = 0
    SPAM = 1
    INSULT = 2
    SWEARING = 3
    OFFTOPIC = 4


class UserBlockObject(pydantic.BaseModel):
    admin_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    unblock_date: int = pydantic.Field(None, description="")
    reason: BlockReasonEnum = pydantic.Field(None, description="")
    comment: str = pydantic.Field(None, description="")


class UserBlock(BaseBotEvent):
    object: UserBlockObject = pydantic.Field(None, description="")


class UnblockByEndDateEnum(int, Enum):
    DATE_IS_NOT_END = 0
    DATE_IS_END = 1


class UserUnblockObject(pydantic.BaseModel):
    admin_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    by_end_date: UnblockByEndDateEnum = pydantic.Field(None, description="")


class UserUnblock(BaseBotEvent):
    object: UserUnblockObject = pydantic.Field(None, description="")


class PollVoteNewObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    poll_id: int = pydantic.Field(None, description="")
    option_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")


class PollVoteNew(BaseBotEvent):
    object: PollVoteNewObject = pydantic.Field(None, description="")


class GroupLevelEnum(int, Enum):
    NO_AUTHORITY = 0
    MODERATOR = 1
    REDACTOR = 2
    ADMINISTRATOR = 3


class GroupOfficersEditObject(pydantic.BaseModel):
    admin_id: int = pydantic.Field(None, description="")
    level_old: GroupLevelEnum = pydantic.Field(None, description="")
    level_new: GroupLevelEnum = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")


class GroupOfficersEdit(BaseBotEvent):
    object: GroupOfficersEditObject = pydantic.Field(None, description="")


class ChangesSettingsModel(pydantic.BaseModel):
    old_value: int = pydantic.Field(None, description="")
    new_value: int = pydantic.Field(None, description="")


class GroupChangeSettingsObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    changes: typing.Dict[str, ChangesSettingsModel] = pydantic.Field(None, description="")


class GroupChangeSettings(BaseBotEvent):
    object: GroupChangeSettingsObject = pydantic.Field(None, description="")


class GroupChangePhotoObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    photo: PhotosPhoto = pydantic.Field(None, description="")


class GroupChangePhoto(BaseBotEvent):
    object: GroupChangePhotoObject = pydantic.Field(None, description="")


class VkpayTransactionObject(pydantic.BaseModel):
    from_id: int = pydantic.Field(None, description="")
    amount: int = pydantic.Field(None, description="")
    description: str = pydantic.Field(None, description="")
    date: int = pydantic.Field(None, description="")


class VkpayTransaction(BaseBotEvent):
    object: VkpayTransactionObject = pydantic.Field(None, description="")


class AppPayloadObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    app_id: int = pydantic.Field(None, description="")
    payload: typing.Dict[str, str] = pydantic.Field(None, description="")
    group_id: int = pydantic.Field(None, description="")


class AppPayload(BaseBotEvent):
    object: AppPayloadObject = pydantic.Field(None, description="")


class CallBackConfirmation(BaseBotEvent):
    pass


_event_dict = {
    "message_new": MessageNew,
    "message_reply": MessageReply,
    "message_edit": MessageEdit,
    "message_allow": MessageAllow,
    "message_deny": MessageDeny,
    "photo_new": PhotoNew,
    "photo_comment_new": PhotoCommentNew,
    "photo_comment_edit": PhotoCommentEdit,
    "photo_comment_restore": PhotoCommentRestore,
    "photo_comment_delete": PhotoCommentDelete,
    "audio_new": AudioNew,
    "video_new": VideoNew,
    "video_comment_new": VideoCommentNew,
    "video_comment_edit": VideoCommentEdit,
    "video_comment_restore": VideoCommentRestore,
    "video_comment_delete": VideoCommentDelete,
    "wall_post_new": WallPostNew,
    "wall_repost": WallRepost,
    "wall_reply_new": WallReplyNew,
    "wall_reply_edit": WallReplyEdit,
    "wall_reply_restore": WallReplyRestore,
    "wall_reply_delete": WallReplyDelete,
    "board_post_new": BoardPostNew,
    "board_post_edit": BoardPostEdit,
    "board_post_restore": BoardPostRestore,
    "board_post_delete": BoardPostDelete,
    "market_comment_new": MarketCommentNew,
    "market_comment_edit": MarketCommentEdit,
    "market_comment_restore": MarketCommentRestore,
    "market_comment_delete": MarketCommentDelete,
    "group_leave": GroupLeave,
    "group_join": GroupJoin,
    "user_block": UserBlock,
    "user_unblock": UserUnblock,
    "poll_vote_new": PollVoteNew,
    "group_officers_edit": GroupOfficersEdit,
    "group_change_settings": GroupChangeSettings,
    "group_change_photo": GroupChangePhoto,
    "vkpay_transaction": VkpayTransaction,
    "app_payload": AppPayload,
    "confirmation": CallBackConfirmation,
    "message_typing_state": MessageTypingState,
}


def get_event_object(
    raw_event: typing.Dict[str, typing.Any],
) -> typing.Union[
    MessageNew,
    MessageReply,
    MessageEdit,
    MessageAllow,
    MessageDeny,
    PhotoNew,
    PhotoCommentNew,
    PhotoCommentEdit,
    PhotoCommentRestore,
    PhotoCommentDelete,
    AudioNew,
    VideoNew,
    VideoCommentNew,
    VideoCommentEdit,
    VideoCommentRestore,
    VideoCommentDelete,
    WallPostNew,
    WallRepost,
    WallReplyNew,
    WallReplyEdit,
    WallReplyRestore,
    WallReplyDelete,
    BoardPostNew,
    BoardPostEdit,
    BoardPostRestore,
    BoardPostDelete,
    MarketCommentNew,
    MarketCommentEdit,
    MarketCommentRestore,
    MarketCommentDelete,
    GroupLeave,
    GroupJoin,
    UserBlock,
    UserUnblock,
    PollVoteNew,
    GroupOfficersEdit,
    GroupChangeSettings,
    GroupChangePhoto,
    VkpayTransaction,
    AppPayload,
    CallBackConfirmation,
    MessageTypingState,
    BaseBotEvent,
]:
    event_type: str = raw_event["type"]
    event_model: typing.Type[BaseBotEvent] = _event_dict[event_type]
    return event_model(**raw_event)
