import asyncio
import typing


class TaskManager:
    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        self.tasks: typing.List[typing.Callable] = []
        self.loop = loop or asyncio.get_event_loop()

    def add_task(self, task: typing.Callable):
        if asyncio.iscoroutinefunction(task):
            self.tasks.append(task)
        else:
            raise RuntimeError("only coro")

    async def __run(self):
        if not self.tasks:
            raise RuntimeError("task manager got 0 tasks")

        [await self.loop.create_task(task()) for task in self.tasks]

    def run(
        self, on_shutdown: typing.Callable = None, on_startup: typing.Callable = None,
    ):
        try:
            if on_startup is not None:
                self.loop.run_until_complete(on_startup())

            self.loop.create_task(self.__run())
            self.loop.run_forever()
        finally:
            if on_shutdown is not None:
                self.loop.run_until_complete(on_shutdown())
