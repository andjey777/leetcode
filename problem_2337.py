# 2337. Move Pieces to Obtain a String
# You are given two lstings lst and target, both of length n. Each lsting consists only of the characters 'L', 'R', and '_' where:
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left,
# and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the lsting target by moving the pieces of the lsting lst any number of times. Otherwise, return false.

var = {
    "input": [
        "_L__R__R_",
        "R_L_",
        "_R",
        "__L_L_RR_R",
        "R_L_L_R_",
    ],
    "target": [
        "L______RR",
        "__LR",
        "R_",
        "LL_____RRR",
        "LL____RR",
    ],
    "result": [True, False, False, True, False],
}


def Move_Pieces(start, target):
    lst = list(start)
    length = len(lst)
    for i in range(length):
        for j in range(1, length):
            if lst[j] == "L" and lst[j - 1] != "L":
                lst[j - 1] = "L"
                lst[j] = "_"
            if lst[j - 1] == "R" and lst[j] != "R":
                lst[j] = "R"
                lst[j - 1] = "_"
    if "".join(lst) == target:
        return True
    else:
        return False


def test_prob_2337():
    for i in range(len(var["input"])):
        if Move_Pieces(var["input"][i], var["target"][i]) != var["result"][i]:
            raise Exception("Wrong result at dataset #", i)
