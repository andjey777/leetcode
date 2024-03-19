# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/description/


vars = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 5, 8, 12, 15, 16], 20, [1, 4]),
    ([2, 5, 7, 8, 14, 15, 22, 45], 59, [4, 7]),
]


def Two_Sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


for i in vars:
    if Two_Sum(i[0], i[1]) != i[2]:
        raise Exception("Wrong result at", i)
