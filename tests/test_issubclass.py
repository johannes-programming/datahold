from __future__ import annotations

__all__: list[str] = ["TestIssubclass"]

import unittest
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestIssubclass(unittest.TestCase):
    def _test_issubclass(self: Self, name: str, /, **kwargs: bool) -> None:
        answer: Any
        datatype: Any
        superclass: Any
        x: str
        y: bool
        datatype = getattr(datahold, name)
        for x, y in kwargs.items():
            superclass = Lazy.get_import(x)
            answer = issubclass(datatype, superclass)
            with self.subTest(superclass=x, answer=answer, solution=y):
                self.assertEqual(answer, y)

    def test_issubclass(self: Self, /) -> None:
        data: Any
        name: str
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test_issubclass(name, **data.get("issubclass", {}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
