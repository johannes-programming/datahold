import unittest
from collections.abc import (
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    Set,
)
from typing import Any, Self

from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet
from datahold.frozen.FrozenHoldDict import FrozenHoldDict
from datahold.frozen.FrozenHoldList import FrozenHoldList
from datahold.frozen.FrozenHoldSet import FrozenHoldSet

__all__ = ["TestProtocols"]


class TestProtocols(unittest.TestCase):
    def test_mapping_protocols_x(self: Self) -> None:
        x: FrozenHoldDict[Any, Any]
        x = FrozenHoldDict({"a": 1})

        self.assertIsInstance(x, Mapping)
        self.assertNotIsInstance(x, MutableMapping)

    def test_mapping_protocols_y(self: Self) -> None:
        y: HoldDict[Any, Any]
        y = HoldDict({"a": 1})

        self.assertIsInstance(y, Mapping)
        self.assertIsInstance(y, MutableMapping)

    def test_sequence_protocols_x(self: Self) -> None:
        f: FrozenHoldList[Any]
        f = FrozenHoldList([1, 2, 3])

        self.assertIsInstance(f, Sequence)
        self.assertNotIsInstance(f, MutableSequence)

    def test_sequence_protocols_y(self: Self) -> None:
        m: HoldList[Any]
        m = HoldList([1, 2, 3])
        self.assertIsInstance(m, Sequence)
        self.assertIsInstance(m, MutableSequence)

    def test_set_protocols(self: Self) -> None:
        f: FrozenHoldSet[Any]
        m: HoldSet[Any]
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        self.assertIsInstance(f, Set)
        self.assertNotIsInstance(f, MutableSet)

        self.assertIsInstance(m, Set)
        self.assertIsInstance(m, MutableSet)


if __name__ == "__main__":
    unittest.main()
