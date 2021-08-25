# Кастомные фильтры

Вы можете писать свои фильтры, если встроенных недостаточно.

Предусмотрено несколько способов для создания кастомных фильтров:

## Объектно-ориентированный BaseFilter

Для этого нужно создать класс, унаследовавшись от `BaseFilter` из `vkwave.bots.core.dispatching.filters.base`

Логика фильтрации должна быть определена в методе check, который принимает аргумент event — свежепришедшее событие

``` python
from vkwave.bots.core.dispatching.filters import base, builtin


class AttachmentsFilter(base.BaseFilter):
    """Фильтр-пример.
    
    Проверяет наличие вложений в сообщении.
    """

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        """Метод, в котором определяется логика фильтрации.
        
        Должен возвращать FilterResult со значением True или False, от которого зависит успех фильтра.
        """
        builtin.is_message_event(event)
        
        return base.FilterResult(event.object.object.message.attachments is not None)
```


## Функциональный filter_caster

Любую функцию/лямбду/корутину можно превратить в фильтр используя `filter_caster`

```python
from vkwave.bots.core.dispatching.filters import filter_caster

has_attachments = filter_caster.cast(lambda event: event.object.object.message.attachments is not None)

```

Если указывать функцию/лямбду/корутину напрямую в определении хендлера, то можно не вызывать `filter.caster`, он сработает под капотом автоматически:

``` python
@bot.message_handler(lambda event: event.object.object.message.attachments is not None)
async def handler(event):
    await event.answer("Найдены вложения")
```
