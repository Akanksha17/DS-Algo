# Given two arrays, write a function to compute their intersection.

class Solution:
    @staticmethod
    def find_intersection_of_array(nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0

        while i < len(nums1) or j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


