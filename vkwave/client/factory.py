"""
Factory of context.
"""
from abc import ABC, abstractmethod
from typing import Dict, Type

from .context import RequestContext
from .types import MethodName, RequestCallbackCallable


class AbstractFactory(ABC):
    @abstractmethod
    def create_context(
        self,
        exceptions: Dict[Type[Exception], None],
        request_callback: RequestCallbackCallable,
        method_name: MethodName,
        request_params: dict,
        *args,
        **kwargs,
    ) -> RequestContext:
        ...


class DefaultFactory(AbstractFactory):
    def create_context(
        self,
        exceptions: Dict[Type[Exception], None],
        request_callback: RequestCallbackCallable,
        method_name: MethodName,
        request_params: dict,
        *args,
        **kwargs,
    ) -> RequestContext:
        return RequestContext(
            exceptions=exceptions,
            request_callback=request_callback,
            method_name=method_name,
            request_params=request_params,
        )
