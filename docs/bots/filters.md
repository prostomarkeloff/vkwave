# Filters

Фильтры нужны для _фильтрации_ событий для роутеров/хендлеров.

В VKWave они представлены объектами класса `BaseFilter`. Также вы можете превратить лямбду/функцию/корутину в фильтр с помощью `filter_caster`.

```python
from vkwave.bots.core.dispatching.filters import filter_caster

# here we are creating function that will create another function and cast it to filter
# it's called `currying`.
text = lambda text: filter_caster.cast(lambda event: event.object.object.message.text.lower() == text)
```

На самом деле, вам вряд ли понадобится filter_caster в большинстве задач, потому что когда вы регистрируете хендлер он вызывается автоматически.

```python

# `lambda event: 1` converted into `BaseFilter`
r.new().with_filters(lambda event: 1).handle(...).ready()

# totally equal
r.new().with_filters(filter_caster.cast(lambda event: 1).handle(...).ready())
```

Но знание о его существовании может помочь вам. По умолчанию у вас есть только 3 кастера в фильтры: лямбды, обычные синхронные и асинхронные функции. Вы можете расширить эту функциональность.

```python
from typing import Optional
from vkwave.bots.core.dispatching.filters.base import BaseFilter, FilterResult

# простой фильтр для текста
class TextFilter(BaseFilter):
    def __init__(self, text: str):
        self.text = text

    async def check(self, event: BaseEvent) -> FilterResult:
        return FilterResult(event.object.object.message.text.lower() == self.text)

# можно использовать так
r.new().with_filters(TextFilter("some pretty text"))

# или создать кастер для него

def str_caster(text: str) -> Optional[BaseFilter]:
    if isinstance(text, str):
        return TextFilter(text)
    return None

filter_caster.add_caster(str_caster)


# и... можно использовать его очень просто!
r.new().with_filters("some pretty text")

```

Если у вас есть объект класса `BaseFilter` - вы можете делать _магические_ вещи. 

```python
from vkwave.bots.core.dispatching.filters import filter_caster

text = lambda text: filter_caster.cast(lambda event: event.object.object.message.text.lower() == text)

# ~text("hi") любой текст кроме hi
# Работает как простое отрицание, там где обычный фильтр вернет True, фильтр с ~ вернет False
r.new().with_filters(~text("hi"))

# filter & filter возвращает False если хотя бы один фильтр вернет False
r.new().with_filters(text("hi") & lambda event: ...)

# filter | filter работает как питоновское `or`
r.new().with_filters(text("hi") | text("hello"))

# вы можете совмещать их
r.new().with_filters(some_filter & (text("hi") | text("hello") | ~text("bye")))

```
