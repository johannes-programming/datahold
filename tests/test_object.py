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

from iterprod import iterprod


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def METHODS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["METHODS"])

    @cached_property
    def MUTES(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.varia["MUTES"])

    @cached_property
    def ROOTS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.varia["ROOTS"])

    @cached_property
    def SLOTS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.varia["SLOTS"])

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @classmethod
    def get_typemodule(cls: type[Self], typename: str) -> Optional[ModuleType]:
        try:
            return import_module(name=cls.get_typemodulename(typename))
        except ImportError:
            return None

    @classmethod
    def get_typemodulename(cls: type[Self], typename: str) -> str:
        ans: str
        ans = "datahold"
        ans += "."
        for prefix in ("Base", "Frozen"):
            if typename.startswith(prefix):
                ans += prefix.lower()
                break
        else:
            ans += "core"
        ans += "."
        ans += typename
        return ans

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])

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
        mute: str
        root: str
        slot: str
        typemodule: Optional[ModuleType]
        typemodulename: str
        typename: str
        for mute, slot, root in iterprod(
            Lazy.lazy.MUTES, Lazy.lazy.SLOTS, Lazy.lazy.ROOTS
        ):
            typename = mute + slot + root
            typemodulename = Lazy.get_typemodulename(typename)
            typemodule = import_module(name=typemodulename)
            if typemodule is None:
                raise TypeError
            cls = getattr(typemodule, typename)
            self._test_cls(cls)


if __name__ == "__main__":
    unittest.main()
