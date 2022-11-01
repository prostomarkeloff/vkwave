from vkwave.types.extension_objects import *
from vkwave.types.objects import *


class MessagesSendPeerIdsResponse(pydantic.BaseModel):
    response: typing.List[MessagesSendPeerIdsData] = pydantic.Field(
        ...,
        description="",
    )


class ExecuteError(pydantic.BaseModel):
    method: str = pydantic.Field(..., description="")
    error_code: int = pydantic.Field(..., description="")
    error_msg: str = pydantic.Field(..., description="")


class ExecuteResponse(pydantic.BaseModel):
    response: typing.Any = pydantic.Field(..., description="")
    execute_errors: typing.Optional[typing.List[ExecuteError]] = pydantic.Field(
        None, description=""
    )


class AudioGetResponseModel(pydantic.BaseModel):
    count: int = pydantic.Field(..., description="")
    items: typing.List[AudioAudio] = pydantic.Field(..., description="")


class AudioGetResponse(pydantic.BaseModel):
    response: AudioGetResponseModel = pydantic.Field(..., description="")


class AudioGetByIdResponse(pydantic.BaseModel):
    response: typing.List[AudioAudio] = pydantic.Field(..., description="")
