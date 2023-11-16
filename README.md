# Griffe Inherited Docstrings

[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mkdocstrings.github.io/griffe-inherited-docstrings/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-inherited-docstrings)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/mkdocstrings/mkdocstrings)

Griffe extension for inheriting docstrings.

## Installation

See [Insiders installation](https://mkdocstrings.github.io/mkdocstrings/insiders/installation.md).

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
