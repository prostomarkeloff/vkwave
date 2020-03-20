import typing

JSONEncoder = typing.Callable[[typing.Any], str]
Button = typing.Dict[str, typing.Union[typing.Dict[str, typing.Union[str, typing.Dict[str, str]]]]]
