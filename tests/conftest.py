import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--trace-path",
        required=True,
        help="Path to converted CTF trace (with UST)"
    )
