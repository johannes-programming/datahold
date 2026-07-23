__all__: list[str] = [
    "TestAbstractness",
    "TestCollection",
    "TestConstructor",
    "TestData",
    "TestDirData",
    "TestGeneric",
    "TestHasCopy",
    "TestParents",
]

import collections.abc
import enum
import inspect as ins
import io
import tomllib
import unittest
from functools import cached_property
from pathlib import Path
from typing import Any, Self, TypeAliasType, cast, get_args, get_origin

import datahold


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def METHODS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["METHODS"])

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @classmethod
    def get_type(cls: type[Self], typename: str) -> type[Any]:
        ans: Any
        if typename in collections.abc.__all__:
            ans = getattr(collections.abc, typename)
        else:
            ans = getattr(datahold, typename)
        return cast(type[Any], ans)

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])

    @cached_property
    def types(self: Self) -> dict[str, dict[str, Any]]:
        return cast(dict[str, dict[str, Any]], self.data["types"])


class TestAbstractness(unittest.TestCase):

    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        cls = Lazy.get_type(typename)
        if kwargs.get("isabstract") is not None:
            self.assertEqual(ins.isabstract(cls), kwargs.get("isabstract"))

    def test_abstract_classes(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestCollection(unittest.TestCase):
    def _test_cls(self: Self, cls: type) -> None:
        method: Any
        for method in Lazy.lazy.METHODS:
            with self.subTest(cls=cls):
                self.assertIs(getattr(cls, method), getattr(object, method))

    def test_object(self: Self) -> None:
        cls: type[Any]
        typename: str
        for typename in Lazy.lazy.types.keys():
            cls = Lazy.get_type(typename=typename)
            if cls is None:
                raise Exception
            self._test_cls(cls)


class TestConstructor(unittest.TestCase):
    def go_constructor(self: Self, cls: type[Any], /, **info: Any) -> None:
        obj: Any
        parenttype: Any
        x: Any
        y: Any
        if info.get("valid", True):
            obj = cls(
                *info.get("args", []),
                **info.get("kwargs", {}),
            )
        else:
            with self.assertRaises(Exception):
                obj = cls(
                    *info.get("args", []),
                    **info.get("kwargs", {}),
                )
            return
        self.assertNotEqual(
            cls.__name__.startswith("Base")
            or cls.__name__.startswith("Frozen"),
            hasattr(obj, "copy"),
        )
        self.assertIn(info.get("repr"), [None, repr(obj)])
        self.assertIn(info.get("str"), [None, str(obj)])
        for x, y in info.get("parents", {}).items():
            parenttype = Lazy.get_type(x)
            self.assertEqual(isinstance(obj, parenttype), y)

    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        x: Any
        y: Any
        cls = Lazy.get_type(typename)
        for x, y in kwargs.get("constructor", {}).items():
            with self.subTest(constructor=x):
                self.go_constructor(cls, **y)

    def test_abstract_classes(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestData(unittest.TestCase):

    def test_doc(self: Self) -> None:
        self.assertIsNot(datahold.__doc__, None)
        for name in Lazy.lazy.types.keys():
            self.go(name=name)

    def go(self: Self, name: str) -> None:
        attrname: Any
        cls: Any
        doc: Any
        error: Any
        member: Any
        obj: Any
        cls = Lazy.get_type(typename=name)
        doc = getattr(cls, "__doc__", None)
        self.assertIsNotNone(doc, "class %r has no docstring" % name)
        for attrname in dir(cls):
            member = getattr(cls, attrname)
            if not callable(member) and not isinstance(member, property):
                continue
            if isinstance(member, TypeAliasType):
                continue
            if getattr(member, "__isabstractmethod__", False):
                continue
            if attrname in ("__init_subclass__", "__subclasshook__"):
                continue
            if getattr(member, "__module__", None) == "collections.abc":
                continue
            doc = getattr(member, "__doc__", None)
            error = "%r inside %r has no docstring" % (attrname, name)
            self.assertIsNotNone(doc, error)
        try:
            obj = cls()
        except TypeError:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


class TestDirData(unittest.TestCase):
    def go_dirData(self: Self, x: Any, /, **y: Any) -> None:
        cls = getattr(datahold, x)
        dirData = y.get("dirData")
        if dirData is None:
            return
        for z in dirData:
            self.assertTrue(hasattr(cls.Data, z))

    def go_init(self: Self, x: str, /) -> None:
        cls: Any
        cls = getattr(datahold, x)
        self.assertEqual(
            "__fget__" in cls.__dict__,
            "Data" in cls.__dict__ or not ins.isabstract(cls),
        )
        if "__fset__" in cls.__dict__:
            self.assertIn("__fget__", cls.__dict__)
        self.assertEqual(
            "Init" in cls.__dict__,
            "__init__" in cls.__dict__,
        )
        self.assertNotEqual(
            hasattr(cls, "Init"),
            cls.__init__ is object.__init__,
        )

    def test_types(self: Self) -> None:
        for x, y in Lazy.lazy.types.items():
            with self.subTest(type=x):
                self.go_dirData(x, **y)
                self.go_init(x)


class TestGeneric(unittest.TestCase):
    def go_assert_is_generic(
        self: Self,
        cls: Any,
        n_type_params: Any,
    ) -> None:
        """
        Helper: assert that `cls[...]` works and that typing.get_origin/get_args
        see it as a proper generic alias of `cls`.
        """
        alias: Any
        args: Any
        exc: BaseException
        origin: Any
        params: tuple[type, ...]
        sample_types: tuple[type, ...]

        if n_type_params is None:
            return
        if not isinstance(n_type_params, int):
            raise Exception

        # Pick some arbitrary distinct types for the parameters
        sample_types = (int, str, float, bytes)
        params = sample_types[:n_type_params]
        try:
            alias = cls[params if n_type_params > 1 else params[0]]
        except TypeError as exc:  # not subscriptable ⇒ not generic
            self.fail(f"{cls.__name__} is not generic: {exc!r}")

        origin = get_origin(alias)
        args = get_args(alias)

        self.assertIs(
            origin,
            cls,
            f"get_origin({cls.__name__}[...]) is {origin!r}, expected {cls!r}",
        )
        self.assertEqual(
            args,
            params,
            f"get_args({cls.__name__}[...]) is {args!r}, expected {params!r}",
        )

    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        cls = Lazy.get_type(typename)
        self.go_assert_is_generic(cls, kwargs.get("n_type_params"))

    def test_generic(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestHasCopy(unittest.TestCase):
    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        cls = Lazy.get_type(typename)
        if cls is None:
            raise Exception
        if typename.startswith("Base") or typename.startswith("Frozen"):
            self.assertFalse(hasattr(cls, "copy"))

    def test_has_copy(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestParents(unittest.TestCase):
    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        parenttype: type[Any]
        x: Any
        y: Any
        cls = Lazy.get_type(typename)
        if cls is None:
            raise Exception
        for x, y in kwargs.get("parents", {}).items():
            parenttype = Lazy.get_type(x)
            self.assertEqual(issubclass(cls, parenttype), y, x)

    def test_parents(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


if __name__ == "__main__":
    unittest.main()
