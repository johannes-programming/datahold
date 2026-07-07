"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection
from typing import Final, Protocol, Self, TypeVar

import setdoc

from .BaseDataContainer import BaseDataContainer
from .BaseDataIterable import BaseDataIterable
from .BaseDataSized import BaseDataSized

Item = TypeVar("Item", covariant=True)


class Data(Collection[Item], Protocol[Item]):
    """Provide hashable collection protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataCollection(
    BaseDataSized,
    BaseDataIterable[Item],
    BaseDataContainer,
    Collection[Item],
):
    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[type-abstract, type-arg]

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]:  # type: ignore[valid-type]
        ...
