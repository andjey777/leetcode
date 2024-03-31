import pytest


@pytest.fixture
def two_sum() -> dict:
    return {
        "input": [
            [2, 7, 11, 15],
            [3, 2, 4],
            [3, 3],
            [1, 5, 8, 12, 15, 16],
            [2, 5, 7, 8, 14, 15, 22, 45],
        ],
        "target": [9, 6, 6, 20, 59],
        "result": [[0, 1], [1, 2], [0, 1], [1, 4], [4, 7]],
    }
