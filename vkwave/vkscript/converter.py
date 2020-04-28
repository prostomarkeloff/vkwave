import typing
import contextvars
from typing import Type, TypeVar

import pydantic


T = TypeVar("T")


class ContextInstanceMixin:
    def __init_subclass__(cls, **kwargs):
        cls.__context_instance = contextvars.ContextVar(
            "instance_" + cls.__name__
        )
        return cls

    @classmethod
    def get_current(cls: Type[T], no_error=True) -> T:
        if no_error:
            return cls.__context_instance.get(None)
        return cls.__context_instance.get()

    @classmethod
    def set_current(cls: Type[T], value: T):
        if not isinstance(value, cls):
            raise TypeError(
                f"Value should be instance of '{cls.__name__}' not '{type(value).__name__}'"
            )
        cls.__context_instance.set(value)


class Scope(pydantic.BaseModel):
    locals: list = []
    globals: dict = {}


class VKScriptConverter(ContextInstanceMixin):
    handlers: dict = {}

    @classmethod
    def register(cls, expr):
        def meta(handler: typing.Callable):
            cls.handlers[expr] = handler

        return meta

    def __init__(self, scope: Scope = None):
        self.scope = scope or Scope()
        self.set_current(self)

    def convert_node(self, node):
        if node.__class__ in self.handlers:
            return self.handlers[node.__class__](node)
        raise NotImplementedError(
            f"Conversion for type {node.__class__} not implemented."
        )

    def convert_block(self, nodes: list):
        return "".join(self.convert_node(child) for child in nodes)
