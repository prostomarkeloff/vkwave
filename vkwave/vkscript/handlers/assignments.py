import ast

from ..converter import VKScriptConverter


@VKScriptConverter.register(ast.Assign)
def assign_handler(node: ast.Assign):
    converter = VKScriptConverter.get_current()
    left = node.targets
    left_ = []
    for target in left:
        if target.__class__ == ast.Name:
            left_.append(target.id)
            converter.scope.locals.append(target.id)
        elif target.__class__ == ast.Subscript:
            pass
        elif target.__class__ == ast.Tuple:
            raise NotImplementedError("Tuple assignments are not allowed")
        else:
            raise NotImplementedError(
                f"Assignments of {target.__class__} are not implemented"
            )

    right = converter.convert_node(node.value)
    return "var " + ",".join(f"{target}={right}" for target in left_) + ";"


@VKScriptConverter.register(ast.AugAssign)
def aug_assign_handler(node: ast.AugAssign):
    converter = VKScriptConverter.get_current()
    ops = {
        ast.Add: "+",
        ast.Sub: "-",
        ast.Mult: "*",
        ast.Div: "/",
        ast.Pow: "**",
        ast.RShift: ">>",
        ast.LShift: "<<",
        ast.BitOr: "|",
        ast.BitAnd: "&",
        ast.Mod: "%",
    }

    if node.op.__class__ not in ops:
        raise NotImplementedError(f"Operation {node.op} is not implemented.")

    if (
        node.target.__class__ == ast.Name
        and node.target.id not in converter.scope.locals
    ):
        raise NameError(f"name '{node.target.id}' is not defined")
    target = converter.convert_node(node.target)
    return f"{target}={target}{ops[node.op.__class__]}({converter.convert_node(node.value)});"


@VKScriptConverter.register(ast.Name)
def name_handler(node: ast.Name):
    converter = VKScriptConverter.get_current()
    if node.id in converter.scope.locals:
        return node.id
    if node.id not in converter.scope.globals:
        raise NameError(f"name '{node.id}' is not defined")
    if (
        type(converter.scope.globals[node.id])
        not in (str, int, tuple, dict, list)
        and converter.scope.globals[node.id] is not None
    ):
        raise NotImplementedError(
            f'type "{type(converter.scope.globals[node.id])}" not allowed inside VK Script'
        )
    return converter.convert_node(
        ast.parse(repr(converter.scope.globals[node.id]), mode="eval").body
    )
