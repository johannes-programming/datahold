from typing import Any, Self

import setdoc
from copyable import Copyable

from ..base.BaseDataObject import BaseDataObject

__all__ = ["DataObject"]


class DataObject(BaseDataObject, Copyable):
    data: Any

    __slots__ = ()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.data)
