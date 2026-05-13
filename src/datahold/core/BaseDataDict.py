import collections
from abc import abstractmethod
from typing import *

import setdoc
from frozendict import frozendict

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class BaseDataDict(
    BaseDataObject,
    collections.abc.Mapping[Key, Value],
):
    data: frozendict[Key, Value]
    __slots__ = ()

    @setdoc.setdoc(dict.__contains__.__doc__)
    def __contains__(self: Self, key: Any, /) -> Any:
        return dict(self.data).__contains__(key)

    @setdoc.setdoc(dict.__getitem__.__doc__)
    def __getitem__(self: Self, key: Key, /) -> Value:
        return dict(self.data).__getitem__(key)

    @abstractmethod
    @setdoc.setdoc(dict.__init__.__doc__)
    def __init__(self: Self, data: Any = (), /, **kwargs: Value) -> None: ...

    @setdoc.setdoc(dict.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterable[Key]:
        return dict(self.data).__iter__()

    @setdoc.setdoc(dict.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return dict(self.data).__len__()

    @setdoc.setdoc(dict.__or__.__doc__)
    def __or__(self: Self, value: Any, /) -> Any:
        return dict(self.data).__or__(value)

    @setdoc.setdoc(dict.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return dict(self.data).__repr__()

    @setdoc.setdoc(dict.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterable[Key]:
        return dict(self.data).__reversed__()

    @setdoc.setdoc(dict.__ror__.__doc__)
    def __ror__(self: Self, value: Any, /) -> Any:
        return dict(self.data).__ror__(value)

    @classmethod
    @setdoc.setdoc(dict.fromkeys.__doc__)
    def fromkeys(
        cls: type[Self], iterable: Iterable[Key], value: Any = None, /
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))

    @setdoc.setdoc(dict.get.__doc__)
    def get(self: Self, key: Any, default: Any = None, /) -> Any:
        return dict(self.data).get(key, default)

    @setdoc.setdoc(dict.items.__doc__)
    def items(self: Self, /) -> Iterable[tuple[Key, Value]]:
        return dict(self.data).items()

    @setdoc.setdoc(dict.keys.__doc__)
    def keys(self: Self, /) -> Iterable[Key]:
        return dict(self.data).keys()

    @setdoc.setdoc(dict.values.__doc__)
    def values(self: Self, /) -> Iterable[Value]:
        return dict(self.data).values()
