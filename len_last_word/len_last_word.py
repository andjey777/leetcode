# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# https://leetcode.com/problems/length-of-last-word/description/


def Len_last_Word(inp_str: str):
    list_str = inp_str.split()
    return len(max(list_str, key=len))
