"""Provide HashableSized."""

__all__: list[str] = ["HashableSized"]

from collections.abc import Sized
from typing import Protocol, Self

import setdoc



class HashableSized(Sized, Protocol):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
