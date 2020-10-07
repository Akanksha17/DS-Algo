# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution:
    @staticmethod
    def single_number(nums):
        a = 0
        for n in nums:
            a ^= n
        return a
