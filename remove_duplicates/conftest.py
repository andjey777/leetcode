import pytest


@pytest.fixture
def remove_duplicates() -> dict:
    return {
        "input": [
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        ],
        "k": [
            2,
            5,
        ],
        "target": [
            [1, 2, "_"],
            [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"],
        ],
    }
