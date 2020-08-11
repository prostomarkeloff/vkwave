# Клавиатуры

Поможет вам в создании клавиатур для ботов.

```python
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor

kb = Keyboard(one_time=False)
kb.add_text_button("hello")

kb.add_row()
kb.add_text_button("red hello", color=ButtonColor.NEGATIVE)
```

`Keyboard` предоставляет методы для создания любого типа кнопок:

- `add_text_button` - кнопка с текстом
- `add_callback_button`- кнопка действия
- `add_location_button` - кнопка, отправляющая местоположение
- `add_link_button` - кнопка с ссылкой
- `add_vkpay_button`- кнопка оплаты через VKPay

После этих действий вы можете отправлять клавиатуру пользователям:

```python
api.messages.send(user_id=1, random_id=0, keyboard=kb.get_keyboard())
```
