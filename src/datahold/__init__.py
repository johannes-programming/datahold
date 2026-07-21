"""Provide __init__."""

from __future__ import annotations

__all__: list[str] = [
    "Collection",
]

from collections import abc
from abc import abstractmethod
import setdoc
from typing import Self, Never, Protocol, overload, Optional, SupportsIndex


type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]

### COLLECTION ###

class Collection[Item](
    abc.Sized, 
    abc.Iterable[Item], 
    abc.Container[object],
):
    __slots__ = ()
    class Data[DataItem](
        abc.Sized,
        abc.Iterable[DataItem],
        abc.Container[Never],
        Protocol[DataItem],
    ):
        ...
    @setdoc.basic
    def __contains__(self:Self, other: object) -> bool:
        try:
            return other in self.__fget__()
        except TypeError:
            return other in (x for x in self)
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
    @setdoc.basic
    def __iter__(self:Self) -> abc.Iterator[Item]:
        return iter(self.__fget__())
    @setdoc.basic
    def __len__(self:Self)->int:
        return len(self.__fget__())


class HashableCollection[Item](Collection[Item], abc.Hashable):
    __slots__=()
    @setdoc.basic
    class Data[DataItem](Collection.Data[DataItem], abc.Hashable):
        ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
    @setdoc.basic
    def __hash__(self:Self)-> int:
        return hash(self.__fget__())

class MutableCollection[Item](Collection[Item]):
    __slots__=()
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> MutableCollection.Data[Item]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:MutableCollection.Data[Item], /) -> None:
        ...

### ABSTRACT SET ###
class AbstractSet[Item](Collection[Item], abc.Set[Item]):
    __slots__=()

class HashableAbstractSet[Item](
    AbstractSet[Item], 
    HashableCollection[Item],
):
    __slots__=()
    class Data[DataItem](
        AbstractSet.Data[DataItem],
        HashableCollection[DataItem],
    ):
        ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
class MutableAbstractSet[Item](
    AbstractSet[Item], 
    MutableCollection[Item],
    abc.MutableSet[Item],
):
    __slots__=()
    class Data[DataItem](AbstractSet.Data[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def add(self:Self, item:DataItem, /) -> None:
            ...
        @setdoc.basic
        def discard(self:Self, item:DataItem, /) -> None:
            ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:Data[Item], /) -> None:
        ...

    @setdoc.basic
    def add(self:Self, item:Item, /) -> None:
        data:MutableAbstractSet.Data[Item]
        data = self.__fget__()
        data.add(item)
        self.__fset__(data)

    @setdoc.basic
    def discard(self:Self, item:Item)->None:
        data:MutableAbstractSet.Data[Item]
        data = self.__fget__()
        data.discard(item)
        self.__fset__(data)

### MAPPINGS ###

class Mapping[Key, Value](
    Collection[Key],
    abc.Mapping[Key, Value],
):
    __slots__=()
    class Data[DataKey, DataValue](
        Collection.Data[DataKey],
        Protocol[DataKey, DataValue],
    ):
        @setdoc.basic
        def __getitem__(self:Self, key:Never, /) -> DataValue:
            ...
    
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Key, Value]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:Data[Key, Value], /) -> None:
        ...

    @setdoc.basic
    def __getitem__(self:Self, key:object, /) -> Value:
        try:
            return self.__fget__()[key]
        except TypeError:
            raise KeyError(key) from None
    
class HashableMapping[Key, Value](
    Mapping[Key, Value],
    HashableCollection[Key],
):
    __slots__=()
    class Data[DataKey, DataValue](
        Mapping.Data[DataKey, DataValue],
        HashableCollection.Data[DataKey],
        Protocol[DataKey, DataValue],
    ):
        ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Key, Value]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:Data[Key, Value], /) -> None:
        ...

class MutableMapping[Key, Value](
    Mapping[Key, Value],
    MutableCollection[Key],
):
    __slots__=()
    class Data[DataKey, DataValue](
        Mapping.Data[DataKey, DataValue],
        MutableCollection.Data[DataKey],
        Protocol[DataKey, DataValue],
    ):
        @setdoc.basic
        def __delitem__(self:Self, key:Never, /) -> None:...
        @setdoc.basic
        def __setitem__(self:Self, key:Never, value:Value,/) -> None:
    
    @setdoc.basic
    def __delitem__(self:Self, key:object, /) -> None:
        data:MutableMapping.Data[Key, Value]
        data=self.__fget__()
        try:
            del data[key]
        except TypeError:
            raise KeyError(key) from None
        self.__fset__(data)

    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Key, Value]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:Data[Key, Value], /) -> None:
        ...

    @setdoc.basic
    def __setitem__(self:Self, key:object, value:Value,/) -> None:
        data:MutableMapping.Data[Key, Value]
        data=self.__fget__()
        try:
            data[key] = value
        except TypeError:
            raise KeyError(key) from None
        self.__fset__(data)
    
### SEQUENCES ###

class Sequence[Item](
    Collection[Item],
    abc.Sequence[Item],
):
    __slots__=()
    class Data[DataItem](
        Collection.Data[DataItem],
        Protocol[DataItem],
    ):
        @overload
        @setdoc.basic
        def __getitem__(self:Self, key: int) -> DataItem:
        @overload
        @setdoc.basic
        def __getitem__(self:Self, key: Slice[int]) -> Sequence[DataItem]:
        @setdoc.basic
        def __getitem__(self:Self, key: int | Slice[int]) -> DataItem | Sequence[DataItem]:
            ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
    @overload
    @setdoc.basic
    def __getitem__(self:Self, key:int, /)-> Item:
        ...
    @overload
    @setdoc.basic
    def __getitem__(self:Self, key:Slice[int], /)-> Sequence[Item]:
        ...
    @setdoc.basic
    def __getitem__(self:Self, key:int, /)-> Item:
        return self.__fget__()[key]

class HashableSequence[Item](
    Sequence[Item],
    HashableCollection[Item],
):
    __slots__=()
    class Data[DataItem](
        Sequence.Data[DataItem],
        HashableCollection.Data[DataItem],
        Protocol[DataItem],
    ):
        ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...

class MutableSequence[Item](
    Sequence[Item],
    MutableCollection[Item],
    abc.MutableSequence[Item],
):
    __slots__=()
    class Data[DataItem](
        Sequence.Data[DataItem],
        MutableCollection.Data[DataItem],
        Protocol[DataItem],
    ):
        @setdoc.basic
        def __delitem__(self:Self, key:int, /) -> None:
            ...
        @setdoc.basic
        def __setitem__(self:Self, key:int, value:DataItem, /) -> None:
            ...
        @setdoc.basic
        def insert(self: Self, index: int, item: DataItem, /) -> None:
            ...
    @abstractmethod
    @setdoc.basic
    def __fget__(self:Self) -> Data[Item]:
        ...
    @abstractmethod
    @setdoc.basic
    def __fset__(self:Self, data:Data[Item], /) -> None:
        ...

### LIST ###

class List[Item](Sequence[Item]):
    __slots__=()
    @setdoc.basic
    def __add__(self:Self, other:List[Item]) -> List[Item]:
        return type(self)(list(self.__fget__()) + list(other.__fget__()))
    @abstractmethod
    @setdoc.basic
    def __init__(self:Self, data:abc.Iterable[Item], /)-> None:
        ...
    @setdoc.basic
    def __mul__(self:Self, other:SupportsIndex) -> List[Item]:
        return type(self)(list(self.__fget__()) * other)
    @setdoc.basic
    def __rmul__(self:Self, other:SupportsIndex) -> List[Item]:
        return type(self)(other * list(self.__fget__()))

class MutableList[Item](List[Item], MutableCollection[Item]):
    __slots__=()
    @setdoc.basic
    def __imul__(self:Self, other: SupportsIndex, /) -> Self:
        return type(self)(list(self.__fget__()).__imul__(other))
    @setdoc.basic
    def copy(self:Self) -> Self:
        return type(self)(list(self.__fget__()))
    @setdoc.basic
    def sort(self:Self, *, key:Any=None, reverse:bool=False) -> Self:
        return type(self)(list(self.__fget__()))
    # '__imul__', 
    # 'copy', 
    # 'sort',

    