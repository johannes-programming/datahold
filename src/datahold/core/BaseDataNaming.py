from abc import abstractmethod
from typing import *

import namings

from datahold._utils.wrapping import wraps

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataNaming"]

Value = TypeVar("Value")


class BaseDataNaming(
    BaseDataObject,
    namings.abc.BaseNamingABC.BaseNamingABC[Value],
):
    data: namings.FrozenNaming[Value]
    __slots__ = ()

    @wraps(namings.Naming[Value])
    def __contains__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__contains__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __eq__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__eq__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __getitem__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__getitem__(*args, **kwargs)

    @abstractmethod
    @wraps(namings.Naming[Value])
    def __init__(self: Self, *args: Any, **kwargs: Any) -> None:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ...

    @wraps(namings.Naming[Value])
    def __iter__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__iter__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __len__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__len__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __or__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__or__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __repr__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__repr__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def __reversed__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).__reversed__(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def get(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).get(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def items(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).items(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def keys(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).keys(*args, **kwargs)

    @wraps(namings.Naming[Value])
    def values(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        return namings.Naming[Value](self.data).values(*args, **kwargs)
