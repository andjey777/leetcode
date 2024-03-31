import pytest


@pytest.fixture
def com_prefix() -> dict:
    return {
        "input": [
            ["flower", "flow", "flight"],
            ["dog", "racecar", "car"],
        ],
        "result": ["fl", ""],
    }
