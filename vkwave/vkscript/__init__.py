import vkwave.vkscript.handlers.assignments
import vkwave.vkscript.handlers.blocks
import vkwave.vkscript.handlers.calls
import vkwave.vkscript.handlers.expressions
import vkwave.vkscript.handlers.statements
import vkwave.vkscript.handlers.types  # noqa: F401

from .converter import VKScriptConverter
from .execute import Execute, execute

__all__ = ("execute", "Execute", "VKScriptConverter")
