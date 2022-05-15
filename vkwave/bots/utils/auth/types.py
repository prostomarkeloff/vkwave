from enum import Enum

from pydantic import BaseModel, Field


class OAuthResponse(BaseModel):
    access_token: str = Field(None, description="")
    expires_in: int = Field(None, description="")
    user_id: int = Field(None, description="")
    trusted_hash: str = Field(None, description="")


class ClientHash(Enum):
    ANDROID_APP = 'hHbZxrka2uZ6jB1inYsH'
    WINDOWS_APP = 'AlVXZFMUqyrnABp8ncuU'
    IPHONE_APP = 'VeWdmVclDCtn6ihuP1nt'
    KATE_MOBILE = 'hHbJug59sKJie78wjrH8'
    VK_ME = 'qVxWRF1CwHERuIrKBnqe'


class ClientID(Enum):
    ANDROID_APP = 2274003
    WINDOWS_APP = 3697615
    IPHONE_APP = 3140623
    KATE_MOBILE = 2685278
    VK_ME = 6146827
