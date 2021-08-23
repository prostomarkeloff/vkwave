# Keyboards

For convinient generating of keyboards use the `Keyboard` from `vkwave.bots.utils.keyboards`

## Buttons types

VkWave supports all the button types, available in VK. [More details in the documentation](https://vk.com/dev.php?f=4.%20%D0%9A%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%B1%D0%BE%D1%82%D0%BE%D0%B2&method=bots_docs_3)

| Type     | Method to create      |
| -------- | --------------------- |
| Text     | add_text_button()     |
| Link     | add_link_button()     |
| Location | add_location_button() |
| Vk Pay   | add_vkpay_button()    |
| Vk App   | add_vkapps_button()   |
| Callback | add_callback_button() |

## Setting up layout of keyboard

VK keyboard is a grid. Max size of it's 5 &times; 10 buttons in normal mode, and (keyboard inside of message) &ndash; 5 &times; 6 buttons in inline mode.

`Keyboard` accept this parametrs to describe how keyboard will looks like and behave.

| Parameter | Description                                 |
| --------- | ------------------------------------------- |
| one_time  | Keyboard will hide after button touched     |
| inline    | Show keyboard in inline mode                |

To create new row in the keyboard call `#!python keyboard.add_row()`


## Payload

VK's keyboards supports sending hidden inforamtion by touching any button. It's predefined JSON, by which you can i.e filter events, or send some information to next steps of bot.

``` python
from vkwave.bots.utils.keyboards.keyboard import Keyboard

keyboard = Keyboard()

kb.add_text_button("Blue button", payload={"button": "test"})
```

VkWave will automatcally convert dict to JSON


## Configuring color of buttons

You can recolor Text и Callback buttons. Use enumeration `ButtonColor` from `vkwave.bots.utils.keyboards.keyboard`

``` python
kb.add_text_button("Blue button", color=ButtonColor.PRIMARY)
kb.add_text_button("White button", color=ButtonColor.SECONDARY)
kb.add_text_button("Red button", color=ButtonColor.NEGATIVE)
kb.add_text_button("Red button", color=ButtonColor.POSITIVE)
```

By default all button are blue (`ButtonColor.PRIMARY`)

## Sending keyboard

Call any function sending messages and pass to it JSON with keyboard to parameter keyboard.  
It generates by method `keyboard.get_keyboard()`

``` python
await event.answer("Message with keyboard", keyboard=keyboard.get_keyboard())
```