"""Tests for the extension."""

from __future__ import annotations

from typing import Callable

import pytest
from griffe import Extensions, temporary_visited_package

from griffe_inherited_docstrings import InheritDocstringsExtension
from griffe_inherited_docstrings.extension import DocstringInheritStrategy


@pytest.fixture(params=[
    (
        "Method docstrings",
        """
        class Obj: # just to verify that additional parent classes don't affect the result
            ...

        class Base(Obj):
            def base(self):
                {docstring_base} # Without triple quotes so we can control between empty docstring and no docstring.
                ...

        class Main(Base):
            def base(self):
                {docstring_main}
                ...

        class Sub(Main):
            def base(self):
                {docstring_sub}
                ...
        """,
        lambda package, class_: package[f"{class_}.base"].docstring,
    ),
    (
        "Attribute docstrings",
        """
        class Obj:
            ...

        class Base(Obj):
            attr: int
            {docstring_base}

        class Main(Base):
            attr: int
            {docstring_main}


        class Sub(Main):
            attr: int
            {docstring_sub}
        """,
        lambda package, class_: package[class_].members["attr"].docstring,
    ),

])
def content(request: pytest.FixtureRequest) -> tuple[str, str, Callable]:
    return request.param

@pytest.mark.parametrize(
    ("merge_docstrings", "docstrings_list", "expected_docstrings_list"),
    [
        (
            False,
            ['"""base"""', '"""main"""', ""],
            ["base", "main", "main"],
        ),  # main: stays the same (no merge); sub: main is taken (not base)
        (
            True,
            ['"""base"""', '"""main"""', ""],
            ["base", "base\n\nmain", "base\n\nmain"],
        ),  # main: is merged with base; sub: empty is merged with base\n\nmain (not base\n\nmain\n\n)
        (
            True,
            ["", '"""main"""', '"""sub"""'],
            [None, "main", "main\n\nsub"],
        ),  # Base class has no docstring after merging (as opposed to an empty one)
    ],
)
def test_inherit_docstrings(
    merge_docstrings: DocstringInheritStrategy, docstrings_list: list[str], expected_docstrings_list: list[str], content: tuple[str, str, Callable]
) -> None:
    """Test the inheritance strategies of docstrings for members.

    Parameters:
        strategy: The docstring inheritance strategy to use.
        docstrings_list: The list of docstrings for the base, main, and sub classes. Needs triple quotes.
        expected_docstrings_list: The expected list of docstrings for the base, main, and sub classes. Just the content, i.e. without triple quotes. None for no docstring at all.
    """
    docstring_base, docstring_main, docstring_sub = docstrings_list

    to_test, code, get_docstring = content

    with temporary_visited_package(
        "package",
        modules={"__init__.py": code.format(docstring_base=docstring_base, docstring_main=docstring_main, docstring_sub=docstring_sub)},
        extensions=Extensions(InheritDocstringsExtension(merge_docstrings=merge_docstrings)),
    ) as package:
        classes = ["Base", "Main", "Sub"]
        docstrings = [get_docstring(package, class_) for class_ in classes]
        docstring_values = [docstring.value if docstring else None for docstring in docstrings]

        assert docstring_values == expected_docstrings_list, f"Failed for merge='{merge_docstrings}' during testing '{to_test}'"
