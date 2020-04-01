import typing

Key = typing.NewType("Key", str)
Value = typing.Any
TTL = typing.NewType("TTL", float)

Dumper = typing.Callable[[Value], str]
Loader = typing.Callable[[str], Value]
