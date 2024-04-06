# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# https://leetcode.com/problems/search-insert-position/description/


def Search_Insert(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    if index == -1:
        if nums[0] >= target:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] < target and nums[i] > target:
                return i
        if nums[-1] < target:
            return len(nums)
    else:
        return index
