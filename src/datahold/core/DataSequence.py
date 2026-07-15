# Concrete subclasses must provide __new__ or __init__,
# __getitem__, __setitem__, __delitem__, __len__, and insert().


from __future__ import annotations

__all__: list[str] = ["DataSequence"]

from abc import abstractmethod
from collections.abc import Iterable, MutableSequence
from typing import Self, SupportsIndex, overload, Optional

import setdoc
import operator

from ..base.BaseDataSequence import BaseDataSequence, Slice, sequenceSlice

@overload
def sequenceKey(key: SupportsIndex )  -> int:...
@overload
def sequenceKey(key: Slice[SupportsIndex]) -> Slice[int]: ...
def sequenceKey(key: SupportsIndex| Slice[SupportsIndex]) -> Optional[int] | Slice[int]:
    if isinstance(key, SupportsIndex):
        return operator.index(key)
    
    return sequenceSlice(key)
class DataSequence[Item](
    BaseDataSequence[Item],
    MutableSequence[Item],
):
    """Act as base class for mutable sequence implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](BaseDataSequence.Data[DataItem]):
        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: int, /) -> None: ...
        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: Slice[int], /) -> None: ...
        @setdoc.basic
        def __delitem__(self: Self, key: int | Slice[int], /) -> None: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: int, value: DataItem, /
        ) -> None: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: Slice[int], value: Iterable[DataItem], /
        ) -> None: ...
        @setdoc.basic
        def __setitem__(
            self: Self,
            key: int | Slice[int],
            value: DataItem | Iterable[DataItem],
            /,
        ) -> None: ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex, /) -> None: ...
    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: Slice, /) -> None:
        # def __delitem__(self, slice[int | None, int | None, int | None], /) -> None
        ...

    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex | Slice, /) -> None:
        if isinstance(key, SupportsIndex):
            del self.__data__()[ operator.index(key)]
        else:
            del self.__data__()[sequenceSlice(key)]

    @overload
    @setdoc.basic
    def __setitem__(self: Self, key: SupportsIndex, value: Item, /) -> None:
        # def [_T] (list[_T], typing.SupportsIndex, _T)
        ...

    @overload
    @setdoc.basic
    def __setitem__(self: Self, key: Slice, value: Iterable[Item], /) -> None:
        # def [_T] (list[_T], slice[typing.SupportsIndex | None, typing.SupportsIndex | None, typing.SupportsIndex | None], typing.Iterable[_T])
        ...

    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex | Slice, value: Item | Iterable[Item], /
    ) -> None:
        if isinstance(key, SupportsIndex):
            self.__data__()[ operator.index(key)] = value
        else:
            self.__data__()[sequenceSlice(key)]= value

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        self.__data__().insert(operator.index(index), item)
