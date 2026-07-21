__all__: list[str] = ["TestAbstractness", "TestCollection", "TestData"]

import collections.abc
import enum
import inspect as ins
import io
import tomllib
import unittest
from functools import cached_property
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Any, Optional, Self, cast, get_args, get_origin

from datahold import core


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
    def get_parenttype(cls: type[Self], typename: str) -> type[Any]:
        ans: Optional[type[Any]]
        if typename in collections.abc.__all__:
            return cast(type[Any], getattr(collections.abc, typename))
        ans = cls.get_type(typename)
        if ans is None:
            raise Exception("get_parenttype(%r)" % typename)
        else:
            return ans

    @classmethod
    def get_type(cls: type[Self], typename: str) -> Optional[type[Any]]:
        module: Optional[ModuleType]
        module = cls.get_typemodule(typename)
        if module is None:
            return None
        return cast(type[Any], getattr(module, typename))

    @classmethod
    def get_typemodule(cls: type[Self], typename: str) -> Optional[ModuleType]:
        try:
            return import_module(name=cls.get_typemodulename(typename))
        except ImportError:
            return None

    @classmethod
    def get_typemodulename(cls: type[Self], typename: str) -> str:
        ans: str
        ans = "datahold"
        ans += "."
        for prefix in ("Base", "Frozen"):
            if typename.startswith(prefix):
                ans += prefix.lower()
                break
        else:
            ans += "core"
        ans += "."
        ans += typename
        return ans

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])

    @cached_property
    def types(self: Self) -> dict[str, dict[str, Any]]:
        return cast(dict[str, dict[str, Any]], self.data["types"])


class TestAbstractness(unittest.TestCase):
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
            parenttype = Lazy.get_parenttype(x)
            self.assertEqual(isinstance(obj, parenttype), y)

    def go_types(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: Optional[type[Any]]
        parenttype: type[Any]
        x: Any
        y: Any
        cls = Lazy.get_type(typename)
        if cls is None:
            raise Exception
        if kwargs.get("isabstract") is not None:
            self.assertEqual(ins.isabstract(cls), kwargs.get("isabstract"))
        self.go_assert_is_generic(cls, kwargs.get("n_type_params"))
        for x, y in kwargs.get("constructor", {}).items():
            with self.subTest(constructor=x):
                self.go_constructor(cls, **y)
        for x, y in kwargs.get("parents", {}).items():
            parenttype = Lazy.get_parenttype(x)
            self.assertEqual(issubclass(cls, parenttype), y)
        if typename.startswith("Base") or typename.startswith("Frozen"):
            self.assertFalse(hasattr(cls, "copy"))

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
        cls: Optional[type[Any]]
        typename: str
        for typename in Lazy.lazy.types.keys():
            cls = Lazy.get_type(typename=typename)
            if cls is None:
                raise Exception
            self._test_cls(cls)


class TestData(unittest.TestCase):

    def test_doc(self: Self) -> None:
        for name in Lazy.lazy.types.keys():
            self.go(name=name)

    def go(self: Self, name: str) -> None:
        attrname: Any
        cls: Any
        doc: Any
        error: Any
        member: Any
        module: Any
        obj: Any
        module = Lazy.get_typemodule(typename=name)
        doc = getattr(module, "__doc__", None)
        self.assertIsNotNone(doc, "module %r has no docstring" % name)
        cls = Lazy.get_type(typename=name)
        doc = getattr(cls, "__doc__", None)
        self.assertIsNotNone(doc, "class %r has no docstring" % name)
        for attrname in dir(cls):
            member = getattr(cls, attrname)
            if not callable(member) and not isinstance(member, property):
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


if __name__ == "__main__":
    unittest.main()
