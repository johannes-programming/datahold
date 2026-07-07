"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]
from typing import Final

from datahold.base.BaseDataCollection import Data

HashableCollection: Final[type[Data]] = Data  # type: ignore[type-abstract, type-arg]
