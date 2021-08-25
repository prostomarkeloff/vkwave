# Custom filters

You can write your own filters.

There is two ways to create filters:

## Object-oriented BaseFilter

Create new class, inherited from `BaseFilter` from `vkwave.bots.core.dispatching.filters.base`

Filtration logic must be implemented in method `check`, which gets argument `event` - new event.

``` python
from vkwave.bots.core.dispatching.filters import base, builtin


class AttachmentsFilter(base.BaseFilter):
    """Example filter.
    
    Checks if message has an attachments.
    """

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        """Filtration logic.
        
        Must return FilterResult with True or False value, on which the success of the filter depends.
        """
        builtin.is_message_event(event)
        
        return base.FilterResult(event.object.object.message.attachments is not None)
```


## Functional filter_caster

You may cast to filter any function/lambda/coroutine using `filter_caster`

```python
from vkwave.bots.core.dispatching.filters import filter_caster

has_attachments = filter_caster.cast(lambda event: event.object.object.message.attachments is not None)

```

If pass function/lambda/coroutine directly to handler, then you shouldn't call `filter.caster`, it will be called automatically:

``` python
@bot.message_handler(lambda event: event.object.object.message.attachments is not None)
async def handler(event):
    await event.answer("Attachments found")
```
