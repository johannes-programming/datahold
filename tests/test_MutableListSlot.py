from __future__ import annotations

__all__: list[str] = [
    "TestMethodsMutableListSlot",
    "TestOperatorsMutableListSlot",
]

import unittest
from collections.abc import Iterator
from functools import wraps
from types import GenericAlias
from typing import Any, Callable, Self, get_args, get_origin

from datahold import MutableListSlot


def _first(value: list[int], /) -> int:
    return value[0]


def _negative_one(value: object, /) -> int:
    return -1


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


def _raise_on_three(value: int, /) -> int:
    if value == 3:
        raise RuntimeError("key failed")
    return value


def _squares(limit: int, /) -> Iterator[int]:
    number: int

    for number in range(limit):
        yield number * number


def list_deco[Case](
    old: Callable[[Case, type[Any]], None],
    /,
) -> Callable[[Case], None]:

    @wraps(old)
    def new(self: Case, /) -> None:
        old(self, list)
        old(self, MutableListSlot)

    return new


class IndexOnly:
    """An object that is a legal sequence index through __index__."""

    __slots__ = ("value",)
    value: int

    def __init__(self: Self, value: int) -> None:
        self.value = value

    def __index__(self: Self) -> int:
        return self.value


class IntOnly:
    """An object with __int__, but no __index__."""

    def __int__(self: Self) -> int:
        return 2


class ExplodingEquality:
    """Ensures that comparisons triggered by searches propagate errors."""

    def __eq__(self: Self, other: object) -> bool:
        raise RuntimeError("equality failed")


class TestMethodsMutableListSlot(unittest.TestCase):
    """One decorated test method for each of list's eleven public methods."""

    @list_deco
    def test_append(self: Self, cls: type[Any]) -> None:
        child: Any
        result: Any
        value: Any

        value = cls()
        result = value.append(1)
        self.assertIsNone(result)
        self.assertEqual(value, cls([1]))
        self.assertIsNone(value.append(None))
        child = cls([3])
        value.append(child)
        self.assertIs(value[2], child)
        self.assertEqual(value, cls([1, None, child]))
        with self.assertRaises(TypeError):
            value.append()
        with self.assertRaises(TypeError):
            value.append(1, 2)
        with self.assertRaises(TypeError):
            value.append(object=1)
        self.assertEqual(len(value), 3)

    @list_deco
    def test_clear(self: Self, cls: type[Any]) -> None:
        original: Any
        value: Any

        value = cls([1, 2, 3])
        original = value
        self.assertIsNone(value.clear())
        self.assertIs(value, original)
        self.assertEqual(value, cls())
        self.assertIsNone(value.clear())
        with self.assertRaises(TypeError):
            value.clear(1)
        with self.assertRaises(TypeError):
            value.clear(value=1)

    @list_deco
    def test_copy(self: Self, cls: type[Any]) -> None:
        child: Any
        copied: Any
        original: Any

        child = cls([1])
        original = cls([child, 2])
        copied = original.copy()
        self.assertIsInstance(copied, cls)
        self.assertIsNot(copied, original)
        self.assertEqual(copied, original)
        self.assertIs(copied[0], child)
        copied.append(3)
        self.assertEqual(original, cls([child, 2]))
        self.assertEqual(copied, cls([child, 2, 3]))
        copied = cls().copy()
        self.assertIsInstance(copied, cls)
        self.assertEqual(copied, cls())
        with self.assertRaises(TypeError):
            original.copy(1)
        with self.assertRaises(TypeError):
            original.copy(value=1)

    @list_deco
    def test_count(self: Self, cls: type[Any]) -> None:
        nan: float
        value: Any

        value = cls([1, 2, 1, 3, 1, 2, None, False, 0, 1.0])
        self.assertEqual(value.count(1), 4)
        self.assertEqual(value.count(True), 4)
        self.assertEqual(value.count(2), 2)
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
            value.count(1, 2)
        with self.assertRaises(TypeError):
            value.count(value=1)

    @list_deco
    def test_extend(self: Self, cls: type[Any]) -> None:
        original: Any
        value: Any

        value = cls([1])
        original = value
        self.assertIsNone(value.extend(cls([2, 3])))
        self.assertEqual(value, cls([1, 2, 3]))
        self.assertIsNone(value.extend(range(2)))
        self.assertEqual(value, cls([1, 2, 3, 0, 1]))
        self.assertIsNone(value.extend(_squares(3)))
        self.assertEqual(value, cls([1, 2, 3, 0, 1, 0, 1, 4]))
        self.assertIsNone(value.extend("xy"))
        self.assertEqual(value[-2:], cls(["x", "y"]))
        self.assertIsNone(value.extend(cls()))
        self.assertIs(value, original)
        value = cls([9, 8])
        self.assertIsNone(value.extend(value))
        self.assertEqual(value, cls([9, 8, 9, 8]))
        with self.assertRaises(TypeError):
            value.extend(3)
        with self.assertRaises(TypeError):
            value.extend()
        with self.assertRaises(TypeError):
            value.extend([1], [2])
        with self.assertRaises(TypeError):
            value.extend(iterable=[3])
        self.assertEqual(value, cls([9, 8, 9, 8]))

    @list_deco
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

    @list_deco
    def test_insert(self: Self, cls: type[Any]) -> None:
        original: Any
        value: Any

        value = cls([2, 3])
        original = value
        self.assertIsNone(value.insert(0, 1))
        self.assertEqual(value, cls([1, 2, 3]))
        self.assertIsNone(value.insert(1, 9))
        self.assertEqual(value, cls([1, 9, 2, 3]))
        self.assertIsNone(value.insert(-1, 8))
        self.assertEqual(value, cls([1, 9, 2, 8, 3]))
        self.assertIsNone(value.insert(-100, 0))
        self.assertEqual(value, cls([0, 1, 9, 2, 8, 3]))
        self.assertIsNone(value.insert(100, 10))
        self.assertEqual(value, cls([0, 1, 9, 2, 8, 3, 10]))
        self.assertIsNone(value.insert(IndexOnly(2), 7))
        self.assertEqual(value, cls([0, 1, 7, 9, 2, 8, 3, 10]))
        self.assertIs(value, original)
        with self.assertRaises(TypeError):
            value.insert(1.2, 3)
        with self.assertRaises(TypeError):
            value.insert(IntOnly(), 3)
        with self.assertRaises(TypeError):
            value.insert(0)
        with self.assertRaises(TypeError):
            value.insert(0, 1, 2)
        with self.assertRaises(TypeError):
            value.insert(index=0, object=1)

    @list_deco
    def test_pop(self: Self, cls: type[Any]) -> None:
        _: Any
        original: Any
        value: Any

        value = cls([0, 1, 2, 3])
        original = value
        self.assertEqual(value.pop(), 3)
        self.assertEqual(value, cls([0, 1, 2]))
        self.assertEqual(value.pop(0), 0)
        self.assertEqual(value, cls([1, 2]))
        self.assertEqual(value.pop(IndexOnly(-2)), 1)
        self.assertEqual(value, cls([2]))
        self.assertEqual(value.pop(-1), 2)
        self.assertIs(value, original)
        self.assertEqual(value, cls())
        with self.assertRaises(IndexError):
            value.pop()
        with self.assertRaises(IndexError):
            value.pop(0)
        with self.assertRaises(IndexError):
            cls([1]).pop(1)
        with self.assertRaises(IndexError):
            cls([1]).pop(-2)
        for _ in (1.5, None, "0", IntOnly()):
            with self.assertRaises(TypeError):
                cls([1]).pop(_)
        with self.assertRaises(TypeError):
            cls([1]).pop(0, 1)

    @list_deco
    def test_remove(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2, 1, 3, 2])
        self.assertIsNone(value.remove(1))
        self.assertEqual(value, cls([2, 1, 3, 2]))
        self.assertIsNone(value.remove(2))
        self.assertEqual(value, cls([1, 3, 2]))
        self.assertIsNone(value.remove(True))
        self.assertEqual(value, cls([3, 2]))
        with self.assertRaises(ValueError):
            value.remove(99)
        self.assertEqual(value, cls([3, 2]))
        with self.assertRaises(ValueError):
            cls().remove(1)
        with self.assertRaises(RuntimeError):
            cls([ExplodingEquality()]).remove(123)
        with self.assertRaises(TypeError):
            value.remove()
        with self.assertRaises(TypeError):
            value.remove(1, 2)

    @list_deco
    def test_reverse(self: Self, cls: type[Any]) -> None:
        original: Any
        value: Any

        value = cls([1, 2, 3, 4])
        original = value
        self.assertIsNone(value.reverse())
        self.assertIs(value, original)
        self.assertEqual(value, cls([4, 3, 2, 1]))
        self.assertIsNone(value.reverse())
        self.assertEqual(value, cls([1, 2, 3, 4]))
        self.assertIsNone(cls().reverse())
        self.assertIsNone(cls([1]).reverse())
        with self.assertRaises(TypeError):
            value.reverse(True)
        with self.assertRaises(TypeError):
            value.reverse(value=1)

    @list_deco
    def test_sort(self: Self, cls: type[Any]) -> None:
        original: Any
        value: Any

        value = cls([3, 1, 4, 1, 5, 2])
        original = value
        self.assertIsNone(value.sort())
        self.assertIs(value, original)
        self.assertEqual(value, cls([1, 1, 2, 3, 4, 5]))
        self.assertIsNone(value.sort(reverse=True))
        self.assertEqual(value, cls([5, 4, 3, 2, 1, 1]))
        self.assertIsNone(value.sort(reverse=False))
        self.assertEqual(value, cls([1, 1, 2, 3, 4, 5]))
        self.assertIsNone(cls().sort())
        self.assertIsNone(cls([1]).sort())

        value = cls(["bbb", "A", "cc", "aaaa"])
        self.assertIsNone(value.sort(key=len))
        self.assertEqual(value, cls(["A", "cc", "bbb", "aaaa"]))
        value = cls(["a", "C", "b", "A"])
        self.assertIsNone(value.sort(key=str.lower))
        self.assertEqual(value, cls(["a", "A", "b", "C"]))
        value = cls([[2, 1], [1, 9], [2, 2], [1, 8]])
        self.assertIsNone(value.sort(key=_first))
        self.assertEqual(value, cls([[1, 9], [1, 8], [2, 1], [2, 2]]))
        self.assertIsNone(value.sort(key=_first, reverse=True))
        self.assertEqual(value, cls([[2, 1], [2, 2], [1, 9], [1, 8]]))
        with self.assertRaises(TypeError):
            cls([1, "a"]).sort()
        with self.assertRaises(RuntimeError):
            cls([2, 3, 1]).sort(key=_raise_on_three)
        with self.assertRaises(TypeError):
            cls([1]).sort(None)
        with self.assertRaises(TypeError):
            cls([1]).sort(key=3)
        with self.assertRaises(TypeError):
            cls([1]).sort(unknown=True)


class TestOperatorsMutableListSlot(unittest.TestCase):
    """One decorated test method per operator or operator-level protocol."""

    @list_deco
    def test_constructor(self: Self, cls: type[Any]) -> None:

        inner: Any
        original: list[int]
        outer: Any
        result: Any
        source: Any
        value: Any

        self.assertIsInstance(cls(), cls)
        self.assertEqual(cls(), cls([]))
        self.assertEqual(cls([1, 2]), cls([1, 2]))
        self.assertEqual(cls(range(4)), cls([0, 1, 2, 3]))
        self.assertEqual(cls(_squares(4)), cls([0, 1, 4, 9]))
        self.assertEqual(cls("ab"), cls(["a", "b"]))
        self.assertEqual(cls(b"\x00\xff"), cls([0, 255]))
        self.assertEqual(
            cls({"first": 1, "second": 2}), cls(["first", "second"])
        )
        self.assertEqual(cls(iter([1, 2])), cls([1, 2]))

        inner = cls([3])
        outer = cls([inner, "x"])
        self.assertIs(outer[0], inner)
        source = cls([4, 5])
        result = cls(source)
        self.assertIsInstance(result, cls)
        self.assertEqual(result, source)
        self.assertIsNot(result, source)
        source.append(6)
        self.assertEqual(result, cls([4, 5]))

        original = [1, 2]
        value = cls(original)
        original.append(3)
        self.assertEqual(value, cls([1, 2]))
        value.__init__([7, 8])
        self.assertEqual(value, cls([7, 8]))
        value.__init__()
        self.assertEqual(value, cls())

        with self.assertRaises(TypeError):
            cls(None)
        with self.assertRaises(TypeError):
            cls(10)
        with self.assertRaises(TypeError):
            cls([1], [2])

        class BrokenIterable:
            def __iter__(self: Self) -> Iterator[Any]:
                raise RuntimeError("iteration failed")

        with self.assertRaises(RuntimeError):
            cls(BrokenIterable())

    @list_deco
    def test_add(self: Self, cls: type[Any]) -> None:
        _: Any
        expected: list[int]
        left: Any
        other: object
        result: Any
        right: Any
        value: Any

        for left, right, expected in [
            (cls([1, 2]), cls([3, 4]), [1, 2, 3, 4]),
            (cls(), cls([1]), [1]),
            (cls([1]), cls(), [1]),
            (cls(), cls(), []),
            (cls([1]), cls([1]), [1, 1]),
        ]:
            result = left + right
            self.assertIsInstance(result, cls)
            self.assertEqual(result, cls(expected))
            self.assertEqual(left, cls(list(left)))

        value = cls([1, 2])
        for other in (range(2), "ab", 2, None, {3, 4}):
            with self.subTest(other=type(other).__name__):
                with self.assertRaises(TypeError):
                    _ = value + other
                with self.assertRaises(TypeError):
                    _ = other + value
        self.assertEqual(value, cls([1, 2]))

    @list_deco
    def test_iadd(self: Self, cls: type[Any]) -> None:
        before: Any
        result: Any
        value: Any

        value = cls([1, 2])
        before = value
        value += cls([3, 4])
        self.assertIs(value, before)
        self.assertEqual(value, cls([1, 2, 3, 4]))
        value += range(2)
        self.assertIs(value, before)
        self.assertEqual(value, cls([1, 2, 3, 4, 0, 1]))
        value += _squares(3)
        self.assertEqual(value, cls([1, 2, 3, 4, 0, 1, 0, 1, 4]))
        value += "ab"
        self.assertEqual(value[-2:], cls(["a", "b"]))
        with self.assertRaises(TypeError):
            value += 3
        result = cls([5])
        result += result
        self.assertEqual(result, cls([5, 5]))

    @list_deco
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
        self.assertEqual(cls() * 100, cls())
        self.assertEqual(len(value * 1000), 2000)
        for invalid in (2.5, "2", None, IntOnly()):
            with self.assertRaises(TypeError):
                _ = value * invalid
        self.assertEqual(value, cls([1, 2]))

    @list_deco
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

    @list_deco
    def test_imul(self: Self, cls: type[Any]) -> None:
        _: Any
        original: Any
        value: Any

        value = cls([1, 2])
        original = value
        value *= 3
        self.assertIs(value, original)
        self.assertEqual(value, cls([1, 2, 1, 2, 1, 2]))
        value *= 1
        self.assertIs(value, original)
        value *= 0
        self.assertIs(value, original)
        self.assertEqual(value, cls())
        value = cls([7])
        value *= IndexOnly(2)
        self.assertEqual(value, cls([7, 7]))
        value *= -1
        self.assertEqual(value, cls())
        with self.assertRaises(TypeError):
            value *= 1.5
        with self.assertRaises(TypeError):
            _ = cls([1]) * None

    @list_deco
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
                self.assertIsNot(result, value)
        with self.assertRaises(ValueError):
            _ = value[::0]
        with self.assertRaises(TypeError):
            _ = value[::1.5]
        with self.assertRaises(TypeError):
            _ = value["1":]
        nested = cls(["nested"])
        self.assertIs(cls([nested])[0], nested)

    @list_deco
    def test_setitem(self: Self, cls: type[Any]) -> None:
        _: Any
        item: Any
        value: Any

        value = cls([0, 1, 2, 3, 4, 5])
        value[0] = 10
        value[-1] = 50
        value[IndexOnly(1)] = 11
        value[True] = 12
        self.assertEqual(value, cls([10, 12, 2, 3, 4, 50]))
        with self.assertRaises(IndexError):
            value[6] = 0
        with self.assertRaises(IndexError):
            value[-7] = 0
        for item in (1.0, "1", None, IntOnly()):
            with self.assertRaises(TypeError):
                value[item] = 0

        value[1:4] = cls([20, 30])
        self.assertEqual(value, cls([10, 20, 30, 4, 50]))
        value[:2] = cls()
        self.assertEqual(value, cls([30, 4, 50]))
        value[1:1] = range(2)
        self.assertEqual(value, cls([30, 0, 1, 4, 50]))
        value[::2] = cls([9, 8, 7])
        self.assertEqual(value, cls([9, 0, 8, 4, 7]))
        value[::-2] = cls([5, 6, 7])
        self.assertEqual(value, cls([7, 0, 6, 4, 5]))
        with self.assertRaises(ValueError):
            value[::2] = cls([1])
        with self.assertRaises(ValueError):
            value[::-2] = cls([1, 2])
        with self.assertRaises(ValueError):
            value[::0] = cls([1])
        with self.assertRaises(TypeError):
            value[1:2] = 99
        with self.assertRaises(TypeError):
            value[1:2] = None
        self.assertEqual(value, cls([7, 0, 6, 4, 5]))

        value = cls([1, 2, 3])
        value[1:2] = _squares(3)
        self.assertEqual(value, cls([1, 0, 1, 4, 3]))
        value = cls([1, 2, 3])
        value[:] = value
        self.assertEqual(value, cls([1, 2, 3]))
        value[1:2] = value
        self.assertEqual(value, cls([1, 1, 2, 3, 3]))
        self.assertIsNone(value.__setitem__(0, 42))
        self.assertEqual(value[0], 42)

    @list_deco
    def test_delitem(self: Self, cls: type[Any]) -> None:
        _: Any
        value: Any

        value = cls([0, 1, 2, 3, 4, 5, 6])
        del value[0]
        self.assertEqual(value, cls([1, 2, 3, 4, 5, 6]))
        del value[-1]
        self.assertEqual(value, cls([1, 2, 3, 4, 5]))
        del value[IndexOnly(1)]
        self.assertEqual(value, cls([1, 3, 4, 5]))
        del value[1:3]
        self.assertEqual(value, cls([1, 5]))
        del value[:]
        self.assertEqual(value, cls())
        with self.assertRaises(IndexError):
            del value[0]
        with self.assertRaises(TypeError):
            del value[1.5]
        with self.assertRaises(TypeError):
            del value[None]

        value = cls(list(range(10)))
        del value[::2]
        self.assertEqual(value, cls([1, 3, 5, 7, 9]))
        del value[::-2]
        self.assertEqual(value, cls([3, 7]))
        with self.assertRaises(ValueError):
            del value[::0]
        self.assertIsNone(value.__delitem__(slice(None)))
        self.assertEqual(value, cls())

    @list_deco
    def test_contains(self: Self, cls: type[Any]) -> None:
        member: object
        missing: object
        nan: float
        value: Any

        value = cls([1, "ab", None, 1, cls([2, 3])])
        for member in (1, True, "ab", None, cls([2, 3])):
            self.assertTrue(member in value)
        for missing in (0, "a", 2, cls([3, 2]), object()):
            self.assertFalse(missing in value)
        self.assertFalse(1 in cls())
        nan = float("nan")
        self.assertTrue(nan in cls([nan]))
        self.assertFalse(float("nan") in cls([nan]))
        with self.assertRaises(RuntimeError):
            1 in cls([ExplodingEquality()])

    @list_deco
    def test_iter(self: Self, cls: type[Any]) -> None:
        iterator: Iterator[Any]
        value: Any

        value = cls([1, 2, 3])
        self.assertEqual(list(iter(value)), [1, 2, 3])
        self.assertEqual(list(value), [1, 2, 3])
        self.assertEqual(list(iter(cls())), [])
        iterator = iter(value)
        self.assertIs(iter(iterator), iterator)
        self.assertEqual(next(iterator), 1)
        value.append(4)
        self.assertEqual(list(iterator), [2, 3, 4])

        value = cls([1, 2, 3, 4])
        iterator = iter(value)
        self.assertEqual(next(iterator), 1)
        del value[1]
        self.assertEqual(list(iterator), [3, 4])
        iterator = iter(cls([8]))
        self.assertEqual(next(iterator), 8)
        with self.assertRaises(StopIteration):
            next(iterator)
        with self.assertRaises(StopIteration):
            next(iterator)

    @list_deco
    def test_reversed(self: Self, cls: type[Any]) -> None:
        iterator: Iterator[Any]
        value: Any

        value = cls([1, 2, 3])
        self.assertEqual(list(reversed(value)), [3, 2, 1])
        self.assertEqual(list(reversed(cls())), [])
        self.assertEqual(list(reversed(cls([4]))), [4])
        iterator = reversed(value)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(list(iterator), [2, 1])
        self.assertEqual(value, cls([1, 2, 3]))

        value = list("world")
        iterator = reversed(value)
        self.assertEqual(next(iterator, None), "d")
        self.assertEqual(next(iterator, None), "l")
        self.assertEqual(value.pop(1), "o")
        self.assertEqual(next(iterator, None), "l")
        self.assertEqual(next(iterator, None), "r")
        self.assertEqual(next(iterator, None), "w")
        self.assertEqual(next(iterator, None), None)

    @list_deco
    def test_len(self: Self, cls: type[Any]) -> None:
        count: int

        for count in (0, 1, 2, 8, 1000):
            self.assertEqual(len(cls(range(count))), count)
        self.assertEqual(len(cls("abc")), 3)

    @list_deco
    def test_bool(self: Self, cls: type[Any]) -> None:
        self.assertFalse(bool(cls()))
        self.assertTrue(bool(cls([0])))
        self.assertTrue(bool(cls([None])))
        self.assertTrue(bool(cls([False])))

    @list_deco
    def test_hash(self: Self, cls: type[Any]) -> None:
        with self.assertRaises(TypeError):
            hash(cls())
        with self.assertRaises(TypeError):
            hash(cls([1, 2]))

    @list_deco
    def test_eq(self: Self, cls: type[Any]) -> None:
        nan: float

        self.assertTrue(cls() == cls())
        self.assertTrue(cls([1, 2]) == cls([1, 2]))
        self.assertTrue(cls([True]) == cls([1]))
        self.assertFalse(cls([1]) == cls())
        self.assertFalse(cls([1]) == cls([2]))
        self.assertFalse(cls([1]) == cls([1, 2]))
        self.assertFalse(cls([1]) == object())
        nan = float("nan")
        self.assertTrue(cls([nan]) == cls([nan]))
        self.assertFalse(cls([float("nan")]) == cls([float("nan")]))

    @list_deco
    def test_ne(self: Self, cls: type[Any]) -> None:
        nan: float

        self.assertFalse(cls() != cls())
        self.assertFalse(cls([1, 2]) != cls([1, 2]))
        self.assertFalse(cls([True]) != cls([1]))
        self.assertTrue(cls([1]) != cls())
        self.assertTrue(cls([1]) != cls([2]))
        self.assertTrue(cls([1]) != cls([1, 2]))
        self.assertTrue(cls([1]) != object())
        nan = float("nan")
        self.assertFalse(cls([nan]) != cls([nan]))
        self.assertTrue(cls([float("nan")]) != cls([float("nan")]))

    @list_deco
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
            _ = cls([1]) < object()
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) < cls([1, "x"])

    @list_deco
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
            _ = cls([1]) <= object()
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) <= cls([1, "x"])

    @list_deco
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
            _ = cls([1]) > object()
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) > cls([1, "x"])

    @list_deco
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
            _ = cls([1]) >= object()
        with self.assertRaises(TypeError):
            _ = cls([1, 2]) >= cls([1, "x"])

    @list_deco
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
        self.assertEqual(middle, [1, 2])  # Star unpacking is always a list.
        self.assertEqual(last, 3)
        first, *rest = cls([5])
        self.assertEqual(first, 5)
        self.assertEqual(rest, [])
        with self.assertRaises(ValueError):
            a, b = cls([1])
        with self.assertRaises(ValueError):
            a, b = cls([1, 2, 3])

    @list_deco
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

    @list_deco
    def test_setattr(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2])
        with self.assertRaises(AttributeError):
            value.new_attribute = 123
        with self.assertRaises(AttributeError):
            value.count = _negative_one
        self.assertEqual(value, cls([1, 2]))

    @list_deco
    def test_delattr(self: Self, cls: type[Any]) -> None:
        value: Any

        value = cls([1, 2])
        with self.assertRaises(AttributeError):
            del value.nonexistent_attribute
        with self.assertRaises(AttributeError):
            del value.count
        self.assertEqual(value, cls([1, 2]))

    @list_deco
    def test_call(self: Self, cls: type[Any]) -> None:
        with self.assertRaises(TypeError):
            cls([1, 2])()

    @list_deco
    def test_sequence_pattern_matching(self: Self, cls: type[Any]) -> None:

        self.assertEqual(_parse_sequence_pattern(cls()), ["empty"])
        self.assertEqual(_parse_sequence_pattern(cls([1])), ["no match"])
        self.assertEqual(_parse_sequence_pattern(cls([1, 2])), [1, 2, []])
        self.assertEqual(
            _parse_sequence_pattern(cls([1, 2, 3, 4])), [1, 2, [3, 4]]
        )
