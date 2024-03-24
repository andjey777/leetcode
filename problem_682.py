# 682. Baseball Game
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x. Record a new score of x.
# '+'. Record a new score that is the sum of the previous two scores.
# 'D'. Record a new score that is the double of the previous score.
# 'C'. Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
# https://leetcode.com/problems/baseball-game/description/

var = {
    "input": [
        ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"],
        ["1", "C"],
        ["2", "3", "D", "5", "C", "+", "2"],
        ["3", "C", "2", "D", "+", "4", "5", "C", "C", "5"],
    ],
    "result": [30, 27, 0, 22, 17],
}


def Baseball_Game(ops):
    symb = ["+", "D", "C"]
    result = []
    for i in range(len(ops)):
        if ops[i] not in symb:
            result.append(int(ops[i]))
        if ops[i] == "+":
            result.append(int(result[-1]) + int(result[-2]))
        if ops[i] == "D":
            result.append(int(result[-1]) * 2)
        if ops[i] == "C":
            result.pop()
    return sum(result)


def test_prob_682():
    for i in range(len(var["input"])):
        if Baseball_Game(var["input"][i]) != var["result"][i]:
            raise Exception("Wrong result at dataset #", i)
