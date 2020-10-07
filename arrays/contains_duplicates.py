# Given an array of integers, find if the array contains any duplicates.


class Solution:
    @staticmethod
    def contains_duplicate(nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

