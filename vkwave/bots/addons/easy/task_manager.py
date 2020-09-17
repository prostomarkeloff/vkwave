import asyncio
import logging
from typing import Callable, Optional, List, Union, Coroutine

logger = logging.getLogger(__name__)


class TaskManager:
    def __init__(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        self.tasks: List[Coroutine] = []
        self.loop = loop or asyncio.get_event_loop()

    def add_task(self, task: Union[Coroutine, Callable]):
        logger.info(f"Task {task.__name__} successfully added!")
        if asyncio.iscoroutinefunction(task):
            self.tasks.append(task())
        elif asyncio.iscoroutine(task):
            task: Coroutine
            self.tasks.append(task)
        else:
            raise RuntimeError(
                "Unexpected task. Tasks may be only coroutine or coroutine function"
            )

    async def __run(self):
        if not self.tasks:
            raise RuntimeError("task manager got 0 tasks")

        logger.debug("Start creating tasks....")
        [self.loop.create_task(task) for task in self.tasks]
        logger.debug("Tasks succesfully are created!")

    def run(
        self,
        on_shutdown: Optional[Callable] = None,
        on_startup: Optional[Callable] = None,
        asyncio_debug_mode: bool = False,
    ):
        """
        Method which run event loop
        :param on_shutdown: coroutine which will run after complete tasks
        :param on_startup: coroutine which will run before start main tasks
        :param asyncio_debug_mode: asyncio debug mode state
        :return:
        """
        try:
            if on_startup is not None:
                logger.debug("On startup coroutine is passed. It will be running now.")
                self.loop.run_until_complete(on_startup())

            if asyncio_debug_mode:
                self.loop.set_debug(True)
                logger.debug("Asyncio debug mode is enabled.")

            self.loop.create_task(self.__run())
            self.loop.run_forever()
        finally:
            if on_shutdown is not None:
                logger.debug("On shutdown coroutine is passed. It will be running now.")
                self.loop.run_until_complete(on_shutdown())

    def run_task(self, task: Callable):
        """
        Create task in loop
        >>> async def other_coro():
        >>>    while True:
        >>>        print("hello, my friend!")
        >>>        await asyncio.sleep(5)
        >>> async def my_pretty_coro():
        >>>    task_manager.run_task(other_coro)
        >>>    return True
        :param task:
        :return:
        """

        self.loop.create_task(task())

    def close(self):
        """
        Close event loop manually
        >>> task_manager.close()
        :return:
        """
        logger.debug("Loop is closing...")
        self.loop.close()
