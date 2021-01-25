import pydantic


class MessagesSendPeerIdsData(pydantic.BaseModel):
    peer_id: int = pydantic.Field(
        ..., description="",
    )
    message_id: int = pydantic.Field(
        None, description=""
    )
    conversation_message_id: int = pydantic.Field(
        None, description=""
    )
    error: dict = pydantic.Field(
        None, description=""
    )
 
