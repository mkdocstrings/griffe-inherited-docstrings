# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.1.2](https://github.com/mkdocstrings/griffe-inherited-docstrings/releases/tag/1.1.2) - 2025-09-05

<small>[Compare with 1.1.1](https://github.com/mkdocstrings/griffe-inherited-docstrings/compare/1.1.1...1.1.2)</small>

### Build

- Depend on Griffe 1.14 ([3e39e7d](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/3e39e7dcac620de7524d4264ab6b9ca9ee10098c) by Timothée Mazzucotelli).

### Code Refactoring

- Move modules under internal folder ([aee4b19](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/aee4b19f8d13910721e3729d7702ec9672d468b6) by Timothée Mazzucotelli).

## [1.1.1](https://github.com/mkdocstrings/griffe-inherited-docstrings/releases/tag/1.1.1) - 2024-11-05

<small>[Compare with 1.1.0](https://github.com/mkdocstrings/griffe-inherited-docstrings/compare/1.1.0...1.1.1)</small>

### Bug Fixes

- Fix inheritance logic when intermediate class without member is present ([639ff80](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/639ff807c34edc25e1841626f8ac6f4b743e8539) by thomasmarwitz). [Issue-4](https://github.com/mkdocstrings/griffe-inherited-docstrings/issues/4), [PR-5](https://github.com/mkdocstrings/griffe-inherited-docstrings/pull/5), Co-authored-by: Timothée Mazzucotelli <dev@pawamoy.fr>

## [1.1.0](https://github.com/mkdocstrings/griffe-inherited-docstrings/releases/tag/1.1.0) - 2024-10-25

<small>[Compare with 1.0.1](https://github.com/mkdocstrings/griffe-inherited-docstrings/compare/1.0.1...1.1.0)</small>

### Build

- Drop support for Python 3.8 ([48370d6](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/48370d6d6cb9766bc28aca4c88144fd5f27d8300) by Timothée Mazzucotelli).

### Features

- Add `merge` option to merge docstrings downwards ([232fbb0](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/232fbb0a151eb58a34d4579881cc2bed8f689bbc) by thomasmarwitz). [Issue-2](https://github.com/mkdocstrings/griffe-inherited-docstrings/issues/2), [PR-3](https://github.com/mkdocstrings/griffe-inherited-docstrings/pull/3), Co-authored-by: Timothée Mazzucotelli <dev@pawamoy.fr>

## [1.0.1](https://github.com/mkdocstrings/griffe-inherited-docstrings/releases/tag/1.0.1) - 2024-08-15

<small>[Compare with 1.0.0](https://github.com/mkdocstrings/griffe-inherited-docstrings/compare/1.0.0...1.0.1)</small>

### Build

- Depend on Griffe 0.49 ([ce6bf5f](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/ce6bf5fe21e839aa7e1b9b84c9c531a5841ece3c) by Timothée Mazzucotelli).

### Code Refactoring

- Update code for Griffe 0.49 ([b975f7f](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/b975f7f523c369c9ab3bc889cf9f558ef7c133a0) by Timothée Mazzucotelli).

## [1.0.0](https://github.com/mkdocstrings/griffe-inherited-docstrings/releases/tag/1.0.0) - 2024-01-05

<small>[Compare with first commit](https://github.com/mkdocstrings/griffe-inherited-docstrings/compare/b0d27df17aab12337a426b1d2e642593bdc9231b...1.0.0)</small>

### Features

- Implement extension ([993e4e1](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/993e4e1e9a316e8b472df47c6568392605ca07f6) by Timothée Mazzucotelli).
- Generate project with copier-pdm template ([2e71db6](https://github.com/mkdocstrings/griffe-inherited-docstrings/commit/2e71db6086e2507cc058d8b387d33eb7c228ed9a) by Timothée Mazzucotelli).
