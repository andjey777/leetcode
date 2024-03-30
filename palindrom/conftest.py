import pytest


@pytest.fixture
def palindrom() -> list[int]:
    return [
        121,
        1234554321,
    ]


@pytest.fixture
def not_palindrom() -> list[int]:
    return [
        -121,
        10,
        12345,
    ]
