__all__: list[str] = []

from datahold import FrozenHoldList, BaseDataList
from typing import Any

def search_mro(cls_:type[Any], /, name:str) -> None:
    print("find %r from %s" % (name, cls_))
    for cls in cls_.__mro__:
        if name in cls.__dict__:
            print(f"{cls.__name__}: {cls.__dict__[name]!r}")
    print()

print("FrozenHoldList.__mro__", FrozenHoldList.__mro__)
print("FrozenHoldList.__hash__", FrozenHoldList.__hash__)

search_mro(FrozenHoldList, "__hash__")
search_mro(BaseDataList, "__hash__")
