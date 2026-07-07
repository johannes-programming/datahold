"""Provide BaseDataObject."""

__all__: list[str] = ["BaseDataObject"]

from abc import ABCMeta, abstractmethod
from collections.abc import Hashable
from typing import Any, Final, Self

import setdoc


class BaseDataObject(metaclass=ABCMeta):

    __slots__ = ()

    Data: Final[type[Hashable]] = Hashable  # type: ignore[type-abstract]

    @setdoc.basic
    def __eq__(self: Self, other: Any, /) -> Any:
        if isinstance(other, BaseDataObject):
            return self.data.__eq__(other.data)
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(self: Self, other: Any, /) -> Any:
        if not isinstance(other, BaseDataObject):
            return NotImplemented
        try:
            return self.data.__ge__(other.data)  # type: ignore[operator]
        except Exception:
            return NotImplemented

    @setdoc.basic
    def __gt__(self: Self, other: Any, /) -> Any:
        if not isinstance(other, BaseDataObject):
            return NotImplemented
        try:
            return self.data.__gt__(other.data)  # type: ignore[operator]
        except Exception:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Self, /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: Any, /) -> Any:
        if not isinstance(other, BaseDataObject):
            return NotImplemented
        try:
            return self.data.__le__(other.data)  # type: ignore[operator]
        except Exception:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: Any, /) -> Any:
        if not isinstance(other, BaseDataObject):
            return NotImplemented
        try:
            return self.data.__lt__(other.data)  # type: ignore[operator]
        except Exception:
            return NotImplemented

    @setdoc.basic
    def __ne__(self: Self, other: Any, /) -> Any:
        if isinstance(other, BaseDataObject):
            return self.data.__ne__(other.data)
        else:
            return NotImplemented

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Hashable: ...
