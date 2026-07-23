__all__: list[str] = [
    "TestCopy",
    "TestDataAttribute",
    "TestHoldList",
    "TestMutableBehavior",
]
import unittest
from typing import Any, Self

from datahold import BaseHoldObject, DataList


class HoldList[Item](
    BaseHoldObject[DataList.Data[Item]],
    DataList[Item],
):
    """Provide usable mutable list-like with slots."""

    __slots__ = ()


class TestCopy(unittest.TestCase):

    def test_list_copy(self: Self) -> None:
        lst: HoldList[Any]
        lst_copy: HoldList[Any]
        lst = HoldList([[1], [2]])
        lst_copy = lst.copy()
        self.assertIsInstance(lst_copy, type(lst))
        self.assertIsNot(lst_copy, lst)
        self.assertEqual(list(lst_copy), list(lst))

        lst[0].append(99)
        self.assertEqual(lst_copy[0], [1, 99])


class TestDataAttribute(unittest.TestCase):
    def test_list_data_is_tuple(self: Self) -> None:
        m: HoldList[Any]
        m = HoldList([1, 2, 3])
        self.assertIsInstance(m.__fget__(), list)


class TestHoldList(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj: HoldList[int]
        self.other: HoldList[int]
        self.same: HoldList[int]
        self.obj = HoldList([1, 2, 3])
        self.same = HoldList([1, 2, 3])
        self.other = HoldList([1, 2, 4])

    # __init__
    def test_init(self: Self) -> None:
        obj: HoldList[int]
        obj = HoldList([42])
        self.assertEqual(obj.__fget__(), [42])

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), list)
        self.assertEqual(self.obj.__fget__(), [1, 2, 3])

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn(2, self.obj)
        self.assertNotIn(999, self.obj)

    # __getitem__
    def test_getitem(self: Self) -> None:
        self.assertEqual(self.obj[0], 1)
        self.assertEqual(self.obj[-1], 3)

    # __setitem__
    def test_setitem(self: Self) -> None:
        self.obj[1] = 99
        self.assertEqual(self.obj[1], 99)

    # __delitem__
    def test_delitem(self: Self) -> None:
        del self.obj[1]
        self.assertEqual(self.obj.__fget__(), [1, 3])

    # __iter__
    def test_iter(self: Self) -> None:
        self.assertEqual(list(iter(self.obj)), [1, 2, 3])

    # __len__
    def test_len(self: Self) -> None:
        self.assertEqual(len(self.obj), 3)

    # __eq__
    def test_eq(self: Self) -> None:
        self.assertEqual(self.obj, self.same)
        self.assertFalse(self.obj == self.other)

    # __ne__
    def test_ne(self: Self) -> None:
        self.assertNotEqual(self.obj, self.other)
        self.assertFalse(self.obj != self.same)

    # __lt__
    def test_lt(self: Self) -> None:
        expected: bool
        expected = self.obj.__fget__() < self.other.__fget__()
        self.assertEqual(self.obj < self.other, expected)

    # __le__
    def test_le(self: Self) -> None:
        expected: bool
        expected = self.obj.__fget__() <= self.same.__fget__()
        self.assertEqual(self.obj <= self.same, expected)

    # __gt__
    def test_gt(self: Self) -> None:
        expected: bool
        expected = self.other.__fget__() > self.obj.__fget__()
        self.assertEqual(self.other > self.obj, expected)

    # __ge__
    def test_ge(self: Self) -> None:
        expected: bool
        expected = self.same.__fget__() >= self.obj.__fget__()
        self.assertEqual(self.same >= self.obj, expected)

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(self.obj),
            "HoldList([1, 2, 3])",
        )

    # append
    def test_append(self: Self) -> None:
        self.obj.append(4)
        self.assertEqual(
            self.obj,
            HoldList([1, 2, 3, 4]),
        )

    # extend
    def test_extend(self: Self) -> None:
        self.obj.extend([4, 5])
        self.assertEqual(
            self.obj,
            HoldList([1, 2, 3, 4, 5]),
        )

    # insert
    def test_insert(self: Self) -> None:
        self.obj.insert(1, 99)
        self.assertEqual(
            self.obj,
            HoldList([1, 99, 2, 3]),
        )

    # remove
    def test_remove(self: Self) -> None:
        self.obj.remove(2)
        self.assertEqual(
            self.obj,
            HoldList([1, 3]),
        )

    # pop
    def test_pop(self: Self) -> None:
        value: Any
        value = self.obj.pop()
        self.assertEqual(value, 3)
        self.assertEqual(
            self.obj,
            HoldList([1, 2]),
        )

    # clear
    def test_clear(self: Self) -> None:
        self.obj.clear()
        self.assertEqual(len(self.obj), 0)

    # index
    def test_index(self: Self) -> None:
        self.assertEqual(
            self.obj.index(2),
            1,
        )

    # count
    def test_count(self: Self) -> None:
        obj: HoldList[int]
        obj = HoldList([1, 2, 2, 3])
        self.assertEqual(
            obj.count(2),
            2,
        )

    # reverse
    def test_reverse(self: Self) -> None:
        self.obj.reverse()
        self.assertEqual(
            self.obj,
            HoldList([3, 2, 1]),
        )

    # sort
    def test_sort(self: Self) -> None:
        obj: HoldList[int]
        obj = HoldList([3, 1, 2])
        obj.sort()
        self.assertEqual(
            obj,
            HoldList([1, 2, 3]),
        )

    # copy
    def test_copy(self: Self) -> None:
        result: HoldList[Any]
        result = self.obj.copy()
        self.assertIsInstance(result, HoldList)
        self.assertEqual(result, self.obj)
        self.assertIsNot(result, self.obj)

    # __add__
    def test_add(self: Self) -> None:
        result: HoldList[int]
        result = HoldList([1, 2]) + HoldList([3, 4])
        self.assertEqual(
            result,
            HoldList([1, 2, 3, 4]),
        )

    # __mul__
    def test_mul(self: Self) -> None:
        result: HoldList[int]
        result = HoldList([1, 2]) * 2
        self.assertEqual(
            result,
            HoldList([1, 2, 1, 2]),
        )

    # __rmul__
    def test_rmul(self: Self) -> None:
        result: HoldList[int]
        result = 2 * HoldList([1, 2])
        self.assertEqual(
            result,
            HoldList([1, 2, 1, 2]),
        )


class TestMutableBehavior(unittest.TestCase):

    def test_hold_list_mutates_and_syncs_data(self: Self) -> None:
        x: HoldList[Any]
        x = HoldList([1, 2])
        x.append(3)
        self.assertEqual(list(x), [1, 2, 3])
        self.assertEqual(x.__fget__(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
