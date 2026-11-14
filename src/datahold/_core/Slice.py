from __future__ import annotations

__all__: list[str] = [
    "Slice",
]


### TYPING ###

type Slice[Index] = slice[Index, Index, Index]
