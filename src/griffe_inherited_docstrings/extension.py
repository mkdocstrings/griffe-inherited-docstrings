"""The Griffe extension."""

from __future__ import annotations

import contextlib
from enum import Enum
from typing import TYPE_CHECKING, Any

from griffe import AliasResolutionError, Class, Docstring, Extension

if TYPE_CHECKING:
    from griffe import Module, Object

class DocstringInheritStrategy(str, Enum):
    """Enumeration for the possible docstring inheritance strategies."""

    if_not_present = "if_not_present"
    """Inherit docstrings of members if not present. This takes the first docstring of a member according to the MRO."""
    merge = "merge"
    """Merge docstrings of members in parent classes with given docstring. This proceeds down the inheritance tree, going from general docstrings to more specific ones."""






class InheritDocstringsExtension(Extension):
    """Griffe extension for inheriting docstrings."""

    def __init__(self, merge_docstrings: bool = False) -> None:
        super().__init__()

        self.merge = merge_docstrings
        self.merge_separator: str = "\n\n"
        self.merge_cache = {}

    def on_package_loaded(self, *, pkg: Module, **kwargs: Any) -> None:  # noqa: ARG002
        """Inherit docstrings from parent classes once the whole package is loaded."""
        self.merge_cache.clear()
        self._inherit_docstrings(pkg, self.merge, self.merge_separator)
        self.merge_cache.clear()

    def _construct_docstring(
        self, obj: Object, merge: bool = False, merge_separator: str = "\n\n",
    ) -> Docstring | None:
        """Construct a docstring object according to the strategy.

        Parameters:
            name: The name of the member. Needed to lookup the member in the parent classes.
            obj: The object that contains the member. Needed to access parent classes.
            strategy: The strategy to use: default, if_not_present, merge.
            merge_separator: The delimiter to use when merging docstrings.

        Returns:
            A new docstring object that just contains the docstring content.
        """
        name = obj.name

        if not merge:
            for parent_class in obj.parent.mro():  # type: ignore[union-attr]
                if name in parent_class.members and (docstring := parent_class.members[obj.name].docstring):
                    return docstring
            return None


        docstrings = []
        traversal_order: list[Class | Object] = [obj.parent, *obj.parent.mro()]
        # We traverse the parents in the order of the MRO, i.e. the first entry is the most direct parent
        # We also include the object itself because we don't want to miss the docstring of the object itself if present
        # In the end, the docstrings are merged in reverse order, to have the most general docstring come first
        # We traverse in the order of the MRO to be able to break as soon as we find a previously merged docstring
        # This is to avoid merging the same docstring multiple times

        for parent_class in traversal_order: # type: ignore[assignment]
            if (parent_class.name, name) in self.merge_cache:
                docstrings.append(
                    self.merge_cache[(parent_class.name, name)]
                )
                break


            if name in parent_class.members and (docstring := parent_class.members[obj.name].docstring):
                docstrings.append(docstring.value)

        if not docstrings:
            # This guarantees that no empty docstring is constructed for a member that shouldn't have one at all
            return None

        docstring = merge_separator.join(reversed(docstrings))
        self.merge_cache[(obj.parent.name, name)] = docstring

        return Docstring(docstring)


    def _inherit_docstrings(self, obj: Object, merge: bool = False, merge_separator: str = "\n\n") -> None:
        if obj.is_module:
            for member in obj.members.values():
                if not member.is_alias:
                    with contextlib.suppress(AliasResolutionError):
                        self._inherit_docstrings(member, merge=merge, merge_separator=merge_separator)  # type: ignore[arg-type]
        elif obj.is_class:
            for member in obj.members.values():
                if member.is_alias:
                    continue

                if member.is_class:
                    self._inherit_docstrings(member)  # type: ignore[arg-type]

                docstring = self._construct_docstring(member, merge=merge, merge_separator=merge_separator)  # type: ignore[arg-type]

                if not docstring:
                    # if the docstring is None, we don't want to set it
                    continue

                if not member.docstring and not merge:
                    member.docstring = docstring
                elif merge:
                    member.docstring = docstring


