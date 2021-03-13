import typing

from vkwave.bots.core.dispatching.events.base import BaseEvent
from .base import BaseFilter, FilterResult
from .builtin import get_text

try:
    import vbml
except ImportError:
    vbml = None


class VBMLFilter(BaseFilter):
    def __init__(
        self,
        pattern: typing.Union["vbml.Pattern", str],
        patcher: typing.Optional["vbml.Patcher"] = None,
        ignore_case: bool = False,
    ):
        if vbml is None:
            raise RuntimeError("you have to install vbml - pip install vbml")

        self.patcher: vbml.Patcher = patcher or vbml.Patcher()

        if isinstance(pattern, str):
            self.pattern = vbml.Pattern(pattern)
        elif isinstance(pattern, vbml.Pattern):
            self.pattern = pattern
        self.ignore_case = ignore_case

    async def check(self, event: BaseEvent) -> FilterResult:
        text = get_text(event) if not self.ignore_case else get_text(event).lower()
        if text is None:
            return FilterResult(False)

        result = self.patcher.check(self.pattern, text)
        if not result:
            return FilterResult(False)

        event["vmbl_data"] = self.pattern.dict()
        return FilterResult(True)
