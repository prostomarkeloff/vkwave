import vkwave.bots.vkscript.handlers.assignments
import vkwave.bots.vkscript.handlers.blocks
import vkwave.bots.vkscript.handlers.calls
import vkwave.bots.vkscript.handlers.expressions
import vkwave.bots.vkscript.handlers.statements
import vkwave.bots.vkscript.handlers.types
from .converter import VKScriptConverter
from .execute import Execute
from .execute import execute


__all__ = ("execute", "Execute", "VKScriptConverter")
