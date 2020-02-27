import typing
from enum import Enum

import pydantic

from .objects import (
    CallbackGroupJoinType,
    MessagesMessage,
    PhotosPhoto,
    AudioAudio,
    WallWallComment,
    WallWallpost,
    VideoVideo,
    BoardTopicComment,
)


class BaseEvent(pydantic.BaseModel):
    type: str
    group_id: int
    object: typing.Optional[typing.Any]
    event_id: str

class ClientInfo(pydantic.BaseModel):
    button_actions: list = pydantic.Field(None, description="")
    keyboard: bool = pydantic.Field(None, description="")
    inline_keyboard: bool = pydantic.Field(None, description="")
    carousel: bool = pydantic.Field(None, description="")
    lang_id: int = pydantic.Field(None, description="")


class MessageNewObject(pydantic.BaseModel):
    message: MessagesMessage = pydantic.Field(None, description="")
    client_info: ClientInfo = pydantic.Field(None, description="")


class MessageNew(BaseEvent):
    object: MessageNewObject = pydantic.Field(None, description="")


class MessageReply(BaseEvent):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageEdit(BaseEvent):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageTypingStateObject(pydantic.BaseModel):
    state: str = pydantic.Field(None, description="")
    from_id: int = pydantic.Field(None, description="")
    to_id: int = pydantic.Field(None, description="")


class MessageTypingState(BaseEvent):
    object: MessageTypingStateObject = pydantic.Field(None, description="")


class MessageAllowObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    key: str = pydantic.Field(None, description="")


class MessageAllow(BaseEvent):
    object: MessageAllowObject = pydantic.Field(None, description="")


class MessageDenyObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")


class MessageDeny(BaseEvent):
    object: MessageDenyObject = pydantic.Field(None, description="")


class PhotoNew(BaseEvent):
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
    parents_stack: list = pydantic.Field(None, description="")


class PhotoCommentNew(BaseEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentEdit(BaseEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentRestore(BaseEvent):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    photo_id: int = pydantic.Field(None, description="")


class PhotoCommentDelete(BaseEvent):
    object: PhotoCommentDeleteObject = pydantic.Field(None, description="")


class AudioNew(BaseEvent):
    object: AudioAudio = pydantic.Field(None, description="")


class VideoNew(BaseEvent):
    object: VideoVideo = pydantic.Field(None, description="")


class VideoCommentObject(pydantic.BaseModel):
    video_id: int = pydantic.Field(None, description="")
    video_owner_id: int = pydantic.Field(None, description="")


class VideoCommentNew(BaseEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentEdit(BaseEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentRestore(BaseEvent):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    video_id: int = pydantic.Field(None, description="")


class VideoCommentDelete(BaseEvent):
    object: VideoCommentDeleteObject = pydantic.Field(None, description="")


class WallPostObject(pydantic.BaseModel):
    post: WallWallpost = pydantic.Field(None, description="")
    postponed_id: int = pydantic.Field(None, description="")


class WallPostNew(BaseEvent):
    object: WallPostObject = pydantic.Field(None, description="")


class WallRepost(BaseEvent):
    object: WallPostObject = pydantic.Field(None, description="")


class WallReplyObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")
    post_owner_id: int = pydantic.Field(None, description="")


class WallReplyNew(BaseEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyEdit(BaseEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyRestore(BaseEvent):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")


class WallReplyDelete(BaseEvent):
    object: WallReplyDeleteObject = pydantic.Field(None, description="")


class BoardPostObject(pydantic.BaseModel):
    comment: BoardTopicComment = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")
    topic_owner_id: int = pydantic.Field(None, description="")


class BoardPostNew(BaseEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostEdit(BaseEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostRestore(BaseEvent):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostDeleteObject(pydantic.BaseModel):
    topic_owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")


class BoardPostDelete(BaseEvent):
    object: BoardPostDeleteObject = pydantic.Field(None, description="")


class MarketCommentObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    market_owner_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentNew(BaseEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentEdit(BaseEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentRestore(BaseEvent):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentDelete(BaseEvent):
    object: MarketCommentDeleteObject = pydantic.Field(None, description="")


class GroupLeaveEnum(int, Enum):
    NOT_SELF_LEAVED = 0
    SELF_LEAVED = 1


class GroupLeaveObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    self: GroupLeaveEnum = pydantic.Field(None, description="")


class GroupLeave(BaseEvent):
    object: GroupLeaveObject = pydantic.Field(None, description="")


class GroupJoinObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    join_type: CallbackGroupJoinType = pydantic.Field(None, description="")


class GroupJoin(BaseEvent):
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


class UserBlock(BaseEvent):
    object: UserBlockObject = pydantic.Field(None, description="")


class UnblockByEndDateEnum(int, Enum):
    DATE_IS_NOT_END = 0
    DATE_IS_END = 1


class UserUnblockObject(pydantic.BaseModel):
    admin_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    by_end_date: UnblockByEndDateEnum = pydantic.Field(None, description="")


class UserUnblock(BaseEvent):
    object: UserUnblockObject = pydantic.Field(None, description="")


class PollVoteNewObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    poll_id: int = pydantic.Field(None, description="")
    option_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")


class PollVoteNew(BaseEvent):
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


class GroupOfficersEdit(BaseEvent):
    object: GroupOfficersEditObject = pydantic.Field(None, description="")


class ChangesSettingsModel(pydantic.BaseModel):
    old_value: int = pydantic.Field(None, description="")
    new_value: int = pydantic.Field(None, description="")


class GroupChangeSettingsObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    changes: typing.Dict[str, ChangesSettingsModel] = pydantic.Field(None, description="")


class GroupChangeSettings(BaseEvent):
    object: GroupChangeSettingsObject = pydantic.Field(None, description="")


class GroupChangePhotoObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    photo: PhotosPhoto = pydantic.Field(None, description="")


class GroupChangePhoto(BaseEvent):
    object: GroupChangePhotoObject = pydantic.Field(None, description="")


class VkpayTransactionObject(pydantic.BaseModel):
    from_id: int = pydantic.Field(None, description="")
    amount: int = pydantic.Field(None, description="")
    description: str = pydantic.Field(None, description="")
    date: int = pydantic.Field(None, description="")


class VkpayTransaction(BaseEvent):
    object: VkpayTransactionObject = pydantic.Field(None, description="")


class AppPayloadObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    app_id: int = pydantic.Field(None, description="")
    payload: typing.Dict[str, str] = pydantic.Field(None, description="")
    group_id: int = pydantic.Field(None, description="")


class AppPayload(BaseEvent):
    object: AppPayloadObject = pydantic.Field(None, description="")


class CallBackConfirmation(BaseEvent):
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
        raw_event: dict,
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
    BaseEvent,
]:
    event_type: str = raw_event["type"]
    event_model: typing.Type[BaseEvent] = _event_dict[event_type]
    return event_model(**raw_event)
