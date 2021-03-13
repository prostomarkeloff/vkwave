import typing
import pydantic
from enum import Enum


class MessagesSendPeerIdsData(pydantic.BaseModel):
    peer_id: int = pydantic.Field(
        ..., description="",
    )
