from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Money(Category):
    async def send_request(
        self,
        amount: int,
        receiver_id: int,
        message: str,
        pin_message: int = 0,
        total_amount: int = 0,
        accept_card: str = "",
        currency: str = "RUB",
        return_raw_response: bool = False,
    ) -> typing.Union[dict, BaseOkResponse]:
        """
        :param amount:
        :param receiver_id:
        :param message:
        :param pin_message:
        :param total_amount:
        :param accept_card:
        :param currency:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("sendRequest", params)
        return raw_result if return_raw_response else BaseOkResponse(**raw_result)
