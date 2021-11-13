from vkwave.types.objects import *
from vkwave.types.extension_objects import *


class MessagesSendPeerIdsResponse(pydantic.BaseModel):
    response: List[MessagesSendPeerIdsData] = pydantic.Field(
        ...,
        description="",
    )


class ExecuteError(pydantic.BaseModel):
    method: str = pydantic.Field(..., description="")
    error_code: int = pydantic.Field(..., description="")
    error_msg: str = pydantic.Field(..., description="")


class ExecuteResponse(pydantic.BaseModel):
    response: Any = pydantic.Field(..., description="")
    execute_errors: Optional[List[ExecuteError]] = pydantic.Field(
        None, description=""
    )


class AudioGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(..., description="")
    items: List[AudioAudio] = pydantic.Field(..., description="")


class AudioGetResponse(pydantic.BaseModel):
    response: AudioGetResponseModel = pydantic.Field(..., description="")


class AudioGetByIdResponse(pydantic.BaseModel):
    response: List[AudioAudio] = pydantic.Field(..., description="")
