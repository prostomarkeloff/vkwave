# Templates

## Carousel

### Creating

You can create "Carousel" by `Template` from `vkwave.bots.utils.keyboards`:

``` python
from vkwave.bots.utils.keyboards import Template


template_1 = Template(
    title="First title",
    description="First description",
    photo_id="-191459391_457239025",
)
template_1.add_text_button("Hello world!")
template_1.add_text_button("123")

template_2 = Template(
    title="Second title",
    description="Second description",
    photo_id="-191459391_457239026",
)

template_2.add_text_button("World hello!")
template_2.add_text_button("Wow, another button")

carousel = Template.generate_carousel(template_1, template_2)
```

### Sending

#### Via separate api object

``` python
api_session = API(...)
api = api_session.get_context()
await api.messages.send(user_id=1, random_id=0, template=carousel)
```

#### Via bundled with event API

```python
await event.api_ctx.messages.send(user_id=1, random_id=0, template=carousel)
```

#### Via answer (SimpleBot)

```python
await event.answer(template=carousel)
```
