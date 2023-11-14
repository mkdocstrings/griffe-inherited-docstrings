"""The Griffe extension."""

from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING

from griffe import Extension
from griffe.exceptions import AliasResolutionError

if TYPE_CHECKING:
    from griffe import Docstring, Module, Object


def _inherited_docstring(obj: Object) -> Docstring | None:
    for parent_class in obj.parent.mro():  # type: ignore[union-attr]
        try:
            if docstring := parent_class.members[obj.name].docstring:
                return docstring
        except KeyError:
            pass
    return None


def _inherit_docstrings(obj: Object) -> None:
    if obj.is_module:
        for member in obj.members.values():
            if not member.is_alias:
                with contextlib.suppress(AliasResolutionError):
                    _inherit_docstrings(member)  # type: ignore[arg-type]
    elif obj.is_class:
        for member in obj.members.values():
            if not member.is_alias:
                if member.docstring is None and (inherited := _inherited_docstring(member)):  # type: ignore[arg-type]
                    member.docstring = inherited
                if member.is_class:
                    _inherit_docstrings(member)  # type: ignore[arg-type]


class InheritDocstringsExtension(Extension):
    """Griffe extension for inheriting docstrings."""

    def on_package_loaded(self, *, pkg: Module) -> None:
        """Inherit docstrings from parent classes once the whole package is loaded."""
        _inherit_docstrings(pkg)
