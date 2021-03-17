# Клавиатуры

Для удобной генерации клавиатур используйте класс Keyboard из `vkwave.bots.utils.keyboards`

## Типы кнопок

VkWave поддерживает все типы кнопок, доступные в ВК. [Подробнее в документации](https://vk.com/dev.php?f=4.%20%D0%9A%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%B1%D0%BE%D1%82%D0%BE%D0%B2&method=bots_docs_3)

| Тип      | Метод для создания    |
| -------- | --------------------- |
| Text     | add_text_button()     |
| Link     | add_link_button()     |
| Location | add_location_button() |
| Vk Pay   | add_vkpay_button()    |
| Vk App   | add_vkapps_button()   |
| Callback | add_callback_button() |

## Настройка лейаута клавиатуры

Клавиатура ВКонтакте это сетка, максимальный размер которой в обычном режиме составляет 5 &times; 10 кнопок, в инлайн-режиме (клавиатура в рамке сообщения) &ndash; 5 &times; 6 кнопок.

`Keyboard` принимает несколько параметров, настраивающих то, как будет выглядеть клавиатура.

| Параметр | Описание                                    |
| -------- | ------------------------------------------- |
| one_time | Клавиатура исчезнет после нажатия на кнопку |
| inline   | Отображать клавиатуру в инлайн-режиме       |

Для создания новой строки в клавиатуре вызовите метод `#!python keyboard.add_row()`


## Payload (полезная нагрузка)

Клавиатуры ВКонтакте поддерживают отправку скрытой информации по нажатию на любую кнопку. Это заранее определённый JSON, по которому можно, например, фильтровать события, или передавать какую-нибудь информацию на следующие шаги работы бота.

``` python
from vkwave.bots.utils.keyboards.keyboard import Keyboard

keyboard = Keyboard()

kb.add_text_button("Синяя кнопка", payload={"button": "test"})
```

О конвертации словаря в JSON позаботится VkWave


## Настройка цвета кнопки

Кнопки типа Text и Callback можно перекрасить. Используйте для этого перечисление `ButtonColor` из `vkwave.bots.utils.keyboards.keyboard`

``` python
kb.add_text_button("Синяя кнопка", color=ButtonColor.PRIMARY)
kb.add_text_button("Белая кнопка", color=ButtonColor.SECONDARY)
kb.add_text_button("Красная кнопка", color=ButtonColor.NEGATIVE)
kb.add_text_button("Зелёная кнопка", color=ButtonColor.POSITIVE)
```

По умолчанию все кнопки синие (`ButtonColor.PRIMARY`)

## Отправка клавиатуры

Вызовите любую функцию, отправляющую сообщения с параметром keyboard, в который передайте JSON с клавиатурой.  
Он генерируется методом `keyboard.get_keyboard()`

``` python
await event.answer("Сообщение с клавиатурой", keyboard=keyboard.get_keyboard())
```