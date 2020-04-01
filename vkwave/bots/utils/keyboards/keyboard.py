import json
import typing
from enum import Enum

from vkwave.bots.core.types.json_types import JSONEncoder
from vkwave.bots.utils.keyboards._types import Button


class ButtonColor(Enum):
    PRIMARY = "primary"  # blue
    SECONDARY = "secondary"  # white
    NEGATIVE = "negative"  # red
    POSITIVE = "positive"  # green


class ButtonType(Enum):
    TEXT = "text"
    LINK = "open_link"
    LOCATION = "location"
    VKPAY = "vkpay"
    VKAPPS = "open_app"


class Keyboard:
    def __init__(self, one_time: bool, inline: bool = False):
        """
        Create a keyboard object
        :param one_time:
        """
        self.one_time = one_time
        self.buttons: typing.List[typing.List[Button]] = [[]]
        self.keyboard = {
            "one_time": one_time,
            "buttons": self.buttons,
            "inline": inline,
        }

    @staticmethod
    def _generate_payload(
        payload: typing.Optional[typing.Dict[str, str]]
    ) -> typing.Union[str, typing.Dict[str, str]]:
        return payload if payload is not None else ""

    def add_row(self) -> None:
        """
        :return:
        """
        self.buttons.append([])

    def _add_button(self, action: dict) -> None:
        """
        :param action:
        :return:
        """
        current_row = self.buttons[-1]
        current_row.append(action)

    def add_text_button(
        self,
        text: str,
        color: ButtonColor = ButtonColor.PRIMARY,
        payload: typing.Optional[typing.Dict[str, str]] = None,
    ) -> None:
        """
        :param text:
        :param color:
        :param payload:
        :return:
        """
        action = {
            "action": {
                "type": ButtonType.TEXT.value,
                "payload": self._generate_payload(payload),
                "label": text,
            },
            "color": color.value,
        }

        self._add_button(action)

    def add_location_button(self, payload: dict = None) -> None:
        """
        :param payload:
        :return:
        """

        action = {
            "action": {
                "type": ButtonType.LOCATION.value,
                "payload": self._generate_payload(payload),
            }
        }

        self._add_button(action)

    def add_link_button(self, text: str, link: str, payload: dict = None) -> None:
        action = {
            "action": {
                "type": ButtonType.LINK.value,
                "label": text,
                "link": link,
                "payload": self._generate_payload(payload),
            }
        }

        self._add_button(action)

    def add_vkpay_button(self, hash: str, payload: dict = None) -> None:
        """
        :param hash:
        :param payload:
        :return:
        """

        action = {
            "action": {
                "type": ButtonType.VKPAY.value,
                "payload": self._generate_payload(payload),
                "hash": hash,
            }
        }

        self._add_button(action)

    def add_vkapps_button(
        self, app_id: int, owner_id: int, label: str, payload: dict = None
    ) -> None:
        """
        :param app_id:
        :param owner_id:
        :param payload:
        :param label:
        :return:
        """

        action = {
            "action": {
                "type": ButtonType.VKAPPS.value,
                "app_id": app_id,
                "owner_id": owner_id,
                "payload": self._generate_payload(payload),
                "label": label,
            }
        }

        self._add_button(action)

    def get_keyboard(self, json_serialize: JSONEncoder = json.dumps) -> str:
        """
        Get keyboard json to send.
        If keyboard is 'static', you can generate json once and send it every time.
        :return:
        """
        return json_serialize(self.keyboard)

    @classmethod
    def get_empty_keyboard(cls) -> str:
        """
        :return:
        """
        keyboard = Keyboard(one_time=True)
        keyboard.keyboard["buttons"] = []
        return keyboard.get_keyboard()
