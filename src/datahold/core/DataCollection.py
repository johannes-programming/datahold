"""Provide DataCollection."""

__all__: list[str] = ["DataCollection"]

from abc import abstractmethod
from collections.abc import Hashable
from typing import Protocol, Self, Never

import setdoc

from ..base.BaseDataCollection import BaseDataCollection


class DataCollection[Item](BaseDataCollection[Item]):

    __slots__ = ()

    class Data[DataItem](
        BaseDataCollection.Data[DataItem],
        Hashable,
        Protocol[DataItem],
    ):
        ...
        

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(self: Self, value: Never) -> None: ...
