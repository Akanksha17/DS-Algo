# Given an array nums,
# write a function to move all 0's
# to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    @staticmethod
    def move_zeroes(nums):
        nums_len = len(nums)
        if nums_len > 1:
            i = 0
            for j in range(1, nums_len):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[i] != 0:
                    i += 1
        return nums
