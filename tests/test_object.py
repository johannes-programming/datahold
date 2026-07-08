__all__: list[str] = ["TestObject"]
import enum
import io
import tomllib
import unittest
from functools import cached_property
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Any, Optional, Self, cast


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def METHODS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["METHODS"])

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @classmethod
    def get_module(cls: type[Self], typename: str) -> Optional[ModuleType]:
        for pkgname, prefix in cls.lazy.subpackages.items():
            if typename.startswith(prefix):
                break
        else:
            pkgname = "core"
        try:
            return import_module(f"datahold.{pkgname}.{typename}")
        except ImportError:
            return None

    @classmethod
    def get_type(cls: type[Self], typename: str, /) -> Optional[type[Any]]:
        module: Optional[ModuleType]
        module = cls.get_module(typename=typename)
        if module is None:
            return None
        else:
            return cast(type[Any], getattr(module, typename))

    @cached_property
    def subpackages(self: Self) -> dict[str, str]:
        return cast(dict[str, str], self.varia["subpackages"])

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])

    @cached_property
    def typenames(self: Self) -> list[str]:
        return cast(list[str], self.varia["typenames"])

    @cached_property
    def varia(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["varia"])


class TestObject(unittest.TestCase):
    def _test_cls(self: Self, cls: type) -> None:
        method: Any
        for method in Lazy.lazy.METHODS:
            with self.subTest(cls=cls):
                self.assertIs(getattr(cls, method), getattr(object, method))

    def test_object(self: Self) -> None:
        cls: type[Any]
        typename: str
        for typename in Lazy.lazy.typenames:
            cls = cast(type[Any], Lazy.lazy.get_type(typename))
            self._test_cls(cls)


if __name__ == "__main__":
    unittest.main()
