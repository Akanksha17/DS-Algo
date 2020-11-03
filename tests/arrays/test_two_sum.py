from arrays import two_sum
import unittest


class Solution(unittest.TestCase):

    def test_two_sum_target_present(self):
        solution = two_sum.Solution()
        arr = [3, 3]
        target = 6
        result = solution.two_sum(arr, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_target_absent(self):
        solution = two_sum.Solution()
        arr = [2, 7, 11, 15]
        target = 20
        result = solution.two_sum(arr, target)
        self.assertTrue(len(result) == 0)


if __name__ == '__main__':
    unittest.main()
