# Middleware

Middleware is an event handler, which runs before passing event to handlers. It allows skip handling of event by some condition without need to write same filter in each handler.


## Creating middleware

Any midleware must return `MiddlewareResult` with value `True` or `False`.

If middleware returns `MiddlewareResult(False)`, handling event stops and doesn't pass an event to handlers.

### Object-oriented way

- You can pass additional arguments
- You can define `pre_process_event` (required), which will run before event handling and `post_process_event`, which will run after

```python

from vkwave import SimpleLongPollBot, MiddlewareResult, BaseMiddleware


class UserShouldNotLoveDogs(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        if event.object.object.message.text == "dog":
            print(f"{event.object.object.message.from_id} loves dogs")
            return MiddlewareResult(False)
        return MiddlewareResult(True)


```

### Functional way

- You can't pass additional arguments to middleware
- You can't define `post_process_event`

```python

from vkwave import SimpleLongPollBot, MiddlewareResult

@bot.middleware()
async def check(event: BotEvent) -> MiddlewareResult:
    if event.object.object.message.text == "dog":
        print(f"{event.object.object.message.from_id} loves dogs")
        return MiddlewareResult(False)
    return MiddlewareResult(True)

```
