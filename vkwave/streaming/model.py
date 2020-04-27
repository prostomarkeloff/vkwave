from enum import Enum
from typing import Optional, Any, List

import pydantic

from vkwave.api.methods import APIOptionsRequestContext
from vkwave.types.user_events import PlatformEnum


class Rule(pydantic.BaseModel):
    value: str
    tag: str


class StreamingClientData:
    def __init__(self, endpoint: str, key: str):
        self.endpoint: str = endpoint
        self.key: str = key

    @classmethod
    async def get(cls, api: APIOptionsRequestContext) -> "StreamingClientData":
        s = await api.streaming.get_server_url()
        return cls(endpoint=s.response.endpoint, key=s.response.key)


class ServiceMessage(pydantic.BaseModel):
    message: str
    service_code: int


class EventType(str, Enum):
    post = "post"
    comment = "comment"
    share = "share"
    topic_post = "topic_post"


class EventID(pydantic.BaseModel):
    post_owner_id: Optional[int]
    post_id: Optional[int]
    comment_id: Optional[int]
    shared_post_id: Optional[int]
    topic_owner_id: Optional[int]
    topic_id: Optional[int]
    topic_post_id: Optional[int]


class Action(str, Enum):
    new = "new"
    update = "update"
    delete = "delete"
    restore = "restore"


class Author(pydantic.BaseModel):
    id: int
    author_url: str
    shared_post_author_id: Optional[int]
    shared_post_author_url: Optional[str]
    platform: Optional[PlatformEnum]


class Event(pydantic.BaseModel):
    event_type: EventType
    event_id: EventID
    event_url: str
    text: str
    action: Action
    creation_time: int
    attachments: Any
    geo: Any
    shared_post_text: Optional[str]
    shared_post_creation_time: Optional[int]
    singer_id: Optional[int]
    tags: List[str]
    author: Author


class StreamingMessage(pydantic.BaseModel):
    code: int
    service_message: Optional[ServiceMessage]
    event: Event
