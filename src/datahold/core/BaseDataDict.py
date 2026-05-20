
from abc import abstractmethod
from typing import *
import collections.abc

import setdoc
from frozendict import frozendict

from .BaseDataCollection import BaseDataCollection

__all__ = ["BaseDataDict"]

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseDataDict(
    BaseDataCollection,
    Generic[Key, Value],
):
    data: frozendict[Key, Value]
    __slots__ = ()

    @staticmethod
    def Repr() -> type:
        return dict

    @setdoc.setdoc(dict.__getitem__.__doc__)
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        return self.data.__getitem__(key)

    @abstractmethod
    @setdoc.setdoc(dict.__init__.__doc__)
    def __init__(self: Self, data: Any = (), /, **kwargs: Value) -> None: ...

    @setdoc.setdoc(dict.__or__.__doc__)
    def __or__(self: Self, value: Any, /) -> Any:
        return self.data.__or__(value)

    @setdoc.setdoc(dict.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterable[Key]:
        return self.data.__reversed__()

    @setdoc.setdoc(dict.__ror__.__doc__)
    def __ror__(self: Self, value: Any, /) -> Any:
        return self.data.__ror__(value)

    @classmethod
    @setdoc.setdoc(dict.fromkeys.__doc__)
    def fromkeys(
        cls: type[Self], iterable: Iterable[Key], value: Any = None, /
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))

    @overload
    @setdoc.setdoc(dict.get.__doc__)
    def get(self: Self, key: Hashable, /) -> Optional[Value]: ...

    @setdoc.setdoc(dict.get.__doc__)
    def get(self: Self, key: Hashable, default: Value_, /) -> Value|Value_: ...

    @setdoc.setdoc(dict.get.__doc__)
    def get(
            self: Self, 
            key: Hashable, 
            default: Optional[Value_] = None, 
            /,
    ) -> Optional[Value|Value_]:
        return self.data.get(key, default)

    @setdoc.setdoc(dict.items.__doc__)
    def items(self: Self, /) -> Iterable[tuple[Key, Value]]:
        return self.data.items()

    @setdoc.setdoc(dict.keys.__doc__)
    def keys(self: Self, /) -> Iterable[Key]:
        return self.data.keys()

    @setdoc.setdoc(dict.values.__doc__)
    def values(self: Self, /) -> Iterable[Value]:
        return self.data.values()
collections.abc.Mapping.register(BaseDataDict)