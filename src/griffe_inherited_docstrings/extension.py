"""The Griffe extension."""

from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING, Any

from griffe import AliasResolutionError, Docstring, Extension

if TYPE_CHECKING:
    from griffe import Module, Object


def _docstring_above(obj: Object) -> Docstring | None:
    with contextlib.suppress(IndexError, KeyError):
        for parent in obj.parent.mro(): # type: ignore[union-attr]
            # Fetch docstring from first parent that has the member
            if obj.name in parent.members:
                return parent.members[obj.name].docstring
    return None


def _inherit_docstrings(obj: Object, *, merge: bool = False, seen: set[str] | None = None) -> None:
    if seen is None:
        seen = set()

    if obj.path in seen:
        return

    seen.add(obj.path)

    if obj.is_module:
        for member in obj.members.values():
            if not member.is_alias:
                with contextlib.suppress(AliasResolutionError):
                    _inherit_docstrings(member, merge=merge, seen=seen)  # type: ignore[arg-type]

    elif obj.is_class:
        # Recursively handle top-most parents first.
        # It means that we can just check the first parent
        # when actually inheriting (and optionally merging) a docstring,
        # since the docstrings of the other parents have already been inherited.
        for parent in reversed(obj.mro()):  # type: ignore[attr-defined]
            _inherit_docstrings(parent, merge=merge, seen=seen)

        for member in obj.members.values():
            if not member.is_alias:
                if docstring_above := _docstring_above(member):  # type: ignore[arg-type]
                    if merge:
                        if member.docstring is None:
                            member.docstring = Docstring(
                                docstring_above.value,
                                parent=member,  # type: ignore[arg-type]
                                parser=docstring_above.parser,
                                parser_options=docstring_above.parser_options,
                            )
                        elif member.docstring.value:
                            member.docstring.value = docstring_above.value + "\n\n" + member.docstring.value
                        else:
                            member.docstring.value = docstring_above.value
                    elif member.docstring is None:
                        member.docstring = docstring_above
                if member.is_class:
                    _inherit_docstrings(member, merge=merge, seen=seen)  # type: ignore[arg-type]


class InheritDocstringsExtension(Extension):
    """Griffe extension for inheriting docstrings."""

    def __init__(self, *, merge: bool = False) -> None:
        """Initialize the extension by setting the merge flag.

        Parameters:
            merge: Whether to merge the docstrings from the parent classes into the docstring of the member.
        """
        self.merge = merge

    def on_package_loaded(self, *, pkg: Module, **kwargs: Any) -> None:  # noqa: ARG002
        """Inherit docstrings from parent classes once the whole package is loaded."""
        _inherit_docstrings(pkg, merge=self.merge, seen=set())
