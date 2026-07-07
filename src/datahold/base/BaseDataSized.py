"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Sized
from typing import Protocol, Self

import setdoc

from .BaseDataObject import BaseDataObject


class BaseDataSized(BaseDataObject, Sized):
    __slots__ = ()

    class Data(
        BaseDataObject.Data,
        Sized,
        Protocol,
    ):
        """Provide hashable sized protocol."""

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data:  # type: ignore[valid-type]
        ...
