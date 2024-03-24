# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# https://leetcode.com/problems/longest-common-prefix/description/

var = {
    "input": [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
    ],
    "result": ["fl", ""],
}


def Longest_Common_Prefix(strs):
    min_len = len(min(strs, key=len))
    suff = ""
    for i in range(min_len):
        symb = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != symb:
                return suff
        suff += symb


def test_prob_14():
    for i in range(len(var["input"])):
        if Longest_Common_Prefix(var["input"][i]) != var["result"][i]:
            raise Exception("Wrong result at dataset #", i)
