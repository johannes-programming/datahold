import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.FrozenHoldList import FrozenHoldList
from datahold.core.FrozenHoldSet import FrozenHoldSet
from datahold.core.HoldDict import HoldDict
from datahold.core.HoldList import HoldList
from datahold.core.HoldSet import HoldSet

__all__ = ["TestCopy"]


class TestCopy(unittest.TestCase):
    def test_frozen_have_no_copy(self: Self) -> None:
        self.assertFalse(hasattr(FrozenHoldDict({"a": 1}), "copy"))
        self.assertFalse(hasattr(FrozenHoldList([1, 2]), "copy"))
        self.assertFalse(hasattr(FrozenHoldSet({1, 2}), "copy"))

    def test_frozen_have_no_copy_2(self: Self) -> None:
        """
        Frozen classes should not define their own copy method.
        (If a parent class or wrapped object exposes one, we ignore that.)
        """
        args: Any
        cls: Any
        copy_obj: Any
        obj: Any
        for cls, args in (
            (FrozenHoldDict, ({"a": 1},)),
            (FrozenHoldList, ([1, 2],)),
            (FrozenHoldSet, ({1, 2},)),
        ):
            # They must not *define* copy themselves
            self.assertNotIn("copy", cls.__dict__)

            # Optional: if they *do* expose copy on the instance, it should not
            # create a mutable variant; you can drop this if you prefer.
            obj = cls(*args)
            if hasattr(obj, "copy"):
                copy_obj = obj.copy()
                self.assertIsInstance(copy_obj, cls)

    def test_mutable_copy_returns_same_type_and_is_shallow(self: Self) -> None:
        d: HoldDict
        d_copy: HoldDict
        d = HoldDict({"a": {"x": 1}})
        d_copy = d.copy()
        self.assertIsInstance(d_copy, type(d))
        self.assertIsNot(d_copy, d)
        self.assertEqual(dict(d_copy), dict(d))

        # shallow: inner object is shared
        d["a"]["x"] = 2
        self.assertEqual(d_copy["a"]["x"], 2)

    def test_list_copy(self: Self) -> None:
        lst: HoldList
        lst_copy: HoldList
        lst = HoldList([[1], [2]])
        lst_copy = lst.copy()
        self.assertIsInstance(lst_copy, type(lst))
        self.assertIsNot(lst_copy, lst)
        self.assertEqual(list(lst_copy), list(lst))

        lst[0].append(99)
        self.assertEqual(lst_copy[0], [1, 99])

    def test_set_copy(self: Self) -> None:
        s: HoldSet
        s_copy: HoldSet
        s = HoldSet({1, 2, 3})
        s_copy = s.copy()
        self.assertIsInstance(s_copy, type(s))
        self.assertIsNot(s_copy, s)
        self.assertEqual(set(s_copy), set(s))

        s.add(4)
        self.assertNotIn(4, s_copy)


if __name__ == "__main__":
    unittest.main()
