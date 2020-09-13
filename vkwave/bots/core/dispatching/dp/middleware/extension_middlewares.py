from typing import Optional

from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult

from ....dispatching.filters.builtin import get_text

# bot.middleware_manager.add_middleware(Middleware())
# or
# bot.add_middleware(Middleware())


class CommandLineMiddleware(BaseMiddleware):
    """Для парсинга сообщения like argparse.
    
    >>> clm = CommandLineMiddleware # alias
    >>> bot.add_middleware(clm)
    """

    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        text: Optional[str] = get_text(event)

        if text is None:
            return MiddlewareResult(False)
        # TODO: Добавить ignore case, я хз как это сделать

        event["args"] = args = text.split()
        event["arguments"] = {}

        def start_with_command(el: str):
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

        for el in args:
            start_with_command(el)
            if el.startswith("-"):
                if "=" in el:  # TODO: если попадется -arg="ghjhgtrf" нам писец
                    event["arguments"].update({el[: el.index("=")]: el[el.index("=") + 1 :]})
                else:  # Я уже забыл как наяваял эту херню
                    try:
                        event["arguments"].update({el: args[args.index(el) + 1]})
                    except IndexError:
                        raise ValueError("Missing argument value")

        return MiddlewareResult(True)
