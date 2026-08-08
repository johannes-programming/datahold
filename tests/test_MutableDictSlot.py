__all__: list[str] = [
    "TestMethodClear",
    "TestMethodCopy",
    "TestMethodFromKeys",
    "TestMethodGet",
    "TestMethodItems",
    "TestMethodKeys",
    "TestMethodPop",
    "TestMethodPopItem",
    "TestMethodSetDefault",
    "TestMethodUpdate",
    "TestMethodValues",
    "TestOperatorContains",
    "TestOperatorDelItem",
    "TestOperatorEqual",
    "TestOperatorGetItem",
    "TestOperatorInPlaceUnion",
    "TestOperatorIteration",
    "TestOperatorLength",
    "TestOperatorNotEqual",
    "TestOperatorReversed",
    "TestOperatorReverseUnion",
    "TestOperatorSetItem",
    "TestOperatorTruthiness",
]


import unittest
from collections import abc
from typing import Any, Self

from datahold import MutableDictSlot


class TestMethodClear(unittest.TestCase):
    def test_clear_removes_all_entries(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        value.clear()
        self.assertEqual(value, {})
        self.assertEqual(len(value), 0)

    def test_clear_empty_mapping(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        value.clear()
        self.assertEqual(value, {})
        self.assertFalse(value)

    def test_clear_returns_none(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.clear()  # type: ignore[func-returns-value]
        self.assertIsNone(result)
        self.assertEqual(value, {})

    def test_clear_updates_existing_views(self: Self, /) -> None:
        items_view: abc.Collection[Any]
        keys_view: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        keys_view = value.keys()
        items_view = value.items()
        value.clear()
        self.assertEqual(list(keys_view), [])
        self.assertEqual(list(items_view), [])


class TestMethodCopy(unittest.TestCase):
    def test_copy_has_equal_contents(self: Self, /) -> None:
        copied: MutableDictSlot[Any, Any]
        original: MutableDictSlot[Any, Any]
        original = MutableDictSlot({"a": 1, "b": 2})
        copied = original.copy()
        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)

    def test_copy_of_empty_mapping(self: Self, /) -> None:
        copied: MutableDictSlot[Any, Any]
        original: MutableDictSlot[Any, Any]
        original = MutableDictSlot()
        copied = original.copy()
        self.assertEqual(copied, {})
        self.assertIsNot(copied, original)

    def test_copy_is_shallow(self: Self, /) -> None:
        copied: MutableDictSlot[Any, Any]
        nested: list[int]
        original: MutableDictSlot[Any, Any]
        nested = [1, 2]
        original = MutableDictSlot({"nested": nested})
        copied = original.copy()
        copied["nested"].append(3)  # type: ignore
        self.assertIs(copied["nested"], original["nested"])
        self.assertEqual(original["nested"], [1, 2, 3])

    def test_copy_has_independent_top_level_entries(self: Self, /) -> None:
        copied: MutableDictSlot[Any, Any]
        original: MutableDictSlot[Any, Any]
        original = MutableDictSlot({"a": 1})
        copied = original.copy()
        copied["a"] = 2
        copied["b"] = 3
        self.assertEqual(original, {"a": 1})
        self.assertEqual(copied, {"a": 2, "b": 3})


class TestMethodFromKeys(unittest.TestCase):
    def test_fromkeys_uses_none_by_default(self: Self, /) -> None:
        result: Any
        result = MutableDictSlot.fromkeys(["a", "b", "c"])
        self.assertEqual(result, {"a": None, "b": None, "c": None})
        self.assertEqual(list(result), ["a", "b", "c"])

    def test_fromkeys_uses_supplied_value(self: Self, /) -> None:
        result: MutableDictSlot[Any, Any]
        result = MutableDictSlot.fromkeys(["a", "b"], 10)
        self.assertEqual(result, {"a": 10, "b": 10})
        self.assertEqual(result["a"], 10)

    def test_fromkeys_ignores_duplicate_keys(self: Self, /) -> None:
        result: MutableDictSlot[Any, Any]
        result = MutableDictSlot.fromkeys(["a", "b", "a", "c", "b"], 0)
        self.assertEqual(result, {"a": 0, "b": 0, "c": 0})
        self.assertEqual(list(result), ["a", "b", "c"])

    def test_fromkeys_reuses_same_mutable_value(self: Self, /) -> None:
        result: MutableDictSlot[Any, Any]
        shared: list[Any]
        shared = []
        result = MutableDictSlot.fromkeys(["a", "b"], shared)
        result["a"].append(1)  # type: ignore
        self.assertIs(result["a"], shared)
        self.assertIs(result["b"], shared)
        self.assertEqual(result["b"], [1])


class TestMethodGet(unittest.TestCase):
    def test_get_returns_existing_value(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        self.assertEqual(value.get("a"), 1)
        self.assertEqual(value, {"a": 1})

    def test_get_returns_none_for_missing_key(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.get("missing")
        self.assertIsNone(result)
        self.assertNotIn("missing", value)

    def test_get_returns_custom_default(self: Self, /) -> None:
        default: object
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        default = object()
        result = value.get("missing", default)
        self.assertIs(result, default)
        self.assertEqual(value, {})

    def test_get_rejects_unhashable_key(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        self.assertIsNone(value.get([]))
        self.assertEqual(value, {"a": 1})


class TestMethodItems(unittest.TestCase):
    def test_items_contains_key_value_pairs(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.items()
        self.assertEqual(set(result), {("a", 1), ("b", 2)})
        self.assertEqual(len(result), 2)

    def test_items_preserves_iteration_order(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        value["first"] = 1
        value["second"] = 2
        value["third"] = 3
        self.assertEqual(
            list(value.items()),
            [("first", 1), ("second", 2), ("third", 3)],
        )

    def test_items_view_is_dynamic(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.items()
        value["a"] = 2
        value["b"] = 3
        self.assertEqual(list(result), [("a", 2), ("b", 3)])

    def test_items_supports_pair_membership(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.items()
        self.assertIn(("a", 1), result)
        self.assertIn(("b", 2), result)
        self.assertNotIn(("a", 2), result)
        self.assertNotIn(("missing", 1), result)


class TestMethodKeys(unittest.TestCase):
    def test_keys_contains_all_keys(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.keys()
        self.assertEqual(set(result), {"a", "b"})
        self.assertEqual(len(result), 2)

    def test_keys_preserves_iteration_order(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        value["first"] = 1
        value["second"] = 2
        value["third"] = 3
        self.assertEqual(
            list(value.keys()),
            ["first", "second", "third"],
        )

    def test_keys_view_is_dynamic(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.keys()
        del value["a"]
        value["c"] = 3
        self.assertEqual(list(result), ["b", "c"])

    def test_keys_supports_membership(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.keys()
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertNotIn("missing", result)
        self.assertNotIn(1, result)


class TestMethodPop(unittest.TestCase):
    def test_pop_returns_and_removes_existing_value(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.pop("a")
        self.assertEqual(result, 1)
        self.assertEqual(value, {"b": 2})

    def test_pop_missing_key_raises_key_error(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        with self.assertRaises(KeyError) as context:
            value.pop("missing")
        self.assertEqual(context.exception.args, ("missing",))
        self.assertEqual(value, {"a": 1})

    def test_pop_missing_key_returns_default(self: Self, /) -> None:
        default: object
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        default = object()
        result = value.pop("missing", default)
        self.assertIs(result, default)
        self.assertEqual(value, {"a": 1})

    def test_pop_handles_none_as_explicit_default(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        result = value.pop("missing", None)
        self.assertIsNone(result)
        self.assertEqual(value, {})


class TestMethodPopItem(unittest.TestCase):
    def test_popitem_removes_last_inserted_pair(self: Self, /) -> None:
        result: tuple[Any, Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2, "c": 3})
        result = value.popitem()
        self.assertEqual(result, ("c", 3))
        self.assertEqual(value, {"a": 1, "b": 2})

    def test_popitem_uses_lifo_order_repeatedly(self: Self, /) -> None:
        first: tuple[Any, Any]
        second: tuple[Any, Any]
        third: tuple[Any, Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2, "c": 3})
        first = value.popitem()
        second = value.popitem()
        third = value.popitem()
        self.assertEqual(first, ("c", 3))
        self.assertEqual(second, ("b", 2))
        self.assertEqual(third, ("a", 1))
        self.assertEqual(len(value), 0)

    def test_popitem_removes_only_entry(self: Self, /) -> None:
        result: tuple[Any, Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.popitem()
        self.assertEqual(result, ("a", 1))
        self.assertEqual(value, {})

    def test_popitem_empty_mapping_raises_key_error(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        with self.assertRaises(KeyError):
            value.popitem()
        self.assertEqual(value, {})


class TestMethodSetDefault(unittest.TestCase):
    def test_setdefault_returns_existing_value(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.setdefault("a", 2)
        self.assertEqual(result, 1)
        self.assertEqual(value, {"a": 1})

    def test_setdefault_inserts_supplied_default(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        result = value.setdefault("b", 2)
        self.assertEqual(result, 2)
        self.assertEqual(value, {"a": 1, "b": 2})

    def test_setdefault_inserts_none_by_default(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        result = value.setdefault("a")
        self.assertIsNone(result)
        self.assertEqual(value, {"a": None})

    def test_setdefault_preserves_mutable_default_identity(
        self: Self, /
    ) -> None:
        default: list[Any]
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        default = []
        result = value.setdefault("a", default)
        result.append(1)
        self.assertIs(result, default)
        self.assertIs(value["a"], default)
        self.assertEqual(value["a"], [1])


class TestMethodUpdate(unittest.TestCase):
    def test_update_from_mapping(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        value.update({"b": 2, "c": 3})
        self.assertEqual(value, {"a": 1, "b": 2, "c": 3})

    def test_update_from_iterable_of_pairs(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        value.update([("b", 2), ("c", 3)])
        self.assertEqual(value, {"a": 1, "b": 2, "c": 3})

    def test_update_from_keyword_arguments(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1})
        value.update(b=2, c=3)
        self.assertEqual(value, {"a": 1, "b": 2, "c": 3})

    def test_update_overwrites_values_and_returns_none(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.update({"a": 10}, b=20, c=30)
        self.assertIsNone(result)
        self.assertEqual(value, {"a": 10, "b": 20, "c": 30})


class TestMethodValues(unittest.TestCase):
    def test_values_contains_all_values(self: Self, /) -> None:
        result: Any
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2, "c": 3})
        result = value.values()
        self.assertEqual(list(result), [1, 2, 3])
        self.assertEqual(len(result), 3)

    def test_values_preserves_iteration_order(self: Self, /) -> None:
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot()
        value["first"] = 10
        value["second"] = 20
        value["third"] = 30

        self.assertEqual(list(value.values()), [10, 20, 30])

    def test_values_view_is_dynamic(self: Self, /) -> None:
        result: abc.Collection[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 2})
        result = value.values()
        value["a"] = 10
        del value["b"]
        value["c"] = 3
        self.assertEqual(list(result), [10, 3])

    def test_values_preserves_duplicate_values(self: Self, /) -> None:
        result: list[Any]
        value: MutableDictSlot[Any, Any]
        value = MutableDictSlot({"a": 1, "b": 1, "c": 2})
        result = list(value.values())
        self.assertEqual(result, [1, 1, 2])
        self.assertEqual(result.count(1), 2)


class TestOperatorGetItem(unittest.TestCase):
    def test_existing_key(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"name": "Alice"})
        self.assertEqual(slot["name"], "Alice")

    def test_missing_key_raises_key_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"name": "Alice"})
        with self.assertRaises(KeyError):
            _ = slot["missing"]

    def test_none_value(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"value": None})
        self.assertIsNone(slot["value"])

    def test_unhashable_key_raises_type_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        with self.assertRaises(Exception):
            _ = slot[["unhashable"]]


class TestOperatorSetItem(unittest.TestCase):
    def test_adds_new_key(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        slot["name"] = "Alice"
        self.assertEqual(slot, {"name": "Alice"})

    def test_replaces_existing_value(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"count": 1})
        slot["count"] = 2
        self.assertEqual(slot["count"], 2)

    def test_accepts_none_value(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        slot["value"] = None
        self.assertIn("value", slot)
        self.assertIsNone(slot["value"])

    def test_unhashable_key_raises_type_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        with self.assertRaises(TypeError):
            slot[["unhashable"]] = "value"


class TestOperatorDelItem(unittest.TestCase):
    def test_deletes_existing_key(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1, "b": 2})
        del slot["a"]
        self.assertEqual(slot, {"b": 2})

    def test_missing_key_raises_key_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        with self.assertRaises(KeyError):
            del slot["missing"]

    def test_delete_only_item_makes_empty(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        del slot["a"]
        self.assertEqual(slot, {})

    def test_unhashable_key_raises_type_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            del slot[["unhashable"]]


class TestOperatorContains(unittest.TestCase):
    def test_existing_key_is_contained(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        self.assertIn("a", slot)

    def test_missing_key_is_not_contained(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        self.assertNotIn("b", slot)

    def test_values_are_not_checked(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": "value"})
        self.assertNotIn("value", slot)

    def test_unhashable_key_raises_type_error(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        self.assertFalse(["unhashable"] in slot)


class TestOperatorEqual(unittest.TestCase):
    def test_equal_contents(self: Self, /) -> None:
        x: MutableDictSlot[str, int]
        y: MutableDictSlot[str, int]
        x = MutableDictSlot({"a": 1, "b": 2})
        y = MutableDictSlot({"a": 1, "b": 2})
        self.assertTrue(x == x)
        self.assertTrue(x == y)

    def test_order_does_not_affect_equality(self: Self, /) -> None:
        x: MutableDictSlot[str, int]
        y: MutableDictSlot[str, int]
        x = MutableDictSlot({"a": 1, "b": 2})
        y = MutableDictSlot({"b": 2, "a": 1})
        self.assertTrue(x == y)

    def test_equal_to_plain_dict(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertTrue(slot == {"a": 1})

    def test_different_values_are_not_equal(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertFalse(slot == {"a": 2})


class TestOperatorNotEqual(unittest.TestCase):
    def test_different_values(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertTrue(slot != {"a": 2})

    def test_different_keys(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertTrue(slot != {"b": 1})

    def test_different_lengths(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertTrue(slot != {"a": 1, "b": 2})

    def test_identical_contents_are_not_unequal(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot[str, int]({"a": 1})
        self.assertFalse(slot != {"a": 1})


class TestOperatorInPlaceUnion(unittest.TestCase):
    def test_adds_distinct_keys(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        slot |= {"b": 2}
        self.assertEqual(slot, {"a": 1, "b": 2})

    def test_overrides_duplicate_key(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        slot |= {"a": 2}
        self.assertEqual(slot, {"a": 2})

    def test_preserves_object_identity(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        original_id = id(slot)
        slot |= {"b": 2}
        self.assertEqual(id(slot), original_id)

    def test_accepts_iterable_of_pairs(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        slot |= [("b", 2), ("c", 3)]
        self.assertEqual(slot, {"a": 1, "b": 2, "c": 3})


class TestOperatorIteration(unittest.TestCase):
    def test_iterates_over_keys(self: Self, /) -> None:
        slot: MutableDictSlot[str, int]
        slot = MutableDictSlot({"a": 1, "b": 2})
        self.assertEqual(list(slot), ["a", "b"])

    def test_empty_slot_has_no_iterations(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        self.assertEqual(list(slot), [])

    def test_iteration_preserves_insertion_order(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        slot["third"] = 3
        slot["first"] = 1
        slot["second"] = 2
        self.assertEqual(list(slot), ["third", "first", "second"])

    def test_size_change_during_iteration_raises_runtime_error(
        self: Self, /
    ) -> None:
        init: list[tuple[str, int]]
        x: dict[str, int]
        x_iter: abc.Iterator[str]
        x_next: str
        y: MutableDictSlot[str, int]
        y_iter: abc.Iterator[str]
        y_next: str
        init = [("a", 1), ("b", 2)]
        x = dict(init)
        y = MutableDictSlot(init)
        x_iter = iter(x)
        y_iter = iter(y)
        x_next = next(x_iter)
        y_next = next(y_iter)
        self.assertEqual(x_next, y_next)
        x["c"] = 3
        y["c"] = 3
        self.assertListEqual(list(x), list(y))
        self.assertListEqual(list("abc"), list(y))


class TestOperatorReversed(unittest.TestCase):
    def test_reverses_key_order(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1, "b": 2, "c": 3})
        self.assertEqual(list(reversed(slot)), ["c", "b", "a"])

    def test_empty_slot_reverses_to_empty(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        self.assertEqual(list(reversed(slot)), [])

    def test_single_key(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        self.assertEqual(list(reversed(slot)), ["a"])

    def test_replacing_value_does_not_change_order(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1, "b": 2})
        slot["a"] = 3
        self.assertEqual(list(reversed(slot)), ["b", "a"])


class TestOperatorLength(unittest.TestCase):
    def test_empty_length(self: Self, /) -> None:
        self.assertEqual(len(MutableDictSlot()), 0)

    def test_nonempty_length(self: Self, /) -> None:
        x: MutableDictSlot[str, int]
        x = MutableDictSlot({"a": 1, "b": 2})
        self.assertEqual(len(x), 2)

    def test_replacing_value_does_not_change_length(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        slot["a"] = 2
        self.assertEqual(len(slot), 1)

    def test_adding_and_deleting_changes_length(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot()
        slot["a"] = 1
        slot["b"] = 2
        del slot["a"]
        self.assertEqual(len(slot), 1)


class TestOperatorTruthiness(unittest.TestCase):
    def test_empty_slot_is_false(self: Self, /) -> None:
        self.assertFalse(MutableDictSlot())

    def test_nonempty_slot_is_true(self: Self, /) -> None:
        self.assertTrue(MutableDictSlot({"a": 1}))

    def test_false_value_still_makes_slot_true(self: Self, /) -> None:
        self.assertTrue(MutableDictSlot({"a": False}))

    def test_deleting_last_key_makes_slot_false(self: Self, /) -> None:
        slot: MutableDictSlot[Any, Any]
        slot = MutableDictSlot({"a": 1})
        del slot["a"]
        self.assertFalse(slot)


if __name__ == "__main__":
    unittest.main()
