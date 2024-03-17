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

print("Problem 682 Baseball Game")

vars = [
    (["5","2","C","D","+"], 30),
    (["5","-2","4","C","D","9","+","+"], 27),
    (["1","C"], 0),
]

def Baseball_Game(ops):
    symb = ['+', 'D', 'C']
    result = []
    for i in range(len(ops)):
        if ops[i] not in symb:
            result.append(int(ops[i]))
        if ops[i] == '+':
            result.append(int(result[-1]) + int(result[-2]))
        if ops[i] == 'D':
            result.append(int(result[-1]) * 2)
        if ops[i] == 'C':
            result.pop()
    return sum(result)

for i in vars:
    if Baseball_Game(i[0]) == i[1]:
        print(i, "Success")
    else:
        raise Exception("Wrong result at", i)
