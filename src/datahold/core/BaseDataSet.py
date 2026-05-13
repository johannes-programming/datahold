import collections
from abc import abstractmethod
from typing import *

import setdoc

from datahold._utils.wrapping import wraps

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataSet"]

Item = TypeVar("Item")


class BaseDataSet(
    BaseDataObject,
    collections.abc.Set[Item],
):
    __slots__ = ()

    @wraps(set[Item])
    def __and__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__and__(*args, **kwargs)

    @wraps(set[Item])
    def __contains__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__contains__(*args, **kwargs)

    @wraps(set[Item])
    def __ge__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__ge__(*args, **kwargs)

    @wraps(set[Item])
    def __gt__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__gt__(*args, **kwargs)

    @abstractmethod
    @wraps(set[Item])
    def __init__(self: Self, *args: Any, **kwargs: Any) -> None:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ...

    @wraps(set[Item])
    def __iter__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__iter__(*args, **kwargs)

    @wraps(set[Item])
    def __le__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__le__(*args, **kwargs)

    @wraps(set[Item])
    def __len__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__len__(*args, **kwargs)

    @wraps(set[Item])
    def __lt__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__lt__(*args, **kwargs)

    @wraps(set[Item])
    def __or__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__or__(*args, **kwargs)

    @wraps(set[Item])
    def __rand__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__rand__(*args, **kwargs)

    @wraps(set[Item])
    def __repr__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__repr__(*args, **kwargs)

    @wraps(set[Item])
    def __ror__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__ror__(*args, **kwargs)

    @wraps(set[Item])
    def __rsub__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__rsub__(*args, **kwargs)

    @wraps(set[Item])
    def __rxor__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__rxor__(*args, **kwargs)

    @wraps(set[Item])
    def __sub__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__sub__(*args, **kwargs)

    @wraps(set[Item])
    def __xor__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).__xor__(*args, **kwargs)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]: ...

    @wraps(set[Item])
    def difference(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).difference(*args, **kwargs)

    @wraps(set[Item])
    def intersection(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).intersection(*args, **kwargs)

    @wraps(set[Item])
    def isdisjoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).isdisjoint(*args, **kwargs)

    @wraps(set[Item])
    def issubset(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).issubset(*args, **kwargs)

    @wraps(set[Item])
    def issuperset(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).issuperset(*args, **kwargs)

    @wraps(set[Item])
    def symmetric_difference(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).symmetric_difference(*args, **kwargs)

    @wraps(set[Item])
    def union(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return set(self.data).union(*args, **kwargs)
