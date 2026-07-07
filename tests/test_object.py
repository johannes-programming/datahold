__all__: list[str] = ["TestObject"]
import enum
import io
import tomllib
import unittest
from functools import cached_property
from importlib import import_module
from pathlib import Path
from typing import Any, Self, cast

from iterprod import iterprod


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def METHODS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["METHODS"])

    @cached_property
    def MUTES(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["MUTES"])

    @cached_property
    def ROOTS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["ROOTS"])

    @cached_property
    def SLOTS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["SLOTS"])

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])


class TestObject(unittest.TestCase):
    def _test_cls(self: Self, cls: type) -> None:
        method: Any
        for method in Lazy.lazy.METHODS:
            with self.subTest(cls=cls):
                self.assertIs(getattr(cls, method), getattr(object, method))

    def test_object(self: Self) -> None:
        cls: type
        clsname: str
        importname: str
        mute: str
        root: str
        slot: str
        for mute, slot, root in iterprod(
            Lazy.lazy.MUTES, Lazy.lazy.SLOTS, Lazy.lazy.ROOTS
        ):
            clsname = mute + slot + root
            importname = "datahold."
            if mute:
                importname += mute.lower()
            else:
                importname += "core"
            importname += "." + clsname
            cls = getattr(import_module(name=importname), clsname)
            self._test_cls(cls)


if __name__ == "__main__":
    unittest.main()
