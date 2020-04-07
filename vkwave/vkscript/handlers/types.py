import ast

from ..converter import VKScriptConverter


@VKScriptConverter.register(ast.Dict)
def dict_handler(node: ast.Dict):
    converter = VKScriptConverter.get_current()
    inner = ",".join(
        f"{converter.convert_node(key)}:{converter.convert_node(value)}"
        for key, value in zip(node.keys, node.values)
    )
    return f"{{{inner}}}"


@VKScriptConverter.register(ast.List)
def list_handler(node: ast.List):
    converter = VKScriptConverter.get_current()
    return f'[{",".join(converter.convert_node(element) for element in node.elts)}]'


@VKScriptConverter.register(ast.Tuple)
def tuple_handler(node: ast.Tuple):
    converter = VKScriptConverter.get_current()
    return f'[{",".join(converter.convert_node(element) for element in node.elts)}]'


@VKScriptConverter.register(ast.Num)
def num_handler(node: ast.Num):
    return repr(node.n)


@VKScriptConverter.register(ast.Str)
def str_handler(node: ast.Str):
    return repr(node.s)


@VKScriptConverter.register(ast.NameConstant)
def name_constant_handler(node: ast.NameConstant):
    constants = {None: "null", True: "true", False: "false"}
    if node.value not in constants:
        raise NotImplementedError(f"constant {node.value} not implemented")
    return constants[node.value]
