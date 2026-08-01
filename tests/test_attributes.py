from __future__ import annotations

__all__: list[str] = ["TestAttributes"]

import math
import unittest
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestAttributes(unittest.TestCase):
    def _test_attribute(self: Self, name: str, x: str, y: str, /) -> None:
        ancestor: Any
        datatype: Any
        datatype = getattr(datahold, name)
        if y:
            ancestor = Lazy.get_import(y)
            self.assertIs(getattr(datatype, x), getattr(ancestor, x))
        else:
            self.assertFalse(
                hasattr(datatype, x),
                f"{datatype.__name__} has attribute {x}",
            )

    def _test_attributes(self: Self, name: str, /, **kwargs: bool) -> None:
        for x, y in kwargs.items():
            with self.subTest(datatype=name, ancestor=y, attribute=x):
                self._test_attribute(name, x, y)

    def test_attributes(self: Self, /) -> None:
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test_attributes(name, **data["attributes"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
