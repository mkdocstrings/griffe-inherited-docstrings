# Griffe Inherited Docstrings

[![ci](https://github.com/mkdocstrings/griffe-inherited-docstrings/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-inherited-docstrings/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mkdocstrings.github.io/griffe-inherited-docstrings/)
[![pypi version](https://img.shields.io/pypi/v/griffe-inherited-docstrings.svg)](https://pypi.org/project/griffe-inherited-docstrings/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-inherited-docstrings)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-inherited-docstrings:gitter.im)

Griffe extension for inheriting docstrings.

## Installation

With `pip`:

```bash
pip install griffe-inherited-docstrings
```

With [`pipx`](https://github.com/pipxproject/pipx):

```bash
python3.8 -m pip install --user pipx
pipx install griffe-inherited-docstrings
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
