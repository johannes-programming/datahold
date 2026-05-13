from abc import abstractmethod
from typing import *

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item", covariant=True)


class FrozenDataSet(FrozenDataObject, BaseDataSet[Item]):

    __slots__ = ()
