import unittest
from collections.abc import (
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
)
from collections.abc import Set as AbstractSet
from typing import Self

from frozendict import frozendict

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet

__all__ = ["TestProtocols"]


class TestProtocols(unittest.TestCase):
    def test_mapping_protocols_x(self: Self) -> None:
        x: FrozenHoldDict
        x = FrozenHoldDict({"a": 1})

        self.assertIsInstance(x, Mapping)
        self.assertNotIsInstance(x, MutableMapping)

    def test_mapping_protocols_y(self: Self) -> None:
        y: HoldDict
        y = HoldDict({"a": 1})

        self.assertIsInstance(y, Mapping)
        self.assertIsInstance(y, MutableMapping)

    def test_sequence_protocols_x(self: Self) -> None:
        f: FrozenHoldList
        f = FrozenHoldList([1, 2, 3])

        self.assertIsInstance(f, Sequence)
        self.assertNotIsInstance(f, MutableSequence)

    def test_sequence_protocols_y(self: Self) -> None:
        m: HoldList
        m = HoldList([1, 2, 3])
        self.assertIsInstance(m, Sequence)
        self.assertIsInstance(m, MutableSequence)

    def test_set_protocols(self: Self) -> None:
        f: FrozenHoldSet
        m: HoldSet
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        self.assertIsInstance(f, AbstractSet)
        self.assertNotIsInstance(f, MutableSet)

        self.assertIsInstance(m, AbstractSet)
        self.assertIsInstance(m, MutableSet)


if __name__ == "__main__":
    unittest.main()
