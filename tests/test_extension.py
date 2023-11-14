"""Tests for the extension."""

from __future__ import annotations

from griffe.extensions import Extensions
from griffe.tests import temporary_visited_package

from griffe_inherited_docstrings import InheritDocstringsExtension


def test_inherit_docstrings() -> None:
    """Inherit docstrings from parent classes."""
    with temporary_visited_package(
        "package",
        modules={
            "__init__.py": """
                class Parent:
                    def method(self):
                        '''Docstring from parent method.'''

                class Child(Parent):
                    def method(self):
                        ...
            """,
        },
        extensions=Extensions(InheritDocstringsExtension()),
    ) as package:
        assert package["Child.method"].docstring.value == package["Parent.method"].docstring.value
