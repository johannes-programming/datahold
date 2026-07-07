"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]
from typing import Final

from datahold.base.BaseDataCollection import BaseDataCollection

HashableCollection: Final[type[BaseDataCollection.Data]] = BaseDataCollection.Data  # type: ignore[type-abstract, type-arg]
