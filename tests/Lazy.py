from __future__ import annotations

__all__: list[str] = ["TestAll"]

import enum
import tomllib
from functools import cached_property
from importlib import import_module
from typing import Any, Self

import datahold


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
    def get_abstractmethods(cls: type[Self], name: str, /) -> set[str]:
        # slot
        if name.endswith("Slot"):
            if name.startswith("Frozen"):
                return set()
            elif name.startswith("Mutable"):
                return set()
            else:
                return {"__init__"}
        # like
        if name.endswith("Like"):
            if name.startswith("Mutable"):
                return {"__mutate__"}
            else:
                return {"__frozen__", "__init__"}
        # no suffix
        if name.startswith("Mutable"):
            return {"__frozen__", "__mutate__"}
        else:
            return {"__frozen__"}

    @classmethod
    def get_example(cls: type[Self], typename: str, objname: str) -> Any:
        datatype = getattr(datahold, typename)
        info = cls.lazy.datatypes[typename]["examples"][objname]
        return datatype(*info.get("args", []), **info.get("kwargs", {}))

    @classmethod
    def get_import(cls: type[Self], name: str, /) -> Any:
        """Get the import for a given name."""
        if name == "":
            return None
        modulename = ".".join(name.split(".")[:-1])
        targetname = name.split(".")[-1]
        module = import_module(modulename)
        return getattr(module, targetname)
