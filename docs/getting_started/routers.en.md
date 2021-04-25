# Routers

Routers is must important part of any bot in VkWave. Routers contains handlers, thanks to which the event processing is carried out

``` python
from vkwave.bots import DefaultRouter

router = DefaultRouter()
```

You can pass [filters](filters/index.en.md) when creating a router (add a default filters), thanks to which events will process faster.

``` python
router = DefaultRouter(SomeFilter())
```
