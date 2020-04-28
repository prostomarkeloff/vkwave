import ast

from ..converter import VKScriptConverter

WHILE_TEMPLATE = "while(%(test)s){%(body)s};"
IF_TEMPLATE = "if(%(test)s){%(content)s}%(other)s;"
FOR_TEMPLATE = "var __vkwave_iter_list__ = %(iter)s;while(__vkwave_iter_list__.length > 0){var %(target)s=__vkwave_iter_list__.pop();%(body)s};"


@VKScriptConverter.register(ast.While)
def while_handler(node: ast.While):
    converter = VKScriptConverter.get_current()
    if node.orelse:
        raise NotImplementedError("while...else not implemented.")
    test = converter.convert_node(node.test)
    body = converter.convert_block(node.body)
    return WHILE_TEMPLATE % {"test": test, "body": body}


@VKScriptConverter.register(ast.For)
def for_handler(node: ast.For):
    converter = VKScriptConverter.get_current()
    if node.orelse:
        raise NotImplementedError("for...else not implemented.")

    converter.scope.locals.append(node.target.id)
    target = converter.convert_node(node.target)
    _iter = converter.convert_node(node.iter)
    body = converter.convert_block(node.body)
    return FOR_TEMPLATE % {"target": target, "iter": _iter, "body": body}


@VKScriptConverter.register(ast.If)
def if_handler(node: ast.If):
    converter = VKScriptConverter.get_current()
    test = converter.convert_node(node.test)
    content = converter.convert_block(node.body)
    if node.orelse:
        other = f"else{{{converter.convert_block(node.orelse)}}}"
    else:
        other = ""
    return IF_TEMPLATE % {"test": test, "content": content, "other": other}
