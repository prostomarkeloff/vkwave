# Роутеры

Без роутеров существование ботов в VKWave невозможно. Это одна из важнейших сущностей в вашем боте.

Другими словами, ваш бот это просто набор роутеров с фильтрами.

# Пособие по роутерам

Создание:
```python
from vkwave.bots import DefaultRouter

router = DefaultRouter()  # also you can pass here filters
# it can be like: router = Router(SomeFilter(...))
```

Как регистрировать хендлеры?

Больше о хендлерах вы можете узнать в `handlers.md`.

```python
r = router.registrar  # just a shortcut
handler = r.new().with_filters(lambda event: event.object.object.message.text.lower() == "hi there").handle("hey!")  # here we are creating the handler that answers 'hey' to messages with content 'hi there'
r.register(handler)  # and.. we register it.
```

Также можно использовать декораторы.

```python
@r.with_decorator(lambda event: event.object.object.message.text.lower() == "hi there")
def handler(event: BaseEvent) -> str:
    return "Hey!"
```

Есть еще один способ делать это, но он не нужен для повсеместного использования.

registrar роутера имеет опцию для установки стандартных фильтров. Она добавляет фильтр ко всем хендлерам в роутере.

```python
router.registrar.add_default_filter(SomeFilter(...))
```

И наконец, как добавить роутер в диспатчер (`dispatcher.md`, please).

```python
dp.add_router(router)
```

# Разбивка бота по файлам

Для разбивки бота по файлам вам нужно создать в каждом файле по роутеру и добавить туда хендлеры, далее просто объединить все в главном файле путем добавления всех роутеров в диспатчер.

Пример бота

- [VkWaveBotExample](https://github.com/kesha1225/VkWaveBotExample)
