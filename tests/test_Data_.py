__all__: list[str] = ["Test_Data"]
import enum
import io
import tomllib
import unittest
from functools import cached_property
from importlib import import_module
from pathlib import Path
from types import GenericAlias
from typing import Any, Self, cast


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @cached_property
    def subpackages(self: Self) -> dict[str, str]:
        return cast(dict[str, str], self.varia["subpackages"])

    @cached_property
    def test_Data_(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_Data_"])

    @cached_property
    def typenames(self: Self) -> list[str]:
        return cast(list[str], self.varia["typenames"])

    @cached_property
    def varia(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["varia"])


class Test_Data(unittest.TestCase):
    def test_Data_(self: Self) -> None:
        for typename in Lazy.lazy.typenames:
            self._test_Data_exists(typename)

    def _test_Data_exists(self: Self, typename: str) -> None:
        for pkgname, prefix in Lazy.lazy.subpackages.items():
            if typename.startswith(prefix):
                break
        else:
            pkgname = "core"
        try:
            module = import_module(f"datahold.{pkgname}.{typename}")
        except ImportError:
            return
        cls = getattr(module, typename)
        self.assertIsInstance(
            getattr(cls, "Data"),
            type | GenericAlias,
        )


if __name__ == "__main__":
    unittest.main()
