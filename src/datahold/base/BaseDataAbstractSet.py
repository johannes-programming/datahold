"""Provide BaseDataAbstractSet."""

from __future__ import annotations

__all__: list[str] = ["BaseDataAbstractSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable, Set
from typing import Any, Final, Protocol, Self, TypeVar, cast

import setdoc

from .BaseDataCollection import BaseDataCollection

Item = TypeVar("Item", bound=Hashable, covariant=True)


class Data(Set[Item], Protocol[Item]):  # type: ignore[misc]
    """Provide hashable abstract set protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataAbstractSet(BaseDataCollection[Item], Set[Item]):
    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[type-arg,type-abstract,valid-type]

    @setdoc.basic
    def __and__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data & frozenset(other))  # type: ignore[operator]

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __or__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        return type(self)(self.data | frozenset(other))

    @setdoc.basic
    def __rand__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(cast(frozenset[Item], frozenset(other) & self.data))

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.data)!r})"

    @setdoc.basic
    def __ror__(
        self: Self,
        other: Set[Item],
        /,
    ) -> Self:
        return type(self)(frozenset(other) | self.data)

    @setdoc.basic
    def __rsub__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(cast(frozenset[Item], frozenset(other) - self.data))

    @setdoc.basic
    def __rxor__(
        self: Self,
        other: Set[Item],
        /,
    ) -> Self:
        return type(self)(frozenset(other) ^ self.data)

    @setdoc.basic
    def __sub__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data - frozenset(other))  # type: ignore[operator]

    @setdoc.basic
    def __xor__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        return type(self)(self.data ^ frozenset(other))  # type: ignore[operator]

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...  # type: ignore[valid-type]

    @setdoc.basic
    def isdisjoint(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.data.isdisjoint(other)  # type: ignore[attr-defined,no-any-return]
