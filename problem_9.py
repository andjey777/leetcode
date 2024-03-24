# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# https://leetcode.com/problems/palindrome-number/description/

var = {
    "input": [121, -121, 10, 12345, 1234554321],
    "result": [True, False, False, False, True],
}


def Palindrome_Number(n):
    n = str(n)
    length = len(n)
    for i in range(0, length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True


def test_prob_9():
    for i in range(len(var["input"])):
        if Palindrome_Number(var["input"][i]) != var["result"][i]:
            raise Exception("Wrong result at dataset #", i)
