__all__: list[str] = ["SlotDict"]
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class SlotDict(BaseDataDict[Key, Value]):
    """Work as a dict-like class."""

    __slots__ = ("_data",)

    @setdoc.basic
    def __fget__(self: Self) -> frozendict[Key | str, Optional[Value]]:
        return self._data

    @setdoc.basic
    def __fset__(
        self: Self, data: frozendict[Key | str, Optional[Value]], /
    ) -> None:
        self._data: frozendict[Key | str, Optional[Value]] = data
