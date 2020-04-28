import vkwave.vkscript.handlers.assignments
import vkwave.vkscript.handlers.blocks
import vkwave.vkscript.handlers.calls
import vkwave.vkscript.handlers.expressions
import vkwave.vkscript.handlers.statements
import vkwave.vkscript.handlers.types
from .converter import VKScriptConverter
from .execute import Execute
from .execute import execute


__all__ = ("execute", "Execute", "VKScriptConverter")
