# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the
# new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory

class Solution:
    @staticmethod
    def remove_duplicates(nums):
        original_arr_length = len(nums)
        i = 0
        for j in range(1, original_arr_length):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


