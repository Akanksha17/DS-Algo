# Given two arrays, write a function to compute their intersection.

class Solution:
    @staticmethod
    def find_intersection_of_array(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        intersection_dict = {}
        i, j = 0, 0
        intersection_arr = []

        while i < nums1_len or j < nums2_len:
            if nums1[i] != nums2[j]:
                i += 1
            if nums1[i] == nums2[j]:
                if (j == 0) or (j - 1 in intersection_dict.keys()):
                    intersection_arr.append(nums1[i])



