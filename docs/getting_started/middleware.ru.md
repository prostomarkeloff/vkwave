# Миддлварь

Миддлварь - это обработчик события, который запускается перед прогоном события по хендлерам. Она позволяет забраковать событие по какому-либо признаку без необходимости писать один и тот же фильтр в каждом хендлере.


## Создание миддлвари

Любая миддлварь должна возвращать `MiddlewareResult` со значением `True` или `False`.

Если миддлварь возвращает `MiddlewareResult(False)`, обработка события останавливается и не идёт дальше по хендлерам

### Объектно-ориентированный способ

- Можно передать дополнительные аргументы
- Можно запускать миддлварь и до поиска подходящего хендлера (`pre_process_event`, должен быть обязательно) и после (`post_process_event`)

```python

from vkwave import SimpleLongPollBot, MiddlewareResult, BaseMiddleware


class UserShouldNotLoveDogs(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        if event.object.object.message.text == "dog":
            print(f"{event.object.object.message.from_id} loves dogs")
            return MiddlewareResult(False)
        return MiddlewareResult(True)


```

### Функциональный способ

- Не может передавать дополнительные аргументы (кроме события) в миддлварь
- Нельзя создать `post_process_event`

```python

from vkwave import SimpleLongPollBot, MiddlewareResult

@bot.middleware()
async def check(event: BotEvent) -> MiddlewareResult:
    if event.object.object.message.text == "dog":
        print(f"{event.object.object.message.from_id} loves dogs")
        return MiddlewareResult(False)
    return MiddlewareResult(True)

```
