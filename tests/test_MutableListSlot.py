from __future__ import annotations

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
    "TestOperatorAddition",
    "TestOperatorEquality",
    "TestOperatorGreaterThan",
    "TestOperatorGreaterThanOrEqual",
    "TestOperatorIndexing",
    "TestOperatorInequality",
    "TestOperatorInPlaceAddition",
    "TestOperatorInPlaceMultiplication",
    "TestOperatorItemAssignment",
    "TestOperatorItemDeletion",
    "TestOperatorIteration",
    "TestOperatorLength",
    "TestOperatorLessThan",
    "TestOperatorLessThanOrEqual",
    "TestOperatorMembership",
    "TestOperatorMultiplication",
    "TestOperatorNonMembership",
    "TestOperatorReversed",
    "TestOperatorReverseMultiplication",
    "TestOperatorSliceAssignment",
    "TestOperatorSliceDeletion",
    "TestOperatorSlicing",
    "TestOperatorTruthValue",
    "TestOperatorUnhashable",
]


import unittest
from typing import Never, Optional, Self

import datahold


class TestMethodAppend(unittest.TestCase):
    def test_append_integer(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2])
        expected = [1, 2]
        actual.append(3)
        expected.append(3)
        self.assertEqual(list(actual), expected)

    def test_append_none(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Optional[int]]
        expected: list[Optional[int]]
        actual = datahold.MutableListSlot([])
        expected = []
        actual.append(None)
        expected.append(None)
        self.assertEqual(list(actual), expected)

    def test_append_nested_list(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int | list[int]]
        expected: list[int | list[int]]
        value: list[int]
        value = [2, 3]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.append(value)
        expected.append(value)
        self.assertEqual(list(actual), expected)
        self.assertIs(actual[-1], value)

    def test_append_same_object_twice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[object]
        expected: list[object]
        value: object
        value = object()
        actual = datahold.MutableListSlot([])
        expected = []
        actual.append(value)
        actual.append(value)
        expected.append(value)
        expected.append(value)
        self.assertEqual(list(actual), expected)
        self.assertIs(actual[0], actual[1])


class TestMethodClear(unittest.TestCase):
    def test_clear_nonempty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)

    def test_clear_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Never]
        expected: list[Never]
        actual = datahold.MutableListSlot([])
        expected = []
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)

    def test_clear_nested_values(self: Self, /) -> None:
        actual = datahold.MutableListSlot([[1], [2]])
        expected = [[1], [2]]
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)

    def test_clear_twice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)


class TestMethodCopy(unittest.TestCase):
    def test_copy_equal_contents(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        copied: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        copied = actual.copy()
        self.assertEqual(list(copied), [1, 2, 3])
        self.assertIsNot(copied, actual)

    def test_copy_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Never]
        copied: datahold.MutableListSlot[Never]
        actual = datahold.MutableListSlot([])
        copied = actual.copy()
        self.assertEqual(list(copied), [])
        self.assertIsNot(copied, actual)

    def test_copy_is_shallow(self: Self, /) -> None:
        actual: datahold.MutableListSlot[list[int]]
        nested: list[int]
        nested = [1]
        actual = datahold.MutableListSlot([nested])
        copied = actual.copy()
        self.assertIs(copied[0], nested)
        self.assertIs(copied[0], actual[0])

    def test_copy_is_independent_container(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        copied: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2])
        copied = actual.copy()
        copied.append(3)
        self.assertEqual(list(actual), [1, 2])
        self.assertEqual(list(copied), [1, 2, 3])


class TestMethodCount(unittest.TestCase):
    def test_count_present_value(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 1, 3, 1])
        self.assertEqual(actual.count(1), [1, 2, 1, 3, 1].count(1))

    def test_count_absent_value(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual.count(4), [1, 2, 3].count(4))

    def test_count_none(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Optional[int]]
        actual = datahold.MutableListSlot([None, 1, None])
        self.assertEqual(actual.count(None), [None, 1, None].count(None))

    def test_count_uses_equality(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, True, 0, False])
        self.assertEqual(actual.count(1), [1, True, 0, False].count(1))


class TestMethodExtend(unittest.TestCase):
    def test_extend_list(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.extend([2, 3])
        expected.extend([2, 3])
        self.assertEqual(list(actual), expected)

    def test_extend_tuple(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.extend((2, 3))
        expected.extend((2, 3))
        self.assertEqual(list(actual), expected)

    def test_extend_generator(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.extend(x for x in [2, 3])
        expected.extend(x for x in [2, 3])
        self.assertEqual(list(actual), expected)

    def test_extend_self(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2])
        expected = [1, 2]
        actual.extend(actual)
        expected.extend(expected)
        self.assertEqual(list(actual), expected)


class TestMethodIndex(unittest.TestCase):
    def test_index_first_match(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 1])
        self.assertEqual(actual.index(1), [1, 2, 1].index(1))

    def test_index_with_start(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 1, 3])
        self.assertEqual(actual.index(1, 1), [1, 2, 1, 3].index(1, 1))

    def test_index_with_start_and_stop(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 1, 3])
        self.assertEqual(actual.index(1, 2, 5), [0, 1, 2, 1, 3].index(1, 2, 5))

    def test_index_missing_raises_value_error(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        with self.assertRaises(ValueError):
            actual.index(4)


class TestMethodInsert(unittest.TestCase):
    def test_insert_middle(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 3])
        expected = [1, 3]
        actual.insert(1, 2)
        expected.insert(1, 2)
        self.assertEqual(list(actual), expected)

    def test_insert_negative_index(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual.insert(-1, 9)
        expected.insert(-1, 9)
        self.assertEqual(list(actual), expected)

    def test_insert_index_beyond_end(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.insert(100, 2)
        expected.insert(100, 2)
        self.assertEqual(list(actual), expected)

    def test_insert_index_before_start(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual.insert(-100, 0)
        expected.insert(-100, 0)
        self.assertEqual(list(actual), expected)


class TestMethodPop(unittest.TestCase):
    def test_pop_default(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(), expected.pop())
        self.assertEqual(list(actual), expected)

    def test_pop_positive_index(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(1), expected.pop(1))
        self.assertEqual(list(actual), expected)

    def test_pop_negative_index(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(-2), expected.pop(-2))
        self.assertEqual(list(actual), expected)

    def test_pop_empty_raises_index_error(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Never]
        actual = datahold.MutableListSlot([])
        with self.assertRaises(IndexError):
            actual.pop()


class TestMethodRemove(unittest.TestCase):
    def test_remove_present_value(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual.remove(2)
        expected.remove(2)
        self.assertEqual(list(actual), expected)

    def test_remove_only_first_match(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2, 1])
        expected = [1, 2, 1]
        actual.remove(1)
        expected.remove(1)
        self.assertEqual(list(actual), expected)

    def test_remove_none(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Optional[int]]
        expected: list[Optional[int]]
        actual = datahold.MutableListSlot([1, None, 2])
        expected = [1, None, 2]
        actual.remove(None)
        expected.remove(None)
        self.assertEqual(list(actual), expected)

    def test_remove_missing_raises_value_error(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        with self.assertRaises(ValueError):
            actual.remove(4)


class TestMethodReverse(unittest.TestCase):
    def test_reverse_even_length(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        actual.reverse()
        expected.reverse()
        self.assertEqual(list(actual), expected)

    def test_reverse_odd_length(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual.reverse()
        expected.reverse()
        self.assertEqual(list(actual), expected)

    def test_reverse_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[Never]
        expected: list[Never]
        actual = datahold.MutableListSlot([])
        expected = []
        actual.reverse()
        expected.reverse()
        self.assertEqual(list(actual), expected)

    def test_reverse_single_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[object]
        value: object
        value = object()
        actual = datahold.MutableListSlot([value])
        actual.reverse()
        self.assertEqual(len(actual), 1)
        self.assertIs(actual[0], value)


class TestMethodSort(unittest.TestCase):
    def test_sort_ascending(self: Self, /) -> None:
        actual = datahold.MutableListSlot([3, 1, 2])
        expected = [3, 1, 2]
        actual_result = actual.sort()
        expected_result = expected.sort()
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_sort_reverse(self: Self, /) -> None:
        actual = datahold.MutableListSlot([3, 1, 2])
        expected = [3, 1, 2]
        actual.sort(reverse=True)
        expected.sort(reverse=True)
        self.assertEqual(list(actual), expected)

    def test_sort_with_key(self: Self, /) -> None:
        actual = datahold.MutableListSlot(["bbb", "a", "cc"])
        expected = ["bbb", "a", "cc"]
        actual.sort(key=len)
        expected.sort(key=len)
        self.assertEqual(list(actual), expected)

    def test_sort_is_stable(self: Self, /) -> None:
        actual = datahold.MutableListSlot([(1, "a"), (2, "b"), (1, "c")])
        expected = [(1, "a"), (2, "b"), (1, "c")]
        actual.sort(key=lambda item: item[0])
        expected.sort(key=lambda item: item[0])
        self.assertEqual(list(actual), expected)


class TestOperatorAddition(unittest.TestCase):
    def test_add_nonempty(self: Self, /) -> None:
        actual = datahold.MutableListSlot([1, 2]) + datahold.MutableListSlot(
            [3, 4]
        )
        self.assertEqual(list(actual), [1, 2] + [3, 4])

    def test_add_empty_left(self: Self, /) -> None:
        x: datahold.MutableListSlot[int]
        y: datahold.MutableListSlot[int]
        x = datahold.MutableListSlot([])
        y = datahold.MutableListSlot([1])
        self.assertEqual(list(x + y), [] + [1])

    def test_add_empty_right(self: Self, /) -> None:
        x: datahold.MutableListSlot[int]
        y: datahold.MutableListSlot[int]
        x = datahold.MutableListSlot([1])
        y = datahold.MutableListSlot([])
        self.assertEqual(list(x + y), [1] + [])

    def test_add_does_not_mutate_operands(self: Self, /) -> None:
        left: datahold.MutableListSlot[int]
        right: datahold.MutableListSlot[int]
        left = datahold.MutableListSlot([1])
        right = datahold.MutableListSlot([2])
        result = left + right
        self.assertEqual(list(left), [1])
        self.assertEqual(list(right), [2])
        self.assertEqual(list(result), [1, 2])


class TestOperatorInPlaceAddition(unittest.TestCase):
    def test_iadd_list_like(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual += datahold.MutableListSlot([2, 3])
        expected += [2, 3]
        self.assertEqual(list(actual), expected)

    def test_iadd_tuple(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual += (2, 3)
        expected += (2, 3)
        self.assertEqual(list(actual), expected)

    def test_iadd_generator(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        expected = [1]
        actual += (x for x in [2, 3])
        expected += (x for x in [2, 3])
        self.assertEqual(list(actual), expected)

    def test_iadd_preserves_identity(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        original_id = id(actual)
        actual += [2]
        self.assertEqual(id(actual), original_id)
        self.assertEqual(list(actual), [1, 2])


class TestOperatorMultiplication(unittest.TestCase):
    def test_mul_positive(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2]) * 3
        self.assertEqual(list(actual), [1, 2] * 3)

    def test_mul_zero(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2]) * 0
        self.assertEqual(list(actual), [1, 2] * 0)

    def test_mul_negative(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2]) * -2
        self.assertEqual(list(actual), [1, 2] * -2)

    def test_mul_does_not_mutate_operand(self: Self, /) -> None:
        result: datahold.MutableListSlot[int]
        source: datahold.MutableListSlot[int]
        source = datahold.MutableListSlot([1, 2])
        result = source * 2
        self.assertEqual(list(source), [1, 2])
        self.assertEqual(list(result), [1, 2, 1, 2])


class TestOperatorReverseMultiplication(unittest.TestCase):
    def test_rmul_positive(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = 3 * datahold.MutableListSlot([1, 2])
        self.assertEqual(list(actual), 3 * [1, 2])

    def test_rmul_zero(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = 0 * datahold.MutableListSlot([1, 2])
        self.assertEqual(list(actual), 0 * [1, 2])

    def test_rmul_negative(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = -2 * datahold.MutableListSlot([1, 2])
        self.assertEqual(list(actual), -2 * [1, 2])

    def test_rmul_does_not_mutate_operand(self: Self, /) -> None:
        result: datahold.MutableListSlot[int]
        source: datahold.MutableListSlot[int]
        source = datahold.MutableListSlot([1, 2])
        result = 2 * source
        self.assertEqual(list(source), [1, 2])
        self.assertEqual(list(result), [1, 2, 1, 2])


class TestOperatorInPlaceMultiplication(unittest.TestCase):
    def test_imul_positive(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        expected: list[int]
        actual = datahold.MutableListSlot([1, 2])
        expected = [1, 2]
        actual *= 3
        expected *= 3
        self.assertEqual(list(actual), expected)

    def test_imul_zero(self: Self, /) -> None:
        actual = datahold.MutableListSlot([1, 2])
        expected = [1, 2]
        actual *= 0
        expected *= 0
        self.assertEqual(list(actual), expected)

    def test_imul_negative(self: Self, /) -> None:
        actual = datahold.MutableListSlot([1, 2])
        expected = [1, 2]
        actual *= -2
        expected *= -2
        self.assertEqual(list(actual), expected)

    def test_imul_preserves_identity(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        original_id: int
        actual = datahold.MutableListSlot([1, 2])
        original_id = id(actual)
        actual *= 2
        self.assertEqual(id(actual), original_id)
        self.assertEqual(list(actual), [1, 2, 1, 2])


class TestOperatorEquality(unittest.TestCase):
    def test_equal_same_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) == datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] == [1, 2])

    def test_equal_different_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) == datahold.MutableListSlot(
            [1, 3]
        )
        self.assertEqual(actual, [1, 2] == [1, 3])

    def test_equal_different_lengths(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1]) == datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1] == [1, 2])

    def test_equal_nested_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot(
            [[1], [2]]
        ) == datahold.MutableListSlot([[1], [2]])
        self.assertEqual(actual, [[1], [2]] == [[1], [2]])


class TestOperatorInequality(unittest.TestCase):
    def test_not_equal_same_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) != datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] != [1, 2])

    def test_not_equal_different_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) != datahold.MutableListSlot(
            [1, 3]
        )
        self.assertEqual(actual, [1, 2] != [1, 3])

    def test_not_equal_different_lengths(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1]) != datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1] != [1, 2])

    def test_not_equal_nested_contents(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot(
            [[1], [2]]
        ) != datahold.MutableListSlot([[1], [3]])
        self.assertEqual(actual, [[1], [2]] != [[1], [3]])


class TestOperatorLessThan(unittest.TestCase):
    def test_less_at_first_difference(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) < datahold.MutableListSlot(
            [1, 3]
        )
        self.assertEqual(actual, [1, 2] < [1, 3])

    def test_less_when_prefix(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1]) < datahold.MutableListSlot(
            [1, 0]
        )
        self.assertEqual(actual, [1] < [1, 0])

    def test_less_false_for_equal(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) < datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] < [1, 2])

    def test_less_empty(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([]) < datahold.MutableListSlot([0])
        self.assertEqual(actual, [] < [0])


class TestOperatorLessThanOrEqual(unittest.TestCase):
    def test_less_equal_when_less(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) <= datahold.MutableListSlot(
            [1, 3]
        )
        self.assertEqual(actual, [1, 2] <= [1, 3])

    def test_less_equal_when_equal(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) <= datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] <= [1, 2])

    def test_less_equal_false_when_greater(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([2]) <= datahold.MutableListSlot([1])
        self.assertEqual(actual, [2] <= [1])

    def test_less_equal_prefix(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1]) <= datahold.MutableListSlot(
            [1, 0]
        )
        self.assertEqual(actual, [1] <= [1, 0])


class TestOperatorGreaterThan(unittest.TestCase):
    def test_greater_at_first_difference(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 3]) > datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 3] > [1, 2])

    def test_greater_when_other_is_prefix(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 0]) > datahold.MutableListSlot(
            [1]
        )
        self.assertEqual(actual, [1, 0] > [1])

    def test_greater_false_for_equal(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) > datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] > [1, 2])

    def test_greater_than_empty(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([0]) > datahold.MutableListSlot([])
        self.assertEqual(actual, [0] > [])


class TestOperatorGreaterThanOrEqual(unittest.TestCase):
    def test_greater_equal_when_greater(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 3]) >= datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 3] >= [1, 2])

    def test_greater_equal_when_equal(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 2]) >= datahold.MutableListSlot(
            [1, 2]
        )
        self.assertEqual(actual, [1, 2] >= [1, 2])

    def test_greater_equal_false_when_less(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1]) >= datahold.MutableListSlot([2])
        self.assertEqual(actual, [1] >= [2])

    def test_greater_equal_other_is_prefix(self: Self, /) -> None:
        actual: bool
        actual = datahold.MutableListSlot([1, 0]) >= datahold.MutableListSlot(
            [1]
        )
        self.assertEqual(actual, [1, 0] >= [1])


class TestOperatorIndexing(unittest.TestCase):
    def test_get_first_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual[0], [1, 2, 3][0])

    def test_get_last_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual[-1], [1, 2, 3][-1])

    def test_get_middle_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual[1], [1, 2, 3][1])

    def test_get_out_of_range_raises_index_error(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        with self.assertRaises(IndexError):
            actual[3]


class TestOperatorItemAssignment(unittest.TestCase):
    def test_set_first_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual[0] = 9
        expected[0] = 9
        self.assertEqual(list(actual), expected)

    def test_set_negative_index(self: Self, /) -> None:
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        actual[-1] = 9
        expected[-1] = 9
        self.assertEqual(list(actual), expected)

    def test_set_nested_value(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int | list[int]]
        value: list[int]
        value = [9]
        actual = datahold.MutableListSlot([1, 2, 3])
        actual[1] = value
        self.assertIs(actual[1], value)
        self.assertEqual(list(actual), [1, value, 3])

    def test_set_out_of_range_raises_index_error(self: Self, /) -> None:
        actual = datahold.MutableListSlot([1, 2, 3])
        with self.assertRaises(IndexError):
            actual[3] = 9


class TestOperatorItemDeletion(unittest.TestCase):
    def test_delete_first_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        del actual[0]
        del expected[0]
        self.assertEqual(list(actual), expected)

    def test_delete_negative_index(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        del actual[-1]
        del expected[-1]
        self.assertEqual(list(actual), expected)

    def test_delete_middle_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        expected = [1, 2, 3]
        del actual[1]
        del expected[1]
        self.assertEqual(list(actual), expected)

    def test_delete_out_of_range_raises_index_error(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        with self.assertRaises(IndexError):
            del actual[3]


class TestOperatorIteration(unittest.TestCase):
    def test_iterates_in_order(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(list(iter(actual)), [1, 2, 3])

    def test_iterates_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([])
        self.assertEqual(list(iter(actual)), [])

    def test_independent_iterators(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2])
        first = iter(actual)
        second = iter(actual)
        self.assertEqual(next(first), 1)
        self.assertEqual(next(second), 1)

    def test_iterator_raises_stop_iteration(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        iterator = iter(actual)
        self.assertEqual(next(iterator), 1)
        with self.assertRaises(StopIteration):
            next(iterator)


class TestOperatorLength(unittest.TestCase):
    def test_len_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([])
        self.assertEqual(len(actual), len([]))

    def test_len_one(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        self.assertEqual(len(actual), len([1]))

    def test_len_many(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3, 4])
        self.assertEqual(len(actual), len([1, 2, 3, 4]))

    def test_len_after_mutation(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2])
        actual.append(3)
        self.assertEqual(len(actual), 3)


class TestOperatorMembership(unittest.TestCase):
    def test_contains_present_value(self: Self, /) -> None:
        actual: bool
        actual = 2 in datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual, 2 in [1, 2, 3])

    def test_contains_absent_value(self: Self, /) -> None:
        actual: bool
        actual = 4 in datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual, 4 in [1, 2, 3])

    def test_contains_none(self: Self, /) -> None:
        actual: bool
        actual = None in datahold.MutableListSlot([1, None, 2])
        self.assertEqual(actual, None in [1, None, 2])

    def test_contains_uses_equality(self: Self, /) -> None:
        actual: bool
        actual = True in datahold.MutableListSlot([1])
        self.assertEqual(actual, True in [1])


class TestOperatorNonMembership(unittest.TestCase):
    def test_not_contains_present_value(self: Self, /) -> None:
        actual: bool
        actual = 2 not in datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual, 2 not in [1, 2, 3])

    def test_not_contains_absent_value(self: Self, /) -> None:
        actual: bool
        actual = 4 not in datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(actual, 4 not in [1, 2, 3])

    def test_not_contains_none(self: Self, /) -> None:
        actual: bool
        actual = None not in datahold.MutableListSlot([1, None, 2])
        self.assertEqual(actual, None not in [1, None, 2])

    def test_not_contains_uses_equality(self: Self, /) -> None:
        actual: bool
        actual = True not in datahold.MutableListSlot([1])
        self.assertEqual(actual, True not in [1])


class TestOperatorReversed(unittest.TestCase):
    def test_reversed_nonempty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        self.assertEqual(list(reversed(actual)), list(reversed([1, 2, 3])))

    def test_reversed_empty(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([])
        self.assertEqual(list(reversed(actual)), list(reversed([])))

    def test_reversed_single_item(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        self.assertEqual(list(reversed(actual)), list(reversed([1])))

    def test_reversed_does_not_mutate(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        result: list[int]
        actual = datahold.MutableListSlot([1, 2, 3])
        result = list(reversed(actual))
        self.assertEqual(result, [3, 2, 1])
        self.assertEqual(list(actual), [1, 2, 3])


class TestOperatorSliceAssignment(unittest.TestCase):
    def test_replace_slice_same_length(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3])
        expected = [0, 1, 2, 3]
        actual[1:3] = [8, 9]
        expected[1:3] = [8, 9]
        self.assertEqual(list(actual), expected)

    def test_replace_slice_different_length(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3])
        expected = [0, 1, 2, 3]
        actual[1:3] = [8, 9, 10]
        expected[1:3] = [8, 9, 10]
        self.assertEqual(list(actual), expected)

    def test_insert_with_empty_slice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1, 3])
        expected = [1, 3]
        actual[1:1] = [2]
        expected[1:1] = [2]
        self.assertEqual(list(actual), expected)

    def test_extended_slice_requires_matching_length(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3])
        with self.assertRaises(ValueError):
            actual[::2] = [9]


class TestOperatorSliceDeletion(unittest.TestCase):
    def test_delete_middle_slice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        expected = [0, 1, 2, 3, 4]
        del actual[1:4]
        del expected[1:4]
        self.assertEqual(list(actual), expected)

    def test_delete_slice_with_step(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        expected = [0, 1, 2, 3, 4]
        del actual[::2]
        del expected[::2]
        self.assertEqual(list(actual), expected)

    def test_delete_empty_slice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2])
        expected = [0, 1, 2]
        del actual[1:1]
        del expected[1:1]
        self.assertEqual(list(actual), expected)

    def test_delete_all_items_by_slice(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2])
        expected = [0, 1, 2]
        del actual[:]
        del expected[:]
        self.assertEqual(list(actual), expected)


class TestOperatorSlicing(unittest.TestCase):
    def test_slice_start_stop(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[1:4]), [0, 1, 2, 3, 4][1:4])

    def test_slice_with_step(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[::2]), [0, 1, 2, 3, 4][::2])

    def test_slice_negative_bounds(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[-4:-1]), [0, 1, 2, 3, 4][-4:-1])

    def test_slice_reverse(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[::-1]), [0, 1, 2, 3, 4][::-1])


class TestOperatorTruthValue(unittest.TestCase):
    def test_empty_is_false(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([])
        self.assertEqual(bool(actual), bool([]))

    def test_nonempty_is_true(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([0])
        self.assertEqual(bool(actual), bool([0]))

    def test_falsey_elements_do_not_make_container_false(
        self: Self, /
    ) -> None:
        actual: datahold.MutableListSlot[Optional[int]]
        actual = datahold.MutableListSlot([False, None, 0])
        self.assertEqual(bool(actual), bool([False, None, 0]))

    def test_truth_value_after_clear(self: Self, /) -> None:
        actual: datahold.MutableListSlot[int]
        actual = datahold.MutableListSlot([1])
        actual.clear()
        self.assertEqual(bool(actual), bool([]))


class TestOperatorUnhashable(unittest.TestCase):
    def test_hash(self: Self, /) -> None:
        with self.assertRaises(Exception):
            hash(datahold.MutableListSlot())


if __name__ == "__main__":
    unittest.main(verbosity=2)
