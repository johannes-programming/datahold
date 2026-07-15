from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]
from abc import abstractmethod
from collections.abc import Container, Hashable, Iterable, Mapping, Sized
from typing import Never, Protocol, Self

import setdoc

from .BaseDataCollection import BaseDataCollection



class BaseDataMapping[Key, Value](  # type: ignore[type-var]
    BaseDataCollection[Key],
    Mapping[Key, Value],
):
    """Act as base class for mapping implementation which only needs overriding of __data__ to work immediately."""

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

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        return self.__data__()[key]
