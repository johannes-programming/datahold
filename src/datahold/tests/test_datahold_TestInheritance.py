import unittest
from typing import Self

from datahold.core.BaseDataDict import BaseDataDict
from datahold.core.BaseDataList import BaseDataList
from datahold.core.BaseDataNaming import BaseDataNaming
from datahold.core.BaseDataSet import BaseDataSet
from datahold.core.BaseHoldDict import BaseHoldDict
from datahold.core.BaseHoldList import BaseHoldList
from datahold.core.BaseHoldNaming import BaseHoldNaming
from datahold.core.BaseHoldSet import BaseHoldSet
from datahold.core.DataDict import DataDict
from datahold.core.DataList import DataList
from datahold.core.DataNaming import DataNaming
from datahold.core.DataObject import DataObject
from datahold.core.DataSet import DataSet
from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenDataList import FrozenDataList
from datahold.core.FrozenDataNaming import FrozenDataNaming
from datahold.core.FrozenDataObject import FrozenDataObject
from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldNaming import FrozenHoldNaming
from datahold.core.FrozenHoldObject import FrozenHoldObject
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldNaming import HoldNaming
from datahold.core.HoldObject import HoldObject
from datahold.core.HoldSet import HoldSet

__all__ = ["TestInheritance"]


class TestInheritance(unittest.TestCase):
    def test_dict_inheritance(self: Self) -> None:
        # base → concrete
        self.assertTrue(issubclass(DataDict, DataObject))
        self.assertTrue(issubclass(FrozenDataDict, FrozenDataObject))
        self.assertTrue(issubclass(HoldDict, HoldObject))
        self.assertTrue(issubclass(FrozenHoldDict, FrozenHoldObject))

        # non-frozen data inherit from frozen
        self.assertTrue(issubclass(DataDict, BaseDataDict))
        self.assertTrue(issubclass(HoldDict, BaseHoldDict))

    def test_list_inheritance(self: Self) -> None:
        self.assertTrue(issubclass(DataList, DataObject))
        self.assertTrue(issubclass(FrozenDataList, FrozenDataObject))
        self.assertTrue(issubclass(HoldList, HoldObject))
        self.assertTrue(issubclass(FrozenHoldList, FrozenHoldObject))

        self.assertTrue(issubclass(DataList, BaseDataList))
        self.assertTrue(issubclass(HoldList, BaseHoldList))

    def test_naming_inheritance(self: Self) -> None:
        # base → concrete
        self.assertTrue(issubclass(DataNaming, DataObject))
        self.assertTrue(issubclass(FrozenDataNaming, FrozenDataObject))
        self.assertTrue(issubclass(HoldNaming, HoldObject))
        self.assertTrue(issubclass(FrozenHoldNaming, FrozenHoldObject))

        # non-frozen data inherit from frozen
        self.assertTrue(issubclass(DataNaming, BaseDataNaming))
        self.assertTrue(issubclass(HoldNaming, BaseHoldNaming))

    def test_set_inheritance(self: Self) -> None:
        self.assertTrue(issubclass(DataSet, DataObject))
        self.assertTrue(issubclass(FrozenDataSet, FrozenDataObject))
        self.assertTrue(issubclass(HoldSet, HoldObject))
        self.assertTrue(issubclass(FrozenHoldSet, FrozenHoldObject))

        self.assertTrue(issubclass(DataSet, BaseDataSet))
        self.assertTrue(issubclass(HoldSet, BaseHoldSet))


if __name__ == "__main__":
    unittest.main()
