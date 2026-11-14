from __future__ import annotations

__all__: list[str] = [
    "ListLike",
]

from abc import abstractmethod
from collections import abc
from reprlib import recursive_repr
from types import NotImplementedType
from typing import Any, Self, SupportsIndex, overload

from datahold._core.Collection import Collection
from datahold._core.typing import (
    Slice,
    SupportsGE,
    SupportsGT,
    SupportsLE,
    SupportsLT,
)

### LIST-LIKE ###


class ListLike[Item](Collection[Item], abc.Sequence[Item]):
    """Shared read-only sequence with cross-variant tuple-style comparison."""

    type Frozen[FrozenItem] = tuple[FrozenItem, ...]

    __slots__ = ()

    def __add__(self: Self, other: ListLike[Item], /) -> ListLike[Item]:
        if not isinstance(other, ListLike):
            return NotImplemented
        return type(self).__type__(self.__frozen__() + other.__frozen__())

    # __contains__ is inherited
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() == other.__frozen__()

    @abstractmethod
    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        """Return an immutable tuple snapshot."""

    @overload
    def __ge__[Item_](
        self: ListLike[SupportsGE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __ge__(self: Self, other: ListLike[SupportsLE[Item]], /) -> bool: ...
    def __ge__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() >= other.__frozen__()

    @overload
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    def __getitem__(
        self: Self, index: Slice[SupportsIndex | None], /
    ) -> ListLike[Item]: ...

    def __getitem__(
        self: Self, index: SupportsIndex | Slice[SupportsIndex | None], /
    ) -> Any:
        if isinstance(index, SupportsIndex):
            return self.__frozen__()[index]
        else:
            return type(self).__type__(self.__frozen__()[index])

    @overload
    def __gt__[Item_](
        self: ListLike[SupportsGT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __gt__(self: Self, other: ListLike[SupportsLT[Item]], /) -> bool: ...
    def __gt__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() > other.__frozen__()

    @abstractmethod
    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None: ...

    @overload
    def __le__[Item_](
        self: ListLike[SupportsLE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __le__(self: Self, other: ListLike[SupportsGE[Item]], /) -> bool: ...
    def __le__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() <= other.__frozen__()

    @overload
    def __lt__[Item_](
        self: ListLike[SupportsLT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __lt__(self: Self, other: ListLike[SupportsGT[Item]], /) -> bool: ...
    def __lt__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() < other.__frozen__()

    def __mul__(self: Self, other: SupportsIndex, /) -> ListLike[Item]:
        return type(self).__type__(self.__frozen__() * other)

    # __ne__ is inherited from object (negates __eq__).
    @recursive_repr()
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.__frozen__())})"

    # __reversed__ is inherited from abc.Sequence.

    __rmul__ = __mul__

    @classmethod
    def __type__[Item_](
        cls: type[Any],
        data: abc.Iterable[Item_],
        /,
    ) -> ListLike[Item_]:
        return cls(data)  # type: ignore[no-any-return]

    # count is inherited from abc.Sequence.
    # index is inherited from abc.Sequence.
