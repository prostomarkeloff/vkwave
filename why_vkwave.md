VKWave - это фреймворк для создания производительных и лёгких в расширении проектов, взаимодействующих с API ВКонтакте.

VKWave вдохновлен многими библиотеками, в частности: [aiogram](https://github.com/aiogram/aiogram), vk.py и многими другими.

Главная причина, почему вам нужен VKWave - это возможность контролировать и конфигурировать все (не без возможности отдать конфигурацию под ответственность самой библиотеки, занимаясь лишь самым высокоуровневым кодом).
Действительно, хотите отправлять сообщение в телеграм когда оно пришло в вк? Просто используйте middleware. Что насчёт конвертирования классов в хендлеры, фильтры, что-то еще? VKWave позволяет вам все это.

Для примера, я конвертирую строки в  `TextFilter`
```python
from vkwave.bots.core.dispatching.filters import filter_caster
from vkwave.bots.core.dispatching.filters.base import BaseFilter
from vkwave.bots.core.dispatching.filters.builtin import TextFilter
from typing import Optional

def cast_str_to_filter(something) -> Optional[BaseFilter]:
    if isinstance(something, str):
        return TextFilter(something)
    else:
        return None

filter_caster.add_caster(cast_str_to_filter)
```
Если вы спросите, доступен ли он только в высокоуровневом коде (например в vkwave.bots), я отвечу нет.
 Например, вы можете создать собственный `Token` над абстракциями. Это позволяет вам настроить VKWave
  под ваши собственные задачи. Если перейти к более низкоуровневым вещам, таким как взаимодействие с VK, вы можете создать собственный HTTP-клиент.
   Клиенту API это нужно, конечно, если вы делаете в нем HTTP-запросы. Ваш API-клиент может даже не отправлять HTTP-запросы.
    Может быть, вы сумасшедший (как я) и хотите поместить свои запросы в очередь RabbitMQ и получать откуда то еще?
     VKWave позволяет вам это сделать. И окончательный код все еще будет `high-level`.

