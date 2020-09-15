[Карусели](./templates.md)
# Клавиатуры

Поможет вам в создании клавиатур для ботов.
```python
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor

kb = Keyboard(one_time=False)
kb.add_text_button("hello")
```
Есть несколько цветов кнопок:
```python
kb.add_row()
kb.add_text_button("blue hello", color=ButtonColor.PRIMARY)

kb.add_row()
kb.add_text_button("white hello", color=ButtonColor.SECONDARY)

kb.add_row()
kb.add_text_button("red hello", color=ButtonColor.NEGATIVE)

kb.add_row()
kb.add_text_button("green hello", color=ButtonColor.POSITIVE)

```
Также если вам нужна синяя кнопка, то
```python
color=ButtonColor.PRIMARY
```
можно просто не писать
***
После этих действий вы можете отправлять клавиатуру пользователям:

```python
api.messages.send(user_id=1, random_id=0, keyboard=kb.get_keyboard())
```
