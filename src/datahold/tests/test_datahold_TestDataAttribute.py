import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold.frozen.FrozenHoldDict import FrozenHoldDict
from datahold.frozen.FrozenHoldList import FrozenHoldList
from datahold.frozen.FrozenHoldSet import FrozenHoldSet
from datahold.unfrozen.HoldDict import HoldDict
from datahold.unfrozen.HoldList import HoldList
from datahold.unfrozen.HoldSet import HoldSet


class TestDataAttribute(unittest.TestCase):
    def test_dict_data_is_immutable_mapping(self: Self) -> None:
        f: FrozenHoldDict
        m: HoldDict
        obj: Any
        f = FrozenHoldDict({"a": 1})
        m = HoldDict({"a": 1})

        for obj in (f, m):
            self.assertIsInstance(obj.data, frozendict)

            # try to mutate underlying data
            with self.assertRaises((TypeError, AttributeError)):
                obj.data["b"] = 2

    def test_list_data_is_tuple(self: Self) -> None:
        f: FrozenHoldList
        m: HoldList
        o: Any
        f = FrozenHoldList([1, 2, 3])
        m = HoldList([1, 2, 3])

        for o in (f, m):
            self.assertIsInstance(o.data, tuple)
            with self.assertRaises(Exception):
                o.data.append(4)

    def test_set_data_is_frozenset(self: Self) -> None:
        f: FrozenHoldSet
        m: HoldSet
        obj: Any
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        for obj in (f, m):
            self.assertIsInstance(obj.data, frozenset)
            with self.assertRaises(AttributeError):
                obj.data.add(4)


if __name__ == "__main__":
    unittest.main()
