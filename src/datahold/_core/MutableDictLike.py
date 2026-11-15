from __future__ import annotations

__all__: list[str] = [
    "MutableDictLike",
]

from abc import abstractmethod
from collections import abc
from typing import Any, Self, TypeVar, overload

from frozendict import frozendict
from typing_extensions import TypeAliasType

from datahold._core.ContextManager import ContextManager
from datahold._core.dictable import dictable
from datahold._core.DictInit import DictInit
from datahold._core.DictLike import DictLike

Key = TypeVar("Key", bound=abc.Hashable)
Value = TypeVar("Value")

InitKey = TypeVar("InitKey", bound=abc.Hashable)
MutableKey = TypeVar("MutableKey", bound=abc.Hashable)
MutableValue = TypeVar("MutableValue")
OrKey = TypeVar("OrKey", bound=abc.Hashable)
OrValue = TypeVar("OrValue")
TypeKey = TypeVar("TypeKey", bound=abc.Hashable)
TypeValue = TypeVar("TypeValue")
UpdateKey = TypeVar("UpdateKey", bound=abc.Hashable)


class MutableDictLike(DictLike[Key, Value], abc.MutableMapping[Key, Value]):
    """Mutable mapping operations performed on a temporary dict."""

    Mutable = TypeAliasType(
        "Mutable",
        dict[MutableKey, MutableValue],
        type_params=(MutableKey, MutableValue),
    )

    __slots__ = ()

    def __delitem__(self: Self, key: abc.Hashable, /) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            del mutable[key]  # type: ignore[arg-type]

    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            return frozendict(mutable)

    __hash__ = None  # type: ignore[assignment]

    @overload
    def __init__(
        self: Self,
        other: DictInit[Key, Value] = (),
        /,
    ) -> None: ...

    @overload
    def __init__(
        self: DictLike[InitKey | str, Value],
        other: DictInit[InitKey | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    def __init__(
        self: Any,
        other: Any = (),
        /,
        **kwargs: Any,
    ) -> None:
        self.update(other, **kwargs)

    def __ior__(  # type: ignore[misc, override]
        self: Self, other: DictInit[Key, Value], /
    ) -> MutableDictLike[Key, Value]:
        self.update(other)
        return self

    @abstractmethod
    def __mutate__(self: Self, /) -> ContextManager[dict[Key, Value]]:
        """Yield a mutable working dictionary and commit on normal exit."""

    def __or__(
        self: Self, other: DictLike[OrKey, OrValue], /
    ) -> MutableDictLike[Key | OrKey, Value | OrValue]:
        if not isinstance(other, DictLike):
            return NotImplemented
        return type(self).__type__(
            self.__frozen__() | other.__frozen__()  # type: ignore[arg-type]
        )

    def __setitem__(self: Self, key: Key, value: Value, /) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            mutable[key] = value

    @classmethod
    def __type__(
        cls: type[Any],
        other: DictInit[TypeKey, TypeValue],
        /,
    ) -> MutableDictLike[TypeKey, TypeValue]:
        # redoing the same method is necessary because copy must return MutableDictLike[Item]
        return cls(other)  # type: ignore[no-any-return]

    # clear is inherited from abc.MutableMapping.

    def copy(self: Self, /) -> MutableDictLike[Key, Value]:
        return type(self).__type__(self.__frozen__())  # type: ignore[arg-type]

    # pop is inherited from abc.MutableMapping.
    def popitem(self: Self, /) -> tuple[Key, Value]:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            return mutable.popitem()

    # setdefault is inherited from abc.MutableMapping.

    @overload  # type: ignore[override]
    def update(
        self: Self,
        other: DictInit[Key, Value] = (),
        /,
    ) -> None: ...
    @overload
    def update(
        self: MutableDictLike[UpdateKey | str, Value],
        other: DictInit[UpdateKey | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...
    def update(
        self: Any, other: DictInit[Any, Any] = (), /, **kwargs: Value
    ) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            mutable.update(dictable(other), **kwargs)
