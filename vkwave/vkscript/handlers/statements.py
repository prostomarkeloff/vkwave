import ast

from ..converter import VKScriptConverter


@VKScriptConverter.register(ast.Return)
def return_handler(node: ast.Return):
    converter = VKScriptConverter.get_current()
    if node.value is None:
        return "return null;"
    return f"return {converter.convert_node(node.value)};"


@VKScriptConverter.register(ast.Delete)
def delete_handler(node: ast.Attribute):
    converter = VKScriptConverter.get_current()
    return "".join(
        f"delete {converter.convert_node(target)};" for target in node.targets
    )


@VKScriptConverter.register(ast.Pass)
def pass_handler(node: ast.Pass):
    return ""
