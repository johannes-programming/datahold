__all__: list[str] = ["TestDataAttribute"]

import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold import (
    FrozenHoldDict,
    FrozenHoldList,
    FrozenHoldSet,
    HoldDict,
    HoldList,
    HoldSet,
)


class TestDataAttribute(unittest.TestCase):
    def test_dict_data_is_immutable_mapping(self: Self) -> None:
        f: FrozenHoldDict[Any, Any]
        m: HoldDict[Any, Any]
        obj: Any
        f = FrozenHoldDict({"a": 1})
        m = HoldDict({"a": 1})

        for obj in (f, m):
            self.assertIsInstance(obj.__fget__(), frozendict)

            # try to mutate underlying data
            with self.assertRaises((TypeError, AttributeError)):
                obj.__fget__()["b"] = 2

    def test_list_data_is_tuple(self: Self) -> None:
        f: FrozenHoldList[Any]
        m: HoldList[Any]
        o: Any
        f = FrozenHoldList([1, 2, 3])
        m = HoldList([1, 2, 3])

        for o in (f, m):
            self.assertIsInstance(o.__fget__(), tuple)
            with self.assertRaises(Exception):
                o.__fget__().append(4)

    def test_set_data_is_frozenset(self: Self) -> None:
        f: FrozenHoldSet[Any]
        m: HoldSet[Any]
        obj: Any
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        for obj in (f, m):
            self.assertIsInstance(obj.__fget__(), frozenset)
            with self.assertRaises(AttributeError):
                obj.__fget__().add(4)


if __name__ == "__main__":
    unittest.main()
