import unittest
from collections import abc
from typing import Any, Self

from datahold import MutableDictSlot


class TestClear(unittest.TestCase):
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


class TestCopy(unittest.TestCase):
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


class TestFromKeys(unittest.TestCase):
    def test_fromkeys_uses_none_by_default(self: Self, /) -> None:
        result: MutableDictSlot[Any, Any]
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


class TestGet(unittest.TestCase):
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


class TestItems(unittest.TestCase):
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


class TestKeys(unittest.TestCase):
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


class TestPop(unittest.TestCase):
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


class TestPopItem(unittest.TestCase):
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


class TestSetDefault(unittest.TestCase):
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


class TestUpdate(unittest.TestCase):
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


class TestValues(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
