from __future__ import annotations

__all__: list[str] = ["BaseDataFgettable"]
from abc import abstractmethod, ABCMeta
from typing import Self, TypeVar, Generic

import setdoc

Data = TypeVar("Data", covariant=True)


class BaseDataFgettable(Generic[Data], metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data: ...
