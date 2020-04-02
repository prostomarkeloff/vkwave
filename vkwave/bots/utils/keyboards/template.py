import json

from vkwave.bots.core.types.json_types import JSONEncoder
from vkwave.bots.utils.keyboards.keyboard import ButtonColor, Keyboard


class Template:
    def __init__(self, title: str, description: str, photo_id: str):
        """
        create template object
        :param title:
        :param description:
        :param photo_id: have to have ratio 13/8 and png format
        """
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

    def add_vkpay_button(self, hash: str, payload: dict = None):
        self._local_keyboard.add_vkpay_button(hash=hash, payload=payload)

    def add_vkapps_button(self, app_id: int, owner_id: int, label: str, payload: dict = None):
        self._local_keyboard.add_vkapps_button(
            app_id=app_id, owner_id=owner_id, label=label, payload=payload
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
                    "buttons": template._local_keyboard.buttons[0],
                }
            )

        return json_serialize({"type": "carousel", "elements": elements})
