from __future__ import annotations

__all__: list[str] = [
    "Mirror",
    "MirrorFrozenDictSlot",
    "MirrorFrozenListSlot",
    "MirrorFrozenSetSlot",
    "MirrorMutableDictSlot",
    "MirrorMutableListSlot",
    "MirrorMutableSetSlot",
    "TestFrozenDictSlotDunderMethodBool",
    "TestFrozenDictSlotDunderMethodClassGetitem",
    "TestFrozenDictSlotDunderMethodContains",
    "TestFrozenDictSlotDunderMethodDelattr",
    "TestFrozenDictSlotDunderMethodDir",
    "TestFrozenDictSlotDunderMethodEq",
    "TestFrozenDictSlotDunderMethodFormat",
    "TestFrozenDictSlotDunderMethodGe",
    "TestFrozenDictSlotDunderMethodGetattribute",
    "TestFrozenDictSlotDunderMethodGetitem",
    "TestFrozenDictSlotDunderMethodGt",
    "TestFrozenDictSlotDunderMethodHash",
    "TestFrozenDictSlotDunderMethodInit",
    "TestFrozenDictSlotDunderMethodIter",
    "TestFrozenDictSlotDunderMethodLe",
    "TestFrozenDictSlotDunderMethodLen",
    "TestFrozenDictSlotDunderMethodLt",
    "TestFrozenDictSlotDunderMethodNe",
    "TestFrozenDictSlotDunderMethodNew",
    "TestFrozenDictSlotDunderMethodOr",
    "TestFrozenDictSlotDunderMethodRepr",
    "TestFrozenDictSlotDunderMethodReversed",
    "TestFrozenDictSlotDunderMethodSetattr",
    "TestFrozenDictSlotDunderMethodSizeof",
    "TestFrozenDictSlotDunderMethodStr",
    "TestFrozenDictSlotDunderMethodSubclasshook",
    "TestFrozenDictSlotPublicMethodFromkeys",
    "TestFrozenDictSlotPublicMethodGet",
    "TestFrozenDictSlotPublicMethodItems",
    "TestFrozenDictSlotPublicMethodKeys",
    "TestFrozenDictSlotPublicMethodValues",
    "TestFrozenListSlotDunderMethodAdd",
    "TestFrozenListSlotDunderMethodBool",
    "TestFrozenListSlotDunderMethodClassGetitem",
    "TestFrozenListSlotDunderMethodContains",
    "TestFrozenListSlotDunderMethodDelattr",
    "TestFrozenListSlotDunderMethodDir",
    "TestFrozenListSlotDunderMethodEq",
    "TestFrozenListSlotDunderMethodFormat",
    "TestFrozenListSlotDunderMethodGe",
    "TestFrozenListSlotDunderMethodGetattribute",
    "TestFrozenListSlotDunderMethodGetitem",
    "TestFrozenListSlotDunderMethodGt",
    "TestFrozenListSlotDunderMethodHash",
    "TestFrozenListSlotDunderMethodInit",
    "TestFrozenListSlotDunderMethodIter",
    "TestFrozenListSlotDunderMethodLe",
    "TestFrozenListSlotDunderMethodLen",
    "TestFrozenListSlotDunderMethodLt",
    "TestFrozenListSlotDunderMethodMul",
    "TestFrozenListSlotDunderMethodNe",
    "TestFrozenListSlotDunderMethodNew",
    "TestFrozenListSlotDunderMethodRepr",
    "TestFrozenListSlotDunderMethodReversed",
    "TestFrozenListSlotDunderMethodRmul",
    "TestFrozenListSlotDunderMethodSetattr",
    "TestFrozenListSlotDunderMethodSizeof",
    "TestFrozenListSlotDunderMethodStr",
    "TestFrozenListSlotDunderMethodSubclasshook",
    "TestFrozenListSlotPublicMethodCount",
    "TestFrozenListSlotPublicMethodIndex",
    "TestFrozenSetSlotDunderMethodAnd",
    "TestFrozenSetSlotDunderMethodBool",
    "TestFrozenSetSlotDunderMethodClassGetitem",
    "TestFrozenSetSlotDunderMethodContains",
    "TestFrozenSetSlotDunderMethodDelattr",
    "TestFrozenSetSlotDunderMethodDir",
    "TestFrozenSetSlotDunderMethodEq",
    "TestFrozenSetSlotDunderMethodFormat",
    "TestFrozenSetSlotDunderMethodGe",
    "TestFrozenSetSlotDunderMethodGetattribute",
    "TestFrozenSetSlotDunderMethodGt",
    "TestFrozenSetSlotDunderMethodHash",
    "TestFrozenSetSlotDunderMethodInit",
    "TestFrozenSetSlotDunderMethodIter",
    "TestFrozenSetSlotDunderMethodLe",
    "TestFrozenSetSlotDunderMethodLen",
    "TestFrozenSetSlotDunderMethodLt",
    "TestFrozenSetSlotDunderMethodNe",
    "TestFrozenSetSlotDunderMethodNew",
    "TestFrozenSetSlotDunderMethodOr",
    "TestFrozenSetSlotDunderMethodRand",
    "TestFrozenSetSlotDunderMethodRepr",
    "TestFrozenSetSlotDunderMethodRor",
    "TestFrozenSetSlotDunderMethodRsub",
    "TestFrozenSetSlotDunderMethodRxor",
    "TestFrozenSetSlotDunderMethodSetattr",
    "TestFrozenSetSlotDunderMethodSizeof",
    "TestFrozenSetSlotDunderMethodStr",
    "TestFrozenSetSlotDunderMethodSub",
    "TestFrozenSetSlotDunderMethodSubclasshook",
    "TestFrozenSetSlotDunderMethodXor",
    "TestFrozenSetSlotPublicMethodDifference",
    "TestFrozenSetSlotPublicMethodIntersection",
    "TestFrozenSetSlotPublicMethodIsdisjoint",
    "TestFrozenSetSlotPublicMethodIssubset",
    "TestFrozenSetSlotPublicMethodIssuperset",
    "TestFrozenSetSlotPublicMethodSymmetricDifference",
    "TestFrozenSetSlotPublicMethodUnion",
    "TestMutableDictSlotDunderMethodBool",
    "TestMutableDictSlotDunderMethodClassGetitem",
    "TestMutableDictSlotDunderMethodContains",
    "TestMutableDictSlotDunderMethodDelattr",
    "TestMutableDictSlotDunderMethodDelitem",
    "TestMutableDictSlotDunderMethodDir",
    "TestMutableDictSlotDunderMethodEq",
    "TestMutableDictSlotDunderMethodFormat",
    "TestMutableDictSlotDunderMethodGe",
    "TestMutableDictSlotDunderMethodGetattribute",
    "TestMutableDictSlotDunderMethodGetitem",
    "TestMutableDictSlotDunderMethodGt",
    "TestMutableDictSlotDunderMethodHash",
    "TestMutableDictSlotDunderMethodInit",
    "TestMutableDictSlotDunderMethodIor",
    "TestMutableDictSlotDunderMethodIter",
    "TestMutableDictSlotDunderMethodLe",
    "TestMutableDictSlotDunderMethodLen",
    "TestMutableDictSlotDunderMethodLt",
    "TestMutableDictSlotDunderMethodNe",
    "TestMutableDictSlotDunderMethodNew",
    "TestMutableDictSlotDunderMethodOr",
    "TestMutableDictSlotDunderMethodRepr",
    "TestMutableDictSlotDunderMethodReversed",
    "TestMutableDictSlotDunderMethodSetattr",
    "TestMutableDictSlotDunderMethodSetitem",
    "TestMutableDictSlotDunderMethodSizeof",
    "TestMutableDictSlotDunderMethodStr",
    "TestMutableDictSlotDunderMethodSubclasshook",
    "TestMutableDictSlotPublicMethodClear",
    "TestMutableDictSlotPublicMethodCopy",
    "TestMutableDictSlotPublicMethodFromkeys",
    "TestMutableDictSlotPublicMethodGet",
    "TestMutableDictSlotPublicMethodItems",
    "TestMutableDictSlotPublicMethodKeys",
    "TestMutableDictSlotPublicMethodPop",
    "TestMutableDictSlotPublicMethodPopitem",
    "TestMutableDictSlotPublicMethodSetdefault",
    "TestMutableDictSlotPublicMethodUpdate",
    "TestMutableDictSlotPublicMethodValues",
    "TestMutableListSlotDunderMethodAdd",
    "TestMutableListSlotDunderMethodBool",
    "TestMutableListSlotDunderMethodClassGetitem",
    "TestMutableListSlotDunderMethodContains",
    "TestMutableListSlotDunderMethodDelattr",
    "TestMutableListSlotDunderMethodDelitem",
    "TestMutableListSlotDunderMethodDir",
    "TestMutableListSlotDunderMethodEq",
    "TestMutableListSlotDunderMethodFormat",
    "TestMutableListSlotDunderMethodGe",
    "TestMutableListSlotDunderMethodGetattribute",
    "TestMutableListSlotDunderMethodGetitem",
    "TestMutableListSlotDunderMethodGt",
    "TestMutableListSlotDunderMethodHash",
    "TestMutableListSlotDunderMethodIadd",
    "TestMutableListSlotDunderMethodImul",
    "TestMutableListSlotDunderMethodInit",
    "TestMutableListSlotDunderMethodIter",
    "TestMutableListSlotDunderMethodLe",
    "TestMutableListSlotDunderMethodLen",
    "TestMutableListSlotDunderMethodLt",
    "TestMutableListSlotDunderMethodMul",
    "TestMutableListSlotDunderMethodNe",
    "TestMutableListSlotDunderMethodNew",
    "TestMutableListSlotDunderMethodRepr",
    "TestMutableListSlotDunderMethodReversed",
    "TestMutableListSlotDunderMethodRmul",
    "TestMutableListSlotDunderMethodSetattr",
    "TestMutableListSlotDunderMethodSetitem",
    "TestMutableListSlotDunderMethodSizeof",
    "TestMutableListSlotDunderMethodStr",
    "TestMutableListSlotDunderMethodSubclasshook",
    "TestMutableListSlotPublicMethodAppend",
    "TestMutableListSlotPublicMethodClear",
    "TestMutableListSlotPublicMethodCopy",
    "TestMutableListSlotPublicMethodCount",
    "TestMutableListSlotPublicMethodExtend",
    "TestMutableListSlotPublicMethodIndex",
    "TestMutableListSlotPublicMethodInsert",
    "TestMutableListSlotPublicMethodPop",
    "TestMutableListSlotPublicMethodRemove",
    "TestMutableListSlotPublicMethodReverse",
    "TestMutableListSlotPublicMethodSort",
    "TestMutableSetSlotDunderMethodAnd",
    "TestMutableSetSlotDunderMethodBool",
    "TestMutableSetSlotDunderMethodClassGetitem",
    "TestMutableSetSlotDunderMethodContains",
    "TestMutableSetSlotDunderMethodDelattr",
    "TestMutableSetSlotDunderMethodDir",
    "TestMutableSetSlotDunderMethodEq",
    "TestMutableSetSlotDunderMethodFormat",
    "TestMutableSetSlotDunderMethodGe",
    "TestMutableSetSlotDunderMethodGetattribute",
    "TestMutableSetSlotDunderMethodGt",
    "TestMutableSetSlotDunderMethodHash",
    "TestMutableSetSlotDunderMethodIand",
    "TestMutableSetSlotDunderMethodInit",
    "TestMutableSetSlotDunderMethodIor",
    "TestMutableSetSlotDunderMethodIsub",
    "TestMutableSetSlotDunderMethodIter",
    "TestMutableSetSlotDunderMethodIxor",
    "TestMutableSetSlotDunderMethodLe",
    "TestMutableSetSlotDunderMethodLen",
    "TestMutableSetSlotDunderMethodLt",
    "TestMutableSetSlotDunderMethodNe",
    "TestMutableSetSlotDunderMethodNew",
    "TestMutableSetSlotDunderMethodOr",
    "TestMutableSetSlotDunderMethodRand",
    "TestMutableSetSlotDunderMethodRepr",
    "TestMutableSetSlotDunderMethodRor",
    "TestMutableSetSlotDunderMethodRsub",
    "TestMutableSetSlotDunderMethodRxor",
    "TestMutableSetSlotDunderMethodSetattr",
    "TestMutableSetSlotDunderMethodSizeof",
    "TestMutableSetSlotDunderMethodStr",
    "TestMutableSetSlotDunderMethodSub",
    "TestMutableSetSlotDunderMethodSubclasshook",
    "TestMutableSetSlotDunderMethodXor",
    "TestMutableSetSlotPublicMethodAdd",
    "TestMutableSetSlotPublicMethodClear",
    "TestMutableSetSlotPublicMethodCopy",
    "TestMutableSetSlotPublicMethodDifference",
    "TestMutableSetSlotPublicMethodDifferenceUpdate",
    "TestMutableSetSlotPublicMethodDiscard",
    "TestMutableSetSlotPublicMethodIntersection",
    "TestMutableSetSlotPublicMethodIntersectionUpdate",
    "TestMutableSetSlotPublicMethodIsdisjoint",
    "TestMutableSetSlotPublicMethodIssubset",
    "TestMutableSetSlotPublicMethodIssuperset",
    "TestMutableSetSlotPublicMethodPop",
    "TestMutableSetSlotPublicMethodRemove",
    "TestMutableSetSlotPublicMethodSymmetricDifference",
    "TestMutableSetSlotPublicMethodSymmetricDifferenceUpdate",
    "TestMutableSetSlotPublicMethodUnion",
    "TestMutableSetSlotPublicMethodUpdate",
]

import sys
import unittest
from collections import abc
from typing import Any, ClassVar, Self, get_args, get_origin

from frozendict import frozendict

from datahold import (
    FrozenDictSlot,
    FrozenListSlot,
    FrozenSetSlot,
    MutableDictSlot,
    MutableListSlot,
    MutableSetSlot,
)


class Mirror:

    New: ClassVar[type[Any]]
    Old: ClassVar[type[Any]]

    def test_mirror(self: Self, /) -> None:
        index: int
        method: abc.Callable[[type[Any]], None] | None

        index = 0
        while True:
            method = getattr(self, f"mirror_{index}", None)
            if method is None:
                return
            method(type(self).Old)
            method(type(self).New)
            index += 1


class MirrorFrozenDictSlot(Mirror):

    New: ClassVar[type[Any]] = FrozenDictSlot
    Old: ClassVar[type[Any]] = frozendict


class MirrorFrozenListSlot(Mirror):

    New: ClassVar[type[Any]] = FrozenListSlot
    Old: ClassVar[type[Any]] = tuple


class MirrorFrozenSetSlot(Mirror):

    New: ClassVar[type[Any]] = FrozenSetSlot
    Old: ClassVar[type[Any]] = frozenset


class MirrorMutableDictSlot(Mirror):

    New: ClassVar[type[Any]] = MutableDictSlot
    Old: ClassVar[type[Any]] = dict


class MirrorMutableListSlot(Mirror):

    New: ClassVar[type[Any]] = MutableListSlot
    Old: ClassVar[type[Any]] = list


class MirrorMutableSetSlot(Mirror):

    New: ClassVar[type[Any]] = MutableSetSlot
    Old: ClassVar[type[Any]] = set


class TestFrozenDictSlotDunderMethodBool(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls({})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls({"a": 1, "b": 2}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls({"x": None}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls({"x": 0})), len(cls({"x": 0})) != 0)


class TestFrozenDictSlotDunderMethodClassGetitem(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[str, int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[str, int]), (str, int))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[str, int]), get_origin(cls[str, int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[str, int]))


class TestFrozenDictSlotDunderMethodContains(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("a", cls({"a": 1, "b": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn("a", cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn("z", cls({"a": 1}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(
            "a" in cls({"a": 1, "b": 2}), "a" not in cls({"a": 1, "b": 2})
        )


class TestFrozenDictSlotDunderMethodDelattr(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertEqual(len(obj), 2)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestFrozenDictSlotDunderMethodDir(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls({"a": 1, "b": 2})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dir(cls({"a": 1, "b": 2})), sorted(dir(cls({"a": 1, "b": 2})))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls({"a": 1, "b": 2})))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls({"a": 1, "b": 2}))),
            len(set(dir(cls({"a": 1, "b": 2})))),
        )


class TestFrozenDictSlotDunderMethodEq(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1, "b": 2}), cls({"a": 1, "b": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({}), cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls({"a": 1}), cls({"a": 2}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1, "b": 2}), cls({"b": 2, "a": 1}))


class TestFrozenDictSlotDunderMethodFormat(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls({})), str(cls({})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            format(cls({"a": 1, "b": 2}), ""), str(cls({"a": 1, "b": 2}))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls({"x": 1}), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls({"a": 1, "b": 2})}", str)


class TestFrozenDictSlotDunderMethodGe(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) >= cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) >= cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) >= cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) >= cls({"x": 1})


class TestFrozenDictSlotDunderMethodGetattribute(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls({"a": 1, "b": 2}), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls({"a": 1, "b": 2}), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(
            getattr(cls({"a": 1, "b": 2}), "missing_property", None), None
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls({"a": 1, "b": 2}), "__class__").__name__, cls.__name__
        )


class TestFrozenDictSlotDunderMethodGetitem(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1})["a"], 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({1: "number"})[1], "number")

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"x": None})["x"], None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(KeyError):
            cls({"a": 1})["missing"]


class TestFrozenDictSlotDunderMethodGt(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) > cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) > cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) > cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) > cls({"x": 1})


class TestFrozenDictSlotDunderMethodHash(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(hash(cls({"a": 1})), int)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls({"a": 1})), hash(cls({"a": 1})))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls({})), hash(cls({})))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls({"a": []}))


class TestFrozenDictSlotDunderMethodInit(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls([("a", 1), ("b", 2)])), {"a": 1, "b": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1})), {"a": 1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}, b=2)), {"a": 1, "b": 2})


class TestFrozenDictSlotDunderMethodIter(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"a": 1, "b": 2}))), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls({"a": 1, "b": 2})),
            len(cls({"a": 1, "b": 2})),
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"b": 2, "a": 1}))), {"a", "b"})


class TestFrozenDictSlotDunderMethodLe(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) <= cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) <= cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) <= cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) <= cls({"x": 1})


class TestFrozenDictSlotDunderMethodLen(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2})), 2)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"x": 7})), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"x": None, "y": None})), 2)


class TestFrozenDictSlotDunderMethodLt(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) < cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) < cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) < cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) < cls({"x": 1})


class TestFrozenDictSlotDunderMethodNe(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls({"a": 1}), cls({"a": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls({}) != cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls({"a": 1, "b": 2}) != cls({"a": 1, "b": 2}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            cls({"a": 1}) != cls({"b": 1}),
            not (cls({"a": 1}) == cls({"b": 1})),
        )


class TestFrozenDictSlotDunderMethodNew(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls({})), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls({"a": 1})), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls({"a": 1}), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls({"a": 1})), 0)


class TestFrozenDictSlotDunderMethodOr(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}) | cls({"b": 2})), {"a": 1, "b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}) | cls({"a": 3})), {"a": 3})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({}) | cls({"b": 2})), {"b": 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls({"a": 1}) | cls({"b": 2}), cls)


class TestFrozenDictSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(FrozenDictSlot({})), "FrozenDictSlot({})")

    def test_1_repr(self: Self, /) -> None:
        self.assertEqual(
            repr(FrozenDictSlot({"a": 1})), "FrozenDictSlot({'a': 1})"
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertIn("None", repr(FrozenDictSlot({"a": None})))

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        value: Any
        value = []
        obj = FrozenDictSlot({"a": value})
        value.append(obj)
        self.assertIn("...", repr(obj))


class TestFrozenDictSlotDunderMethodReversed(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({"a": 1, "b": 2}))), ["b", "a"])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({"z": 3}))), ["z"])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(reversed(cls({"a": 1, "b": 2, "c": 3}))), ["c", "b", "a"]
        )


class TestFrozenDictSlotDunderMethodSetattr(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestFrozenDictSlotDunderMethodSizeof(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls({"a": 1})), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls({"a": 1})), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls({})), sys.getsizeof(cls({})))


class TestFrozenDictSlotDunderMethodStr(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls({})), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            str(cls({"a": 1, "b": 2})), repr(cls({"a": 1, "b": 2}))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls({"a": 1, "b": 2}))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls({"a": 1, "b": 2}))), 0)


class TestFrozenDictSlotDunderMethodSubclasshook(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestFrozenDictSlotPublicMethodFromkeys(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dict(cls.fromkeys(["a", "b"])), {"a": None, "b": None}
        )

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls.fromkeys(["a", "b"], 7)), {"a": 7, "b": 7})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls.fromkeys([])), {})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls.fromkeys(["a"]), cls)


class TestFrozenDictSlotPublicMethodGet(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1}).get("a"), 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"a": 1}).get("missing"), None)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({}).get("missing", 7), 7)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"a": None}).get("a", 7), None)


class TestFrozenDictSlotPublicMethodItems(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            set(cls({"a": 1, "b": 2}).items()), {("a", 1), ("b", 2)}
        )

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).items()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1}).items()), [("a", 1)])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2}).items()), 2)


class TestFrozenDictSlotPublicMethodKeys(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls({"a": 1, "b": 2}).keys()), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).keys()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1}).keys()), ["a"])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIn("a", cls({"a": 1}).keys())


class TestFrozenDictSlotPublicMethodValues(
    MirrorFrozenDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1, "b": 2}).values()), [1, 2])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).values()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": None}).values()), [None])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2}).values()), 2)


class TestFrozenListSlotDunderMethodAdd(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) + cls([2]), cls([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]) + cls([3]), cls([3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 1]) + cls([1]), cls([1, 1, 1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) + cls([2]), cls)


class TestFrozenListSlotDunderMethodBool(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2, 3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(bool(cls([1, 2, 3])), True)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls([1, 2, 3])), len(cls([1, 2, 3])) != 0)


class TestFrozenListSlotDunderMethodClassGetitem(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[int]), (int,))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), get_origin(cls[int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[int]))


class TestFrozenListSlotDunderMethodContains(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn(2, cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(2, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(99, cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(2 in cls([1, 2, 3]), 2 not in cls([1, 2, 3]))


class TestFrozenListSlotDunderMethodDelattr(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertEqual(len(obj), 3)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 3)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestFrozenListSlotDunderMethodDir(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestFrozenListSlotDunderMethodEq(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1, 2]), cls([2, 1]))


class TestFrozenListSlotDunderMethodFormat(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([])), str(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([1, 2, 3]), ""), str(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls([1]), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls([1, 2, 3])}", str)


class TestFrozenListSlotDunderMethodGe(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) >= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) >= cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 3]) >= cls([1, 2]), True)


class TestFrozenListSlotDunderMethodGetattribute(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls([1, 2, 3]), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "missing_property", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls([1, 2, 3]), "__class__").__name__, cls.__name__
        )


class TestFrozenListSlotDunderMethodGetitem(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[0], 4)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[-1], 6)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[1:], cls([5, 6]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[::-1], cls([6, 5, 4]))


class TestFrozenListSlotDunderMethodGt(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) > cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) > cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) > cls([1]), True)


class TestFrozenListSlotDunderMethodHash(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(hash(cls([1, 2])), int)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls([1, 2])), hash(cls([1, 2])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls([])), hash(cls([])))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls([[1]]))


class TestFrozenListSlotDunderMethodInit(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls((1, 2, 3))), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls(iter([1, 2]))), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 2])), 3)


class TestFrozenListSlotDunderMethodIter(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([1, 2, 3]))), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(iter(cls([1, 2, 3]))), list(iter(cls([1, 2, 3])))
        )


class TestFrozenListSlotDunderMethodLe(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) <= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) <= cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) <= cls([1, 3]), True)


class TestFrozenListSlotDunderMethodLen(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 2, 3])), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([7])), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 1])), 3)


class TestFrozenListSlotDunderMethodLt(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) < cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) < cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([1, 2]), True)


class TestFrozenListSlotDunderMethodMul(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * 3, cls([1, 2, 1, 2, 1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * 0, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * -1, cls([]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) * 2, cls)


class TestFrozenListSlotDunderMethodNe(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([]) != cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2, 3]) != cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) != cls([2]), not (cls([1]) == cls([2])))


class TestFrozenListSlotDunderMethodNew(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([])), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([1, 2])), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1, 2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls([1, 2])), 0)


class TestFrozenListSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(FrozenListSlot([])), "FrozenListSlot([])")

    def test_1_repr(self: Self, /) -> None:
        self.assertEqual(
            repr(FrozenListSlot([1, 2])), "FrozenListSlot([1, 2])"
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertEqual(repr(FrozenListSlot(["a"])), "FrozenListSlot(['a'])")

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        value: Any
        value = []
        obj = FrozenListSlot([value])
        value.append(obj)
        self.assertIn("...", repr(obj))


class TestFrozenListSlotDunderMethodReversed(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([1, 2, 3]))), [3, 2, 1])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([9]))), [9])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([1, 1, 2]))), [2, 1, 1])


class TestFrozenListSlotDunderMethodRmul(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(3 * cls([1]), cls([1, 1, 1]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(0 * cls([1, 2]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(-2 * cls([1]), cls([]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(2 * cls([3]), cls)


class TestFrozenListSlotDunderMethodSetattr(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestFrozenListSlotDunderMethodSizeof(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([1, 2])), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls([1, 2])), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls([])), sys.getsizeof(cls([])))


class TestFrozenListSlotDunderMethodStr(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls([])), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(str(cls([1, 2, 3])), repr(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls([1, 2, 3]))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls([1, 2, 3]))), 0)


class TestFrozenListSlotDunderMethodSubclasshook(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestFrozenListSlotPublicMethodCount(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 1]).count(1), 2)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]).count(1), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([None, None, 0]).count(None), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 1, 1]).count(2), 0)


class TestFrozenListSlotPublicMethodIndex(
    MirrorFrozenListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6]).index(5), 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 4]).index(4, 1), 2)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6]).index(6, 0, 3), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(ValueError):
            cls([4, 5, 6]).index(99)


class TestFrozenSetSlotDunderMethodAnd(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) & cls([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) & cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) & cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) & cls([2]), cls)


class TestFrozenSetSlotDunderMethodBool(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2, 3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(bool(cls([1, 2, 3])), True)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls([1, 2, 3])), len(cls([1, 2, 3])) != 0)


class TestFrozenSetSlotDunderMethodClassGetitem(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[int]), (int,))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), get_origin(cls[int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[int]))


class TestFrozenSetSlotDunderMethodContains(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn(2, cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(2, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(99, cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(2 in cls([1, 2, 3]), 2 not in cls([1, 2, 3]))


class TestFrozenSetSlotDunderMethodDelattr(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertEqual(len(obj), 3)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 3)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestFrozenSetSlotDunderMethodDir(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestFrozenSetSlotDunderMethodEq(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]), cls([2, 1]))


class TestFrozenSetSlotDunderMethodFormat(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([])), str(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([1, 2, 3]), ""), str(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls([1]), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls([1, 2, 3])}", str)


class TestFrozenSetSlotDunderMethodGe(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) >= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) >= cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([2]), False)


class TestFrozenSetSlotDunderMethodGetattribute(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls([1, 2, 3]), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "missing_property", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls([1, 2, 3]), "__class__").__name__, cls.__name__
        )


class TestFrozenSetSlotDunderMethodGt(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) > cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) > cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([2]), False)


class TestFrozenSetSlotDunderMethodHash(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(hash(cls([1, 2])), int)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls([1, 2])), hash(cls([1, 2])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(hash(cls([])), hash(cls([])))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls([[]]))


class TestFrozenSetSlotDunderMethodInit(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls((1, 2, 3))), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls(iter([1, 2]))), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 2])), 2)


class TestFrozenSetSlotDunderMethodIter(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set(iter(cls([1, 2, 3]))))


class TestFrozenSetSlotDunderMethodLe(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) <= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) <= cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([2]), False)


class TestFrozenSetSlotDunderMethodLen(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 2, 3])), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([7])), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 1])), 1)


class TestFrozenSetSlotDunderMethodLt(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) < cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) < cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([2]), False)


class TestFrozenSetSlotDunderMethodNe(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([]) != cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2, 3]) != cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) != cls([2]), not (cls([1]) == cls([2])))


class TestFrozenSetSlotDunderMethodNew(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([])), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([1, 2])), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1, 2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls([1, 2])), 0)


class TestFrozenSetSlotDunderMethodOr(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) | cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) | cls([2]), cls)


class TestFrozenSetSlotDunderMethodRand(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) & cls([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() & cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) & cls([2])), {2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() & cls([])), set())


class TestFrozenSetSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(FrozenSetSlot([])), "FrozenSetSlot(set())")

    def test_1_repr(self: Self, /) -> None:
        self.assertIn("1", repr(FrozenSetSlot([1])))

    def test_2_repr(self: Self, /) -> None:
        self.assertTrue(
            repr(FrozenSetSlot([1, 2])).startswith("FrozenSetSlot(")
        )

    def test_3_repr(self: Self, /) -> None:
        self.assertIn("None", repr(FrozenSetSlot([None])))


class TestFrozenSetSlotDunderMethodRor(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) | cls([2])), {1, 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() | cls([])), set())


class TestFrozenSetSlotDunderMethodRsub(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) - cls([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() - cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) - cls([2])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() - cls([])), set())


class TestFrozenSetSlotDunderMethodRxor(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) ^ cls([2, 3])), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() ^ cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) ^ cls([2])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() ^ cls([])), set())


class TestFrozenSetSlotDunderMethodSetattr(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestFrozenSetSlotDunderMethodSizeof(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([1, 2])), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls([1, 2])), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls([])), sys.getsizeof(cls([])))


class TestFrozenSetSlotDunderMethodStr(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls([])), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(str(cls([1, 2, 3])), repr(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls([1, 2, 3]))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls([1, 2, 3]))), 0)


class TestFrozenSetSlotDunderMethodSub(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) - cls([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) - cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) - cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) - cls([2]), cls)


class TestFrozenSetSlotDunderMethodSubclasshook(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestFrozenSetSlotDunderMethodXor(MirrorFrozenSetSlot, unittest.TestCase):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) ^ cls([2, 3])), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) ^ cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) ^ cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) ^ cls([2]), cls)


class TestFrozenSetSlotPublicMethodDifference(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).difference([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).difference([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).difference([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).difference(cls([2]))), {1})


class TestFrozenSetSlotPublicMethodIntersection(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).intersection([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).intersection([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).intersection([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).intersection(cls([2]))), {2})


class TestFrozenSetSlotPublicMethodIsdisjoint(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).isdisjoint([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1]).isdisjoint([1]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([]).isdisjoint([1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).isdisjoint(iter([2, 3])))


class TestFrozenSetSlotPublicMethodIssubset(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issubset([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([]).issubset([1]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2]).issubset([1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issubset(cls([1])))


class TestFrozenSetSlotPublicMethodIssuperset(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2]).issuperset([1]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issuperset([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1]).issuperset([1, 2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issuperset(cls([1])))


class TestFrozenSetSlotPublicMethodSymmetricDifference(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([1, 2]).symmetric_difference([2, 3])), {1, 3})

    def mirror_1(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([]).symmetric_difference([])), set())

    def mirror_2(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertIsInstance(cls([1]).symmetric_difference([2]), cls)

    def mirror_3(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([1, 2]).symmetric_difference(cls([2]))), {1})


class TestFrozenSetSlotPublicMethodUnion(
    MirrorFrozenSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).union([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).union([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).union([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).union(cls([2]))), {1, 2})


class TestMutableDictSlotDunderMethodBool(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls({})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls({"a": 1, "b": 2}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls({"x": None}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls({"x": 0})), len(cls({"x": 0})) != 0)


class TestMutableDictSlotDunderMethodClassGetitem(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[str, int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[str, int]), (str, int))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[str, int]), get_origin(cls[str, int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[str, int]))


class TestMutableDictSlotDunderMethodContains(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("a", cls({"a": 1, "b": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn("a", cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn("z", cls({"a": 1}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(
            "a" in cls({"a": 1, "b": 2}), "a" not in cls({"a": 1, "b": 2})
        )


class TestMutableDictSlotDunderMethodDelattr(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertEqual(len(obj), 2)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestMutableDictSlotDunderMethodDelitem(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        del obj["a"]
        self.assertEqual(dict(obj), {"b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        del obj["a"]
        self.assertEqual(dict(obj), {})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        with self.assertRaises(KeyError):
            del obj["missing"]

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({1: None})
        del obj[1]
        self.assertEqual(len(obj), 0)


class TestMutableDictSlotDunderMethodDir(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls({"a": 1, "b": 2})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dir(cls({"a": 1, "b": 2})), sorted(dir(cls({"a": 1, "b": 2})))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls({"a": 1, "b": 2})))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls({"a": 1, "b": 2}))),
            len(set(dir(cls({"a": 1, "b": 2})))),
        )


class TestMutableDictSlotDunderMethodEq(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1, "b": 2}), cls({"a": 1, "b": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({}), cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls({"a": 1}), cls({"a": 2}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1, "b": 2}), cls({"b": 2, "a": 1}))


class TestMutableDictSlotDunderMethodFormat(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls({})), str(cls({})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            format(cls({"a": 1, "b": 2}), ""), str(cls({"a": 1, "b": 2}))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls({"x": 1}), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls({"a": 1, "b": 2})}", str)


class TestMutableDictSlotDunderMethodGe(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) >= cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) >= cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) >= cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) >= cls({"x": 1})


class TestMutableDictSlotDunderMethodGetattribute(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls({"a": 1, "b": 2}), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls({"a": 1, "b": 2}), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(
            getattr(cls({"a": 1, "b": 2}), "missing_property", None), None
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls({"a": 1, "b": 2}), "__class__").__name__, cls.__name__
        )


class TestMutableDictSlotDunderMethodGetitem(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1})["a"], 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({1: "number"})[1], "number")

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"x": None})["x"], None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(KeyError):
            cls({"a": 1})["missing"]


class TestMutableDictSlotDunderMethodGt(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) > cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) > cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) > cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) > cls({"x": 1})


class TestMutableDictSlotDunderMethodHash(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls({"a": 1}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            dict([(cls({"a": 1}), 1)])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls, "__hash__", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            set([cls({"a": 1})])


class TestMutableDictSlotDunderMethodInit(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls([("a", 1), ("b", 2)])), {"a": 1, "b": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1})), {"a": 1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}, b=2)), {"a": 1, "b": 2})


class TestMutableDictSlotDunderMethodIor(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls({"a": 1})
        ref = obj
        obj |= {"b": 2}
        self.assertIs(obj, ref)
        self.assertEqual(dict(obj), {"a": 1, "b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj |= {"a": 5}
        self.assertEqual(dict(obj), {"a": 5})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        obj |= {"a": 1}
        self.assertEqual(dict(obj), {"a": 1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj |= cls({"b": 2})
        self.assertEqual(dict(obj), {"a": 1, "b": 2})


class TestMutableDictSlotDunderMethodIter(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"a": 1, "b": 2}))), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls({"a": 1, "b": 2})),
            len(cls({"a": 1, "b": 2})),
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"b": 2, "a": 1}))), {"a", "b"})


class TestMutableDictSlotDunderMethodLe(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) <= cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) <= cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) <= cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) <= cls({"x": 1})


class TestMutableDictSlotDunderMethodLen(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2})), 2)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"x": 7})), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"x": None, "y": None})), 2)


class TestMutableDictSlotDunderMethodLt(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) < cls({})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) < cls({"x": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({"x": 1}) < cls({})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(
            TypeError, msg="mapping ordering must raise TypeError"
        ):
            cls({}) < cls({"x": 1})


class TestMutableDictSlotDunderMethodNe(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls({"a": 1}), cls({"a": 2}))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls({}) != cls({}))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls({"a": 1, "b": 2}) != cls({"a": 1, "b": 2}))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            cls({"a": 1}) != cls({"b": 1}),
            not (cls({"a": 1}) == cls({"b": 1})),
        )


class TestMutableDictSlotDunderMethodNew(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls({})), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls({"a": 1})), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls({"a": 1}), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls({"a": 1})), 0)


class TestMutableDictSlotDunderMethodOr(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}) | cls({"b": 2})), {"a": 1, "b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}) | cls({"a": 3})), {"a": 3})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({}) | cls({"b": 2})), {"b": 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls({"a": 1}) | cls({"b": 2}), cls)


class TestMutableDictSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(MutableDictSlot({})), "MutableDictSlot({})")

    def test_1_repr(self: Self, /) -> None:
        self.assertEqual(
            repr(MutableDictSlot({"a": 1})), "MutableDictSlot({'a': 1})"
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertIn("None", repr(MutableDictSlot({"a": None})))

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        obj = MutableDictSlot({})
        obj["self"] = obj
        self.assertIn("...", repr(obj))


class TestMutableDictSlotDunderMethodReversed(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({"a": 1, "b": 2}))), ["b", "a"])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls({"z": 3}))), ["z"])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(reversed(cls({"a": 1, "b": 2, "c": 3}))), ["c", "b", "a"]
        )


class TestMutableDictSlotDunderMethodSetattr(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestMutableDictSlotDunderMethodSetitem(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj["b"] = 2
        self.assertEqual(dict(obj), {"a": 1, "b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj["a"] = 3
        self.assertEqual(dict(obj), {"a": 3})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        obj[1] = None
        self.assertEqual(dict(obj), {1: None})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj["b"] = 2
        self.assertEqual(list(obj), ["a", "b"])


class TestMutableDictSlotDunderMethodSizeof(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls({})), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls({"a": 1})), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls({"a": 1})), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls({})), sys.getsizeof(cls({})))


class TestMutableDictSlotDunderMethodStr(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls({})), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            str(cls({"a": 1, "b": 2})), repr(cls({"a": 1, "b": 2}))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls({"a": 1, "b": 2}))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls({"a": 1, "b": 2}))), 0)


class TestMutableDictSlotDunderMethodSubclasshook(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestMutableDictSlotPublicMethodClear(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertIs(obj.clear(), None)
        self.assertEqual(dict(obj), {})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        obj.clear()
        self.assertEqual(dict(obj), {})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        obj.clear()
        self.assertEqual(len(obj), 0)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj.clear()
        obj["b"] = 2
        self.assertEqual(dict(obj), {"b": 2})


class TestMutableDictSlotPublicMethodCopy(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({"a": 1}).copy()), {"a": 1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls({}).copy()), {})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls({"a": 1}).copy(), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertEqual(obj.copy(), obj)


class TestMutableDictSlotPublicMethodFromkeys(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dict(cls.fromkeys(["a", "b"])), {"a": None, "b": None}
        )

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls.fromkeys(["a", "b"], 7)), {"a": 7, "b": 7})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dict(cls.fromkeys([])), {})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls.fromkeys(["a"]), cls)


class TestMutableDictSlotPublicMethodGet(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({"a": 1}).get("a"), 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"a": 1}).get("missing"), None)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls({}).get("missing", 7), 7)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls({"a": None}).get("a", 7), None)


class TestMutableDictSlotPublicMethodItems(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            set(cls({"a": 1, "b": 2}).items()), {("a", 1), ("b", 2)}
        )

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).items()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1}).items()), [("a", 1)])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2}).items()), 2)


class TestMutableDictSlotPublicMethodKeys(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls({"a": 1, "b": 2}).keys()), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).keys()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1}).keys()), ["a"])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIn("a", cls({"a": 1}).keys())


class TestMutableDictSlotPublicMethodPop(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertEqual(obj.pop("a"), 1)
        self.assertEqual(dict(obj), {})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        self.assertEqual(obj.pop("a", 5), 5)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertEqual(obj.pop("a", 5), 1)
        self.assertEqual(dict(obj), {})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        with self.assertRaises(KeyError):
            obj.pop("missing")


class TestMutableDictSlotPublicMethodPopitem(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertEqual(obj.popitem(), ("a", 1))
        self.assertEqual(dict(obj), {})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1, "b": 2})
        self.assertEqual(obj.popitem(), ("b", 2))
        self.assertEqual(dict(obj), {"a": 1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        with self.assertRaises(KeyError):
            obj.popitem()

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": None})
        self.assertEqual(obj.popitem(), ("a", None))


class TestMutableDictSlotPublicMethodSetdefault(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        self.assertEqual(obj.setdefault("a", 1), 1)
        self.assertEqual(dict(obj), {"a": 1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 2})
        self.assertEqual(obj.setdefault("a", 3), 2)
        self.assertEqual(dict(obj), {"a": 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        self.assertIs(obj.setdefault("a"), None)
        self.assertEqual(dict(obj), {"a": None})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": None})
        self.assertIs(obj.setdefault("a", 4), None)


class TestMutableDictSlotPublicMethodUpdate(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        self.assertIs(obj.update({"b": 2}), None)
        self.assertEqual(dict(obj), {"a": 1, "b": 2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj.update({"a": 4})
        self.assertEqual(dict(obj), {"a": 4})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({})
        obj.update([("a", 1)])
        self.assertEqual(dict(obj), {"a": 1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls({"a": 1})
        obj.update(b=2)
        self.assertEqual(dict(obj), {"a": 1, "b": 2})


class TestMutableDictSlotPublicMethodValues(
    MirrorMutableDictSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": 1, "b": 2}).values()), [1, 2])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({}).values()), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(cls({"a": None}).values()), [None])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls({"a": 1, "b": 2}).values()), 2)


class TestMutableListSlotDunderMethodAdd(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) + cls([2]), cls([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]) + cls([3]), cls([3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 1]) + cls([1]), cls([1, 1, 1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) + cls([2]), cls)


class TestMutableListSlotDunderMethodBool(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2, 3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(bool(cls([1, 2, 3])), True)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls([1, 2, 3])), len(cls([1, 2, 3])) != 0)


class TestMutableListSlotDunderMethodClassGetitem(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[int]), (int,))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), get_origin(cls[int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[int]))


class TestMutableListSlotDunderMethodContains(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn(2, cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(2, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(99, cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(2 in cls([1, 2, 3]), 2 not in cls([1, 2, 3]))


class TestMutableListSlotDunderMethodDelattr(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertEqual(len(obj), 3)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 3)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestMutableListSlotDunderMethodDelitem(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        del obj[1]
        self.assertEqual(list(obj), [1, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        del obj[1:]
        self.assertEqual(list(obj), [1])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        del obj[-1]
        self.assertEqual(list(obj), [1, 2])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3, 4])
        del obj[::2]
        self.assertEqual(list(obj), [2, 4])


class TestMutableListSlotDunderMethodDir(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestMutableListSlotDunderMethodEq(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1, 2]), cls([2, 1]))


class TestMutableListSlotDunderMethodFormat(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([])), str(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([1, 2, 3]), ""), str(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls([1]), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls([1, 2, 3])}", str)


class TestMutableListSlotDunderMethodGe(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) >= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) >= cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 3]) >= cls([1, 2]), True)


class TestMutableListSlotDunderMethodGetattribute(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls([1, 2, 3]), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "missing_property", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls([1, 2, 3]), "__class__").__name__, cls.__name__
        )


class TestMutableListSlotDunderMethodGetitem(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[0], 4)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[-1], 6)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[1:], cls([5, 6]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6])[::-1], cls([6, 5, 4]))


class TestMutableListSlotDunderMethodGt(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) > cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) > cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) > cls([1]), True)


class TestMutableListSlotDunderMethodHash(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            dict([(cls([1, 2]), 1)])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls, "__hash__", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            set([cls([1, 2])])


class TestMutableListSlotDunderMethodIadd(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1])
        ref = obj
        obj += [2]
        self.assertIs(obj, ref)
        self.assertEqual(list(obj), [1, 2])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj += [3]
        self.assertEqual(list(obj), [3])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj += []
        self.assertEqual(list(obj), [1])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj += iter([2, 3])
        self.assertEqual(list(obj), [1, 2, 3])


class TestMutableListSlotDunderMethodImul(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1, 2])
        ref = obj
        obj *= 2
        self.assertIs(obj, ref)
        self.assertEqual(list(obj), [1, 2, 1, 2])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj *= 0
        self.assertEqual(list(obj), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj *= -1
        self.assertEqual(list(obj), [])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj *= 1
        self.assertEqual(list(obj), [1])


class TestMutableListSlotDunderMethodInit(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls((1, 2, 3))), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls(iter([1, 2]))), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 2])), 3)


class TestMutableListSlotDunderMethodIter(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([1, 2, 3]))), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(iter(cls([1, 2, 3]))), list(iter(cls([1, 2, 3])))
        )


class TestMutableListSlotDunderMethodLe(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) <= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) <= cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) <= cls([1, 3]), True)


class TestMutableListSlotDunderMethodLen(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 2, 3])), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([7])), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 1])), 3)


class TestMutableListSlotDunderMethodLt(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) < cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([2]) < cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([1, 2]), True)


class TestMutableListSlotDunderMethodMul(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * 3, cls([1, 2, 1, 2, 1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * 0, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]) * -1, cls([]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) * 2, cls)


class TestMutableListSlotDunderMethodNe(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([]) != cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2, 3]) != cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) != cls([2]), not (cls([1]) == cls([2])))


class TestMutableListSlotDunderMethodNew(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([])), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([1, 2])), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1, 2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls([1, 2])), 0)


class TestMutableListSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(MutableListSlot([])), "MutableListSlot([])")

    def test_1_repr(self: Self, /) -> None:
        self.assertEqual(
            repr(MutableListSlot([1, 2])), "MutableListSlot([1, 2])"
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertEqual(
            repr(MutableListSlot(["a"])), "MutableListSlot(['a'])"
        )

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        obj = MutableListSlot([])
        obj.append(obj)
        self.assertIn("...", repr(obj))


class TestMutableListSlotDunderMethodReversed(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([1, 2, 3]))), [3, 2, 1])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([9]))), [9])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(reversed(cls([1, 1, 2]))), [2, 1, 1])


class TestMutableListSlotDunderMethodRmul(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(3 * cls([1]), cls([1, 1, 1]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(0 * cls([1, 2]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(-2 * cls([1]), cls([]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(2 * cls([3]), cls)


class TestMutableListSlotDunderMethodSetattr(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestMutableListSlotDunderMethodSetitem(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj[0] = 9
        self.assertEqual(list(obj), [9, 2])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj[-1] = 9
        self.assertEqual(list(obj), [1, 9])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        obj[1:] = [4, 5]
        self.assertEqual(list(obj), [1, 4, 5])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3, 4])
        obj[::2] = [9, 8]
        self.assertEqual(list(obj), [9, 2, 8, 4])


class TestMutableListSlotDunderMethodSizeof(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([1, 2])), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls([1, 2])), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls([])), sys.getsizeof(cls([])))


class TestMutableListSlotDunderMethodStr(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls([])), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(str(cls([1, 2, 3])), repr(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls([1, 2, 3]))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls([1, 2, 3]))), 0)


class TestMutableListSlotDunderMethodSubclasshook(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestMutableListSlotPublicMethodAppend(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        self.assertIs(obj.append(1), None)
        self.assertEqual(list(obj), [1])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.append(2)
        self.assertEqual(list(obj), [1, 2])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.append(None)
        self.assertEqual(list(obj), [1, None])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.append([1])
        self.assertEqual(list(obj), [[1]])


class TestMutableListSlotPublicMethodClear(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.clear(), None)
        self.assertEqual(list(obj), [])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.clear()
        self.assertEqual(list(obj), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([None])
        obj.clear()
        self.assertEqual(len(obj), 0)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.clear()
        obj.append(2)
        self.assertEqual(list(obj), [2])


class TestMutableListSlotPublicMethodCopy(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        copy: Any
        obj: Any
        obj = cls([1, 2])
        copy = obj.copy()
        self.assertEqual(copy, obj)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        self.assertEqual(obj.copy(), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        self.assertIsInstance(obj.copy(), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        copy: Any
        obj: Any
        obj = cls([1])
        copy = obj.copy()
        self.assertIsNot(copy, obj)


class TestMutableListSlotPublicMethodCount(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 1]).count(1), 2)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]).count(1), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([None, None, 0]).count(None), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 1, 1]).count(2), 0)


class TestMutableListSlotPublicMethodExtend(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        self.assertIs(obj.extend([2, 3]), None)
        self.assertEqual(list(obj), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.extend([])
        self.assertEqual(list(obj), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.extend(iter([2]))
        self.assertEqual(list(obj), [1, 2])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.extend((2, 3))
        self.assertEqual(list(obj), [1, 2, 3])


class TestMutableListSlotPublicMethodIndex(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6]).index(5), 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 4]).index(4, 1), 2)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([4, 5, 6]).index(6, 0, 3), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(ValueError):
            cls([4, 5, 6]).index(99)


class TestMutableListSlotPublicMethodInsert(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 3])
        self.assertIs(obj.insert(1, 2), None)
        self.assertEqual(list(obj), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.insert(0, 0)
        self.assertEqual(list(obj), [0, 1])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.insert(100, 2)
        self.assertEqual(list(obj), [1, 2])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.insert(-100, 0)
        self.assertEqual(list(obj), [0, 1])


class TestMutableListSlotPublicMethodPop(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertEqual(obj.pop(), 2)
        self.assertEqual(list(obj), [1])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertEqual(obj.pop(0), 1)
        self.assertEqual(list(obj), [2])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        self.assertEqual(obj.pop(-1), 1)
        self.assertEqual(list(obj), [])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        with self.assertRaises(IndexError):
            obj.pop()


class TestMutableListSlotPublicMethodRemove(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(obj.remove(2), None)
        self.assertEqual(list(obj), [1, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 1, 2])
        obj.remove(1)
        self.assertEqual(list(obj), [1, 2])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.remove(1)
        self.assertEqual(list(obj), [])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        with self.assertRaises(ValueError):
            obj.remove(2)


class TestMutableListSlotPublicMethodReverse(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(obj.reverse(), None)
        self.assertEqual(list(obj), [3, 2, 1])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.reverse()
        self.assertEqual(list(obj), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.reverse()
        self.assertEqual(list(obj), [1])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 1, 2])
        obj.reverse()
        self.assertEqual(list(obj), [2, 1, 1])


class TestMutableListSlotPublicMethodSort(
    MirrorMutableListSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([3, 1, 2])
        self.assertIs(obj.sort(), None)
        self.assertEqual(list(obj), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 3, 2])
        obj.sort(reverse=True)
        self.assertEqual(list(obj), [3, 2, 1])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls(["aa", "b", "cccc"])
        obj.sort(key=len)
        self.assertEqual(list(obj), ["b", "aa", "cccc"])

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([2, 1, 2, 1])
        obj.sort()
        self.assertEqual(list(obj), [1, 1, 2, 2])


class TestMutableSetSlotDunderMethodAnd(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) & cls([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) & cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) & cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) & cls([2]), cls)


class TestMutableSetSlotDunderMethodBool(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(bool(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2, 3]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(bool(cls([1, 2, 3])), True)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(bool(cls([1, 2, 3])), len(cls([1, 2, 3])) != 0)


class TestMutableSetSlotDunderMethodClassGetitem(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(get_args(cls[int]), (int,))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(get_origin(cls[int]), get_origin(cls[int]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(str(cls[int]))


class TestMutableSetSlotDunderMethodContains(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn(2, cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(2, cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotIn(99, cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(2 in cls([1, 2, 3]), 2 not in cls([1, 2, 3]))


class TestMutableSetSlotDunderMethodDelattr(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="deleting a missing attribute must fail"
        ):
            delattr(obj, "not_a_real_attribute")

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            del obj.nonexistent

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertEqual(len(obj), 3)
        with self.assertRaises(AttributeError):
            delattr(obj, "nonexistent")
        self.assertEqual(len(obj), 3)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertIs(getattr(obj, "not_a_real_attribute", None), None)


class TestMutableSetSlotDunderMethodDir(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        name: Any
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestMutableSetSlotDunderMethodEq(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]), cls([2, 1]))


class TestMutableSetSlotDunderMethodFormat(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([])), str(cls([])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(format(cls([1, 2, 3]), ""), str(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            format(cls([1]), "bad")

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(f"{cls([1, 2, 3])}", str)


class TestMutableSetSlotDunderMethodGe(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) >= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) >= cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([2]), False)


class TestMutableSetSlotDunderMethodGetattribute(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "__class__"), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(callable(getattr(cls([1, 2, 3]), "__iter__")))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls([1, 2, 3]), "missing_property", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            getattr(cls([1, 2, 3]), "__class__").__name__, cls.__name__
        )


class TestMutableSetSlotDunderMethodGt(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) > cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) > cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([2]), False)


class TestMutableSetSlotDunderMethodHash(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            hash(cls([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            dict([(cls([1, 2]), 1)])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(getattr(cls, "__hash__", None), None)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        with self.assertRaises(TypeError):
            set([cls([1, 2])])


class TestMutableSetSlotDunderMethodIand(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1, 2])
        ref = obj
        obj &= cls([2, 3])
        self.assertIs(obj, ref)
        self.assertEqual(set(obj), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj &= cls([1])
        self.assertEqual(set(obj), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj &= cls([1])
        self.assertEqual(set(obj), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj &= cls([])
        self.assertEqual(set(obj), set())


class TestMutableSetSlotDunderMethodInit(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls((1, 2, 3))), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls(iter([1, 2]))), 2)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 2])), 2)


class TestMutableSetSlotDunderMethodIor(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1, 2])
        ref = obj
        obj |= cls([2, 3])
        self.assertIs(obj, ref)
        self.assertEqual(set(obj), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj |= cls([1])
        self.assertEqual(set(obj), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj |= cls([1])
        self.assertEqual(set(obj), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj |= cls([])
        self.assertEqual(set(obj), {1, 2})


class TestMutableSetSlotDunderMethodIsub(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1, 2])
        ref = obj
        obj -= cls([2, 3])
        self.assertIs(obj, ref)
        self.assertEqual(set(obj), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj -= cls([1])
        self.assertEqual(set(obj), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj -= cls([1])
        self.assertEqual(set(obj), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj -= cls([])
        self.assertEqual(set(obj), {1, 2})


class TestMutableSetSlotDunderMethodIter(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        item: Any
        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set(iter(cls([1, 2, 3]))))


class TestMutableSetSlotDunderMethodIxor(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        ref: Any
        obj = cls([1, 2])
        ref = obj
        obj ^= cls([2, 3])
        self.assertIs(obj, ref)
        self.assertEqual(set(obj), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj ^= cls([1])
        self.assertEqual(set(obj), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj ^= cls([1])
        self.assertEqual(set(obj), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj ^= cls([])
        self.assertEqual(set(obj), {1, 2})


class TestMutableSetSlotDunderMethodLe(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) <= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) <= cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([2]), False)


class TestMutableSetSlotDunderMethodLen(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 2, 3])), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([7])), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 1])), 1)


class TestMutableSetSlotDunderMethodLt(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) < cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) < cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([2]), False)


class TestMutableSetSlotDunderMethodNe(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([]) != cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2, 3]) != cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) != cls([2]), not (cls([1]) == cls([2])))


class TestMutableSetSlotDunderMethodNew(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([])), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([1, 2])), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1, 2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls([1, 2])), 0)


class TestMutableSetSlotDunderMethodOr(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) | cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) | cls([2]), cls)


class TestMutableSetSlotDunderMethodRand(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) & cls([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() & cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) & cls([2])), {2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() & cls([])), set())


class TestMutableSetSlotDunderMethodRepr(unittest.TestCase):

    def test_0_repr(self: Self, /) -> None:
        self.assertEqual(repr(MutableSetSlot([])), "MutableSetSlot(set())")

    def test_1_repr(self: Self, /) -> None:
        self.assertIn("1", repr(MutableSetSlot([1])))

    def test_2_repr(self: Self, /) -> None:
        self.assertTrue(
            repr(MutableSetSlot([1, 2])).startswith("MutableSetSlot(")
        )

    def test_3_repr(self: Self, /) -> None:
        self.assertIn("None", repr(MutableSetSlot([None])))


class TestMutableSetSlotDunderMethodRor(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) | cls([2])), {1, 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() | cls([])), set())


class TestMutableSetSlotDunderMethodRsub(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) - cls([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() - cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) - cls([2])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() - cls([])), set())


class TestMutableSetSlotDunderMethodRxor(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) ^ cls([2, 3])), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() ^ cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) ^ cls([2])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() ^ cls([])), set())


class TestMutableSetSlotDunderMethodSetattr(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(
            AttributeError, msg="slots must reject unknown attributes"
        ):
            setattr(obj, "undeclared_attribute", 1)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            obj.undeclared_attribute = 1

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        self.assertFalse(hasattr(obj, "undeclared_attribute"))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        with self.assertRaises(AttributeError):
            setattr(obj, "arbitrary_data", None)
        self.assertFalse(hasattr(obj, "arbitrary_data"))


class TestMutableSetSlotDunderMethodSizeof(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([1, 2])), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls([1, 2])), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls([])), sys.getsizeof(cls([])))


class TestMutableSetSlotDunderMethodStr(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls([])), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(str(cls([1, 2, 3])), repr(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls([1, 2, 3]))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls([1, 2, 3]))), 0)


class TestMutableSetSlotDunderMethodSub(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) - cls([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) - cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) - cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) - cls([2]), cls)


class TestMutableSetSlotDunderMethodSubclasshook(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestMutableSetSlotDunderMethodXor(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) ^ cls([2, 3])), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) ^ cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) ^ cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) ^ cls([2]), cls)


class TestMutableSetSlotPublicMethodAdd(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        self.assertIs(obj.add(1), None)
        self.assertEqual(set(obj), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.add(1)
        self.assertEqual(set(obj), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.add(2)
        self.assertEqual(set(obj), {1, 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.add(None)
        self.assertEqual(set(obj), {None})


class TestMutableSetSlotPublicMethodClear(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.clear(), None)
        self.assertEqual(set(obj), set())

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.clear()
        self.assertEqual(set(obj), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.clear()
        obj.add(3)
        self.assertEqual(set(obj), {3})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        obj.clear()
        self.assertEqual(len(obj), 0)


class TestMutableSetSlotPublicMethodCopy(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]).copy(), cls([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]).copy(), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).copy(), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertEqual(set(obj.copy()), set(obj))


class TestMutableSetSlotPublicMethodDifference(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).difference([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).difference([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).difference([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).difference(cls([2]))), {1})


class TestMutableSetSlotPublicMethodDifferenceUpdate(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.difference_update([2]), None)
        self.assertEqual(set(obj), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        obj.difference_update([3])
        self.assertEqual(set(obj), {1, 2})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.difference_update([1])
        self.assertEqual(set(obj), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        obj.difference_update([1], [3])
        self.assertEqual(set(obj), {2})


class TestMutableSetSlotPublicMethodDiscard(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.discard(2), None)
        self.assertEqual(set(obj), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.discard(9)
        self.assertEqual(set(obj), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.discard(1)
        self.assertEqual(set(obj), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([None])
        obj.discard(None)
        self.assertEqual(set(obj), set())


class TestMutableSetSlotPublicMethodIntersection(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).intersection([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).intersection([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).intersection([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).intersection(cls([2]))), {2})


class TestMutableSetSlotPublicMethodIntersectionUpdate(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.intersection_update([2, 3]), None)
        self.assertEqual(set(obj), {2})

    def mirror_1(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1, 2])
        obj.intersection_update([])
        self.assertEqual(set(obj), set())

    def mirror_2(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([])
        obj.intersection_update([1])
        self.assertEqual(set(obj), set())

    def mirror_3(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1, 2, 3])
        obj.intersection_update([1, 2], [2, 3])
        self.assertEqual(set(obj), {2})


class TestMutableSetSlotPublicMethodIsdisjoint(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).isdisjoint([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1]).isdisjoint([1]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([]).isdisjoint([1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).isdisjoint(iter([2, 3])))


class TestMutableSetSlotPublicMethodIssubset(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issubset([1, 2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([]).issubset([1]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2]).issubset([1]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issubset(cls([1])))


class TestMutableSetSlotPublicMethodIssuperset(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1, 2]).issuperset([1]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issuperset([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1]).issuperset([1, 2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(cls([1]).issuperset(cls([1])))


class TestMutableSetSlotPublicMethodPop(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        self.assertEqual(obj.pop(), 1)
        self.assertEqual(set(obj), set())

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        value: Any
        obj = cls([1, 2])
        value = obj.pop()
        self.assertIn(value, {1, 2})
        self.assertEqual(len(obj), 1)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        with self.assertRaises(KeyError):
            obj.pop()

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([None])
        self.assertIs(obj.pop(), None)
        self.assertEqual(len(obj), 0)


class TestMutableSetSlotPublicMethodRemove(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.remove(2), None)
        self.assertEqual(set(obj), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.remove(1)
        self.assertEqual(len(obj), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        with self.assertRaises(KeyError):
            obj.remove(3)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([None])
        obj.remove(None)
        self.assertEqual(len(obj), 0)


class TestMutableSetSlotPublicMethodSymmetricDifference(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([1, 2]).symmetric_difference([2, 3])), {1, 3})

    def mirror_1(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([]).symmetric_difference([])), set())

    def mirror_2(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertIsInstance(cls([1]).symmetric_difference([2]), cls)

    def mirror_3(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        self.assertEqual(set(cls([1, 2]).symmetric_difference(cls([2]))), {1})


class TestMutableSetSlotPublicMethodSymmetricDifferenceUpdate(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1, 2])
        self.assertIs(obj.symmetric_difference_update([2, 3]), None)
        self.assertEqual(set(obj), {1, 3})

    def mirror_1(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1])
        obj.symmetric_difference_update([1])
        self.assertEqual(set(obj), set())

    def mirror_2(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([])
        obj.symmetric_difference_update([1])
        self.assertEqual(set(obj), {1})

    def mirror_3(
        self: Self,
        cls: type[Any],
        /,
    ) -> None:
        obj: Any
        obj = cls([1])
        obj.symmetric_difference_update([])
        self.assertEqual(set(obj), {1})


class TestMutableSetSlotPublicMethodUnion(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).union([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]).union([])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]).union([2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]).union(cls([2]))), {1, 2})


class TestMutableSetSlotPublicMethodUpdate(
    MirrorMutableSetSlot, unittest.TestCase
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        self.assertIs(obj.update([2, 3]), None)
        self.assertEqual(set(obj), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([])
        obj.update([1])
        self.assertEqual(set(obj), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.update([1])
        self.assertEqual(set(obj), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        obj: Any
        obj = cls([1])
        obj.update([2], [3])
        self.assertEqual(set(obj), {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
