# Griffe Inherited Docstrings

[![ci](https://github.com/mkdocstrings/griffe-inherited-docstrings/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-inherited-docstrings/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-inherited-docstrings/)
[![pypi version](https://img.shields.io/pypi/v/griffe-inherited-docstrings.svg)](https://pypi.org/project/griffe-inherited-docstrings/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#griffe-inherited-docstrings:gitter.im)

Griffe extension for inheriting docstrings.

## Installation

```bash
pip install griffe-inherited-docstrings
```

## Usage

With Python:

```python
import griffe

griffe.load("...", extensions=griffe.load_extensions(["griffe_inherited_docstrings"]))
```

With MkDocs and mkdocstrings:

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_inherited_docstrings
```

The extension will iterate on every class and their members
to set docstrings from parent classes when they are not already defined.

The extension accepts a `merge` option, that when set to true
will actually merge all parent docstrings in the class hierarchy
to the child docstring, if any.

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_inherited_docstrings:
              merge: true
```

```python
class A:
    def method(self):
        """Method in A."""

class B(A):
    def method(self):
        ...

class C(B):
    ...

class D(C):
    def method(self):
        """Method in D."""

class E(D):
    def method(self):
        """Method in E."""
```

With the code above, docstrings will be merged like following:

Class | Method docstring
----- | ----------------
`A`   | Method in A.
`B`   | Method in A.
`C`   | Method in A.
`D`   | Method in A.<br><br>Method in D.
`E`   | Method in A.<br><br>Method in D.<br><br>Method in E.

WARNING: **Limitation**
This extension runs once on whole packages. There is no way to toggle merging or simple inheritance for specifc objects.
