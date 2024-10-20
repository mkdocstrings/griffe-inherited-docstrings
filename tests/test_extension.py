"""Tests for the extension."""

from __future__ import annotations

from griffe import Extensions, temporary_visited_package

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


def test_inherit_and_merge_docstrings() -> None:
    """Inherit and merge docstrings from parent classes."""
    attr_doc = "Attribute docstring from class"
    meth_doc = "Method docstring from class"
    code = f"""
    # Base docstrings.
    class A:
        attr = 42
        '''{attr_doc} A.'''

        def meth(self):
            '''{meth_doc} A.'''


    # Redeclare members but without docstrings.
    class B(A):
        attr = 42

        def meth(self):
            ...


    # Redeclare members but with empty docstrings.
    class C(B):
        attr = 42
        ''''''

        def meth(self):
            ''''''


    # Redeclare members with docstrings.
    class D(C):
        attr = 42
        '''{attr_doc} D.'''

        def meth(self):
            '''{meth_doc} D.'''


    # Redeclare members with docstrings again.
    class E(D):
        attr = 42
        '''{attr_doc} E.'''

        def meth(self):
            '''{meth_doc} E.'''
    """
    with temporary_visited_package(
        "package",
        modules={"__init__.py": code},
        extensions=Extensions(InheritDocstringsExtension(merge=True)),
    ) as package:
        assert package["B.attr"].docstring.value == package["A.attr"].docstring.value
        assert package["B.meth"].docstring.value == package["A.meth"].docstring.value
        assert package["C.attr"].docstring.value == package["A.attr"].docstring.value
        assert package["C.meth"].docstring.value == package["A.meth"].docstring.value
        assert package["D.attr"].docstring.value == package["A.attr"].docstring.value + "\n\n" + f"{attr_doc} D."
        assert package["D.meth"].docstring.value == package["A.meth"].docstring.value + "\n\n" + f"{meth_doc} D."
        assert package["E.attr"].docstring.value == package["D.attr"].docstring.value + "\n\n" + f"{attr_doc} E."
        assert package["E.meth"].docstring.value == package["D.meth"].docstring.value + "\n\n" + f"{meth_doc} E."
