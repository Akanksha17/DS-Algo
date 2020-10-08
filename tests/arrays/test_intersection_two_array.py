import unittest
from arrays import interesection_two_array


class TestArrIntersection(unittest.TestCase):
    def test_intersection(self):
        solution = interesection_two_array.Solution()
        nums1 = [1, 4, 2, 1, 1, 6, 3, 4, 1]
        nums2 = [4, 6, 1]
        result = solution.find_intersection_of_array(nums1, nums2)
        self.assertEqual(result, [1, 4, 6])


if __name__ == '__main__':
    unittest.main()
