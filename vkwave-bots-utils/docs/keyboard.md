
It will helps you with creating keyboards for bots.


```python3
from vkwave_bots_utils.keyboards import Keyboard
from vkwave_bots_utils.keyboards.keyboard import ButtonColor

kb = Keyboard(one_time=False)
kb.add_text_button("hello")

kb.add_row()
kb.add_text_button("red hello", color=ButtonColor.NEGATIVE)
```

After this actions you can send ```kb``` in vk message:


```python3
api.messages.send(user_id=1, random_id=0, keyboard=kb.get_keyboard())
```
