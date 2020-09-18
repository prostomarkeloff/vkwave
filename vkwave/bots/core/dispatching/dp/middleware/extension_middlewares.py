import logging
from typing import Optional

from vkwave.bots import BaseEvent, BaseMiddleware, MiddlewareResult

from ....dispatching.filters.builtin import get_text

# bot.middleware_manager.add_middleware(Middleware())
# or
# bot.add_middleware(Middleware())

logger = logging.getLogger(__name__)


class CommandLineMiddleware(BaseMiddleware):
    """Для парсинга сообщения like argparse.
    
    >>> clm = CommandLineMiddleware # alias
    >>> bot.add_middleware(clm())
    """

    def __init__(self, ignore_case: bool = False):
        self.ic = ignore_case

    async def pre_process_event(self, event: BaseEvent) -> MiddlewareResult:
        logger.debug("CommandLineMiddleware start")
        text: Optional[str] = get_text(event)

        if text is None:
            logger.debug("text is None: return False result")
            return MiddlewareResult(False)

        if self.ic:
            text = text.lower()
            logger.debug("add text ignore case")

        event["args"] = args = text.split()
        event["arguments"] = {}

        def start_with_command(el: str):
            """This func search and append to event commands and options.

            Args:
                el (str): element to check
            """
            nonlocal event
            dic = {"--": "options", ("!", "/"): "commands"}
            for key, val in dic.items():
                if el.startswith(key):
                    if val in event:
                        event[val].append(el)
                    else:
                        event[val] = [
                            el,
                        ]
                    return

        logger.debug("start parsings")
        for el in args:
            start_with_command(el)
            if el.startswith("-"):
                if "=" in el:  # TODO: если попадется -arg="ghjhgtrf" нам писец
                    event["arguments"].update({el[: el.index("=")]: el[el.index("=") + 1 :]})
                else:
                    try:
                        event["arguments"].update({el: args[args.index(el) + 1]})
                    except IndexError:
                        logger.debug("error when parse arguments")
                        raise ValueError("Missing argument value")
        logger.debug("CommandLineMiddleware end")
        return MiddlewareResult(True)
