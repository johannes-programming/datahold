import unittest
from typing import Self

from datahold import MutableListSlot

__all__: list[str] = [
    "TestMethodAppend",
    "TestMethodClear",
    "TestMethodCopy",
    "TestMethodCount",
    "TestMethodExtend",
    "TestMethodIndex",
    "TestMethodInsert",
    "TestMethodPop",
    "TestMethodRemove",
    "TestMethodReverse",
    "TestMethodSort",
    "TestOperatorAdd",
    "TestOperatorIAdd",
    "TestOperatorMul",
    "TestOperatorRMul",
    "TestOperatorIMul",
    "TestOperatorEqual",
    "TestOperatorNotEqual",
    "TestOperatorLessThan",
    "TestOperatorLessThanOrEqual",
    "TestOperatorGreaterThan",
    "TestOperatorGreaterThanOrEqual",
    "TestOperatorContains",
    "TestOperatorGetItem",
    "TestOperatorSetItem",
    "TestOperatorDelItem",
]


class TestMethodAppend(unittest.TestCase):
    def test_append_to_empty(self: Self, /) -> None:
        value: MutableListSlot[int]
        value = MutableListSlot()
        value.append(1)
        self.assertEqual(list(value), [1])

    def test_append_to_nonempty(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value.append(3)
        self.assertEqual(list(value), [1, 2, 3])

    def test_append_object(self: Self, /) -> None:
        value: MutableListSlot[dict[str, int]]
        obj = {"a": 1}
        value = MutableListSlot()
        value.append(obj)
        self.assertIs(value[0], obj)

    def test_append_returns_none(self: Self, /) -> None:
        value: MutableListSlot[int]
        value = MutableListSlot()
        self.assertIsNone(value.append(1))  # type: ignore[func-returns-value]


class TestMethodClear(unittest.TestCase):
    def test_clear_nonempty(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value.clear()
        self.assertEqual(list(value), [])

    def test_clear_empty(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot()
        value.clear()
        self.assertEqual(list(value), [])

    def test_clear_mixed_values(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot([1, "a", None, []])
        value.clear()
        self.assertEqual(list(value), [])

    def test_clear_returns_none(self: Self, /) -> None:
        value = MutableListSlot([1])
        self.assertIsNone(value.clear())  # type: ignore[func-returns-value]


class TestMethodCopy(unittest.TestCase):
    def test_copy_has_same_contents(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        copied = value.copy()
        self.assertEqual(copied, value)

    def test_copy_is_distinct_object(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        copied = value.copy()
        self.assertIsNot(copied, value)

    def test_copy_is_shallow(self: Self, /) -> None:
        nested: list[object]
        nested = []
        value = MutableListSlot([nested])
        copied = value.copy()
        self.assertIs(copied[0], nested)

    def test_copy_empty(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot()
        copied = value.copy()
        self.assertEqual(list(copied), [])


class TestMethodCount(unittest.TestCase):
    def test_count_existing_once(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        self.assertEqual(value.count(2), 1)

    def test_count_existing_multiple_times(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 1, 1])
        self.assertEqual(value.count(1), 3)

    def test_count_missing(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        self.assertEqual(value.count(4), 0)

    def test_count_empty(self: Self, /) -> None:
        value: MutableListSlot[int] = MutableListSlot()
        self.assertEqual(value.count(1), 0)


class TestMethodExtend(unittest.TestCase):
    def test_extend_with_list(self: Self, /) -> None:
        value = MutableListSlot([1])
        value.extend([2, 3])
        self.assertEqual(list(value), [1, 2, 3])

    def test_extend_empty(self: Self, /) -> None:
        value = MutableListSlot([1])
        value.extend([])
        self.assertEqual(list(value), [1])

    def test_extend_with_tuple(self: Self, /) -> None:
        value = MutableListSlot([1])
        value.extend((2, 3))
        self.assertEqual(list(value), [1, 2, 3])

    def test_extend_returns_none(self: Self, /) -> None:
        value: MutableListSlot[int] = MutableListSlot()
        self.assertIsNone(value.extend([1, 2]))  # type: ignore[func-returns-value]


class TestMethodIndex(unittest.TestCase):
    def test_index_existing(self: Self, /) -> None:
        value = MutableListSlot(["a", "b", "c"])
        self.assertEqual(value.index("b"), 1)

    def test_index_returns_first_match(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 1])
        self.assertEqual(value.index(1), 0)

    def test_index_with_start(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 1])
        self.assertEqual(value.index(1, 1), 2)

    def test_index_missing_raises_value_error(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        with self.assertRaises(ValueError):
            value.index(4)


class TestMethodInsert(unittest.TestCase):
    def test_insert_at_start(self: Self, /) -> None:
        value = MutableListSlot([2, 3])
        value.insert(0, 1)
        self.assertEqual(list(value), [1, 2, 3])

    def test_insert_in_middle(self: Self, /) -> None:
        value = MutableListSlot([1, 3])
        value.insert(1, 2)
        self.assertEqual(list(value), [1, 2, 3])

    def test_insert_past_end(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value.insert(100, 3)
        self.assertEqual(list(value), [1, 2, 3])

    def test_insert_returns_none(self: Self, /) -> None:
        value: MutableListSlot[int]
        value = MutableListSlot()
        self.assertIsNone(value.insert(0, 1))  # type: ignore[func-returns-value]


class TestMethodPop(unittest.TestCase):
    def test_pop_last(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        result = value.pop()
        self.assertEqual(result, 3)
        self.assertEqual(list(value), [1, 2])

    def test_pop_first(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        result = value.pop(0)
        self.assertEqual(result, 1)
        self.assertEqual(list(value), [2, 3])

    def test_pop_negative_index(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        result = value.pop(-2)
        self.assertEqual(result, 2)
        self.assertEqual(list(value), [1, 3])

    def test_pop_empty_raises_index_error(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        with self.assertRaises(IndexError):
            value.pop()


class TestMethodRemove(unittest.TestCase):
    def test_remove_existing(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value.remove(2)
        self.assertEqual(list(value), [1, 3])

    def test_remove_only_first_match(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 1])
        value.remove(1)
        self.assertEqual(list(value), [2, 1])

    def test_remove_missing_raises_value_error(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        with self.assertRaises(ValueError):
            value.remove(4)

    def test_remove_returns_none(self: Self, /) -> None:
        value = MutableListSlot([1])
        self.assertIsNone(value.remove(1))  # type: ignore[func-returns-value]


class TestMethodReverse(unittest.TestCase):
    def test_reverse_multiple_items(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value.reverse()
        self.assertEqual(list(value), [3, 2, 1])

    def test_reverse_single_item(self: Self, /) -> None:
        value = MutableListSlot([1])
        value.reverse()
        self.assertEqual(list(value), [1])

    def test_reverse_empty(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        value.reverse()
        self.assertEqual(list(value), [])

    def test_reverse_returns_none(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        self.assertIsNone(value.reverse())  # type: ignore[func-returns-value]


class TestMethodSort(unittest.TestCase):
    def test_sort_ascending(self: Self, /) -> None:
        value = MutableListSlot([3, 1, 2])
        value.sort()
        self.assertEqual(list(value), [1, 2, 3])

    def test_sort_reverse(self: Self, /) -> None:
        value = MutableListSlot([1, 3, 2])
        value.sort(reverse=True)
        self.assertEqual(list(value), [3, 2, 1])

    def test_sort_with_key(self: Self, /) -> None:
        value = MutableListSlot(["bbb", "a", "cc"])
        value.sort(key=len)
        self.assertEqual(list(value), ["a", "cc", "bbb"])

    def test_sort_returns_none(self: Self, /) -> None:
        value = MutableListSlot([2, 1])
        self.assertIsNone(value.sort())


class TestOperatorAdd(unittest.TestCase):
    def test_add_two_nonempty_lists(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) + MutableListSlot([3, 4])
        self.assertEqual(list(result), [1, 2, 3, 4])

    def test_add_empty_list(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) + MutableListSlot([])
        self.assertEqual(list(result), [1, 2])

    def test_add_to_empty_slot(self: Self, /) -> None:
        result = MutableListSlot([]) + MutableListSlot([1, 2])
        self.assertEqual(list(result), [1, 2])

    def test_add_does_not_modify_original(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value + MutableListSlot([3])
        self.assertEqual(list(value), [1, 2])


class TestOperatorIAdd(unittest.TestCase):
    def test_iadd_nonempty_list(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value += [3, 4]
        self.assertEqual(list(value), [1, 2, 3, 4])

    def test_iadd_empty_list(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value += ""  # type: ignore[arg-type]
        self.assertEqual(list(value), [1, 2])

    def test_iadd_to_empty_slot(self: Self, /) -> None:
        value: MutableListSlot[int] = MutableListSlot([])
        value += (1, 2)
        self.assertEqual(list(value), [1, 2])

    def test_iadd_multiple_times(self: Self, /) -> None:
        value = MutableListSlot([1])
        value += [2]
        value += [3]
        self.assertEqual(list(value), [1, 2, 3])


class TestOperatorMul(unittest.TestCase):
    def test_multiply_by_positive_integer(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) * 3
        self.assertEqual(list(result), [1, 2, 1, 2, 1, 2])

    def test_multiply_by_one(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) * 1
        self.assertEqual(list(result), [1, 2])

    def test_multiply_by_zero(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) * 0
        self.assertEqual(list(result), [])

    def test_multiply_by_negative_integer(self: Self, /) -> None:
        result = MutableListSlot([1, 2]) * -2
        self.assertEqual(list(result), [])


class TestOperatorRMul(unittest.TestCase):
    def test_rmul_by_positive_integer(self: Self, /) -> None:
        result = 3 * MutableListSlot([1, 2])
        self.assertEqual(list(result), [1, 2, 1, 2, 1, 2])

    def test_rmul_by_one(self: Self, /) -> None:
        result = 1 * MutableListSlot([1, 2])
        self.assertEqual(list(result), [1, 2])

    def test_rmul_by_zero(self: Self, /) -> None:
        result = 0 * MutableListSlot([1, 2])
        self.assertEqual(list(result), [])

    def test_rmul_by_negative_integer(self: Self, /) -> None:
        result = -3 * MutableListSlot([1, 2])
        self.assertEqual(list(result), [])


class TestOperatorIMul(unittest.TestCase):
    def test_imul_by_positive_integer(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value *= 2
        self.assertEqual(list(value), [1, 2, 1, 2])

    def test_imul_by_one(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value *= 1
        self.assertEqual(list(value), [1, 2])

    def test_imul_by_zero(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value *= 0
        self.assertEqual(list(value), [])

    def test_imul_by_negative_integer(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        value *= -1
        self.assertEqual(list(value), [])


class TestOperatorEqual(unittest.TestCase):
    def test_equal_same_contents(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) == MutableListSlot([1, 2]))

    def test_equal_empty_lists(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([]) == MutableListSlot([]))

    def test_not_equal_different_values(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1, 2]) == MutableListSlot([1, 3]))

    def test_not_equal_different_lengths(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1, 2]) == MutableListSlot([1, 2, 3]))


class TestOperatorNotEqual(unittest.TestCase):
    def test_not_equal_different_contents(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) != MutableListSlot([1, 3]))

    def test_not_equal_different_lengths(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1]) != MutableListSlot([1, 2]))

    def test_equal_values_are_not_unequal(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1, 2]) != MutableListSlot([1, 2]))

    def test_empty_values_are_not_unequal(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([]) != MutableListSlot([]))


class TestOperatorLessThan(unittest.TestCase):
    def test_less_than_by_first_element(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 9]) < MutableListSlot([2, 0]))

    def test_less_than_by_later_element(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) < MutableListSlot([1, 3]))

    def test_prefix_is_less_than_longer_list(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) < MutableListSlot([1, 2, 3]))

    def test_equal_list_is_not_less_than(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1, 2]) < MutableListSlot([1, 2]))


class TestOperatorLessThanOrEqual(unittest.TestCase):
    def test_less_value_is_less_or_equal(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1]) <= MutableListSlot([2]))

    def test_equal_value_is_less_or_equal(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) <= MutableListSlot([1, 2]))

    def test_prefix_is_less_or_equal(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1]) <= MutableListSlot([1, 2]))

    def test_greater_value_is_not_less_or_equal(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([2]) <= MutableListSlot([1]))


class TestOperatorGreaterThan(unittest.TestCase):
    def test_greater_than_by_first_element(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([2, 0]) > MutableListSlot([1, 9]))

    def test_greater_than_by_later_element(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 3]) > MutableListSlot([1, 2]))

    def test_longer_list_is_greater_than_prefix(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2, 3]) > MutableListSlot([1, 2]))

    def test_equal_list_is_not_greater_than(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1, 2]) > MutableListSlot([1, 2]))


class TestOperatorGreaterThanOrEqual(unittest.TestCase):
    def test_greater_value_is_greater_or_equal(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([2]) >= MutableListSlot([1]))

    def test_equal_value_is_greater_or_equal(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) >= MutableListSlot([1, 2]))

    def test_longer_list_is_greater_or_equal_to_prefix(self: Self, /) -> None:
        self.assertTrue(MutableListSlot([1, 2]) >= MutableListSlot([1]))

    def test_smaller_value_is_not_greater_or_equal(self: Self, /) -> None:
        self.assertFalse(MutableListSlot([1]) >= MutableListSlot([2]))


class TestOperatorContains(unittest.TestCase):
    def test_contains_first_element(self: Self, /) -> None:
        self.assertTrue(1 in MutableListSlot([1, 2, 3]))

    def test_contains_last_element(self: Self, /) -> None:
        self.assertTrue(3 in MutableListSlot([1, 2, 3]))

    def test_does_not_contain_missing_element(self: Self, /) -> None:
        self.assertFalse(4 in MutableListSlot([1, 2, 3]))

    def test_empty_slot_contains_nothing(self: Self, /) -> None:
        self.assertFalse(1 in MutableListSlot([]))


class TestOperatorGetItem(unittest.TestCase):
    def test_get_first_item(self: Self, /) -> None:
        value = MutableListSlot([10, 20, 30])
        self.assertEqual(value[0], 10)

    def test_get_last_item_with_negative_index(self: Self, /) -> None:
        value = MutableListSlot([10, 20, 30])
        self.assertEqual(value[-1], 30)

    def test_get_slice(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3, 4])
        self.assertEqual(value[1:3], MutableListSlot([2, 3]))

    def test_out_of_range_index_raises(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        with self.assertRaises(IndexError):
            value[5]


class TestOperatorSetItem(unittest.TestCase):
    def test_set_first_item(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value[0] = 10
        self.assertEqual(list(value), [10, 2, 3])

    def test_set_last_item_with_negative_index(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value[-1] = 10
        self.assertEqual(list(value), [1, 2, 10])

    def test_set_slice_same_length(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3, 4])
        value[1:3] = [20, 30]
        self.assertEqual(list(value), [1, 20, 30, 4])

    def test_set_slice_different_length(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        value[1:2] = [10, 20, 30]
        self.assertEqual(list(value), [1, 10, 20, 30, 3])


class TestOperatorDelItem(unittest.TestCase):
    def test_delete_first_item(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        del value[0]
        self.assertEqual(list(value), [2, 3])

    def test_delete_last_item(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3])
        del value[-1]
        self.assertEqual(list(value), [1, 2])

    def test_delete_slice(self: Self, /) -> None:
        value = MutableListSlot([1, 2, 3, 4])
        del value[1:3]
        self.assertEqual(list(value), [1, 4])

    def test_delete_out_of_range_raises(self: Self, /) -> None:
        value = MutableListSlot([1, 2])
        with self.assertRaises(IndexError):
            del value[5]


if __name__ == "__main__":
    unittest.main()
