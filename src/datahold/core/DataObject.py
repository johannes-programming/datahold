"""Provide DataObject."""

__all__: list[str] = ["DataObject"]

from abc import abstractmethod
from collections.abc import Hashable
from typing import Any, Self

import setdoc

from ..base.BaseDataObject import BaseDataObject


class DataObject(BaseDataObject):
    """Provide easy abc for custom mutable object."""

    __slots__ = ()

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Hashable: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(self: Self, value: Any) -> None: ...
