import pytest


@pytest.fixture
def len_last_word() -> dict:
    return {
        "str": ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"],
        "len": [5, 4, 6],
    }
