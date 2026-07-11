"""Provide DataObject."""

__all__: list[str] = ["DataObject"]

from abc import abstractmethod
from collections.abc import Hashable
from typing import Any, Self

import setdoc
from copyable import Copyable

from ..base.BaseDataObject import BaseDataObject


class DataObject(BaseDataObject, Copyable):

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __init__(self:Self, data:Self, /)->None:
        ...

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Hashable: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(self: Self, value: Any) -> None: ...
