# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# https://leetcode.com/problems/palindrome-number/description/

print("Problem 9 Palindrome Number")

vars = [
    (121, True),
    (-121, False),
    (10, False),
]


def Palindrome_Number(n):
    n = str(n)
    length = len(n)
    for i in range(0, length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True


for i in vars:
    if Palindrome_Number(i[0]) == i[1]:
        print(i, "Success")
    else:
        raise Exception("Wrong result at", i)
