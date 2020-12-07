import pydantic


class MessagesSendPeerIdsData(pydantic.BaseModel):
    peer_id: int = pydantic.Field(
        ..., description="",
    )

