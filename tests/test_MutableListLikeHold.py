from __future__ import annotations

import unittest

import datahold


class MutableListLikeHold[Item](
    datahold.Hold[list[Item]], datahold.MutableListLike[Item]
):
    __slots__ = ("_data",)
    __hash__ = None


class TestAppend(unittest.TestCase):
    def test_append_integer(self):
        actual = MutableListLikeHold([1, 2])
        expected = [1, 2]
        actual_result = actual.append(3)
        expected_result = expected.append(3)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_append_none(self):
        actual = MutableListLikeHold([])
        expected = []
        actual_result = actual.append(None)
        expected_result = expected.append(None)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_append_nested_list(self):
        value = [2, 3]
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.append(value)
        expected.append(value)
        self.assertEqual(list(actual), expected)
        self.assertIs(actual[-1], value)

    def test_append_same_object_twice(self):
        value = object()
        actual = MutableListLikeHold([])
        expected = []
        actual.append(value)
        actual.append(value)
        expected.append(value)
        expected.append(value)
        self.assertEqual(list(actual), expected)
        self.assertIs(actual[0], actual[1])


class TestClear(unittest.TestCase):
    def test_clear_nonempty(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual_result = actual.clear()
        expected_result = expected.clear()
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_clear_empty(self):
        actual = MutableListLikeHold([])
        expected = []
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)

    def test_clear_nested_values(self):
        actual = MutableListLikeHold([[1], [2]])
        expected = [[1], [2]]
        actual.clear()
        expected.clear()
        self.assertEqual(list(actual), expected)

    def test_clear_twice(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.clear()
        actual_result = actual.clear()
        expected.clear()
        expected_result = expected.clear()
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)


class TestCopy(unittest.TestCase):
    def test_copy_equal_contents(self):
        actual = MutableListLikeHold([1, 2, 3])
        copied = actual.copy()
        self.assertEqual(list(copied), [1, 2, 3])
        self.assertIsNot(copied, actual)

    def test_copy_empty(self):
        actual = MutableListLikeHold([])
        copied = actual.copy()
        self.assertEqual(list(copied), [])
        self.assertIsNot(copied, actual)

    def test_copy_is_shallow(self):
        nested = [1]
        actual = MutableListLikeHold([nested])
        copied = actual.copy()
        self.assertIs(copied[0], nested)
        self.assertIs(copied[0], actual[0])

    def test_copy_is_independent_container(self):
        actual = MutableListLikeHold([1, 2])
        copied = actual.copy()
        copied.append(3)
        self.assertEqual(list(actual), [1, 2])
        self.assertEqual(list(copied), [1, 2, 3])


class TestCount(unittest.TestCase):
    def test_count_present_value(self):
        actual = MutableListLikeHold([1, 2, 1, 3, 1])
        self.assertEqual(actual.count(1), [1, 2, 1, 3, 1].count(1))

    def test_count_absent_value(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual.count(4), [1, 2, 3].count(4))

    def test_count_none(self):
        actual = MutableListLikeHold([None, 1, None])
        self.assertEqual(actual.count(None), [None, 1, None].count(None))

    def test_count_uses_equality(self):
        actual = MutableListLikeHold([1, True, 0, False])
        self.assertEqual(actual.count(1), [1, True, 0, False].count(1))


class TestExtend(unittest.TestCase):
    def test_extend_list(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual_result = actual.extend([2, 3])
        expected_result = expected.extend([2, 3])
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_extend_tuple(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.extend((2, 3))
        expected.extend((2, 3))
        self.assertEqual(list(actual), expected)

    def test_extend_generator(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.extend(x for x in [2, 3])
        expected.extend(x for x in [2, 3])
        self.assertEqual(list(actual), expected)



class TestIndex(unittest.TestCase):
    def test_index_first_match(self):
        actual = MutableListLikeHold([1, 2, 1])
        self.assertEqual(actual.index(1), [1, 2, 1].index(1))

    def test_index_with_start(self):
        actual = MutableListLikeHold([1, 2, 1, 3])
        self.assertEqual(actual.index(1, 1), [1, 2, 1, 3].index(1, 1))

    def test_index_with_start_and_stop(self):
        actual = MutableListLikeHold([0, 1, 2, 1, 3])
        self.assertEqual(actual.index(1, 2, 5), [0, 1, 2, 1, 3].index(1, 2, 5))

    def test_index_missing_raises_value_error(self):
        actual = MutableListLikeHold([1, 2, 3])
        with self.assertRaises(ValueError):
            actual.index(4)


class TestInsert(unittest.TestCase):
    def test_insert_middle(self):
        actual = MutableListLikeHold([1, 3])
        expected = [1, 3]
        actual_result = actual.insert(1, 2)
        expected_result = expected.insert(1, 2)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_insert_negative_index(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual.insert(-1, 9)
        expected.insert(-1, 9)
        self.assertEqual(list(actual), expected)

    def test_insert_index_beyond_end(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.insert(100, 2)
        expected.insert(100, 2)
        self.assertEqual(list(actual), expected)

    def test_insert_index_before_start(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual.insert(-100, 0)
        expected.insert(-100, 0)
        self.assertEqual(list(actual), expected)


class TestPop(unittest.TestCase):
    def test_pop_default(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(), expected.pop())
        self.assertEqual(list(actual), expected)

    def test_pop_positive_index(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(1), expected.pop(1))
        self.assertEqual(list(actual), expected)

    def test_pop_negative_index(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual.pop(-2), expected.pop(-2))
        self.assertEqual(list(actual), expected)

    def test_pop_empty_raises_index_error(self):
        actual = MutableListLikeHold([])
        with self.assertRaises(IndexError):
            actual.pop()


class TestRemove(unittest.TestCase):
    def test_remove_present_value(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual_result = actual.remove(2)
        expected_result = expected.remove(2)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_remove_only_first_match(self):
        actual = MutableListLikeHold([1, 2, 1])
        expected = [1, 2, 1]
        actual.remove(1)
        expected.remove(1)
        self.assertEqual(list(actual), expected)

    def test_remove_none(self):
        actual = MutableListLikeHold([1, None, 2])
        expected = [1, None, 2]
        actual.remove(None)
        expected.remove(None)
        self.assertEqual(list(actual), expected)

    def test_remove_missing_raises_value_error(self):
        actual = MutableListLikeHold([1, 2, 3])
        with self.assertRaises(ValueError):
            actual.remove(4)


class TestReverse(unittest.TestCase):
    def test_reverse_even_length(self):
        actual = MutableListLikeHold([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        actual_result = actual.reverse()
        expected_result = expected.reverse()
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_reverse_odd_length(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual.reverse()
        expected.reverse()
        self.assertEqual(list(actual), expected)

    def test_reverse_empty(self):
        actual = MutableListLikeHold([])
        expected = []
        actual.reverse()
        expected.reverse()
        self.assertEqual(list(actual), expected)

    def test_reverse_single_item(self):
        value = object()
        actual = MutableListLikeHold([value])
        actual.reverse()
        self.assertEqual(len(actual), 1)
        self.assertIs(actual[0], value)


class TestSort(unittest.TestCase):
    def test_sort_ascending(self):
        actual = MutableListLikeHold([3, 1, 2])
        expected = [3, 1, 2]
        actual_result = actual.sort()
        expected_result = expected.sort()
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(list(actual), expected)

    def test_sort_reverse(self):
        actual = MutableListLikeHold([3, 1, 2])
        expected = [3, 1, 2]
        actual.sort(reverse=True)
        expected.sort(reverse=True)
        self.assertEqual(list(actual), expected)

    def test_sort_with_key(self):
        actual = MutableListLikeHold(["bbb", "a", "cc"])
        expected = ["bbb", "a", "cc"]
        actual.sort(key=len)
        expected.sort(key=len)
        self.assertEqual(list(actual), expected)

    def test_sort_is_stable(self):
        actual = MutableListLikeHold([(1, "a"), (2, "b"), (1, "c")])
        expected = [(1, "a"), (2, "b"), (1, "c")]
        actual.sort(key=lambda item: item[0])
        expected.sort(key=lambda item: item[0])
        self.assertEqual(list(actual), expected)


class TestAdditionOperator(unittest.TestCase):
    def test_add_nonempty(self):
        actual = MutableListLikeHold([1, 2]) + MutableListLikeHold([3, 4])
        self.assertEqual(list(actual), [1, 2] + [3, 4])

    def test_add_empty_left(self):
        actual = MutableListLikeHold([]) + MutableListLikeHold([1])
        self.assertEqual(list(actual), [] + [1])

    def test_add_empty_right(self):
        actual = MutableListLikeHold([1]) + MutableListLikeHold([])
        self.assertEqual(list(actual), [1] + [])

    def test_add_does_not_mutate_operands(self):
        left = MutableListLikeHold([1])
        right = MutableListLikeHold([2])
        result = left + right
        self.assertEqual(list(left), [1])
        self.assertEqual(list(right), [2])
        self.assertEqual(list(result), [1, 2])


class TestInPlaceAdditionOperator(unittest.TestCase):
    def test_iadd_list_like(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual += MutableListLikeHold([2, 3])
        expected += [2, 3]
        self.assertEqual(list(actual), expected)

    def test_iadd_tuple(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual += (2, 3)
        expected += (2, 3)
        self.assertEqual(list(actual), expected)

    def test_iadd_generator(self):
        actual = MutableListLikeHold([1])
        expected = [1]
        actual += (x for x in [2, 3])
        expected += (x for x in [2, 3])
        self.assertEqual(list(actual), expected)

    def test_iadd_preserves_identity(self):
        actual = MutableListLikeHold([1])
        original_id = id(actual)
        actual += [2]
        self.assertEqual(id(actual), original_id)
        self.assertEqual(list(actual), [1, 2])


class TestMultiplicationOperator(unittest.TestCase):
    def test_mul_positive(self):
        actual = MutableListLikeHold([1, 2]) * 3
        self.assertEqual(list(actual), [1, 2] * 3)

    def test_mul_zero(self):
        actual = MutableListLikeHold([1, 2]) * 0
        self.assertEqual(list(actual), [1, 2] * 0)

    def test_mul_negative(self):
        actual = MutableListLikeHold([1, 2]) * -2
        self.assertEqual(list(actual), [1, 2] * -2)

    def test_mul_does_not_mutate_operand(self):
        source = MutableListLikeHold([1, 2])
        result = source * 2
        self.assertEqual(list(source), [1, 2])
        self.assertEqual(list(result), [1, 2, 1, 2])


class TestReverseMultiplicationOperator(unittest.TestCase):
    def test_rmul_positive(self):
        actual = 3 * MutableListLikeHold([1, 2])
        self.assertEqual(list(actual), 3 * [1, 2])

    def test_rmul_zero(self):
        actual = 0 * MutableListLikeHold([1, 2])
        self.assertEqual(list(actual), 0 * [1, 2])

    def test_rmul_negative(self):
        actual = -2 * MutableListLikeHold([1, 2])
        self.assertEqual(list(actual), -2 * [1, 2])

    def test_rmul_does_not_mutate_operand(self):
        source = MutableListLikeHold([1, 2])
        result = 2 * source
        self.assertEqual(list(source), [1, 2])
        self.assertEqual(list(result), [1, 2, 1, 2])


class TestInPlaceMultiplicationOperator(unittest.TestCase):
    def test_imul_positive(self):
        actual = MutableListLikeHold([1, 2])
        expected = [1, 2]
        actual *= 3
        expected *= 3
        self.assertEqual(list(actual), expected)

    def test_imul_zero(self):
        actual = MutableListLikeHold([1, 2])
        expected = [1, 2]
        actual *= 0
        expected *= 0
        self.assertEqual(list(actual), expected)

    def test_imul_negative(self):
        actual = MutableListLikeHold([1, 2])
        expected = [1, 2]
        actual *= -2
        expected *= -2
        self.assertEqual(list(actual), expected)

    def test_imul_preserves_identity(self):
        actual = MutableListLikeHold([1, 2])
        original_id = id(actual)
        actual *= 2
        self.assertEqual(id(actual), original_id)
        self.assertEqual(list(actual), [1, 2, 1, 2])


class TestEqualityOperator(unittest.TestCase):
    def test_equal_same_contents(self):
        actual = MutableListLikeHold([1, 2]) == MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] == [1, 2])

    def test_equal_different_contents(self):
        actual = MutableListLikeHold([1, 2]) == MutableListLikeHold([1, 3])
        self.assertEqual(actual, [1, 2] == [1, 3])

    def test_equal_different_lengths(self):
        actual = MutableListLikeHold([1]) == MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1] == [1, 2])

    def test_equal_nested_contents(self):
        actual = MutableListLikeHold([[1], [2]]) == MutableListLikeHold(
            [[1], [2]]
        )
        self.assertEqual(actual, [[1], [2]] == [[1], [2]])


class TestInequalityOperator(unittest.TestCase):
    def test_not_equal_same_contents(self):
        actual = MutableListLikeHold([1, 2]) != MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] != [1, 2])

    def test_not_equal_different_contents(self):
        actual = MutableListLikeHold([1, 2]) != MutableListLikeHold([1, 3])
        self.assertEqual(actual, [1, 2] != [1, 3])

    def test_not_equal_different_lengths(self):
        actual = MutableListLikeHold([1]) != MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1] != [1, 2])

    def test_not_equal_nested_contents(self):
        actual = MutableListLikeHold([[1], [2]]) != MutableListLikeHold(
            [[1], [3]]
        )
        self.assertEqual(actual, [[1], [2]] != [[1], [3]])


class TestLessThanOperator(unittest.TestCase):
    def test_less_at_first_difference(self):
        actual = MutableListLikeHold([1, 2]) < MutableListLikeHold([1, 3])
        self.assertEqual(actual, [1, 2] < [1, 3])

    def test_less_when_prefix(self):
        actual = MutableListLikeHold([1]) < MutableListLikeHold([1, 0])
        self.assertEqual(actual, [1] < [1, 0])

    def test_less_false_for_equal(self):
        actual = MutableListLikeHold([1, 2]) < MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] < [1, 2])

    def test_less_empty(self):
        actual = MutableListLikeHold([]) < MutableListLikeHold([0])
        self.assertEqual(actual, [] < [0])


class TestLessThanOrEqualOperator(unittest.TestCase):
    def test_less_equal_when_less(self):
        actual = MutableListLikeHold([1, 2]) <= MutableListLikeHold([1, 3])
        self.assertEqual(actual, [1, 2] <= [1, 3])

    def test_less_equal_when_equal(self):
        actual = MutableListLikeHold([1, 2]) <= MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] <= [1, 2])

    def test_less_equal_false_when_greater(self):
        actual = MutableListLikeHold([2]) <= MutableListLikeHold([1])
        self.assertEqual(actual, [2] <= [1])

    def test_less_equal_prefix(self):
        actual = MutableListLikeHold([1]) <= MutableListLikeHold([1, 0])
        self.assertEqual(actual, [1] <= [1, 0])


class TestGreaterThanOperator(unittest.TestCase):
    def test_greater_at_first_difference(self):
        actual = MutableListLikeHold([1, 3]) > MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 3] > [1, 2])

    def test_greater_when_other_is_prefix(self):
        actual = MutableListLikeHold([1, 0]) > MutableListLikeHold([1])
        self.assertEqual(actual, [1, 0] > [1])

    def test_greater_false_for_equal(self):
        actual = MutableListLikeHold([1, 2]) > MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] > [1, 2])

    def test_greater_than_empty(self):
        actual = MutableListLikeHold([0]) > MutableListLikeHold([])
        self.assertEqual(actual, [0] > [])


class TestGreaterThanOrEqualOperator(unittest.TestCase):
    def test_greater_equal_when_greater(self):
        actual = MutableListLikeHold([1, 3]) >= MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 3] >= [1, 2])

    def test_greater_equal_when_equal(self):
        actual = MutableListLikeHold([1, 2]) >= MutableListLikeHold([1, 2])
        self.assertEqual(actual, [1, 2] >= [1, 2])

    def test_greater_equal_false_when_less(self):
        actual = MutableListLikeHold([1]) >= MutableListLikeHold([2])
        self.assertEqual(actual, [1] >= [2])

    def test_greater_equal_other_is_prefix(self):
        actual = MutableListLikeHold([1, 0]) >= MutableListLikeHold([1])
        self.assertEqual(actual, [1, 0] >= [1])


class TestMembershipOperator(unittest.TestCase):
    def test_contains_present_value(self):
        actual = 2 in MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual, 2 in [1, 2, 3])

    def test_contains_absent_value(self):
        actual = 4 in MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual, 4 in [1, 2, 3])

    def test_contains_none(self):
        actual = None in MutableListLikeHold([1, None, 2])
        self.assertEqual(actual, None in [1, None, 2])

    def test_contains_uses_equality(self):
        actual = True in MutableListLikeHold([1])
        self.assertEqual(actual, True in [1])


class TestNonMembershipOperator(unittest.TestCase):
    def test_not_contains_present_value(self):
        actual = 2 not in MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual, 2 not in [1, 2, 3])

    def test_not_contains_absent_value(self):
        actual = 4 not in MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual, 4 not in [1, 2, 3])

    def test_not_contains_none(self):
        actual = None not in MutableListLikeHold([1, None, 2])
        self.assertEqual(actual, None not in [1, None, 2])

    def test_not_contains_uses_equality(self):
        actual = True not in MutableListLikeHold([1])
        self.assertEqual(actual, True not in [1])


class TestIndexingOperator(unittest.TestCase):
    def test_get_first_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual[0], [1, 2, 3][0])

    def test_get_last_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual[-1], [1, 2, 3][-1])

    def test_get_middle_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(actual[1], [1, 2, 3][1])

    def test_get_out_of_range_raises_index_error(self):
        actual = MutableListLikeHold([1, 2, 3])
        with self.assertRaises(IndexError):
            actual[3]


class TestSlicingOperator(unittest.TestCase):
    def test_slice_start_stop(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[1:4]), [0, 1, 2, 3, 4][1:4])

    def test_slice_with_step(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[::2]), [0, 1, 2, 3, 4][::2])

    def test_slice_negative_bounds(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[-4:-1]), [0, 1, 2, 3, 4][-4:-1])

    def test_slice_reverse(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        self.assertEqual(list(actual[::-1]), [0, 1, 2, 3, 4][::-1])


class TestItemAssignmentOperator(unittest.TestCase):
    def test_set_first_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual[0] = 9
        expected[0] = 9
        self.assertEqual(list(actual), expected)

    def test_set_negative_index(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        actual[-1] = 9
        expected[-1] = 9
        self.assertEqual(list(actual), expected)

    def test_set_nested_value(self):
        value = [9]
        actual = MutableListLikeHold([1, 2, 3])
        actual[1] = value
        self.assertIs(actual[1], value)
        self.assertEqual(list(actual), [1, value, 3])

    def test_set_out_of_range_raises_index_error(self):
        actual = MutableListLikeHold([1, 2, 3])
        with self.assertRaises(IndexError):
            actual[3] = 9


class TestSliceAssignmentOperator(unittest.TestCase):
    def test_replace_slice_same_length(self):
        actual = MutableListLikeHold([0, 1, 2, 3])
        expected = [0, 1, 2, 3]
        actual[1:3] = [8, 9]
        expected[1:3] = [8, 9]
        self.assertEqual(list(actual), expected)

    def test_replace_slice_different_length(self):
        actual = MutableListLikeHold([0, 1, 2, 3])
        expected = [0, 1, 2, 3]
        actual[1:3] = [8, 9, 10]
        expected[1:3] = [8, 9, 10]
        self.assertEqual(list(actual), expected)

    def test_insert_with_empty_slice(self):
        actual = MutableListLikeHold([1, 3])
        expected = [1, 3]
        actual[1:1] = [2]
        expected[1:1] = [2]
        self.assertEqual(list(actual), expected)

    def test_extended_slice_requires_matching_length(self):
        actual = MutableListLikeHold([0, 1, 2, 3])
        with self.assertRaises(ValueError):
            actual[::2] = [9]


class TestItemDeletionOperator(unittest.TestCase):
    def test_delete_first_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        del actual[0]
        del expected[0]
        self.assertEqual(list(actual), expected)

    def test_delete_negative_index(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        del actual[-1]
        del expected[-1]
        self.assertEqual(list(actual), expected)

    def test_delete_middle_item(self):
        actual = MutableListLikeHold([1, 2, 3])
        expected = [1, 2, 3]
        del actual[1]
        del expected[1]
        self.assertEqual(list(actual), expected)

    def test_delete_out_of_range_raises_index_error(self):
        actual = MutableListLikeHold([1, 2, 3])
        with self.assertRaises(IndexError):
            del actual[3]


class TestSliceDeletionOperator(unittest.TestCase):
    def test_delete_middle_slice(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        expected = [0, 1, 2, 3, 4]
        del actual[1:4]
        del expected[1:4]
        self.assertEqual(list(actual), expected)

    def test_delete_slice_with_step(self):
        actual = MutableListLikeHold([0, 1, 2, 3, 4])
        expected = [0, 1, 2, 3, 4]
        del actual[::2]
        del expected[::2]
        self.assertEqual(list(actual), expected)

    def test_delete_empty_slice(self):
        actual = MutableListLikeHold([0, 1, 2])
        expected = [0, 1, 2]
        del actual[1:1]
        del expected[1:1]
        self.assertEqual(list(actual), expected)

    def test_delete_all_items_by_slice(self):
        actual = MutableListLikeHold([0, 1, 2])
        expected = [0, 1, 2]
        del actual[:]
        del expected[:]
        self.assertEqual(list(actual), expected)


class TestLengthOperator(unittest.TestCase):
    def test_len_empty(self):
        actual = MutableListLikeHold([])
        self.assertEqual(len(actual), len([]))

    def test_len_one(self):
        actual = MutableListLikeHold([1])
        self.assertEqual(len(actual), len([1]))

    def test_len_many(self):
        actual = MutableListLikeHold([1, 2, 3, 4])
        self.assertEqual(len(actual), len([1, 2, 3, 4]))

    def test_len_after_mutation(self):
        actual = MutableListLikeHold([1, 2])
        actual.append(3)
        self.assertEqual(len(actual), 3)


class TestIterationOperator(unittest.TestCase):
    def test_iterates_in_order(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(list(iter(actual)), [1, 2, 3])

    def test_iterates_empty(self):
        actual = MutableListLikeHold([])
        self.assertEqual(list(iter(actual)), [])

    def test_independent_iterators(self):
        actual = MutableListLikeHold([1, 2])
        first = iter(actual)
        second = iter(actual)
        self.assertEqual(next(first), 1)
        self.assertEqual(next(second), 1)

    def test_iterator_raises_stop_iteration(self):
        actual = MutableListLikeHold([1])
        iterator = iter(actual)
        self.assertEqual(next(iterator), 1)
        with self.assertRaises(StopIteration):
            next(iterator)


class TestReversedOperator(unittest.TestCase):
    def test_reversed_nonempty(self):
        actual = MutableListLikeHold([1, 2, 3])
        self.assertEqual(list(reversed(actual)), list(reversed([1, 2, 3])))

    def test_reversed_empty(self):
        actual = MutableListLikeHold([])
        self.assertEqual(list(reversed(actual)), list(reversed([])))

    def test_reversed_single_item(self):
        actual = MutableListLikeHold([1])
        self.assertEqual(list(reversed(actual)), list(reversed([1])))

    def test_reversed_does_not_mutate(self):
        actual = MutableListLikeHold([1, 2, 3])
        result = list(reversed(actual))
        self.assertEqual(result, [3, 2, 1])
        self.assertEqual(list(actual), [1, 2, 3])


class TestTruthValueOperator(unittest.TestCase):
    def test_empty_is_false(self):
        actual = MutableListLikeHold([])
        self.assertEqual(bool(actual), bool([]))

    def test_nonempty_is_true(self):
        actual = MutableListLikeHold([0])
        self.assertEqual(bool(actual), bool([0]))

    def test_falsey_elements_do_not_make_container_false(self):
        actual = MutableListLikeHold([False, None, 0])
        self.assertEqual(bool(actual), bool([False, None, 0]))

    def test_truth_value_after_clear(self):
        actual = MutableListLikeHold([1])
        actual.clear()
        self.assertEqual(bool(actual), bool([]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
