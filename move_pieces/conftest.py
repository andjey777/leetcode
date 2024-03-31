import pytest


@pytest.fixture
def move_pieces() -> dict:
    return {
    "input": [
        "_L__R__R_",
        "__L_L_RR_R",
    ],
    "target": [
        "L______RR",
        "LL_____RRR",
    ],
}

@pytest.fixture
def not_move_pieces() -> dict:
    return {
    "input": [
        "R_L_",
        "_RL",
        "R_L_L_R_",
    ],
    "target": [
        "L__R",
        "L_R",
        "LL____RR",
    ],
}
