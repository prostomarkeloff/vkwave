# Контекст

Когда вы вызываете `client.create_request` вы получаете контекст этого запроса.

Он содержит информацию о результате запроса (конечно, если вы вызываете его после `send_request`) и ошибках.

## Исключения

Клиенты могут вызывать исключения. Они должны описывать их в `RequestContext` для обработки хендлерами для исключений.

Одно исключение может иметь только один хендлер.

```python
# ...
async def timeout_handler(ctx: RequestContext) -> None:
    # только словарь
    ctx.result.exception_data = {"data": "Exception was occurred.."}

# ...
ctx.set_exception_handler(TimeoutException, timeout_handler)  # обрабатываем ошибка таймаута

await ctx.send_request() # если произойдет TimeoutException, ошибка обработается в нашем хендлере

if ctx.result.state is ResultState.HANDLED_EXCEPTION:
    data = ctx.result.exception_data
elif ctx.result.state is ResultState.UNHANDLED_EXCEPTION:
    print(f"Exception is {ctx.result.exception}")
    sys.exit(-1)
else:
    data = ctx.result.data

print(data)
```
