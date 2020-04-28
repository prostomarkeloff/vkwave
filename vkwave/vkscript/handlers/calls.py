import ast

from ..converter import VKScriptConverter


@VKScriptConverter.register(ast.Call)
def call_handler(node: ast.Call):
    converter = VKScriptConverter.get_current()
    replacements = {"append": "push", "pop": "pop", "split": "split"}
    funcs = [
        "slice",
        "push",
        "pop",
        "shift",
        "unshift",
        "splice",
        "substr",
        "split",
        "append",
    ]
    attrs = []
    node_ = node.func
    while isinstance(node_, ast.Attribute):
        attrs.append(node_.attr)
        node_ = node_.value

    if node_.id.upper() == "API" and len(attrs) >= 1:
        if node.args:
            raise TypeError("api calls does not accept positional arguments")

        inner = ",".join(
            f"{keyword.arg}:{converter.convert_node(keyword.value)}"
            for keyword in node.keywords
        )

        return "API." + ".".join(attrs[::-1]) + f"({{{inner}}})"

    elif (
        not attrs
        and node_.id == "len"
        and "len" not in converter.scope.globals
    ):
        return f"{converter.convert_node(node.args[0])}.length"

    # TODO: rewrite?
    elif len(attrs) == 1 and attrs[0] in funcs:
        if node.keywords:
            raise NotImplementedError("keywords not allowed")

        if attrs[0] in replacements:
            func = replacements[attrs[0]]
        else:
            func = attrs[0]

        return (
            f"{converter.convert_node(node_)}.{func}"
            f'({",".join(converter.convert_node(arg) for arg in node.args)})'
        )

    else:
        raise NotImplementedError(
            f'function call "{node_.id + ("." if attrs else "") + ".".join(attrs[::-1])}" not allowed inside VK Script!'
        )
