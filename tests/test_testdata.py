__all__: list[str] = [
    "TestAbstractness",
    "TestAll",
    "TestCollection",
    "TestConstructor",
    "TestData",
    "TestDirData",
    "TestGeneric",
    "TestHasCopy",
    "TestParents",
]

import enum
import inspect as ins
import io
import tomllib
import unittest
from functools import cached_property
from importlib import import_module
from pathlib import Path
from typing import (
    Any,
    Optional,
    Self,
    TypeAliasType,
    cast,
    get_args,
    get_origin,
)

import datahold


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def HOLD_TYPES(self: Self) -> list[str]:
        return cast(list[str], self.varia["HOLD_TYPES"])

    @cached_property
    def METHODS(self: Self) -> tuple[str, ...]:
        return cast(tuple[str, ...], self.test_object["METHODS"])

    @cached_property
    def abstractmethods(self: Self) -> frozenset[str]:
        return frozenset(self.varia["abstractmethods"])

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @classmethod
    def get_import(cls: type[Self], qualname: str) -> type[Any]:
        module: Any
        parts: list[str]
        parts = qualname.split(".")
        module = import_module(".".join(parts[:-1]))
        return cast(type[Any], getattr(module, parts[-1]))

    @classmethod
    def get_type(cls: type[Self], typename: str) -> type[Any]:
        return cast(type[Any], getattr(datahold, typename))

    @cached_property
    def test_object(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["test_object"])

    @cached_property
    def types(self: Self) -> dict[str, dict[str, Any]]:
        return cast(dict[str, dict[str, Any]], self.data["types"])

    @cached_property
    def varia(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.data["varia"])


class TestAbstractness(unittest.TestCase):

    def go_types(
        self: Self,
        typename: str,
        /,
        *,
        abstractmethods: Any = None,
        isabstract: Any = None,
        **kwargs: Any,
    ) -> None:
        cls: type[Any]
        cls = Lazy.get_type(typename)
        if isabstract is not None:
            self.assertEqual(
                ins.isabstract(cls),
                isabstract,
            )
        if abstractmethods is not None:
            self.assertSetEqual(
                cls.__abstractmethods__,
                frozenset(abstractmethods),
            )
        self.assertLessEqual(
            cls.__abstractmethods__,
            Lazy.lazy.abstractmethods,
        )
        self.assertFalse(
            "__init__" in cls.__abstractmethods__
            and "__mutable__" in cls.__abstractmethods__
        )

    def test_abstract_classes(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestAll(unittest.TestCase):
    def test_all(self: Self) -> None:
        self.assertLessEqual(
            set(datahold.__all__),
            Lazy.lazy.types.keys() | Lazy.lazy.HOLD_TYPES,
        )
        self.assertListEqual(
            datahold.__all__,
            list(sorted(datahold.__all__)),
        )


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
            parenttype = Lazy.get_import(x)
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
            with self.subTest(type=typename):
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

    def go_Mutable(
        self: Self,
        typename: Any,
        /,
        *,
        attributes: Optional[dict[str, bool | str]] = None,
    ) -> None:
        cls: Any
        cls_: type[Any]
        cls = getattr(datahold, typename)
        self.assertEqual(
            "__mutable__" in cls.__dict__,
            "Mutable" in cls.__dict__,
        )
        self.assertEqual(
            "__mutable__" in cls.__dict__,
            typename.startswith("Mutable"),
        )
        if attributes is None:
            return
        for attrname, hint in attributes.items():
            if isinstance(hint, bool):
                self.assertEqual(hasattr(cls.Mutable, attrname), hint)
                continue
            cls_ = Lazy.get_import(hint)
            self.assertIs(
                getattr(cls.Mutable, attrname),
                getattr(cls_.Mutable, attrname),
            )

    def go_OneWay(
        self: Self,
        typename: Any,
        /,
        *,
        attributes: Optional[dict[str, bool | str]] = None,
    ) -> None:
        cls: Any
        cls_: type[Any]
        cls = getattr(datahold, typename)
        self.assertEqual(
            "__one_way__" in cls.__dict__,
            "OneWay" in cls.__dict__,
        )
        if attributes is None:
            return
        for attrname, hint in attributes.items():
            if isinstance(hint, bool):
                self.assertEqual(hasattr(cls.OneWay, attrname), hint)
                continue
            cls_ = Lazy.get_import(hint)
            self.assertIs(
                getattr(cls.OneWay, attrname),
                getattr(cls_.OneWay, attrname),
            )

    def go_init(self: Self, x: str, /) -> None:
        cls: Any
        cls = getattr(datahold, x)
        self.assertNotEqual(
            cls.__init__ is object.__init__,
            hasattr(cls, "Init"),
        )

    def test_types(self: Self) -> None:
        for x, y in Lazy.lazy.types.items():
            with self.subTest(type=x):
                self.go_Mutable(
                    x,
                    **y.get("Mutable", {}),
                )
                self.go_OneWay(
                    x,
                    **y.get("OneWay", {}),
                )
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
        answer: Any
        cls: type[Any]
        solution: Any
        cls = Lazy.get_type(typename)
        answer = hasattr(cls, "copy")
        solution = typename.startswith("Mutable") and (
            cls.__init__ is not object.__init__
        )
        self.assertEqual(answer, solution)

    def test_has_copy(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_types(typename, **kwargs)


class TestParents(unittest.TestCase):

    def go_parent(
        self: Self, *, cls: type[Any], parentname: str, solution: bool
    ) -> None:
        parenttype: type[Any]
        parenttype = Lazy.get_import(parentname)
        self.assertEqual(issubclass(cls, parenttype), solution)

    def go_parents(self: Self, typename: str, /, **kwargs: Any) -> None:
        cls: type[Any]
        x: Any
        y: Any
        cls = Lazy.get_type(typename)
        for x, y in kwargs.get("parents", {}).items():
            with self.subTest(parentname=x):
                self.go_parent(
                    cls=cls,
                    parentname=x,
                    solution=y,
                )

    def test_parents(self: Self) -> None:
        for typename, kwargs in Lazy.lazy.types.items():
            with self.subTest(typename=typename):
                self.go_parents(typename, **kwargs)


if __name__ == "__main__":
    unittest.main()
