# Griffe Inherited Docstrings

Griffe extension for inheriting docstrings.

## Installation

```
pip install griffe-inherited-docstrings
```

## Usage

With Python:

```
import griffe

griffe.load("...", extensions=griffe.load_extensions(["griffe_inherited_docstrings"]))
```

With MkDocs and mkdocstrings:

```
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_inherited_docstrings
```

The extension will iterate on every class and their members to set docstrings from parent classes when they are not already defined.

The extension accepts a `merge` option, that when set to true will actually merge all parent docstrings in the class hierarchy to the child docstring, if any.

```
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_inherited_docstrings:
              merge: true
```

```
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

| Class | Method docstring                       |
| ----- | -------------------------------------- |
| `A`   | Method in A.                           |
| `B`   | Method in A.                           |
| `C`   | Method in A.                           |
| `D`   | Method in A. Method in D.              |
| `E`   | Method in A. Method in D. Method in E. |

Limitation

This extension runs once on whole packages. There is no way to toggle merging or simple inheritance for specifc objects.
