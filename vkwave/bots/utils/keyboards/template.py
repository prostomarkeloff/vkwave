import json
import typing

from vkwave.bots.core.types.json_types import JSONEncoder
from vkwave.bots.utils.keyboards.keyboard import ButtonColor, Keyboard
from vkwave.bots.utils.keyboards._vkpayaction import VKPayAction


class Template:
    def __init__(
        self,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        photo_id: typing.Optional[str] = None,
        action: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
    ):
        """
        create template object
        :param title:
        :param description:
        :param action: open_link or open_photo when clicking the template
        :param photo_id: have to have ratio 13/8 and png format
        :param link:
        """
        if not title and not photo_id:
            raise RuntimeError("You have to specify title or photo_id, got None")
        if title and not description:
            raise RuntimeError("You have to specify description, got None")

        if action == "open_link":
            if not link:
                raise RuntimeError("You have to specify link, got None")
            else:
                self.action = {
                    "type": "open_link",
                    "link": link,
                }
        else:
            self.action = {
                "type": "open_photo",
            }

        self.title = title
        self.description = description
        self.photo_id = photo_id
        self._local_keyboard = Keyboard(one_time=True)

    def add_text_button(
        self, text: str, color: ButtonColor = ButtonColor.PRIMARY, payload: dict = None,
    ):
        self._local_keyboard.add_text_button(text=text, color=color, payload=payload)

    def add_location_button(self, payload: dict = None):
        self._local_keyboard.add_location_button(payload=payload)

    def add_link_button(self, text: str, link: str, payload: dict = None):
        self._local_keyboard.add_link_button(text=text, link=link, payload=payload)

    def add_vkpay_button(self, hash_action: typing.Union[VKPayAction, str], payload: dict = None):
        self._local_keyboard.add_vkpay_button(hash_action=hash_action, payload=payload)

    def add_vkapps_button(self, app_id: int, owner_id: int, label: str, payload: dict = None):
        self._local_keyboard.add_vkapps_button(
            app_id=app_id, owner_id=owner_id, label=label, payload=payload
        )

    def add_callback_button(
        self,
        text: str,
        color: typing.Union[str, ButtonColor] = ButtonColor.PRIMARY,
        payload: typing.Optional[typing.Dict[str, str]] = None,
    ):
        self._local_keyboard.add_callback_button(
            text=text, color=color, payload=payload,
        )

    @classmethod
    def generate_carousel(cls, *templates: "Template", json_serialize: JSONEncoder = json.dumps):
        """
        templates have to contains identical Templates (same buttons value at least)
        :param templates:
        :param json_serialize:
        :return:
        """
        elements = []

        for template in templates:
            elements.append(
                {
                    "title": template.title,
                    "description": template.description,
                    "photo_id": template.photo_id,
                    "action": template.action,
                    "buttons": template._local_keyboard.buttons[0],
                }
            )

        return json_serialize({"type": "carousel", "elements": elements})
