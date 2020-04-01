# Context

When you call `client.create_request` you get the context of this request.

That contains information about result of request (of course, not defined until you call `send_request`), and exceptions.

## Exceptions

Clients can raise exceptions. They must describe them in `RequestContext` for handling by exception handlers.

One exception can have the only one exception handler.

```python
# ...
async def timeout_handler(ctx: RequestContext) -> None:
    # it must be dict!
    ctx.result.exception_data = {"data": "Exception was occurred.."}

# ...
ctx.set_exception_handler(TimeoutException, timeout_handler)  # here we are handling timeout error

await ctx.send_request() # if timeout error is occurred then our handler will handle it!

if ctx.result.state is ResultState.HANDLED_EXCEPTION:
    data = ctx.result.exception_data
elif ctx.result.state is ResultState.UNHANDLED_EXCEPTION:
    print(f"Exception is {ctx.result.exception}")
    sys.exit(-1)
else:
    data = ctx.result.data

print(data)
```
Here we are handling timeout exception.
