from __future__ import annotations

__all__: list[str] = ["BaseDataDict"]

from abc import abstractmethod
from collections.abc import Container, Iterable, Sized, Hashable
from types import NotImplementedType
from typing import Never, Optional, Protocol, Self, Any

import setdoc
from .BaseDataMapping import BaseDataMapping


class SupportsKeysAndGetitem[Key, Value](Protocol[Key, Value]):

    @setdoc.basic
    def __getitem__(self: Self, key: Any, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> Iterable[Key]: ...
        

class BaseDataDict[Key, Value](BaseDataMapping[Key | str, Optional[Value]]):
    """Act as base class for dict-like implementation which only has to override __data__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        Sized,
        Iterable[DataKey],
        Container[Never],
        Protocol[DataKey, DataValue],
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: Hashable, /) -> DataValue: ...
        @setdoc.basic
        def __or__(self: Self, other: Self, /) -> BaseDataDict.Init[DataKey, DataValue]: ...
        @setdoc.basic
        def keys(self: Self, /) -> Iterable[DataKey | str]: ...

    type Init[Key, Value] = (
        SupportsKeysAndGetitem[Key|str, Optional[Value]]
        | Iterable[tuple[Key|str, Optional[Value]]]
    )

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key | str, Optional[Value]]: ...

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataDict):
            return self.__data__() == other.__data__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None: ...

    @setdoc.basic
    def __or__(
        self: Self, other: BaseDataDict[Key | str, Optional[Value]], /
    ) -> Self:
        # Overload(
        #     def [_KT, _VT] (dict[_KT, _VT], dict[_KT, _VT]) -> dict[_KT, _VT],
        #     def [_KT, _VT, _T1, _T2] (dict[_KT, _VT], dict[_T1, _T2]) -> dict[_KT | _T1, _VT | _T2],
        # )
        return type(self)(self.__data__() | other.__data__())

    # __ror__ is not needed
    # because of how __or__ is defined

    @classmethod
    def fromkeys(
        self: Self, keys: Iterable[Key | str], value: Optional[Value] = None, /
    ) -> Self:
        return type(self)(dict.fromkeys(keys, value))
