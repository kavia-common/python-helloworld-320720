Hello, World
============

A minimal Python package and command-line tool that prints a friendly greeting. This repository demonstrates:

- A simple, installable Python package (`helloworld`)
- A CLI entry point (`helloworld_in_python`)
- Single-sourced package versioning from `helloworld/VERSION.txt`
- Modern packaging via `pyproject.toml` + setuptools

Basic usage
-----------

Install and run:

```shell
$ cd python-helloworld-320720/
$ pip install .
$ helloworld_in_python
Hello, world
```

Show version:

```shell
$ helloworld_in_python --version
helloworld 0.1
```

Run without installing
----------------------

You can run the top-level script directly:

```shell
$ python helloworld.py
Hello, world
```

Logging
-------

The CLI uses Python's standard `logging` module (to stderr). By default it logs at `INFO`.

You can control the log level via the environment variable:

- `HELLOWORLD_LOG_LEVEL` (e.g. `DEBUG`, `INFO`, `WARNING`, `ERROR`)

Example:

```shell
$ HELLOWORLD_LOG_LEVEL=DEBUG helloworld_in_python
Hello, world
```

Development notes
-----------------

- Version is read from `helloworld/VERSION.txt` at runtime and in packaging metadata.
- The CLI entry point is configured in `pyproject.toml`:

  - `helloworld_in_python = "helloworld.main:main"`

References
----------

- Flat layout vs src layout:
  https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

- Single-sourcing package version:
  https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
