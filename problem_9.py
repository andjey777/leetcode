# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# https://leetcode.com/problems/palindrome-number/description/


vars = [
    (121, True),
    (-121, False),
    (10, False),
    (12345, False),
    (1234554321, True),
]


def Palindrome_Number(n):
    n = str(n)
    length = len(n)
    for i in range(0, length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True


def test_prob_9():
    for i in vars:
        if Palindrome_Number(i[0]) != i[1]:
            raise Exception("Wrong result at", i)
