# Роутеры

Без роутеров существование ботов в VKWave невозможно. Это одна из важнейших сущностей в вашем боте.

Другими словами, ваш бот это просто набор роутеров с фильтрами.

## Создание роутера

Создание:
```python
from vkwave.bots import DefaultRouter

router = DefaultRouter()  # also you can pass here filters
# it can be like: router = Router(SomeFilter(...))
```

## Регистрация хендлера

Больше о хендлерах вы можете узнать в handlers.md. `# TODO`

### Напрямую

```python
r = router.registrar  # just a shortcut
handler = r.new().with_filters(lambda event: event.object.object.message.text.lower() == "hi there").handle("hey!")  # here we are creating the handler that answers 'hey' to messages with content 'hi there'
r.register(handler)  # and.. we register it.
```

### Через декораторы

```python
@r.with_decorator(lambda event: event.object.object.message.text.lower() == "hi there")
def handler(event: BaseEvent) -> str:
    return "Hey!"
```

### Фильтры по умолчанию

registrar роутера имеет метод для установки стандартных фильтров. Он добавляет фильтр ко всем хендлерам в роутере.

```python
router.registrar.add_default_filter(SomeFilter(...))
```

## Добавление роутера в диспатчер
(см. dispatcher.md) `# TODO`

```python
dp.add_router(router)
```

Для разбивки бота по файлам вам нужно создать в каждом файле по роутеру и добавить туда хендлеры, далее просто объединить все в главном файле путем добавления всех роутеров в диспатчер.