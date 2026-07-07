"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Iterator
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataContainer import BaseDataContainer
from .BaseDataIterable import BaseDataIterable
from .BaseDataSized import BaseDataSized

Item = TypeVar("Item", covariant=True)


class BaseDataCollection(
    BaseDataSized,
    BaseDataIterable[Item],
    BaseDataContainer,
    Collection[Item],
):
    __slots__ = ()

    class Data(
        BaseDataSized.Data,  # type: ignore[misc, valid-type]
        BaseDataIterable.Data[Item],  # type: ignore[misc, valid-type]
        BaseDataContainer.Data,  # type: ignore[misc, valid-type]
        Collection[Item],
        Protocol[Item],
    ):
        """Provide hashable collection protocol."""

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]:  # type: ignore[valid-type]
        ...
