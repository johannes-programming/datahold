__all__: list[str] = []

import unittest
from typing import Self

from datahold import MutableListSlot


class TestOperatorReprRecursive(unittest.TestCase):

    def test_direct_self_reference(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot()
        value.append(value)
        self.assertEqual(repr(value), "MutableListSlot([...])")

    def test_indirect_reference_cycle(self: Self, /) -> None:
        first: MutableListSlot[object]
        second: MutableListSlot[object]
        first = MutableListSlot()
        second = MutableListSlot()
        first.append(second)
        second.append(first)
        self.assertEqual(
            repr(first),
            "MutableListSlot([MutableListSlot([...])])",
        )

    def test_self_reference_between_values(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot([1])
        value.append(value)
        value.append(2)
        self.assertEqual(
            repr(value),
            "MutableListSlot([1, ..., 2])",
        )

    def test_same_self_reference_twice(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot()
        value.extend((value, value))

        self.assertEqual(
            repr(value),
            "MutableListSlot([..., ...])",
        )

    def test_self_reference_inside_builtin_list(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        nested: list[object] = [value]
        value.append(nested)

        self.assertEqual(
            repr(value),
            "MutableListSlot([[...]])",
        )

    def test_self_reference_inside_tuple(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        nested: tuple[object, ...] = (value,)
        value.append(nested)

        self.assertEqual(
            repr(value),
            "MutableListSlot([(...,)])",
        )

    def test_self_reference_inside_dictionary(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        nested: dict[str, object] = {"value": value}
        value.append(nested)

        self.assertEqual(
            repr(value),
            "MutableListSlot([{'value': ...}])",
        )

    def test_two_object_cycle(self: Self, /) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.append(second)
        second.append(first)

        self.assertEqual(
            repr(first),
            "MutableListSlot([MutableListSlot([...])])",
        )

    def test_three_object_cycle(self: Self, /) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        third: MutableListSlot[object] = MutableListSlot()
        first.append(second)
        second.append(third)
        third.append(first)

        self.assertEqual(
            repr(first),
            (
                "MutableListSlot(["
                "MutableListSlot(["
                "MutableListSlot([...])"
                "])"
                "])"
            ),
        )

    def test_two_object_cycle_with_surrounding_values(
        self: Self,
        /,
    ) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.extend((1, second, 2))
        second.extend((3, first, 4))

        self.assertEqual(
            repr(first),
            ("MutableListSlot([1, " "MutableListSlot([3, ..., 4]), " "2])"),
        )

    def test_cycle_can_be_rendered_from_other_root(
        self: Self,
        /,
    ) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.extend((1, second, 2))
        second.extend((3, first, 4))

        self.assertEqual(
            repr(second),
            ("MutableListSlot([3, " "MutableListSlot([1, ..., 2]), " "4])"),
        )

    def test_two_independent_recursive_values(self: Self, /) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.append(first)
        second.append(second)

        self.assertEqual(repr(first), "MutableListSlot([...])")
        self.assertEqual(repr(second), "MutableListSlot([...])")

    def test_outer_collection_holding_recursive_values(
        self: Self,
        /,
    ) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.append(first)
        second.append(second)
        outer: MutableListSlot[object] = MutableListSlot(
            (first, second),
        )

        self.assertEqual(
            repr(outer),
            (
                "MutableListSlot(["
                "MutableListSlot([...]), "
                "MutableListSlot([...])"
                "])"
            ),
        )

    def test_recursive_subclass_uses_subclass_name(
        self: Self,
        /,
    ) -> None:
        class NamedMutableListSlot(MutableListSlot[object]):
            __slots__ = ()

        value = NamedMutableListSlot()
        value.append(value)

        self.assertEqual(
            repr(value),
            "NamedMutableListSlot([...])",
        )

    def test_repeated_repr_calls(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        value.append(value)

        expected = "MutableListSlot([...])"
        self.assertEqual(repr(value), expected)
        self.assertEqual(repr(value), expected)
        self.assertEqual(repr(value), expected)

    def test_guard_is_cleared_after_element_repr_raises(
        self: Self,
        /,
    ) -> None:
        class ExplodingRepr:
            def __repr__(self) -> str:
                raise RuntimeError("repr failed")

        value: MutableListSlot[object] = MutableListSlot(
            (ExplodingRepr(),),
        )

        with self.assertRaisesRegex(RuntimeError, "repr failed"):
            repr(value)

        value.clear()
        value.append(value)

        self.assertEqual(repr(value), "MutableListSlot([...])")

    def test_repr_after_indirect_cycle_is_broken(
        self: Self,
        /,
    ) -> None:
        first: MutableListSlot[object] = MutableListSlot()
        second: MutableListSlot[object] = MutableListSlot()
        first.append(second)
        second.append(first)

        self.assertIn("...", repr(first))

        second.clear()

        self.assertEqual(
            repr(first),
            "MutableListSlot([MutableListSlot([])])",
        )

    def test_repr_after_direct_cycle_is_replaced(
        self: Self,
        /,
    ) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        value.append(value)

        self.assertEqual(repr(value), "MutableListSlot([...])")

        value[0] = "replacement"

        self.assertEqual(
            repr(value),
            "MutableListSlot(['replacement'])",
        )

    def test_shallow_copy_of_recursive_value(self: Self, /) -> None:
        original: MutableListSlot[object] = MutableListSlot()
        original.append(original)

        copied = original.copy()

        self.assertEqual(
            repr(copied),
            "MutableListSlot([MutableListSlot([...])])",
        )

    def test_multiple_branches_back_to_root(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        list_branch: list[object] = [value]
        dict_branch: dict[str, object] = {"value": value}
        value.extend((list_branch, dict_branch))

        self.assertEqual(
            repr(value),
            "MutableListSlot([[...], {'value': ...}])",
        )

    def test_deep_mixed_container_cycle(self: Self, /) -> None:
        value: MutableListSlot[object] = MutableListSlot()
        tuple_level: tuple[object, ...] = (value,)
        dict_level: dict[str, object] = {"next": tuple_level}
        list_level: list[object] = [dict_level]
        value.append(list_level)

        self.assertEqual(
            repr(value),
            "MutableListSlot([[{'next': (...,)}]])",
        )

    def test_repr_hello(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot("hello")
        self.assertEqual(
            repr(value),
            "MutableListSlot(['h', 'e', 'l', 'l', 'o'])",
        )

    def test_repr_range(self: Self, /) -> None:
        value: MutableListSlot[object]
        value = MutableListSlot(range(2, 42, 5))
        self.assertEqual(
            repr(value),
            "MutableListSlot([2, 7, 12, 17, 22, 27, 32, 37])",
        )
