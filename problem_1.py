# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/description/


var = {
    "input": [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3],
        [1, 5, 8, 12, 15, 16],
        [2, 5, 7, 8, 14, 15, 22, 45],
    ],
    "target": [9, 6, 6, 20, 59],
    "result": [[0, 1], [1, 2], [0, 1], [1, 4], [4, 7]],
}


def Two_Sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


def test_prob_1():
    for i in range(len(var["input"])):
        if Two_Sum(var["input"][i], var["target"][i]) != var["result"][i]:
            raise Exception("Wrong result at dataset #", i)
