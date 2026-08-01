from __future__ import annotations

__all__: list[str] = ["TestAll"]

import unittest
from collections import abc
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestAll(unittest.TestCase):
    def _test_sorted(self: Self, iterable: abc.Iterable[Any], /) -> None:
        self.assertListEqual(
            list(iterable),
            list(sorted(iterable)),
        )

    def test_sorted(self: Self, /) -> None:
        self._test_sorted(datahold.__all__)
        self._test_sorted(Lazy.lazy.data)
        self._test_sorted(Lazy.lazy.non_datatypes)
        self._test_sorted(Lazy.lazy.datatypes)
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test_sorted(data["issubclass"])
                self._test_sorted(data["abstractmethods"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
