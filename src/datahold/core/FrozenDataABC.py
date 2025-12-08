from abc import ABCMeta, abstractmethod
from typing import *

import setdoc

__all__ = ["FrozenDataABC"]


class FrozenDataABC(metaclass=ABCMeta):
    __slots__ = ()

    data: Any

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> None: ...

    @classmethod
    def __subclasshook__(cls: type, other: type, /) -> bool:
        "This magic classmethod can be overwritten for a custom subclass check."
        return NotImplemented

    @property
    @abstractmethod
    def data(self: Self) -> Any: ...
