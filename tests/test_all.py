from __future__ import annotations

__all__: list[str] = ["TestAll"]

import unittest
from typing import Self

from Lazy import Lazy

import datahold


class TestAll(unittest.TestCase):
    def test_and(self: Self, /) -> None:
        self.assertFalse(
            Lazy.lazy.non_datatypes.keys() & Lazy.lazy.datatypes.keys()
        )

    def test_len(self: Self, /) -> None:
        self.assertEqual(
            len(datahold.__all__),
            len(set(datahold.__all__)),
        )

    def test_or(self: Self, /) -> None:
        self.assertSetEqual(
            Lazy.lazy.non_datatypes.keys() | Lazy.lazy.datatypes.keys(),
            set(datahold.__all__),
        )

    def test_type(self: Self, /) -> None:
        self.assertIs(type(datahold.__all__), list)
        self.assertFalse({type(x) for x in datahold.__all__} - {str})


if __name__ == "__main__":
    unittest.main(verbosity=2)
