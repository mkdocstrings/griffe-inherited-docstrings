"""Deprecated. Import from `griffe_inherited_docstrings` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from griffe_inherited_docstrings._internal import extension


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `griffe_inherited_docstrings.extension` is deprecated. Import from `griffe_inherited_docstrings` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(extension, name)
