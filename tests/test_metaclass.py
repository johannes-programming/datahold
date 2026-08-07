from __future__ import annotations

__all__: list[str] = ["TestMetaclass"]

import unittest
from abc import ABCMeta
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestMetaclass(unittest.TestCase):

    def test_metaclass(self: Self, /) -> None:
        datatype: type[Any]
        name: str
        for name in Lazy.lazy.datatypes.keys():
            with self.subTest(datatype=name):
                datatype = getattr(datahold, name)
                self.assertIs(type(datatype), ABCMeta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
