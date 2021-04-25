# Роутеры

Роутеры - самая важная сущность любого бота в VkWave. В роутерах содержатся хендлеры, благодаря которым и осуществляется обработка событий.

``` python
from vkwave.bots import DefaultRouter

router = DefaultRouter()
```

Роутеры могут принимать на вход [фильтры](filters/index.md), благодаря которым события будут отсеиваться быстрее, не проходя сквозь все хендлеры

``` python
router = DefaultRouter(SomeFilter())
```
