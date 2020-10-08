# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    @staticmethod
    def plus_one(arr):
        num = 0
        arr_len = len(arr)
        for i in range(arr_len):
            multiplier = 10 ** (arr_len - 1 - i)
            num += (arr[i] * multiplier)
        incremented_num = num + 1
        temp = incremented_num
        result = []
        while temp > 0:
            rem = temp % 10
            result.append(rem)
            temp = temp // 10
        return result[::-1]

