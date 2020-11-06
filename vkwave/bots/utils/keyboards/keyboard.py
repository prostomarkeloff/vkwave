import json
import typing
from enum import Enum

from vkwave.bots.core.types.json_types import JSONEncoder
from vkwave.bots.utils.keyboards._types import Button

from vkwave.bots.utils.keyboards._vkpayaction import VKPayAction


class ButtonColor(Enum):
    PRIMARY = "primary"  # blue
    SECONDARY = "secondary"  # white
    NEGATIVE = "negative"  # red
    POSITIVE = "positive"  # green


class ButtonType(Enum):
    TEXT = "text"
    LINK = "open_link"
    CALLBACK = "callback"
    LOCATION = "location"
    VKPAY = "vkpay"
    VKAPPS = "open_app"


class Keyboard:
    def __init__(self, one_time: bool = False, inline: bool = False):
        """
        Create a keyboard object
        :param one_time:
        """
        self.one_time = one_time
        self.buttons: typing.List[typing.List[Button]] = [[]]
        self.keyboard = {
            "buttons": self.buttons,
            "inline": inline,
        }
        if not inline:
            self.keyboard["one_time"] = one_time

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
        color: typing.Union[str, ButtonColor] = ButtonColor.PRIMARY,
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
            "color": color.value if isinstance(color, ButtonColor) else color,
        }

        self._add_button(action)

    def add_callback_button(
        self,
        text: str,
        color: typing.Union[str, ButtonColor] = ButtonColor.PRIMARY,
        payload: typing.Optional[typing.Dict[str, str]] = None,
    ):
        action = {
            "action": {
                "type": "callback",
                "payload": self._generate_payload(payload),
                "label": text,
            },
            "color": color.value if isinstance(color, ButtonColor) else color,
        }
        self._add_button(action)

    def add_location_button(self, payload: typing.Optional[typing.Dict[str, str]] = None) -> None:
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

    def add_link_button(
        self, text: str, link: str, payload: typing.Optional[typing.Dict[str, str]] = None
    ) -> None:
        action = {
            "action": {
                "type": ButtonType.LINK.value,
                "label": text,
                "link": link,
                "payload": self._generate_payload(payload),
            }
        }

        self._add_button(action)

    def add_vkpay_button(
        self,
        hash: typing.Union[VKPayAction, str],
        aid: int = 10,
        payload: typing.Optional[typing.Dict[str, str]] = None
    ) -> None:
        """
        :param hash: subclass of VKPayAction or action string like "transfer-to-group&group_id=123"
        :param aid: application id (currently not supported)
        :param payload:
        :return:
        """

        _hash: str
        if isinstance(hash, VKPayAction):
            _hash = hash.generate_hash()
        else:
            _hash = hash
        _hash += f'&aid={aid}'

        action = {
            "action": {
                "type": ButtonType.VKPAY.value,
                "payload": self._generate_payload(payload),
                "hash": _hash,
            }
        }

        self._add_button(action)

    def add_vkapps_button(
        self,
        app_id: int,
        owner_id: int,
        label: str,
        payload: typing.Optional[typing.Dict[str, str]] = None,
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


class CallbackEventDataType(Enum):
    TEXT = "text"
    LINK = "open_link"
    VKAPPS = "open_app"


class CallbackAnswer:
    # custom dumper?

    @classmethod
    def show_snackbar(cls, text: str):
        return json.dumps({"type": "show_snackbar", "text": text})

    @classmethod
    def open_link(cls, link: str):
        return json.dumps({"type": "open_link", "link": link})

    @classmethod
    def open_app(cls, app_id: int, hash: str, owner_id: typing.Optional[int] = None):
        return json.dumps(
            {"type": "open_app", "app_id": app_id, "owner_id": owner_id, "hash": hash}
        )
