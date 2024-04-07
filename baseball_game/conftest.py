import pytest


@pytest.fixture
def baseball_game() -> dict:
    return {
        "input": [
            ["5", "2", "C", "D", "+"],
            ["5", "-2", "4", "C", "D", "9", "+", "+"],
            ["1", "C"],
            ["2", "3", "D", "5", "C", "+", "2"],
            ["3", "C", "2", "D", "+", "4", "5", "C", "C", "5"],
        ],
        "result": [30, 27, 0, 22, 17],
    }
