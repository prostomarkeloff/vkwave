import typing

from vkwave.bots.core.dispatching.events.base import BaseEvent
from .base import BaseFilter, FilterResult
from .builtin import get_text

try:
    import vbml
except ImportError:
    vbml = None


class VBMLFilter(BaseFilter):
    def __init__(self, pattern: typing.Union["vbml.Pattern", str], patcher: typing.Optional["vbml.Patcher"] = None):
        if vbml is None:
            raise RuntimeError("you have to install vbml - pip install vbml")

        if patcher is None:
            self.patcher = vbml.Patcher()

        if isinstance(pattern, str):
            self.pattern = vbml.Patcher.get_current(no_error=False).pattern(pattern)
        elif isinstance(pattern, vbml.Pattern):
            self.pattern = pattern

        self._patcher = vbml.Patcher.get_current(no_error=False)

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event)
        if text is None:
            return FilterResult(False)

        result = self._patcher.check(text, self.pattern)
        if result is None:
            return FilterResult(False)

        event["vmbl_data"] = self.pattern.dict()
        return FilterResult(True)
