# remove in v4.0
"""Provide BaseDataObject."""

__all__: list[str] = ["BaseDataObject"]

from abc import ABCMeta, abstractmethod
from collections.abc import Hashable
from typing import Self

import setdoc


class BaseDataObject(metaclass=ABCMeta):
    """Provide an easy abc for a custom object."""

    __slots__ = ()

    type Data = Hashable

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data: ...
