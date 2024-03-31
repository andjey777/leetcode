# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# https://leetcode.com/problems/palindrome-number/description/


def Palindrome_Number(n: int):
    n = str(n)
    length = len(n)
    for i in range(0, length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True
