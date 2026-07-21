"""Provide DataCollection."""

from __future__ import annotations

__all__: list[str] = ["DataCollection"]

from abc import abstractmethod
from typing import Never, Self

import setdoc

from ..base.BaseDataCollection import BaseDataCollection


class DataCollection[Item](BaseDataCollection[Item]):

    __slots__ = ()

    __hash__ = None  # type: ignore

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> DataCollection.Data[Item]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(self: Self, value: Never) -> None: ...
