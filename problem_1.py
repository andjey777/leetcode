#1. Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

nums = [1, 2, 3, 4, 8, 6]
target = 10
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        if nums[i] + nums[j] == target:
            print(i, j)
            exit()
