from __future__ import annotations

__all__: list[str] = [
    "TestOperatorsFrozenListSlot",
    "TestMethodsFrozenListSlot",
]

import unittest
from collections.abc import Iterator
from functools import wraps
from types import GenericAlias
from typing import Any, Callable, Self, get_args, get_origin

from datahold import FrozenListSlot


def tuple_deco[Case: Any](
    old: Callable[[Case, type[Any]], None],
    /,
) -> Callable[[Case], None]:
    @wraps(old)
    def new(self: Case, /) -> None:
        with self.subTest(type="tuple"):
            old(self, tuple)
        with self.subTest(type="FrozenListSlot"):
            old(self, FrozenListSlot)

    return new


def _negative_one(value: object, /) -> int:
    return -1


def _squares(limit: int, /) -> Iterator[int]:
    number: int

    for number in range(limit):
        yield number * number


def _parse_sequence_pattern(value: Any) -> list[Any]:
    first: Any
    rest: list[Any]
    second: Any

    match value:
        case [first, second, *rest]:
            return [first, second, rest]
        case []:
            return ["empty"]
        case _:
            return ["no match"]


class IndexOnly:
    """An integer-like object supporting __index__, but not __int__."""

    def __init__(self: Self, value: int) -> None:
        self.value: int = value

    def __index__(self: Self) -> int:
        return self.value


class IntOnly:
    """An object with __int__ but no __index__, which must be rejected."""

    def __int__(self: Self) -> int:
        return 2


class ExplodingEquality:
    """Checks that searches propagate exceptions raised by element equality."""

    def __eq__(self: Self, other: object) -> bool:
        raise RuntimeError("equality failed")


class TestOperatorsFrozenListSlot(unittest.TestCase):
    """One method per operator or operator-level protocol."""

    @tuple_deco
    def test_constructor(self: Self, cls: type[Any]) -> None:

        inner: Any
        original: list[int]
        outer: Any
        value: Any

        self.assertIsInstance(cls(), cls)
        self.assertEqual(cls(), cls([]))
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))
        self.assertEqual(cls(range(5)), cls([0, 1, 2, 3, 4]))
        self.assertEqual(cls(_squares(4)), cls([0, 1, 4, 9]))
        self.assertEqual(cls("abc"), cls(["a", "b", "c"]))
        self.assertEqual(cls(b"\x00\x01\xff"), cls([0, 1, 255]))
        self.assertEqual(
            cls({"first": 1, "second": 2}), cls(["first", "second"])
        )
        self.assertEqual(cls(iter([1, 2, 3])), cls([1, 2, 3]))

        inner = cls([8, 9])
        outer = cls([inner, "x"])
        self.assertIs(outer[0], inner)
        self.assertEqual(cls(inner), inner)
        self.assertIsInstance(cls(inner), cls)

        original = [1, 2]
        value = cls(original)
        original.append(3)
        self.assertEqual(value, cls([1, 2]))

        with self.assertRaises(TypeError):
            cls(None)
        with self.assertRaises(TypeError):
            cls(123)
        with self.assertRaises(TypeError):
            cls([1], [2])

        class BrokenIterable:
            def __iter__(self: Self) -> Iterator[Any]:
                raise RuntimeError("iteration failed")

        with self.assertRaises(RuntimeError):
            cls(BrokenIterable())

    @tuple_deco
    def test_add(self: Self, cls: type[Any]) -> None:
        _: Any
        a: Any
        b: Any
        expected: list[int]
        invalid: object
        left: Any
        other_cls: Any
        result: Any
        right: Any

        a, b = cls([1, 2]), cls([3, 4])
        for left, right, expected in [
            (a, b, [1, 2, 3, 4]),
            (cls(), a, [1, 2]),
            (a, cls(), [1, 2]),
            (cls(), cls(), []),
            (a, a, [1, 2, 1, 2]),
        ]:
            result = left + right
            self.assertIsInstance(result, cls)
            self.assertEqual(result, cls(expected))

        self.assertEqual(a, cls([1, 2]))
        self.assertEqual(b, cls([3, 4]))
        for invalid in ([3], "3", 3, None, range(2)):
            with self.assertRaises(TypeError):
                _ = a + invalid
            with self.assertRaises(TypeError):
                _ = invalid + a

        (other_cls,) = {tuple, FrozenListSlot} - {cls}
        with self.assertRaises(TypeError):
            _ = a + other_cls([3, 4])
        with self.assertRaises(TypeError):
            _ = other_cls([3, 4]) + a

    @tuple_deco
    def test_iadd(self: Self, cls: type[Any]) -> None:
        empty: Any
        value: Any

        value = cls([1, 2])
        value += cls([3, 4])
        self.assertIsInstance(value, cls)
        self.assertEqual(value, cls([1, 2, 3, 4]))
        value += cls()
        self.assertEqual(value, cls([1, 2, 3, 4]))
        empty = cls()
        empty += cls([5])
        self.assertEqual(empty, cls([5]))
        with self.assertRaises(TypeError):
            value += [6]
        self.assertEqual(value, cls([1, 2, 3, 4]))

    @tuple_deco
    def test_mul(self: Self, cls: type[Any]) -> None:
        _: Any
        count: int
        expected: list[int]
        invalid: object
        result: Any
        value: Any

        value = cls([1, 2])
        for count, expected in [
            (0, []),
            (1, [1, 2]),
            (2, [1, 2, 1, 2]),
            (3, [1, 2, 1, 2, 1, 2]),
            (-1, []),
            (-100, []),
            (False, []),
            (True, [1, 2]),
        ]:
            with self.subTest(count=count):
                result = value * count
                self.assertIsInstance(result, cls)
                self.assertEqual(result, cls(expected))
        self.assertEqual(value * IndexOnly(2), cls([1, 2, 1, 2]))
        self.assertEqual(cls() * 50, cls())
        self.assertEqual(len(value * 1000), 2000)
        for invalid in (2.0, "2", None, IntOnly()):
            with self.subTest(invalid_type=type(invalid).__name__):
                with self.assertRaises(TypeError):
                    _ = value * invalid
        self.assertEqual(value, cls([1, 2]))

    @tuple_deco
    def test_rmul(self: Self, cls: type[Any]) -> None:
        _: Any
        count: int
        expected: list[str]
        invalid: object
        result: Any
        value: Any

        value = cls(["a", "b"])
        for count, expected in [
            (0, []),
            (1, ["a", "b"]),
            (2, ["a", "b", "a", "b"]),
            (-3, []),
            (False, []),
            (True, ["a", "b"]),
        ]:
            with self.subTest(count=count):
                result = count * value
                self.assertIsInstance(result, cls)
                self.assertEqual(result, cls(expected))
        self.assertEqual(IndexOnly(2) * value, cls(["a", "b", "a", "b"]))
        for invalid in (2.5, "2", None, IntOnly()):
            with self.assertRaises(TypeError):
                _ = invalid * value

    @tuple_deco
    def test_imul(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2])
        value *= 3
        self.assertIsInstance(value, cls)
        self.assertEqual(value, cls([1, 2, 1, 2, 1, 2]))
        value *= 0
        self.assertIsInstance(value, cls)
        self.assertEqual(value, cls())

        value = cls([7])
        value *= IndexOnly(2)
        self.assertEqual(value, cls([7, 7]))
        value *= -1
        self.assertEqual(value, cls())
        with self.assertRaises(TypeError):
            value *= 1.5

    @tuple_deco
    def test_getitem(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: int | list[int]
        index: object
        key: slice
        nested: Any
        result: Any
        value: Any

        value = cls([0, 1, 2, 3, 4, 5])
        for index, expected in [
            (0, 0),
            (3, 3),
            (5, 5),
            (-1, 5),
            (-6, 0),
            (True, 1),
            (False, 0),
            (IndexOnly(2), 2),
        ]:
            with self.subTest(index=index):
                self.assertEqual(value[index], expected)

        for index in (6, -7, 10**50, -(10**50)):
            with self.assertRaises(IndexError):
                _ = value[index]
        for index in (1.0, "0", None, IntOnly()):
            with self.assertRaises(TypeError):
                _ = value[index]
        with self.assertRaises(IndexError):
            _ = cls()[0]

        for key, expected in [
            (slice(None), [0, 1, 2, 3, 4, 5]),
            (slice(1, 4), [1, 2, 3]),
            (slice(2, None), [2, 3, 4, 5]),
            (slice(None, 3), [0, 1, 2]),
            (slice(2, 2), []),
            (slice(5, 2), []),
            (slice(-4, -1), [2, 3, 4]),
            (slice(-100, 100), [0, 1, 2, 3, 4, 5]),
            (slice(None, None, 2), [0, 2, 4]),
            (slice(1, None, 2), [1, 3, 5]),
            (slice(None, None, -1), [5, 4, 3, 2, 1, 0]),
            (slice(4, 1, -2), [4, 2]),
            (slice(None, None, -2), [5, 3, 1]),
            (slice(None, None, 10), [0]),
            (slice(None, None, -10), [5]),
            (slice(IndexOnly(1), IndexOnly(5), IndexOnly(2)), [1, 3]),
        ]:
            with self.subTest(slice_args=(key.start, key.stop, key.step)):
                result = value[key]
                self.assertIsInstance(result, cls)
                self.assertEqual(result, cls(expected))
        self.assertIsInstance(cls()[::], cls)
        self.assertEqual(cls()[::], cls())

        with self.assertRaises(ValueError):
            _ = value[::0]
        with self.assertRaises(TypeError):
            _ = value[::1.5]
        with self.assertRaises(TypeError):
            _ = value["1":]

        nested = cls(["nested"])
        self.assertIs(cls([nested])[0], nested)

    @tuple_deco
    def test_setitem(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2, 3])
        with self.assertRaises(TypeError):
            value[0] = 99
        with self.assertRaises(TypeError):
            value[-1] = 99
        with self.assertRaises(TypeError):
            value[1:2] = cls([99])
        with self.assertRaises(TypeError):
            value[:] = cls()
        self.assertEqual(value, cls([1, 2, 3]))

    @tuple_deco
    def test_delitem(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2, 3])
        with self.assertRaises(TypeError):
            del value[0]
        with self.assertRaises(TypeError):
            del value[-1]
        with self.assertRaises(TypeError):
            del value[1:]
        with self.assertRaises(TypeError):
            del value[:]
        self.assertEqual(value, cls([1, 2, 3]))

    @tuple_deco
    def test_contains(self: Self, cls: type[Any]) -> None:
        _: bool
        member: object
        nan: float
        nonmember: object
        value: Any

        value = cls([1, "abc", None, 1, cls([2, 3])])
        for member in (1, True, "abc", None, cls([2, 3])):
            self.assertTrue(member in value)
        for nonmember in (0, "ab", 2, cls([3, 2]), object()):
            self.assertFalse(nonmember in value)
        self.assertFalse(1 in cls())
        self.assertTrue(7 not in value)
        self.assertFalse(1 not in value)

        nan = float("nan")
        self.assertTrue(nan in cls([nan]))  # Membership checks identity first.
        self.assertFalse(float("nan") in cls([nan]))
        with self.assertRaises(RuntimeError):
            _ = 5 in cls([ExplodingEquality()])

    @tuple_deco
    def test_iter(self: Self, cls: type[Any]) -> None:
        first: Iterator[Any]
        second: Iterator[Any]
        value: Any
        x: Any

        value = cls([0, 1, 2, 3])
        self.assertEqual(list(iter(value)), [0, 1, 2, 3])
        self.assertEqual(list(value), [0, 1, 2, 3])
        self.assertEqual(list(iter(cls())), [])
        self.assertEqual([x * 2 for x in value], [0, 2, 4, 6])
        self.assertEqual(
            list(enumerate(value)), [(0, 0), (1, 1), (2, 2), (3, 3)]
        )
        self.assertEqual(list(zip(value, range(2))), [(0, 0), (1, 1)])
        self.assertEqual(sum(value), 6)
        self.assertEqual(min(value), 0)
        self.assertEqual(max(value), 3)

        first, second = iter(value), iter(value)
        self.assertIs(first, iter(first))
        self.assertEqual(next(first), 0)
        self.assertEqual(next(first), 1)
        self.assertEqual(next(second), 0)  # Independent iterators.
        self.assertEqual(list(first), [2, 3])
        with self.assertRaises(StopIteration):
            next(first)
        with self.assertRaises(StopIteration):
            next(first)
        self.assertEqual(list(second), [1, 2, 3])
        self.assertEqual(value, cls([0, 1, 2, 3]))

    @tuple_deco
    def test_reversed(self: Self, cls: type[Any]) -> None:
        reverse_it: Iterator[Any]
        value: Any

        value = cls([1, 2, 3, 4])
        self.assertEqual(list(reversed(value)), [4, 3, 2, 1])
        self.assertEqual(list(reversed(cls())), [])
        reverse_it = reversed(value)
        self.assertEqual(next(reverse_it), 4)
        self.assertEqual(list(reverse_it), [3, 2, 1])
        with self.assertRaises(StopIteration):
            next(reverse_it)
        self.assertEqual(value, cls([1, 2, 3, 4]))

    @tuple_deco
    def test_len(self: Self, cls: type[Any]) -> None:
        n: int

        for n in (0, 1, 2, 10, 1000):
            with self.subTest(size=n):
                self.assertEqual(len(cls(range(n))), n)
        self.assertEqual(len(cls([None, None, None])), 3)
        self.assertEqual(len(cls([cls([1, 2])])), 1)

    @tuple_deco
    def test_bool(self: Self, cls: type[Any]) -> None:
        element: object

        self.assertFalse(bool(cls()))
        for element in (None, False, 0, "", [], cls()):
            self.assertTrue(bool(cls([element])))
        self.assertTrue(bool(cls([0, 0])))
        self.assertFalse(not cls([0]))
        self.assertTrue(not cls())

    @tuple_deco
    def test_hash(self: Self, cls: type[Any]) -> None:
        a: Any
        b: Any
        elements: list[Any]

        for elements in ([], [1], [1, 2], ["a", None, 3], [cls([4, 5])]):
            with self.subTest(elements=elements):
                a, b = cls(elements), cls(elements)
                self.assertEqual(hash(a), hash(b))
                self.assertEqual(hash(a), hash(a))
                self.assertEqual(a, b)
                self.assertEqual({a: "value"}[b], "value")
                self.assertIn(b, {a})

        self.assertEqual(hash(cls([True])), hash(cls([1])))
        for elements in ([[]], [{}], [{1, 2}], [cls([[]])]):
            with self.assertRaises(TypeError):
                hash(cls(elements))

    @tuple_deco
    def test_eq(self: Self, cls: type[Any]) -> None:
        nan: float

        self.assertTrue(cls() == cls())
        self.assertTrue(cls([1, 2]) == cls([1, 2]))
        self.assertTrue(cls([True, 2.0]) == cls([1, 2]))
        self.assertTrue(cls([cls([1])]) == cls([cls([1])]))
        self.assertFalse(cls([1]) == cls())
        self.assertFalse(cls([1]) == cls([2]))
        self.assertFalse(cls([1, 2]) == cls([1, 2, 3]))
        self.assertFalse(cls([1, 2]) == [1, 2])
        self.assertFalse(cls([1, 2]) == object())
        self.assertFalse(cls() == None)  # noqa: E711 (deliberately tests ==)

        nan = float("nan")
        self.assertTrue(cls([nan]) == cls([nan]))
        self.assertFalse(cls([float("nan")]) == cls([float("nan")]))

    @tuple_deco
    def test_ne(self: Self, cls: type[Any]) -> None:
        nan: float

        self.assertFalse(cls() != cls())
        self.assertFalse(cls([1, 2]) != cls([1, 2]))
        self.assertFalse(cls([True]) != cls([1]))
        self.assertTrue(cls([1]) != cls())
        self.assertTrue(cls([1]) != cls([2]))
        self.assertTrue(cls([1]) != cls([1, 2]))
        self.assertTrue(cls([1]) != [1])
        self.assertTrue(cls([1]) != object())
        nan = float("nan")
        self.assertFalse(cls([nan]) != cls([nan]))
        self.assertTrue(cls([float("nan")]) != cls([float("nan")]))

    @tuple_deco
    def test_lt(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: bool
        left: list[int]
        right: list[int]

        for left, right, expected in [
            ([], [], False),
            ([], [0], True),
            ([0], [], False),
            ([1], [2], True),
            ([2], [1], False),
            ([1], [1], False),
            ([1], [1, 0], True),
            ([1, 2], [1, 3], True),
            ([1, 3], [1, 2], False),
            ([2, 0], [1, 99], False),
        ]:
            self.assertIs(cls(left) < cls(right), expected)
        with self.assertRaises(TypeError):
            _ = cls([1]) < [2]
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) < cls([1, "x"])

    @tuple_deco
    def test_le(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: bool
        left: list[int]
        right: list[int]

        for left, right, expected in [
            ([], [], True),
            ([], [0], True),
            ([0], [], False),
            ([1], [2], True),
            ([2], [1], False),
            ([1], [1], True),
            ([1], [1, 0], True),
            ([1, 2], [1, 3], True),
            ([1, 3], [1, 2], False),
        ]:
            self.assertIs(cls(left) <= cls(right), expected)
        with self.assertRaises(TypeError):
            _ = cls([1]) <= [2]
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) <= cls([1, "x"])

    @tuple_deco
    def test_gt(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: bool
        left: list[int]
        right: list[int]

        for left, right, expected in [
            ([], [], False),
            ([], [0], False),
            ([0], [], True),
            ([1], [2], False),
            ([2], [1], True),
            ([1], [1], False),
            ([1], [1, 0], False),
            ([1, 2], [1, 3], False),
            ([1, 3], [1, 2], True),
        ]:
            self.assertIs(cls(left) > cls(right), expected)
        with self.assertRaises(TypeError):
            _ = cls([1]) > [2]
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) > cls([1, "x"])

    @tuple_deco
    def test_ge(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: bool
        left: list[int]
        right: list[int]

        for left, right, expected in [
            ([], [], True),
            ([], [0], False),
            ([0], [], True),
            ([1], [2], False),
            ([2], [1], True),
            ([1], [1], True),
            ([1], [1, 0], False),
            ([1, 2], [1, 3], False),
            ([1, 3], [1, 2], True),
        ]:
            self.assertIs(cls(left) >= cls(right), expected)
        with self.assertRaises(TypeError):
            _ = cls([1]) >= [2]
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) >= cls([1, "x"])

    @tuple_deco
    def test_unpacking(self: Self, cls: type[Any]) -> None:
        a: Any
        b: Any
        c: Any
        first: Any
        last: Any
        middle: list[Any]
        rest: list[Any]

        a, b, c = cls([10, 20, 30])
        self.assertEqual([a, b, c], [10, 20, 30])
        first, *middle, last = cls([0, 1, 2, 3])
        self.assertEqual(first, 0)
        self.assertEqual(
            middle, [1, 2]
        )  # Star-unpacking always returns a list.
        self.assertEqual(last, 3)
        first, *rest = cls([5])
        self.assertEqual(first, 5)
        self.assertEqual(rest, [])
        with self.assertRaises(ValueError):
            a, b = cls([1])
        with self.assertRaises(ValueError):
            a, b = cls([1, 2, 3])

    @tuple_deco
    def test_class_getitem(self: Self, cls: type[Any]) -> None:
        alias: GenericAlias
        annotation: type[Any]

        for annotation in (int, str, object):
            alias = cls[annotation]
            self.assertIs(get_origin(alias), cls)
            self.assertEqual(get_args(alias), (annotation,))
        alias = cls[int, str]
        self.assertIs(get_origin(alias), cls)
        self.assertEqual(get_args(alias), (int, str))
        alias = cls[int, ...]
        self.assertIs(get_origin(alias), cls)
        self.assertEqual(get_args(alias), (int, Ellipsis))

    @tuple_deco
    def test_setattr(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2])
        with self.assertRaises(AttributeError):
            value.new_attribute = 123
        with self.assertRaises(AttributeError):
            value.count = _negative_one
        self.assertEqual(value, cls([1, 2]))

    @tuple_deco
    def test_delattr(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2])
        with self.assertRaises(AttributeError):
            del value.no_such_attribute
        with self.assertRaises(AttributeError):
            del value.count
        self.assertEqual(value, cls([1, 2]))

    @tuple_deco
    def test_call(self: Self, cls: type[Any]) -> None:
        with self.assertRaises(TypeError):
            cls([1, 2])()

    @tuple_deco
    def test_sequence_pattern_matching(self: Self, cls: type[Any]) -> None:
        self.assertEqual(_parse_sequence_pattern(cls()), ["empty"])
        self.assertEqual(_parse_sequence_pattern(cls([1])), ["no match"])
        self.assertEqual(_parse_sequence_pattern(cls([1, 2])), [1, 2, []])
        self.assertEqual(
            _parse_sequence_pattern(cls([1, 2, 3, 4])), [1, 2, [3, 4]]
        )


class TestMethodsFrozenListSlot(unittest.TestCase):
    """The two public methods defined by tuple: count() and index()."""

    @tuple_deco
    def test_count(self: Self, cls: type[Any]) -> None:
        nan: float
        value: Any

        value = cls([1, 2, 1, 3, 1, 2, None, False, 0, 1.0])
        self.assertEqual(value.count(1), 4)
        self.assertEqual(value.count(True), 4)
        self.assertEqual(value.count(2), 2)
        self.assertEqual(value.count(3), 1)
        self.assertEqual(value.count(None), 1)
        self.assertEqual(value.count(0), 2)
        self.assertEqual(value.count(False), 2)
        self.assertEqual(value.count(999), 0)
        self.assertEqual(cls().count(1), 0)
        self.assertEqual(cls([[], [1], []]).count([]), 2)
        self.assertEqual(
            cls([cls([1]), cls([2]), cls([1])]).count(cls([1])), 2
        )

        nan = float("nan")
        self.assertEqual(cls([nan, nan]).count(nan), 2)
        self.assertEqual(cls([nan, nan]).count(float("nan")), 0)
        with self.assertRaises(RuntimeError):
            cls([ExplodingEquality()]).count(123)

        with self.assertRaises(TypeError):
            value.count()
        with self.assertRaises(TypeError):
            value.count(1, 0)
        with self.assertRaises(TypeError):
            value.count(value=1)

    @tuple_deco
    def test_index(self: Self, cls: type[Any]) -> None:
        args: tuple[object, ...]
        expected: int
        nan: float
        value: Any

        value = cls([0, 1, 0, 2, 0])
        for args, expected in [
            ((0,), 0),
            ((1,), 1),
            ((2,), 3),
            ((0, 1), 2),
            ((0, 3), 4),
            ((0, 1, 4), 2),
            ((0, 3, 5), 4),
            ((0, -3), 2),
            ((0, -2), 4),
            ((0, -100), 0),
            ((0, 0, -1), 0),
            ((0, 0, 100), 0),
            ((0, 0, 5), 0),
            ((0, False, True), 0),
            ((0, IndexOnly(1), IndexOnly(4)), 2),
            ((0, -(10**50), 10**50), 0),
        ]:
            with self.subTest(args=args):
                self.assertEqual(value.index(*args), expected)

        for args in [
            (9,),
            (0, 5),
            (0, 0, 0),
            (0, 4, 4),
            (0, 2, 2),
            (1, 2),
            (0, 100),
            (0, 3, 3),
            (0, 1, -4),
        ]:
            with self.subTest(missing_args=args):
                with self.assertRaises(ValueError):
                    value.index(*args)
        with self.assertRaises(ValueError):
            cls().index(0)

        self.assertEqual(cls([[], [1], []]).index([]), 0)
        self.assertEqual(cls([cls([1]), cls([2])]).index(cls([2])), 1)
        nan = float("nan")
        self.assertEqual(cls([nan]).index(nan), 0)
        with self.assertRaises(ValueError):
            cls([nan]).index(float("nan"))
        with self.assertRaises(RuntimeError):
            cls([ExplodingEquality()]).index(123)

        for args in [
            (0, 1.0),
            (0, None),
            (0, IntOnly()),
            (0, 0, 1.5),
            (0, 0, None),
            (0, 0, "5"),
            (),
            (0, 0, 0, 0),
        ]:
            with self.subTest(invalid_args=args):
                with self.assertRaises(TypeError):
                    value.index(*args)
        with self.assertRaises(TypeError):
            value.index(value=0)
        with self.assertRaises(TypeError):
            value.index(0, start=0)
        with self.assertRaises(TypeError):
            value.index(0, stop=3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
