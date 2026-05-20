import collections.abc
from typing import *
from abc import abstractmethod

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataList"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataCollection(BaseDataObject):
    __slots__ = ()

    @setdoc.setdoc(list.__contains__.__doc__)
    def __contains__(self: Self, value: Any, /) -> Any:
        return self.data.__contains__(value)

    @setdoc.setdoc(list.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterable[Item]:
        return self.data.__iter__()

    @setdoc.setdoc(list.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return self.data.__len__()
    
    @property
    @abstractmethod
    def data(self: Self) -> collections.abc.Collection: ...

collections.abc.Collection.register(BaseDataCollection)