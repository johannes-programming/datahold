from __future__ import annotations

__all__: list[str] = ["TestAll"]

import unittest
from collections import abc
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestAll(unittest.TestCase):
    def _test_sorted(
        self: Self, iterable: abc.Iterable[Any], /, name: str
    ) -> None:
        self.assertListEqual(
            list(iterable),
            list(sorted(iterable)),
            msg=name + " is not sorted",
        )

    def test_sorted(self: Self, /) -> None:
        self._test_sorted(datahold.__all__, name="datahold.__all__")
        self._test_sorted(Lazy.lazy.data, name="testdata.toml")
        self._test_sorted(
            Lazy.lazy.non_datatypes, name="testdata.toml['non_datatypes']"
        )
        self._test_sorted(
            Lazy.lazy.datatypes, name="testdata.toml['datatypes']"
        )
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test_sorted(
                    data["issubclass"],
                    name=f"testdata.toml['datatypes'][{name!r}]['issubclass']",
                )
                self._test_sorted(
                    data["abstractmethods"],
                    name=f"testdata.toml['datatypes'][{name!r}]['abstractmethods']",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
