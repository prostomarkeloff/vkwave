import ast
import string

from ..converter import VKScriptConverter


@VKScriptConverter.register(ast.Expr)
def expr_handler(node: ast.Expr):
    converter = VKScriptConverter.get_current()
    return converter.convert_node(node.value) + ";"


@VKScriptConverter.register(ast.Module)
def module_handler(node: ast.Module):
    converter = VKScriptConverter.get_current()
    return converter.convert_block(node.body)


@VKScriptConverter.register(ast.BinOp)
def bin_op_handler(node: ast.BinOp):
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
    converter = VKScriptConverter.get_current()
    return f"{converter.convert_node(node.left)}{ops[node.op.__class__]}{converter.convert_node(node.right)}"


@VKScriptConverter.register(ast.Compare)
def compare_handler(node: ast.Compare):
    ops = {
        ast.Gt: ">",
        ast.Lt: "<",
        ast.GtE: ">=",
        ast.LtE: "<=",
        ast.Eq: "==",
        ast.NotEq: "!=",
    }

    operations = []
    converter = VKScriptConverter.get_current()
    left = converter.convert_node(node.left)
    for op, comparator in zip(node.ops, node.comparators):
        if op.__class__ not in ops:
            raise NotImplementedError(
                f"comparison operator {op} not supported"
            )
        operations.append(
            f"{left}{ops[op.__class__]}{converter.convert_node(comparator)}"
        )
    return "&&".join(operations)


@VKScriptConverter.register(ast.BoolOp)
def bool_op_handler(node: ast.BoolOp):
    ops = {ast.And: "&&", ast.Or: "||"}
    if node.op.__class__ not in ops:
        raise NotImplementedError(f"operation '{node.op}' not supported")
    converter = VKScriptConverter.get_current()
    return ops[node.op.__class__].join(
        converter.convert_node(value) for value in node.values
    )


@VKScriptConverter.register(ast.UnaryOp)
def unary_op_handler(node: ast.UnaryOp):
    ops = {ast.UAdd: "+", ast.USub: "-"}
    if node.op.__class__ not in ops:
        raise NotImplementedError(f"operation '{node.op}' not supported")
    converter = VKScriptConverter.get_current()
    return f"{ops[node.op.__class__]}{converter.convert_node(node.operand)}"


@VKScriptConverter.register(ast.Subscript)
def subscript_handler(node: ast.Subscript):
    converter = VKScriptConverter.get_current()
    value = converter.convert_node(node.value)
    if node.slice.__class__ == ast.Index:
        safe = frozenset(string.ascii_letters + string.digits + "_")
        if (
            node.slice.value.__class__ == ast.Str
            and set(node.slice.value.s) <= safe
        ):
            # TODO: Improve safety check, first symbol may be digit
            return f"{value}.{node.slice.value.s}"
        return f"{value}[{converter.convert_node(node.slice.value)}]"
    elif node.slice.__class__ == ast.Slice:
        if node.slice.step:
            raise NotImplementedError("steps in slice not supported")
        if (
            node.slice.lower.__class__ != ast.Num
            and node.slice.upper.__class__ != ast.Num
        ):
            raise TypeError("slices must be integers")
        lower = node.slice.lower.n or 0
        if node.slice.upper:
            return f"{value}.slice({lower},{node.slice.upper.n})"
        return f"{value}.slice({lower})"
    raise NotImplementedError(f"slice {node.slice} not supported")


@VKScriptConverter.register(ast.Attribute)
def attribute_handler(node: ast.Attribute):
    converter = VKScriptConverter.get_current()
    return f"{converter.convert_node(node.value)}.{node.attr}"
