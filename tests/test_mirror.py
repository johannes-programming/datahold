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
from contextlib import AbstractContextManager
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

    def subTest(self: Self, /, msg: Any = None, **kwargs: Any) -> Any: ...

    def test_mirror(self: Self, /) -> None:
        index: int
        method: abc.Callable[[type[Any]], None] | None

        index = 0
        while True:
            method = getattr(self, f"mirror_{index}", None)
            if method is None:
                return
            with self.subTest(Old=type(self).Old.__name__, mirror=index):
                method(type(self).Old)
            with self.subTest(New=type(self).New.__name__, mirror=index):
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls({"a": 1, "b": 2})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dir(cls({"a": 1, "b": 2})), sorted(dir(cls({"a": 1, "b": 2})))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls({"a": 1, "b": 2})))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls({"a": 1, "b": 2}))),
            len(set(dir(cls({"a": 1, "b": 2})))),
        )


class TestFrozenDictSlotDunderMethodEq(
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"a": 1, "b": 2}))), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            sum(1 for item in cls({"a": 1, "b": 2})),
            len(cls({"a": 1, "b": 2})),
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"b": 2, "a": 1}))), {"a", "b"})


class TestFrozenDictSlotDunderMethodLe(
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
            repr(FrozenDictSlot({"a": 1})),  # type: ignore[arg-type]
            "FrozenDictSlot({'a': 1})",
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertIn(
            "None",
            repr(FrozenDictSlot({"a": None})),  # type: ignore[arg-type]
        )

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        value: Any
        value = []
        obj = FrozenDictSlot({"a": value})  # type: ignore[arg-type]
        value.append(obj)
        self.assertIn("...", repr(obj))


class TestFrozenDictSlotDunderMethodReversed(
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenDictSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestFrozenListSlotDunderMethodEq(
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([1, 2, 3]))), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(iter(cls([1, 2, 3]))), list(iter(cls([1, 2, 3])))
        )


class TestFrozenListSlotDunderMethodLe(
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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
    unittest.TestCase, MirrorFrozenListSlot
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


class TestFrozenSetSlotDunderMethodAnd(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) & cls([2, 3])), {2})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) & cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) & cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) & cls([2]), cls)


class TestFrozenSetSlotDunderMethodBool(
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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


class TestFrozenSetSlotDunderMethodDir(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestFrozenSetSlotDunderMethodEq(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2, 3]), cls([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([]), cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1, 2]), cls([2, 1]))


class TestFrozenSetSlotDunderMethodFormat(
    unittest.TestCase, MirrorFrozenSetSlot
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


class TestFrozenSetSlotDunderMethodGe(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) >= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) >= cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) >= cls([2]), False)


class TestFrozenSetSlotDunderMethodGetattribute(
    unittest.TestCase, MirrorFrozenSetSlot
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


class TestFrozenSetSlotDunderMethodGt(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) > cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) > cls([1]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([1, 2]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) > cls([2]), False)


class TestFrozenSetSlotDunderMethodHash(
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set(iter(cls([1, 2, 3]))))


class TestFrozenSetSlotDunderMethodLe(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) <= cls([]), True)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) <= cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) <= cls([2]), False)


class TestFrozenSetSlotDunderMethodLen(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 2, 3])), 3)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([7])), 1)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(len(cls([1, 1, 1])), 1)


class TestFrozenSetSlotDunderMethodLt(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([]) < cls([]), False)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([1, 2]), True)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1, 2]) < cls([1]), False)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIs(cls([1]) < cls([2]), False)


class TestFrozenSetSlotDunderMethodNe(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertNotEqual(cls([1]), cls([2]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([]) != cls([]))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(cls([1, 2, 3]) != cls([1, 2, 3]))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(cls([1]) != cls([2]), not (cls([1]) == cls([2])))


class TestFrozenSetSlotDunderMethodNew(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([])), cls)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(cls([1, 2])), cls)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1, 2]), cls)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(cls([1, 2])), 0)


class TestFrozenSetSlotDunderMethodOr(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) | cls([1])), {1})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) | cls([2]), cls)


class TestFrozenSetSlotDunderMethodRand(
    unittest.TestCase, MirrorFrozenSetSlot
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


class TestFrozenSetSlotDunderMethodRor(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset([1, 2]) | cls([2, 3])), {1, 2, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(frozenset() | cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set([1, 2]) | cls([2])), {1, 2})

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(set() | cls([])), set())


class TestFrozenSetSlotDunderMethodRsub(
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([])), 0)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(sys.getsizeof(cls([1, 2])), 0)

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(sys.getsizeof(cls([1, 2])), int)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(sys.getsizeof(cls([])), sys.getsizeof(cls([])))


class TestFrozenSetSlotDunderMethodStr(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(str(cls([])), str)

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(str(cls([1, 2, 3])), repr(cls([1, 2, 3])))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertIs(type(str(cls([1, 2, 3]))), str)

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertGreater(len(str(cls([1, 2, 3]))), 0)


class TestFrozenSetSlotDunderMethodSub(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) - cls([2, 3])), {1})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) - cls([1])), set())

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) - cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) - cls([2]), cls)


class TestFrozenSetSlotDunderMethodSubclasshook(
    unittest.TestCase, MirrorFrozenSetSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Iterable))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Container))

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertTrue(issubclass(cls, abc.Sized))

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertFalse(issubclass(cls, str))


class TestFrozenSetSlotDunderMethodXor(unittest.TestCase, MirrorFrozenSetSlot):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1, 2]) ^ cls([2, 3])), {1, 3})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([]) ^ cls([1])), {1})

    def mirror_2(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(cls([1]) ^ cls([1])), set())

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertIsInstance(cls([1]) ^ cls([2]), cls)


class TestFrozenSetSlotPublicMethodDifference(
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorFrozenSetSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls({"a": 1, "b": 2})))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            dir(cls({"a": 1, "b": 2})), sorted(dir(cls({"a": 1, "b": 2})))
        )

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls({"a": 1, "b": 2})))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls({"a": 1, "b": 2}))),
            len(set(dir(cls({"a": 1, "b": 2})))),
        )


class TestMutableDictSlotDunderMethodEq(
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"a": 1, "b": 2}))), {"a", "b"})

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls({}))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertEqual(
            sum(1 for item in cls({"a": 1, "b": 2})),
            len(cls({"a": 1, "b": 2})),
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls({"b": 2, "a": 1}))), {"a", "b"})


class TestMutableDictSlotDunderMethodLe(
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
            repr(MutableDictSlot({"a": 1})),  # type: ignore[arg-type]
            "MutableDictSlot({'a': 1})",
        )

    def test_2_repr(self: Self, /) -> None:
        self.assertIn(
            "None",
            repr(MutableDictSlot({"a": None})),  # type: ignore[arg-type]
        )

    def test_3_repr(self: Self, /) -> None:
        obj: Any
        obj = MutableDictSlot({})
        obj["self"] = obj
        self.assertIn("...", repr(obj))


class TestMutableDictSlotDunderMethodReversed(
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableDictSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestMutableListSlotDunderMethodEq(
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([1, 2, 3]))), [1, 2, 3])

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            list(iter(cls([1, 2, 3]))), list(iter(cls([1, 2, 3])))
        )


class TestMutableListSlotDunderMethodLe(
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableListSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertIn("__class__", dir(cls([1, 2, 3])))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(dir(cls([1, 2, 3])), sorted(dir(cls([1, 2, 3]))))

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertTrue(
            all(isinstance(name, str) for name in dir(cls([1, 2, 3])))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(
            len(dir(cls([1, 2, 3]))), len(set(dir(cls([1, 2, 3]))))
        )


class TestMutableSetSlotDunderMethodEq(
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
):

    def mirror_0(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set([1, 2, 3]))

    def mirror_1(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(list(iter(cls([]))), [])

    def mirror_2(self: Self, cls: type[Any], /) -> None:

        self.assertEqual(
            sum(1 for item in cls([1, 2, 3])), len(cls([1, 2, 3]))
        )

    def mirror_3(self: Self, cls: type[Any], /) -> None:
        self.assertEqual(set(iter(cls([1, 2, 3]))), set(iter(cls([1, 2, 3]))))


class TestMutableSetSlotDunderMethodIxor(
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
    unittest.TestCase, MirrorMutableSetSlot
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
