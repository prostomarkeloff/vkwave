import typing
import pydantic
from enum import Enum


class ParameterTypesEnum(str, Enum):
    array = "array"
    boolean = "boolean"
    integer = "integer"
    number = "number"
    string = "string"


class ParameterTypes(pydantic.BaseModel):
    enum: typing.Optional[ParameterTypesEnum] = pydantic.Field(
        None, description="",
    )


class ResponseTypesEnum(str, Enum):
    array = "array"
    boolean = "boolean"
    integer = "integer"
    number = "number"
    string = "string"
    object = "object"


class ResponseTypes(pydantic.BaseModel):
    enum: typing.Optional[ResponseTypesEnum] = pydantic.Field(
        None, description="",
    )


class Errors(pydantic.BaseModel):
    items: typing.Optional[typing.List["Error"]] = pydantic.Field(
        None, description="Possible errors",
    )


class JsonReference(pydantic.BaseModel):
    ref: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class ParameterArray(pydantic.BaseModel):
    items: typing.Optional[typing.List[str]] = pydantic.Field(
        None, description="",
    )


class ResponsePropertyTypesEnum(str, Enum):
    array = "array"
    boolean = "boolean"
    integer = "integer"
    number = "number"
    string = "string"


class ResponsePropertyTypes(pydantic.BaseModel):
    enum: typing.Optional[ResponsePropertyTypesEnum] = pydantic.Field(
        None, description="",
    )


class ItemTypesEnum(str, Enum):
    boolean = "boolean"
    integer = "integer"
    number = "number"
    string = "string"


class ItemTypes(pydantic.BaseModel):
    enum: typing.Optional[ItemTypesEnum] = pydantic.Field(
        None, description="",
    )


class Parameter(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Parameter name",
    )
    format: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    type: typing.Optional["ParameterTypes"] = pydantic.Field(
        None, description="Parameter type",
    )
    items: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )
    maxItems: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    minItems: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    maximum: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    minimum: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    ref: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    enum: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    enumNames: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    default: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    required: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    maxLength: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    minLength: typing.Optional[int] = pydantic.Field(
        None, description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Parameter description",
    )
    deprecated_from_version: typing.Optional[str] = pydantic.Field(
        None, description="Property deprecated from version",
    )
    from_version: typing.Optional[str] = pydantic.Field(
        None, description="Property implemented from version",
    )


class ResponseProperty(pydantic.BaseModel):
    type: typing.Optional["ResponseTypes"] = pydantic.Field(
        None, description="",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class Response(pydantic.BaseModel):
    type: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    deprecated_from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    items: typing.Optional[typing.Union[list, dict]] = pydantic.Field(
        None, description="",
    )
    required: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    title: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    oneOf: typing.Optional[list] = pydantic.Field(
        None, description="",
    )
    ref: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    properties: typing.Optional[dict] = pydantic.Field(
        None, description="",
    )


class Error(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Error name",
    )
    code: typing.Optional[int] = pydantic.Field(
        None, description="Error code",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Error description",
    )
    deprecated_from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )


class Method(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None, description="Method name",
    )
    description: typing.Optional[str] = pydantic.Field(
        None, description="Method description",
    )
    deprecated_from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    from_version: typing.Optional[str] = pydantic.Field(
        None, description="",
    )
    access_token_type: typing.Optional[list] = pydantic.Field(
        None, description="Input parameters for method",
    )
    parameters: typing.Optional[list] = pydantic.Field(
        None, description="Input parameters for method",
    )
    responses: typing.Optional[dict] = pydantic.Field(
        None, description="References to response objects",
    )
    emptyResponse: typing.Optional[bool] = pydantic.Field(
        None, description="",
    )
    errors: typing.Optional["Errors"] = pydantic.Field(
        None, description="",
    )
