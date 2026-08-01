from __future__ import annotations

__all__: list[str] = ["TestAll"]

import enum
import tomllib
from functools import cached_property
from importlib import import_module
from typing import Any, Self


class Lazy(enum.Enum):
    """Provide a singleton to store testdata."""

    lazy = enum.auto()

    @cached_property
    def data(self: Self, /) -> dict[str, dict[str, Any]]:
        with open("tests/testdata.toml", "rb") as stream:
            return tomllib.load(stream)

    @cached_property
    def non_datatypes(self: Self, /) -> dict[str, Any]:
        return self.data["non_datatypes"]

    @cached_property
    def datatypes(self: Self, /) -> dict[str, Any]:
        return self.data["datatypes"]

    @classmethod
    def get_import(cls: type[Self], name: str, /) -> Any:
        """Get the import for a given name."""
        modulename = ".".join(name.split(".")[:-1])
        targetname = name.split(".")[-1]
        module = import_module(modulename)
        return getattr(module, targetname)
