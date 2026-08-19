import unittest
from typing import Any, Self

from datahold import MutableListSlot

__all__: list[str] = []


def init() -> None:
    update: dict[str, type[unittest.TestCase]]
    update = dict()
    for x, y in make_test_cases(list).items():
        y.__qualname__ = y.__name__ = x + "List"
        update[y.__name__] = y
    for x, y in make_test_cases(MutableListSlot).items():
        y.__qualname__ = y.__name__ = x + "MutableListSlot"
        update[y.__name__] = y
    update = dict(sorted(update.items()))
    globals().update(update)
    __all__.extend(update)
    __all__.sort()


def make_test_cases(TYPE: type[Any]) -> dict[str, type[unittest.TestCase]]:

    class TestMethodAppend(unittest.TestCase):
        def test_append_to_empty(self: Self, /) -> None:
            value = TYPE()
            value.append(1)
            self.assertEqual(tuple(value), (1,))

        def test_append_to_nonempty(self: Self, /) -> None:
            value = TYPE([1, 2])
            value.append(3)
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_append_object(self: Self, /) -> None:
            obj = {"a": 1}
            value = TYPE()
            value.append(obj)
            self.assertIs(value[0], obj)

        def test_append_returns_none(self: Self, /) -> None:
            value = TYPE()
            self.assertIsNone(value.append(1))

    class TestMethodClear(unittest.TestCase):
        def test_clear_nonempty(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value.clear()
            self.assertEqual(tuple(value), ())

        def test_clear_empty(self: Self, /) -> None:
            value = TYPE()
            value.clear()
            self.assertEqual(tuple(value), ())

        def test_clear_mixed_values(self: Self, /) -> None:
            value = TYPE([1, "a", None, []])
            value.clear()
            self.assertEqual(tuple(value), ())

        def test_clear_returns_none(self: Self, /) -> None:
            value = TYPE([1])
            self.assertIsNone(value.clear())

    class TestMethodCopy(unittest.TestCase):
        def test_copy_has_same_contents(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            copied = value.copy()
            self.assertEqual(copied, value)

        def test_copy_is_distinct_object(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            copied = value.copy()
            self.assertIsNot(copied, value)

        def test_copy_is_shallow(self: Self, /) -> None:
            nested: list[object]
            nested = []
            value = TYPE([nested])
            copied = value.copy()
            self.assertIs(copied[0], nested)

        def test_copy_empty(self: Self, /) -> None:
            value = TYPE()
            copied = value.copy()
            self.assertEqual(tuple(copied), ())

    class TestMethodCount(unittest.TestCase):
        def test_count_existing_once(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            self.assertEqual(value.count(2), 1)

        def test_count_existing_multiple_times(self: Self, /) -> None:
            value = TYPE([1, 2, 1, 1])
            self.assertEqual(value.count(1), 3)

        def test_count_missing(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            self.assertEqual(value.count(4), 0)

        def test_count_empty(self: Self, /) -> None:
            value = TYPE()
            self.assertEqual(value.count(1), 0)

    class TestMethodExtend(unittest.TestCase):
        def test_extend_with_list(self: Self, /) -> None:
            value = TYPE([1])
            value.extend([2, 3])
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_extend_empty(self: Self, /) -> None:
            value = TYPE([1])
            value.extend([])
            self.assertEqual(tuple(value), (1,))

        def test_extend_with_tuple(self: Self, /) -> None:
            value = TYPE([1])
            value.extend((2, 3))
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_extend_returns_none(self: Self, /) -> None:
            value = TYPE()
            self.assertIsNone(value.extend([1, 2]))

    class TestMethodIndex(unittest.TestCase):
        def test_index_existing(self: Self, /) -> None:
            value = TYPE(["a", "b", "c"])
            self.assertEqual(value.index("b"), 1)

        def test_index_returns_first_match(self: Self, /) -> None:
            value = TYPE([1, 2, 1])
            self.assertEqual(value.index(1), 0)

        def test_index_with_start(self: Self, /) -> None:
            value = TYPE([1, 2, 1])
            self.assertEqual(value.index(1, 1), 2)

        def test_index_missing_raises_value_error(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            with self.assertRaises(ValueError):
                value.index(4)

    class TestMethodInsert(unittest.TestCase):
        def test_insert_at_start(self: Self, /) -> None:
            value = TYPE([2, 3])
            value.insert(0, 1)
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_insert_in_middle(self: Self, /) -> None:
            value = TYPE([1, 3])
            value.insert(1, 2)
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_insert_past_end(self: Self, /) -> None:
            value = TYPE([1, 2])
            value.insert(100, 3)
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_insert_returns_none(self: Self, /) -> None:
            value = TYPE()
            self.assertIsNone(value.insert(0, 1))

    class TestMethodPop(unittest.TestCase):
        def test_pop_last(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            result = value.pop()
            self.assertEqual(result, 3)
            self.assertEqual(tuple(value), (1, 2))

        def test_pop_first(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            result = value.pop(0)
            self.assertEqual(result, 1)
            self.assertEqual(tuple(value), (2, 3))

        def test_pop_negative_index(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            result = value.pop(-2)
            self.assertEqual(result, 2)
            self.assertEqual(tuple(value), (1, 3))

        def test_pop_empty_raises_index_error(self: Self, /) -> None:
            value = TYPE()
            with self.assertRaises(IndexError):
                value.pop()

    class TestMethodRemove(unittest.TestCase):
        def test_remove_existing(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value.remove(2)
            self.assertEqual(tuple(value), (1, 3))

        def test_remove_only_first_match(self: Self, /) -> None:
            value = TYPE([1, 2, 1])
            value.remove(1)
            self.assertEqual(tuple(value), (2, 1))

        def test_remove_missing_raises_value_error(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            with self.assertRaises(ValueError):
                value.remove(4)

        def test_remove_returns_none(self: Self, /) -> None:
            value = TYPE([1])
            self.assertIsNone(value.remove(1))

    class TestMethodReverse(unittest.TestCase):
        def test_reverse_multiple_items(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value.reverse()
            self.assertEqual(tuple(value), (3, 2, 1))

        def test_reverse_single_item(self: Self, /) -> None:
            value = TYPE([1])
            value.reverse()
            self.assertEqual(tuple(value), (1,))

        def test_reverse_empty(self: Self, /) -> None:
            value = TYPE()
            value.reverse()
            self.assertEqual(tuple(value), ())

        def test_reverse_returns_none(self: Self, /) -> None:
            value = TYPE([1, 2])
            self.assertIsNone(value.reverse())

    class TestMethodSort(unittest.TestCase):
        def test_sort_ascending(self: Self, /) -> None:
            value = TYPE([3, 1, 2])
            value.sort()
            self.assertEqual(tuple(value), (1, 2, 3))

        def test_sort_reverse(self: Self, /) -> None:
            value = TYPE([1, 3, 2])
            value.sort(reverse=True)
            self.assertEqual(tuple(value), (3, 2, 1))

        def test_sort_with_key(self: Self, /) -> None:
            value = TYPE(["bbb", "a", "cc"])
            value.sort(key=len)
            self.assertEqual(tuple(value), ("a", "cc", "bbb"))

        def test_sort_returns_none(self: Self, /) -> None:
            value = TYPE([2, 1])
            self.assertIsNone(value.sort())

    class TestOperatorAdd(unittest.TestCase):
        def test_add_two_nonempty_lists(self: Self, /) -> None:
            result = TYPE([1, 2]) + TYPE([3, 4])
            self.assertEqual(tuple(result), (1, 2, 3, 4))

        def test_add_empty_list(self: Self, /) -> None:
            result = TYPE([1, 2]) + TYPE([])
            self.assertEqual(tuple(result), (1, 2))

        def test_add_to_empty_slot(self: Self, /) -> None:
            result = TYPE([]) + TYPE([1, 2])
            self.assertEqual(tuple(result), (1, 2))

        def test_add_does_not_modify_original(self: Self, /) -> None:
            value = TYPE([1, 2])
            value + TYPE([3])
            self.assertEqual(tuple(value), (1, 2))

    class TestOperatorContains(unittest.TestCase):
        def test_contains_first_element(self: Self, /) -> None:
            self.assertTrue(1 in TYPE([1, 2, 3]))

        def test_contains_last_element(self: Self, /) -> None:
            self.assertTrue(3 in TYPE([1, 2, 3]))

        def test_does_not_contain_missing_element(self: Self, /) -> None:
            self.assertFalse(4 in TYPE([1, 2, 3]))

        def test_empty_slot_contains_nothing(self: Self, /) -> None:
            self.assertFalse(1 in TYPE([]))

    class TestOperatorDelItem(unittest.TestCase):
        def test_delete_first_item(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            del value[0]
            self.assertEqual(tuple(value), (2, 3))

        def test_delete_last_item(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            del value[-1]
            self.assertEqual(tuple(value), (1, 2))

        def test_delete_slice(self: Self, /) -> None:
            value = TYPE([1, 2, 3, 4])
            del value[1:3]
            self.assertEqual(tuple(value), (1, 4))

        def test_delete_out_of_range_raises(self: Self, /) -> None:
            value = TYPE([1, 2])
            with self.assertRaises(IndexError):
                del value[5]

    class TestOperatorEqual(unittest.TestCase):
        def test_equal_same_contents(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) == TYPE([1, 2]))

        def test_equal_empty_lists(self: Self, /) -> None:
            self.assertTrue(TYPE([]) == TYPE([]))

        def test_not_equal_different_values(self: Self, /) -> None:
            self.assertFalse(TYPE([1, 2]) == TYPE([1, 3]))

        def test_not_equal_different_lengths(self: Self, /) -> None:
            self.assertFalse(TYPE([1, 2]) == TYPE([1, 2, 3]))

    class TestOperatorGetItem(unittest.TestCase):
        def test_get_first_item(self: Self, /) -> None:
            value = TYPE([10, 20, 30])
            self.assertEqual(value[0], 10)

        def test_get_last_item_with_negative_index(self: Self, /) -> None:
            value = TYPE([10, 20, 30])
            self.assertEqual(value[-1], 30)

        def test_get_slice(self: Self, /) -> None:
            value = TYPE([1, 2, 3, 4])
            self.assertEqual(value[1:3], TYPE([2, 3]))

        def test_out_of_range_index_raises(self: Self, /) -> None:
            value = TYPE([1, 2])
            with self.assertRaises(IndexError):
                value[5]

    class TestOperatorGreaterThan(unittest.TestCase):
        def test_greater_than_by_first_element(self: Self, /) -> None:
            self.assertTrue(TYPE([2, 0]) > TYPE([1, 9]))

        def test_greater_than_by_later_element(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 3]) > TYPE([1, 2]))

        def test_longer_list_is_greater_than_prefix(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2, 3]) > TYPE([1, 2]))

        def test_equal_list_is_not_greater_than(self: Self, /) -> None:
            self.assertFalse(TYPE([1, 2]) > TYPE([1, 2]))

    class TestOperatorGreaterThanOrEqual(unittest.TestCase):
        def test_greater_value_is_greater_or_equal(self: Self, /) -> None:
            self.assertTrue(TYPE([2]) >= TYPE([1]))

        def test_equal_value_is_greater_or_equal(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) >= TYPE([1, 2]))

        def test_longer_list_is_greater_or_equal_to_prefix(
            self: Self, /
        ) -> None:
            self.assertTrue(TYPE([1, 2]) >= TYPE([1]))

        def test_smaller_value_is_not_greater_or_equal(self: Self, /) -> None:
            self.assertFalse(TYPE([1]) >= TYPE([2]))

    class TestOperatorIAdd(unittest.TestCase):
        def test_iadd_nonempty_list(self: Self, /) -> None:
            value = TYPE([1, 2])
            value += [3, 4]
            self.assertEqual(tuple(value), (1, 2, 3, 4))

        def test_iadd_empty_list(self: Self, /) -> None:
            value = TYPE([1, 2])
            value += ""
            self.assertEqual(tuple(value), (1, 2))

        def test_iadd_to_empty_slot(self: Self, /) -> None:
            value = TYPE([])
            value += (1, 2)
            self.assertEqual(tuple(value), (1, 2))

        def test_iadd_multiple_times(self: Self, /) -> None:
            value = TYPE([1])
            value += [2]
            value += [3]
            self.assertEqual(tuple(value), (1, 2, 3))

    class TestOperatorLessThan(unittest.TestCase):
        def test_less_than_by_first_element(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 9]) < TYPE([2, 0]))

        def test_less_than_by_later_element(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) < TYPE([1, 3]))

        def test_prefix_is_less_than_longer_list(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) < TYPE([1, 2, 3]))

        def test_equal_list_is_not_less_than(self: Self, /) -> None:
            self.assertFalse(TYPE([1, 2]) < TYPE([1, 2]))

    class TestOperatorLessThanOrEqual(unittest.TestCase):
        def test_less_value_is_less_or_equal(self: Self, /) -> None:
            self.assertTrue(TYPE([1]) <= TYPE([2]))

        def test_equal_value_is_less_or_equal(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) <= TYPE([1, 2]))

        def test_prefix_is_less_or_equal(self: Self, /) -> None:
            self.assertTrue(TYPE([1]) <= TYPE([1, 2]))

        def test_greater_value_is_not_less_or_equal(self: Self, /) -> None:
            self.assertFalse(TYPE([2]) <= TYPE([1]))

    class TestOperatorMul(unittest.TestCase):
        def test_multiply_by_positive_integer(self: Self, /) -> None:
            result = TYPE([1, 2]) * 3
            self.assertEqual(tuple(result), (1, 2, 1, 2, 1, 2))

        def test_multiply_by_one(self: Self, /) -> None:
            result = TYPE([1, 2]) * 1
            self.assertEqual(tuple(result), (1, 2))

        def test_multiply_by_zero(self: Self, /) -> None:
            result = TYPE([1, 2]) * 0
            self.assertEqual(tuple(result), ())

        def test_multiply_by_negative_integer(self: Self, /) -> None:
            result = TYPE([1, 2]) * -2
            self.assertEqual(tuple(result), ())

    class TestOperatorIMul(unittest.TestCase):
        def test_imul_by_positive_integer(self: Self, /) -> None:
            value = TYPE([1, 2])
            value *= 2
            self.assertEqual(tuple(value), (1, 2, 1, 2))

        def test_imul_by_one(self: Self, /) -> None:
            value = TYPE([1, 2])
            value *= 1
            self.assertEqual(tuple(value), (1, 2))

        def test_imul_by_zero(self: Self, /) -> None:
            value = TYPE([1, 2])
            value *= 0
            self.assertEqual(tuple(value), ())

        def test_imul_by_negative_integer(self: Self, /) -> None:
            value = TYPE([1, 2])
            value *= -1
            self.assertEqual(tuple(value), ())

    class TestOperatorIterSequence(unittest.TestCase):
        def test_shrinking_makes_next_index_out_of_range(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = iter(values)

            self.assertEqual(next(iterator), 0)
            del values[1:]

            with self.assertRaises(StopIteration):
                next(iterator)

        def test_exhaustion_remains_after_regrowth(self: Self, /) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = iter(values)

            self.assertEqual(next(iterator), 0)
            del values[1:]

            with self.assertRaises(StopIteration):
                next(iterator)

            values.extend([10, 11, 12, 13])

            with self.assertRaises(StopIteration):
                next(iterator)

        def test_regrowth_before_next_restores_valid_index(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = iter(values)

            self.assertEqual(next(iterator), 0)
            del values[1:]
            values.extend([10, 11, 12])

            self.assertEqual(next(iterator), 10)

        def test_deletion_before_cursor_does_not_repair_index(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = iter(values)

            self.assertEqual(next(iterator), 0)
            del values[0]

            self.assertEqual(next(iterator), 2)

        def test_growth_before_exhaustion_is_seen(self: Self, /) -> None:
            values = TYPE([0, 1])
            iterator = iter(values)

            self.assertEqual(next(iterator), 0)
            self.assertEqual(next(iterator), 1)

            values.append(2)

            self.assertEqual(next(iterator), 2)

    class TestOperatorNotEqual(unittest.TestCase):
        def test_not_equal_different_contents(self: Self, /) -> None:
            self.assertTrue(TYPE([1, 2]) != TYPE([1, 3]))

        def test_not_equal_different_lengths(self: Self, /) -> None:
            self.assertTrue(TYPE([1]) != TYPE([1, 2]))

        def test_equal_values_are_not_unequal(self: Self, /) -> None:
            self.assertFalse(TYPE([1, 2]) != TYPE([1, 2]))

        def test_empty_values_are_not_unequal(self: Self, /) -> None:
            self.assertFalse(TYPE([]) != TYPE([]))

    class TestOperatorRMul(unittest.TestCase):
        def test_rmul_by_positive_integer(self: Self, /) -> None:
            result = 3 * TYPE([1, 2])
            self.assertEqual(tuple(result), (1, 2, 1, 2, 1, 2))

        def test_rmul_by_one(self: Self, /) -> None:
            result = 1 * TYPE([1, 2])
            self.assertEqual(tuple(result), (1, 2))

        def test_rmul_by_zero(self: Self, /) -> None:
            result = 0 * TYPE([1, 2])
            self.assertEqual(tuple(result), ())

        def test_rmul_by_negative_integer(self: Self, /) -> None:
            result = -3 * TYPE([1, 2])
            self.assertEqual(tuple(result), ())

    class TestOperatorReversedSequence(unittest.TestCase):
        def test_shrinking_makes_next_index_out_of_range(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = reversed(values)

            self.assertEqual(next(iterator), 4)
            del values[1:]

            with self.assertRaises(StopIteration):
                next(iterator)

        def test_exhaustion_remains_after_regrowth(self: Self, /) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = reversed(values)

            self.assertEqual(next(iterator), 4)
            del values[1:]

            with self.assertRaises(StopIteration):
                next(iterator)

            values.extend([10, 11, 12, 13])

            with self.assertRaises(StopIteration):
                next(iterator)

        def test_regrowth_before_next_restores_valid_index(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = reversed(values)

            self.assertEqual(next(iterator), 4)
            del values[1:]
            values.extend([10, 11, 12, 13])

            self.assertEqual(next(iterator), 12)

        def test_deletion_before_cursor_does_not_repair_index(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2, 3, 4])
            iterator = reversed(values)

            self.assertEqual(next(iterator), 4)
            del values[0]

            self.assertEqual(next(iterator), 4)

        def test_growth_beyond_initial_reverse_range_is_not_seen(
            self: Self, /
        ) -> None:
            values = TYPE([0, 1, 2])
            iterator = reversed(values)

            values.append(3)

            self.assertEqual(tuple(iterator), (2, 1, 0))

    class TestOperatorSetItem(unittest.TestCase):
        def test_set_first_item(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value[0] = 10
            self.assertEqual(tuple(value), (10, 2, 3))

        def test_set_last_item_with_negative_index(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value[-1] = 10
            self.assertEqual(tuple(value), (1, 2, 10))

        def test_set_slice_same_length(self: Self, /) -> None:
            value = TYPE([1, 2, 3, 4])
            value[1:3] = [20, 30]
            self.assertEqual(tuple(value), (1, 20, 30, 4))

        def test_set_slice_different_length(self: Self, /) -> None:
            value = TYPE([1, 2, 3])
            value[1:2] = [10, 20, 30]
            self.assertEqual(tuple(value), (1, 10, 20, 30, 3))

    return {x: locals()[x] for x in set(locals()) - {"TYPE"}}


###

init()

if __name__ == "__main__":
    unittest.main()
