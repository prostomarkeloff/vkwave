import typing

JSONEncoder = typing.Callable[[typing.Any], str]
JSONDecoder = typing.Callable[[str], typing.Any]
