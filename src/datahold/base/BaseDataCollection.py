"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataContainer import BaseDataContainer
from .BaseDataIterable import BaseDataIterable
from .BaseDataSized import BaseDataSized

Item = TypeVar("Item", covariant=True)
DataItem = TypeVar("DataItem", covariant=True)


class BaseDataCollection(
    BaseDataSized,
    BaseDataIterable[Item],
    BaseDataContainer,
    Collection[Item],
):
    __slots__ = ()

    @runtime_checkable
    class Data(
        BaseDataSized.Data,
        BaseDataIterable.Data[DataItem],
        BaseDataContainer.Data,
        Collection[DataItem],
        Protocol[DataItem],
    ): ...

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
