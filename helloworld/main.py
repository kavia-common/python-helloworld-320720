"""Top-level implementation of the helloworld program.

This module implements a small CLI that prints a friendly greeting.

Notes:
- Human-facing output ("Hello, world") is printed to stdout.
- Operational details are emitted via the standard `logging` module to stderr.
- Log level can be controlled with the `HELLOWORLD_LOG_LEVEL` environment variable.
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
from typing import Sequence

import helloworld


_LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="A simple example program to print a friendly greeting."
)
parser.add_argument(
    "--version",
    action="version",
    version="helloworld " + helloworld.__version__,
)


def _configure_logging() -> None:
    """Configure default logging for the CLI.

    We keep this minimal and dependency-free. The `HELLOWORLD_LOG_LEVEL`
    environment variable can be used to set verbosity, e.g. DEBUG/INFO/WARNING.

    This function is safe to call multiple times; `basicConfig` is a no-op if
    handlers are already configured.
    """
    level_name = os.getenv("HELLOWORLD_LOG_LEVEL", "INFO").strip().upper()
    level = getattr(logging, level_name, None)
    if not isinstance(level, int):
        # Fall back to INFO and record a warning once logging is configured.
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    if level_name != "INFO" and level == logging.INFO:
        _LOGGER.warning(
            "Invalid HELLOWORLD_LOG_LEVEL=%r; falling back to INFO",
            level_name,
        )


# PUBLIC_INTERFACE
def main(argv: Sequence[str] | None = None) -> int:
    """Program entry point for the `helloworld_in_python` command.

    Args:
        argv: Optional argument vector. If not provided, defaults to `sys.argv`.

    Returns:
        Process exit code (0 on success).
    """
    _configure_logging()

    if argv is None:
        argv = sys.argv

    _LOGGER.debug("Starting helloworld (version=%s)", helloworld.__version__)
    _LOGGER.debug("argv=%r", list(argv))

    # The helloworld program doesn't expect any arguments.
    # This just checks for the special --version and --help arguments and
    # ensures the user hasn't passed any other unrecognized arguments.
    parser.parse_args(list(argv)[1:])

    _LOGGER.info("Printing greeting")
    print("Hello, world")

    _LOGGER.debug("Exiting successfully")
    return 0
