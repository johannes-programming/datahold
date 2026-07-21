__all__: list[str] = []

from datahold import FrozenHoldList

print("FrozenHoldList.__mro__", FrozenHoldList.__mro__)
print("FrozenHoldList.__hash__", FrozenHoldList.__hash__)

for cls in FrozenHoldList.__mro__:
    if "__hash__" in cls.__dict__:
        print(f"{cls.__name__}: {cls.__dict__['__hash__']!r}")
