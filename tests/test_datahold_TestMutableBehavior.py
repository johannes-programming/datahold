__all__: list[str] = ["TestMutableBehavior"]

import unittest
from typing import Any, Self

from datahold import HoldDict, HoldList, HoldSet


class TestMutableBehavior(unittest.TestCase):
    def test_hold_dict_mutates_and_syncs_data(self: Self) -> None:
        x: HoldDict[Any, Any]
        x = HoldDict({"a": 1})
        x["b"] = 2
        self.assertEqual(x["b"], 2)
        self.assertEqual(x.__fget__()["b"], 2)

    def test_hold_list_mutates_and_syncs_data(self: Self) -> None:
        x: HoldList[Any]
        x = HoldList([1, 2])
        x.append(3)
        self.assertEqual(list(x), [1, 2, 3])
        self.assertEqual(x.__fget__(), [1, 2, 3])

    def test_hold_set_mutates_and_syncs_data(self: Self) -> None:
        s: HoldSet[Any]
        s = HoldSet({1, 2})
        s.add(3)
        self.assertTrue(3 in s)
        self.assertTrue(3 in s.__fget__())


if __name__ == "__main__":
    unittest.main()
