# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
import copy


class Solution:
    @staticmethod
    def two_sum(nums, target):
        nums_copy = copy.deepcopy(nums)
        nums_copy.sort()
        i = 0
        j = len(nums_copy) - 1
        elements = None
        while i < j:
            if nums_copy[i] + nums_copy[j] == target:
                elements = [nums_copy[i], nums_copy[j]]
                break
            elif nums_copy[i] + nums_copy[j] < target:
                i += 1
            else:
                j -= 1
        if elements:
            idx1 = nums.index(elements[0])
            idx2 = nums.index(elements[1])
            if elements[0] == elements[1]:
                idx2 = nums.index(elements[1], idx1 + 1)
            return [idx1, idx2]
        else:
            return []





