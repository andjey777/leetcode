# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


def Remove_Duplicates(nums):
    new_list = []
    new_list.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            new_list.append(nums[i])
    k = len(new_list)
    for i in range(len(nums) - len(new_list)):
        new_list.append("_")
    return (k, new_list)
