from .objects import *


class ClientInfo(pydantic.BaseModel):
    button_actions: list = pydantic.Field(None, description="")
    keyboard: bool = pydantic.Field(None, description="")
    inline_keyboard: bool = pydantic.Field(None, description="")
    carousel: bool = pydantic.Field(None, description="")
    lang_id: int = pydantic.Field(None, description="")


class MessageNewObject(pydantic.BaseModel):
    message: MessagesMessage = pydantic.Field(None, description="")
    client_info: ClientInfo = pydantic.Field(None, description="")


class MessageNew(pydantic.BaseModel):
    object: MessageNewObject = pydantic.Field(None, description="")


class MessageReply(pydantic.BaseModel):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageEdit(pydantic.BaseModel):
    object: MessagesMessage = pydantic.Field(None, description="")


class MessageAllowObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    key: str = pydantic.Field(None, description="")


class MessageAllow(pydantic.BaseModel):
    object: MessageAllowObject = pydantic.Field(None, description="")


class MessageDenyObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")


class MessageDeny(pydantic.BaseModel):
    object: MessageDenyObject = pydantic.Field(None, description="")


class PhotoNew(pydantic.BaseModel):
    object: PhotosPhoto = pydantic.Field(None, description="")


class PhotoCommentObject(pydantic.BaseModel):
    photo_id: int = pydantic.Field(None, description="")
    photo_owner_id: int = pydantic.Field(None, description="")


class PhotoCommentNew(pydantic.BaseModel):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentEdit(pydantic.BaseModel):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentRestore(pydantic.BaseModel):
    object: PhotoCommentObject = pydantic.Field(None, description="")


class PhotoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    photo_id: int = pydantic.Field(None, description="")


class PhotoCommentDelete(pydantic.BaseModel):
    object: PhotoCommentDeleteObject = pydantic.Field(None, description="")


class AudioNew(pydantic.BaseModel):
    object: AudioAudio = pydantic.Field(None, description="")


class VideoNew(pydantic.BaseModel):
    object: VideoVideo = pydantic.Field(None, description="")


class VideoCommentObject(pydantic.BaseModel):
    video_id: int = pydantic.Field(None, description="")
    video_owner_id: int = pydantic.Field(None, description="")


class VideoCommentNew(pydantic.BaseModel):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentEdit(pydantic.BaseModel):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentRestore(pydantic.BaseModel):
    object: VideoCommentObject = pydantic.Field(None, description="")


class VideoCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    video_id: int = pydantic.Field(None, description="")


class VideoCommentDelete(pydantic.BaseModel):
    object: VideoCommentDeleteObject = pydantic.Field(None, description="")


class WallPostObject(pydantic.BaseModel):
    post: WallWallpost = pydantic.Field(None, description="")
    postponed_id: int = pydantic.Field(None, description="")


class WallPostNew(pydantic.BaseModel):
    object: WallPostObject = pydantic.Field(None, description="")


class WallRepost(pydantic.BaseModel):
    object: WallPostObject = pydantic.Field(None, description="")


class WallReplyObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")
    post_owner_id: int = pydantic.Field(None, description="")


class WallReply(pydantic.BaseModel):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyEdit(pydantic.BaseModel):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyRestore(pydantic.BaseModel):
    object: WallReplyObject = pydantic.Field(None, description="")


class WallReplyDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    post_id: int = pydantic.Field(None, description="")


class WallReplyDelete(pydantic.BaseModel):
    object: WallReplyDeleteObject = pydantic.Field(None, description="")


class BoardPostObject(pydantic.BaseModel):
    comment: BoardTopicComment = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")
    topic_owner_id: int = pydantic.Field(None, description="")


class BoardPostNew(pydantic.BaseModel):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostEdit(pydantic.BaseModel):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostRestore(pydantic.BaseModel):
    object: BoardPostObject = pydantic.Field(None, description="")


class BoardPostDeleteObject(pydantic.BaseModel):
    topic_owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    topic_id: int = pydantic.Field(None, description="")


class BoardPostDelete(pydantic.BaseModel):
    object: BoardPostDeleteObject = pydantic.Field(None, description="")


class MarketCommentObject(pydantic.BaseModel):
    comment: WallWallComment = pydantic.Field(None, description="")
    market_owner_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentNew(pydantic.BaseModel):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentEdit(pydantic.BaseModel):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentRestore(pydantic.BaseModel):
    object: MarketCommentObject = pydantic.Field(None, description="")


class MarketCommentDeleteObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    deleter_id: int = pydantic.Field(None, description="")
    item_id: int = pydantic.Field(None, description="")


class MarketCommentDelete(pydantic.BaseModel):
    object: MarketCommentDeleteObject = pydantic.Field(None, description="")


class GroupLeaveEnum(int, Enum):
    NOT_SELF_LEAVED = 0
    SELF_LEAVED = 1


class GroupLeaveObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    self: GroupLeaveEnum = pydantic.Field(None, description="")


class GroupLeave(pydantic.BaseModel):
    object: GroupLeaveObject = pydantic.Field(None, description="")


class JoinTypeEnum(str, Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class GroupJoinObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    join_type: JoinTypeEnum = pydantic.Field(None, description="")


class GroupJoin(pydantic.BaseModel):
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


class UserBlock(pydantic.BaseModel):
    object: UserBlockObject = pydantic.Field(None, description="")


class UnblockByEndDateEnum(int, Enum):
    DATE_IS_NOT_END = 0
    DATE_IS_END = 1


class UserUnblockObject(pydantic.BaseModel):
    admin_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")
    by_end_date: UnblockByEndDateEnum = pydantic.Field(None, description="")


class UserUnblock(pydantic.BaseModel):
    object: UserUnblockObject = pydantic.Field(None, description="")


class PollVoteNewObject(pydantic.BaseModel):
    owner_id: int = pydantic.Field(None, description="")
    poll_id: int = pydantic.Field(None, description="")
    option_id: int = pydantic.Field(None, description="")
    user_id: int = pydantic.Field(None, description="")


class PollVoteNew(pydantic.BaseModel):
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


class GroupOfficersEdit(pydantic.BaseModel):
    object: GroupOfficersEditObject = pydantic.Field(None, description="")


class ChangedSettingEnum(str, Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    ACCESS = "access"
    SCREEN_NAME = "screen_name"
    PUBLIC_CATEGORY = "public_category"
    PUBLIC_SUBCATEGORY = "public_subcategory"
    AGE_LIMITS = "age_limits"
    WEBSITE = "website"
    ENABLE_STATUS_DEFAULT = "enable_status_default"
    ENABLE_PHOTO = "enable_photo"
    ENABLE_AUDIO = "enable_audio"
    ENABLE_VIDEO = "enable_video"
    ENABLE_MARKET = "enable_market"


class ChangesSettingsModel(pydantic.BaseModel):
    field: ChangedSettingEnum = pydantic.Field(None, description="")
    old_value: int = pydantic.Field(None, description="")
    new_value: int = pydantic.Field(None, description="")


class GroupChangeSettingsObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    changes: ChangesSettingsModel = pydantic.Field(None, description="")


class GroupChangeSettings(pydantic.BaseModel):
    object: GroupChangeSettingsObject = pydantic.Field(None, description="")


class GroupChangePhotoObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    photo: PhotosPhoto = pydantic.Field(None, description="")


class GroupChangePhoto(pydantic.BaseModel):
    object: GroupChangePhotoObject = pydantic.Field(None, description="")


class VkpayTransactionObject(pydantic.BaseModel):
    from_id: int = pydantic.Field(None, description="")
    amount: int = pydantic.Field(None, description="")
    description: str = pydantic.Field(None, description="")
    date: int = pydantic.Field(None, description="")


class VkpayTransaction(pydantic.BaseModel):
    object: VkpayTransactionObject = pydantic.Field(None, description="")


class AppPayloadObject(pydantic.BaseModel):
    user_id: int = pydantic.Field(None, description="")
    app_id: int = pydantic.Field(None, description="")
    payload: typing.Dict[str, str] = pydantic.Field(None, description="")
    group_id: int = pydantic.Field(None, description="")


class AppPayload(pydantic.BaseModel):
    object: AppPayloadObject = pydantic.Field(None, description="")
