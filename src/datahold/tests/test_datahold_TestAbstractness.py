import unittest
from inspect import isabstract
from typing import Self

from frozendict import frozendict

from datahold.core.DataDict import DataDict
from datahold.core.DataList import DataList
from datahold.core.DataObject import DataObject
from datahold.core.DataSet import DataSet
from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenDataList import FrozenDataList
from datahold.core.FrozenDataObject import FrozenDataObject
from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldObject import FrozenHoldObject
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet

__all__ = ["TestAbstractness"]


class TestAbstractness(unittest.TestCase):
    def test_abstract_classes(self: Self) -> None:
        # data
        self.assertTrue(isabstract(DataObject))
        self.assertTrue(isabstract(DataDict))
        self.assertTrue(isabstract(DataList))
        self.assertTrue(isabstract(DataSet))

        self.assertTrue(isabstract(FrozenDataObject))
        self.assertTrue(isabstract(FrozenDataDict))
        self.assertTrue(isabstract(FrozenDataList))
        self.assertTrue(isabstract(FrozenDataSet))

        # hold
        self.assertFalse(isabstract(FrozenHoldObject))
        # self.assertFalse(isabstract(HoldObject))

    def test_concrete_classes(self: Self) -> None:
        FrozenHoldDict({"a": 1})
        FrozenHoldList([1, 2])
        FrozenHoldSet({1, 2})

        HoldDict({"a": 1})
        HoldList([1, 2])
        HoldSet({1, 2})


if __name__ == "__main__":
    unittest.main()
