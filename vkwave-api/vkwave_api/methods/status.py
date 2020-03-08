from ._category import Category
from vkwave_types.responses import StatusGetResponse
from typing import Optional


class Status(Category):
    async def get(
        self, user_id: Optional[int] = None, group_id: Optional[int] = None
    ) -> StatusGetResponse:
        params = {k: v for k, v in locals().items() if k != self and v is not None}
        result = await self.api_request("get", params)
        obj = StatusGetResponse(**result)
        return obj
