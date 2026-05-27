from __future__ import annotations

__all__: list[str] = []
from datahold import MutableListSlot

data: MutableListSlot[int]
data = MutableListSlot([9, 4, 5, 1, 3, 6, 2, 8, 7, 0])
data.sort()
print(data)
