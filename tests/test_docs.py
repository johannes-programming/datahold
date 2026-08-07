from __future__ import annotations

__all__: list[str] = ["TestDocs"]

import unittest
from types import MemberDescriptorType
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestDocs(unittest.TestCase):
    def _test_datatype(self: Self, datatype: type[Any], /) -> None:
        doc: Any
        x: Any
        y: Any
        self.assertIsNotNone(
            datatype.__doc__, f"{datatype.__name__}.__doc__ is None"
        )
        for x, y in datatype.__dict__.items():
            if y is None:
                continue
            if isinstance(y, MemberDescriptorType):
                continue
            doc = getattr(y, "__doc__", "")
            self.assertIsNotNone(
                doc, f"{datatype.__name__}.{x}.__doc__ is None ({type(y)})"
            )

    def test_datatypes(self: Self, /) -> None:
        name: str
        for name in Lazy.lazy.datatypes:
            with self.subTest(datatype=name):
                self._test_datatype(getattr(datahold, name))

    def test_module(self: Self, /) -> None:
        self.assertIsNotNone(datahold.__doc__, "datahold.__doc__ is None")


if __name__ == "__main__":
    unittest.main(verbosity=2)
