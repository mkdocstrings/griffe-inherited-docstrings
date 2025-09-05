# griffe_inherited_docstrings

Griffe Inherited Docstrings package.

Griffe extension for inheriting docstrings.

Modules:

- **`extension`** – Deprecated. Import from griffe_inherited_docstrings directly.

Classes:

- **`InheritDocstringsExtension`** – Griffe extension for inheriting docstrings.

## InheritDocstringsExtension

```
InheritDocstringsExtension(*, merge: bool = False)
```

Bases: `Extension`

Griffe extension for inheriting docstrings.

Parameters:

- **`merge`** (`bool`, default: `False` ) – Whether to merge the docstrings from the parent classes into the docstring of the member.

Methods:

- **`on_package`** – Inherit docstrings from parent classes once the whole package is loaded.

Attributes:

- **`merge`** – Whether to merge the docstrings from the parent classes into the docstring of the member.

Source code in `src/griffe_inherited_docstrings/_internal/extension.py`

```
def __init__(self, *, merge: bool = False) -> None:
    """Initialize the extension by setting the merge flag.

    Parameters:
        merge: Whether to merge the docstrings from the parent classes into the docstring of the member.
    """
    self.merge = merge
    """Whether to merge the docstrings from the parent classes into the docstring of the member."""
```

### merge

```
merge = merge
```

Whether to merge the docstrings from the parent classes into the docstring of the member.

### on_package

```
on_package(*, pkg: Module, **kwargs: Any) -> None
```

Inherit docstrings from parent classes once the whole package is loaded.

Source code in `src/griffe_inherited_docstrings/_internal/extension.py`

```
def on_package(self, *, pkg: Module, **kwargs: Any) -> None:  # noqa: ARG002
    """Inherit docstrings from parent classes once the whole package is loaded."""
    _inherit_docstrings(pkg, merge=self.merge, seen=set())
```
