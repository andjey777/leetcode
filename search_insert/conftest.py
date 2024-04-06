import pytest


@pytest.fixture
def search_insert() -> dict:
    return {
        "nums": [
            [1, 3, 5, 6],
            [1, 3, 5, 6],
            [1, 3, 5, 6],
        ],
        "target": [
            5,
            2,
            7,
        ],
        "output": [
            2,
            1,
            4,
        ],
    }
