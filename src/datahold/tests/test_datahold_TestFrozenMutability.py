import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldSet import FrozenHoldSet


class TestFrozenMutability(unittest.TestCase):
    def test_frozen_dict_cannot_mutate(self: Self) -> None:
        f: FrozenHoldDict
        f = FrozenHoldDict({"a": 1})
        with self.assertRaises((TypeError, AttributeError)):
            f["b"] = 2
        with self.assertRaises((TypeError, AttributeError)):
            f.pop("a", None)

    def test_frozen_list_cannot_mutate(self: Self) -> None:
        f: FrozenHoldList
        f = FrozenHoldList([1, 2, 3])
        with self.assertRaises((TypeError, AttributeError)):
            f.append(4)
        with self.assertRaises((TypeError, AttributeError)):
            f.pop()

    def test_frozen_set_cannot_mutate(self: Self) -> None:
        f: FrozenHoldSet
        f = FrozenHoldSet({1, 2, 3})
        with self.assertRaises((TypeError, AttributeError)):
            f.add(4)
        with self.assertRaises((TypeError, AttributeError)):
            f.remove(1)


if __name__ == "__main__":
    unittest.main()
