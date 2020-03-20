Carousels for vk


```python3
from vkwave_bots_utils.keyboards import Template

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

After this you can send carousel im vk message as template


```python3
api.messages.send(user_id=1, random_id=0, template=carousel)
```