VKWave is a high-performance, easy to scale Python library for creating applications that interact with VK's API.

VKWave is inspired by many libraries such as: [aiogram](https://github.com/aiogram/aiogram), vk.py and a lot of other.

The main reason of using VKWave is that you can configure anything. Really. You want to send message to Telegram when new is coming? It's easy, just use middleware. Or something harder. What's about converting own classes to handlers, filters, anything? VKWave allows you it.

For example, I want to cast strings to `TextFilter`

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

If you ask that it's available only in high-level code (like bots framework) than I'll answer you no. For example, you can create own `Token` over abstractions. It is allowing you to configure VKWave to your own tasks. If go to more low-level things, like interacting with VK, you can create own HTTP client. API client needs it, of course if you do HTTP requests in it. Your API client can even do not sent HTTP requests. Maybe you are crazy (like me) and want to put your requests into RabbitMQ queue and get from other? VKWave allows you to do it. And final code still is high-level.
