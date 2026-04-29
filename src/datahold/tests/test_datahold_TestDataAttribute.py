import unittest
from typing import Any, Self

from frozendict import frozendict
from namings import FrozenNaming

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldNaming import FrozenHoldNaming
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldNaming import HoldNaming
from datahold.core.HoldSet import HoldSet

__all__ = ["TestDataAttribute"]


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

    def test_naming_data_is_immutable_mapping(self: Self) -> None:
        f: FrozenHoldNaming
        m: HoldNaming
        obj: Any
        f = FrozenHoldNaming({"a": 1}.items())
        m = HoldNaming({"a": 1}.items())

        for obj in (f, m):
            self.assertIsInstance(obj.data, FrozenNaming)

            # try to mutate underlying data
            with self.assertRaises((TypeError, AttributeError)):
                obj.data["b"] = 2

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
