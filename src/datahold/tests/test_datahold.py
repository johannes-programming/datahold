import unittest
from collections.abc import (
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
)
from collections.abc import Set as AbstractSet
from inspect import isabstract

from datahold.core.DataBase import DataBase
from datahold.core.DataDict import DataDict
from datahold.core.DataList import DataList
from datahold.core.DataSet import DataSet
from datahold.core.FrozenDataBase import FrozenDataBase
from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenDataList import FrozenDataList
from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldBase import FrozenHoldBase
from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldBase import HoldBase
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet


class TestAbstractness(unittest.TestCase):
    def test_abstract_classes(self):
        # data
        self.assertTrue(isabstract(DataBase))
        self.assertTrue(isabstract(DataDict))
        self.assertTrue(isabstract(DataList))
        self.assertTrue(isabstract(DataSet))

        self.assertTrue(isabstract(FrozenDataBase))
        self.assertTrue(isabstract(FrozenDataDict))
        self.assertTrue(isabstract(FrozenDataList))
        self.assertTrue(isabstract(FrozenDataSet))

        # hold
        self.assertTrue(isabstract(FrozenHoldBase))
        self.assertTrue(isabstract(HoldBase))

    def test_concrete_classes(self):
        FrozenHoldDict({"a": 1})
        FrozenHoldList([1, 2])
        FrozenHoldSet({1, 2})

        HoldDict({"a": 1})
        HoldList([1, 2])
        HoldSet({1, 2})


class TestInheritance(unittest.TestCase):
    def test_dict_inheritance(self):
        # base → concrete
        self.assertTrue(issubclass(DataDict, DataBase))
        self.assertTrue(issubclass(FrozenDataDict, FrozenDataBase))
        self.assertTrue(issubclass(HoldDict, HoldBase))
        self.assertTrue(issubclass(FrozenHoldDict, FrozenHoldBase))

        # non-frozen data inherit from frozen
        self.assertTrue(issubclass(DataDict, FrozenDataDict))
        # hold non-frozen do NOT inherit from frozen
        self.assertFalse(issubclass(HoldDict, FrozenHoldDict))

    def test_list_inheritance(self):
        self.assertTrue(issubclass(DataList, DataBase))
        self.assertTrue(issubclass(FrozenDataList, FrozenDataBase))
        self.assertTrue(issubclass(HoldList, HoldBase))
        self.assertTrue(issubclass(FrozenHoldList, FrozenHoldBase))

        self.assertTrue(issubclass(DataList, FrozenDataList))
        self.assertFalse(issubclass(HoldList, FrozenHoldList))

    def test_set_inheritance(self):
        self.assertTrue(issubclass(DataSet, DataBase))
        self.assertTrue(issubclass(FrozenDataSet, FrozenDataBase))
        self.assertTrue(issubclass(HoldSet, HoldBase))
        self.assertTrue(issubclass(FrozenHoldSet, FrozenHoldBase))

        self.assertTrue(issubclass(DataSet, FrozenDataSet))
        self.assertFalse(issubclass(HoldSet, FrozenHoldSet))


class TestProtocols(unittest.TestCase):
    def test_mapping_protocols(self):
        f = FrozenHoldDict({"a": 1})
        m = HoldDict({"a": 1})

        self.assertIsInstance(f, Mapping)
        self.assertNotIsInstance(f, MutableMapping)

        self.assertIsInstance(m, Mapping)
        self.assertIsInstance(m, MutableMapping)

    def test_sequence_protocols(self):
        f = FrozenHoldList([1, 2, 3])
        m = HoldList([1, 2, 3])

        self.assertIsInstance(f, Sequence)
        self.assertNotIsInstance(f, MutableSequence)

        self.assertIsInstance(m, Sequence)
        self.assertIsInstance(m, MutableSequence)

    def test_set_protocols(self):
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        self.assertIsInstance(f, AbstractSet)
        self.assertNotIsInstance(f, MutableSet)

        self.assertIsInstance(m, AbstractSet)
        self.assertIsInstance(m, MutableSet)


class TestDataAttribute(unittest.TestCase):
    def test_dict_data_is_immutable_mapping(self):
        f = FrozenHoldDict({"a": 1})
        m = HoldDict({"a": 1})

        for obj in (f, m):
            self.assertIsInstance(obj.data, Mapping)
            self.assertNotIsInstance(obj.data, dict)

            # try to mutate underlying data
            with self.assertRaises((TypeError, AttributeError)):
                obj.data["b"] = 2

    def test_list_data_is_tuple(self):
        f = FrozenHoldList([1, 2, 3])
        m = HoldList([1, 2, 3])

        for obj in (f, m):
            self.assertIsInstance(obj.data, tuple)
            with self.assertRaises(TypeError):
                obj.data.append(4)

    def test_set_data_is_frozenset(self):
        f = FrozenHoldSet({1, 2, 3})
        m = HoldSet({1, 2, 3})

        for obj in (f, m):
            self.assertIsInstance(obj.data, frozenset)
            with self.assertRaises(AttributeError):
                obj.data.add(4)


class TestFrozenMutability(unittest.TestCase):
    def test_frozen_dict_cannot_mutate(self):
        f = FrozenHoldDict({"a": 1})
        with self.assertRaises((TypeError, AttributeError)):
            f["b"] = 2
        with self.assertRaises((TypeError, AttributeError)):
            f.pop("a", None)

    def test_frozen_list_cannot_mutate(self):
        f = FrozenHoldList([1, 2, 3])
        with self.assertRaises((TypeError, AttributeError)):
            f.append(4)
        with self.assertRaises((TypeError, AttributeError)):
            f.pop()

    def test_frozen_set_cannot_mutate(self):
        f = FrozenHoldSet({1, 2, 3})
        with self.assertRaises((TypeError, AttributeError)):
            f.add(4)
        with self.assertRaises((TypeError, AttributeError)):
            f.remove(1)


class TestMutableBehavior(unittest.TestCase):
    def test_hold_dict_mutates_and_syncs_data(self):
        d = HoldDict({"a": 1})
        d["b"] = 2
        self.assertEqual(d["b"], 2)
        self.assertEqual(d.data["b"], 2)

    def test_hold_list_mutates_and_syncs_data(self):
        lst = HoldList([1, 2])
        lst.append(3)
        self.assertEqual(list(lst), [1, 2, 3])
        self.assertEqual(lst.data, (1, 2, 3))

    def test_hold_set_mutates_and_syncs_data(self):
        s = HoldSet({1, 2})
        s.add(3)
        self.assertTrue(3 in s)
        self.assertTrue(3 in s.data)


class TestCopy(unittest.TestCase):
    def test_frozen_have_no_copy(self):
        self.assertFalse(hasattr(FrozenHoldDict({"a": 1}), "copy"))
        self.assertFalse(hasattr(FrozenHoldList([1, 2]), "copy"))
        self.assertFalse(hasattr(FrozenHoldSet({1, 2}), "copy"))

    def test_mutable_copy_returns_same_type_and_is_shallow(self):
        d = HoldDict({"a": {"x": 1}})
        d_copy = d.copy()
        self.assertIsInstance(d_copy, type(d))
        self.assertIsNot(d_copy, d)
        self.assertEqual(dict(d_copy), dict(d))

        # shallow: inner object is shared
        d["a"]["x"] = 2
        self.assertEqual(d_copy["a"]["x"], 2)

    def test_list_copy(self):
        lst = HoldList([[1], [2]])
        lst_copy = lst.copy()
        self.assertIsInstance(lst_copy, type(lst))
        self.assertIsNot(lst_copy, lst)
        self.assertEqual(list(lst_copy), list(lst))

        lst[0].append(99)
        self.assertEqual(lst_copy[0], [1, 99])

    def test_set_copy(self):
        s = HoldSet({1, 2, 3})
        s_copy = s.copy()
        self.assertIsInstance(s_copy, type(s))
        self.assertIsNot(s_copy, s)
        self.assertEqual(set(s_copy), set(s))

        s.add(4)
        self.assertNotIn(4, s_copy)


if __name__ == "__main__":
    unittest.main()
