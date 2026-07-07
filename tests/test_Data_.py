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
    def test_Data_(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_Data_"])


class Test_Data(unittest.TestCase):
    def test_Data_(self: Self) -> None:
        for name in Lazy.lazy.test_Data_["names"]:
            module = import_module(f"datahold.base.{name}")
            cls = getattr(module, name)
            self.assertIsInstance(
                getattr(cls, "Data"),
                type | GenericAlias,
            )


if __name__ == "__main__":
    unittest.main()
