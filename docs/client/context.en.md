# Context

When you call `client.create_request` you get context of the request.

It contains request's result

## Exceptions

Clients can raise exceptins. They should describe it in `RequestContext`, so exception handlers can handle them.

One exception can have only one handler.

```python
# ...
async def timeout_handler(ctx: RequestContext) -> None:
    # only dict
    ctx.result.exception_data = {"data": "Exception was occurred.."}

# ...
ctx.set_exception_handler(TimeoutException, timeout_handler)  # handling timeout error

await ctx.send_request() # if TimeoutException occured , error will handled in our handler

if ctx.result.state is ResultState.HANDLED_EXCEPTION:
    data = ctx.result.exception_data
elif ctx.result.state is ResultState.UNHANDLED_EXCEPTION:
    print(f"Exception is {ctx.result.exception}")
    sys.exit(-1)
else:
    data = ctx.result.data

print(data)
```
