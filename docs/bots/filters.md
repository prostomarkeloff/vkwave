# Filters

Filters are needed for _filtering_ events for routers/handlers.

In VKWave, they are represented like instances of `BaseFilter` class. Also you can cast lambdas/functions/coroutines to filters via filter_caster.

```python
from vkwave.bots.core.dispatching.filters import filter_caster

# here we are creating function that will create another function and cast it to filter
# it's called `currying`.
text = lambda text: filter_caster.cast(lambda event: event.object.object.message.text.lower() == text)
```

If be honest, you need not the filter caster in most cases, because when you register handlers it's called automaticaly.

```python

# `lambda event: 1` converted into `BaseFilter`
r.new().with_filters(lambda event: 1).handle(...).ready()

# totally equal
r.new().with_filters(filter_caster.cast(lambda event: 1).handle(...).ready()
```

But knowing that it exists sometimes may help you. By default, you have only 3 casts to filters: lambdas, regular function & async functions. You can extend it.

```python
from typing import Optional
from vkwave.bots.core.dispatching.filters.base import BaseFilter, FilterResult

# simple filter for messages's text
class TextFilter(BaseFilter):
    def __init__(self, text: str):
        self.text = text

    async def check(self, event: BaseEvent) -> FilterResult:
        return FilterResult(event.object.object.message.text.lower() == self.text)

# you can use it so:
r.new().with_filters(TextFilter("some pretty text"))

# or via creating caster for that

def str_caster(text: str) -> Optional[BaseFilter]:
    if isinstance(text, str):
        return TextFilter(text)
    return None

filter_caster.add_caster(str_caster)


# and... we can use it very easy!
r.new().with_filters("some pretty text")

```

If you have `BaseFilter`'s instance you can do _magic_ things. I'll pick up filter from 1st example.

```python
from vkwave.bots.core.dispatching.filters import filter_caster

text = lambda text: filter_caster.cast(lambda event: event.object.object.message.text.lower() == text)

# ~text("hi") means that text should be anything, but not 'hi'
# it works so: if filter returns True - it returns False and vice versa.
r.new().with_filters(~text("hi"))

# filter & filter internals are pretty simple. it executes filter by filter and if some of them fails it returns False
r.new().with_filters(text("hi") & lambda event: ...)

# filter | filter works like Python's boolean `or`.
r.new().with_filters(text("hi") | text("hello"))

# also you can combine them.
r.new().with_filters(some_filter & (text("hi") | text("hello") | ~text("bye")))

```
