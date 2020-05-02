# Routers

Today I wanna tell you about routers and how to use them.

First of all, you should know that you can't handle any kind of events without it (router, of course). It is the main entity of your bot in vkwave. It's pretty simple, yet has own useful features, like filters.

In other words, your bot in VKWave is just a set of routers that handle events. And they can filter events.

# Short guide: how to routers

Initiating:
```python
from vkwave.bots import DefaultRouter

router = DefaultRouter()  # also you can pass here filters
# it can be like: router = Router(SomeFilter(...))
```

The main question of this piece of docs: how to register handlers.

If you wanna know more about handlers read `handlers.md`.

```python
r = router.registrar  # just a shortcut
handler = r.new().with_filters(lambda event: event.object.object.message.text.lower() == "Hi there").handle("hey!")  # here we are creating the handler that answers 'hey' to messages with content 'hi there'
r.register(handler)  # and.. we register it.
```

Also, you can do it in flask-like notation: via decorators.

```python
@r.with_decorator(lambda event: event.object.object.message.text.lower() == "hi there")
def handler(event: BaseEvent) -> str:
    return "Hey!"
```

There is one more way how to do that, but it's not needed for everyday usage and I won't show you it

Router's registrar has option for default filters. It will add them to handler's filters when creates.

```python
router.registrar.add_default_filter(SomeFilter(...))
```


And finally: how to add router to dispatcher (`dispatcher.md`, please).

```python
dp.add_router(router)
```
