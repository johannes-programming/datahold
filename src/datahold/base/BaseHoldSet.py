from collections.abc import Hashable
from typing import TypeVar

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldSet"]

Item = TypeVar("Item", bound=Hashable)


class BaseHoldSet(BaseHoldObject, BaseDataSet[Item]):
    __slots__ = ()
