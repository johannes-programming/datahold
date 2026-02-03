import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet


class TestMutableBehavior(unittest.TestCase):
    def test_hold_dict_mutates_and_syncs_data(self: Self) -> None:
        x: HoldDict
        x = HoldDict({"a": 1})
        x["b"] = 2
        self.assertEqual(x["b"], 2)
        self.assertEqual(x.data["b"], 2)

    def test_hold_list_mutates_and_syncs_data(self: Self) -> None:
        x: HoldList
        x = HoldList([1, 2])
        x.append(3)
        self.assertEqual(list(x), [1, 2, 3])
        self.assertEqual(x.data, (1, 2, 3))

    def test_hold_set_mutates_and_syncs_data(self: Self) -> None:
        s: HoldSet
        s = HoldSet({1, 2})
        s.add(3)
        self.assertTrue(3 in s)
        self.assertTrue(3 in s.data)


if __name__ == "__main__":
    unittest.main()
